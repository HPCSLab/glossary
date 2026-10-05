---
aliases: [OpenZFS, Zettabyte File System, RAID-Z, RAIDZ, zpool, vdev, ARC, ZIL, SLOG]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-06
---
# ZFS

> ボリューム管理とファイルシステムの機能を一体化し、コピーオンライトとエンドツーエンドのチェックサムによってデータの完全性を重視する、ファイルシステムである。

## 概要
ZFSは2001年からSun Microsystemsで開発され、2005年にOpenSolarisの一部としてオープンソース化された。Oracleによる買収の後は、OpenZFSプロジェクトがLinux、FreeBSDなど複数のOS向けの開発を担っている。

従来は、複数のディスクを束ねるボリューム管理（RAIDやLVM）と、その上のファイルシステムが別の層であった。ZFSはこの二つを統合し、物理的なディスクの構成と、その上のファイルの両方を把握する。複数のディスクはvdevとしてまとめられ、vdevの集合がストレージプール（zpool）を構成する。プールの上には、容量を共有する複数のデータセット（ファイルシステム）を作成できる。冗長化には、ミラーのほか、RAID-Zと呼ばれる独自の方式を用いる。RAID-Zはブロックごとに可変幅のストライプを構成するため、従来のRAID5で問題となる、書き込み途中の障害でパリティとデータが食い違う問題（write hole）を回避する。

ZFSは、既存のデータを上書きせず、変更されたブロックを常に新しい場所に書くコピーオンライトの方式を採る。一連の変更は、ルートとなるブロックの更新によって不可分に確定するため、クラッシュしてもファイルシステムが矛盾した状態に陥らない。また、すべてのブロックのチェックサムを、そのブロック自身ではなく、それを指す親のブロックに格納する。これにより、記憶装置が誤ったデータを黙って返す静かなデータ破損も検出でき、冗長性があれば正しい複製から自動的に修復する。コピーオンライトの性質により、ある時点の状態を瞬時に保存するスナップショットや、その差分を別のシステムへ送る `zfs send`/`zfs receive` も容易に実現される。

## どこで出てくるか
ZFSは、データの完全性が重視されるファイルサーバ、バックアップ、アーカイブの用途で広く用いられる。HPCでは、[[Lustre]]のMDTやOSTの下位のファイルシステムとして、[[ext4]]を基にしたldiskfsと並んでZFSを選択できる。性能の面では、独自のキャッシュであるARC（[[Page Cache|ページキャッシュ]]とは別に主記憶を使う）や、同期書き込みを記録するZIL、それを高速な装置に置くSLOGなどの仕組みを理解しておく必要がある。なお、ZFSのライセンス（CDDL）はLinuxカーネルのGPLv2と両立しないとされるため、ZFSは[[Linux Kernel|Linuxカーネル]]本体には含まれず、外部のカーネルモジュールとして提供される。

## 関係
- 上位概念: [[File System]]
- 対比: [[btrfs]]（同じくコピーオンライトでLinuxカーネルに含まれる）, [[ext4]]（ジャーナリングによる整合性）
- 使う / 使われる: [[Lustre]]（下位のファイルシステムとして使う）
- 関連: [[Block Storage]], [[JBD2]], [[Crash Consistency]]

## 出典
- [ZFS - Wikipedia](https://en.wikipedia.org/wiki/ZFS)
- [Basic Concepts - OpenZFS Documentation](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/index.html)
- [Introduction to Lustre - Lustre Wiki](https://wiki.lustre.org/Introduction_to_Lustre)
