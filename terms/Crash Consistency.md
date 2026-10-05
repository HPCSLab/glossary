---
aliases: [クラッシュ整合性, クラッシュ一貫性, Crash Recovery, fsck, Soft Updates, Write Ordering, 書き込み順序, Flush, FUA]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-06
---
# Crash Consistency（クラッシュ整合性）

> 電源断やOSのクラッシュによって更新が途中で中断されても、記憶装置上のデータ構造が矛盾のない状態に回復できる性質である。

## 概要
記憶装置上のデータ構造の一つの論理的な更新は、多くの場合、複数のブロックへの書き込みからなる。例えば、ファイルの末尾にブロックを一つ追加するには、データブロック、それを指す[[Inode|inode]]、ブロックの使用状況を表すビットマップの三か所を更新する必要がある。記憶装置は一度に一つのブロックしか確実に書けないため、その途中でクラッシュすると、inodeが未割り当てのブロックを指す、割り当て済みとされたブロックがどこからも参照されない、などの矛盾が残りうる。さらに、OSや記憶装置は性能のために書き込みの順序を入れ替えるため、プログラムが発行した順序で記憶装置に反映されるとは限らない。

ファイルシステムは、主に次の方法でこの問題に対処してきた。fsckは、クラッシュ後の起動時に全体を走査して矛盾を検出・修復する方法であるが、容量に比例して時間がかかる。ジャーナリングは、変更をまず専用の領域（ジャーナル）に記録し、記録の完了後に本来の位置へ書くことで、クラッシュ後は記録が完了した変更のみを再適用する方法であり、[[ext4]]の[[JBD2]]がこれに当たる。データも含めて記録する方式と、メタデータのみを記録する方式がある。[[Copy-on-Write|コピーオンライト]]は、既存のデータを上書きせず、新しい場所に書いてから参照を不可分に切り替える方法であり、[[ZFS]]や[[btrfs]]が採用している。このほかに、書き込みの順序を慎重に管理するsoft updatesなどの方法がある。いずれの方法も、ある書き込みが記憶装置に確実に到達してから次の書き込みを行う、という順序の制御に依存しており、記憶装置の書き込みキャッシュの書き出し（flush）や、キャッシュを経由せずに書くFUAがそのために用いられる。

ファイルシステムが自身のメタデータの整合性を保証しても、アプリケーションのデータの整合性までは保証されない。アプリケーションは、[[fsync]]と[[rename]]などを組み合わせて、自分で整合性を確保する必要がある。代表的な手順は、一時ファイルに新しい内容を書き、fsyncで永続化し、renameで本来の名前に置き換え、さらに親ディレクトリをfsyncすることである。

## どこで出てくるか
アプリケーションの整合性の確保は、見かけ以上に難しい。2014年のOSDIで発表された研究（Pillaiら）は、ファイルシステムが実際に保証する永続化の性質が、Linuxの代表的なファイルシステムの間で大きく異なることを示した。そのうえで、広く使われているデータベース、キーバリューストア、バージョン管理システムなど11種のアプリケーションから、60のクラッシュ時の脆弱性を発見した。特定のファイルシステムでたまたま問題が起きないことは、正しさの保証にはならない。

研究では、クラッシュ整合性の検証に、すべての書き込みを記録して任意の時点のクラッシュ後の状態を再現する手法が用いられる。[[Device Mapper|device mapper]]のdm-log-writesはその代表的な道具である。また、ジャーナリングやfsyncのコストを削減しながら整合性を保つ手法は、ファイルシステム研究の主要な題材である。カーネルのクラッシュそのものの原因を調べる[[kdump]]とは、名前は似ているが別の話題である。

## 関係
- 使う / 使われる: [[JBD2]]（ジャーナリング）, [[ZFS]], [[btrfs]]（コピーオンライト）
- 関連: [[fsync]], [[rename]], [[Page Cache]], [[Device Mapper]], [[SSD]], [[RAID]]

## 出典
- [Crash Consistency: FSCK and Journaling - Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/file-journaling.pdf)
- [All File Systems Are Not Created Equal: On the Complexity of Crafting Crash-Consistent Applications - USENIX OSDI 2014](https://www.usenix.org/conference/osdi14/technical-sessions/presentation/pillai)
- [dm-log-writes - The Linux Kernel documentation](https://docs.kernel.org/admin-guide/device-mapper/log-writes.html)
