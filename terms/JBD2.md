---
aliases: [jbd2, Journaling Block Device 2, JBD, ジャーナル]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-05
---
# JBD2

> Linuxカーネルにおける汎用のジャーナリング層であり、[[ext4]]やOCFS2が、クラッシュ時にもファイルシステムの整合性を保つために用いる。

## 概要
ファイルの作成一つをとっても、[[Inode|inode]]の割り当て、ディレクトリへのエントリの追加、空き領域の管理情報の更新など、複数のメタデータブロックを書き換える必要がある。途中で電源が断たれると、これらの一部だけが反映された矛盾した状態が残りうる。ジャーナリングは、変更をまずジャーナルと呼ばれる専用領域に記録し、記録の完了を確認してから本来の位置に書き込むことで、この問題を解決する。クラッシュ後の再マウント時には、完了が記録された変更をジャーナルから再適用（リプレイ）し、完了していない変更は破棄する。これにより、一連の更新は全体として反映されるか、全く反映されないかのいずれかとなる。

ファイルシステムは、JBD2のハンドルを単位として更新を行う。`jbd2_journal_start()` でハンドルを開始し、変更するバッファごとに `jbd2_journal_get_write_access()` を呼んでから内容を書き換え、`jbd2_journal_dirty_metadata()` で変更済みとして登録し、`jbd2_journal_stop()` で終える。JBD2は、多数のハンドルを一つのトランザクションにまとめて扱う。トランザクションは、一定時間（ext4では既定5秒、マウントオプション `commit=` で変更可能）ごと、あるいは[[fsync]]などの要求に応じてコミットされる。

ジャーナルには、トランザクションごとに、記述子ブロック（後続のブロックが本来どの位置に属するかを示す）、変更後のメタデータブロックの複製、取り消しブロック（古い記録の再適用を防ぐ）が書かれ、最後にコミットブロックが書かれる。コミットブロックの書き込みをもってトランザクションは確定する。この順序を保証するため、記憶装置の書き込みキャッシュの書き出しなどが用いられる。確定した内容を本来の位置に書き込み、ジャーナルの領域を再利用可能にする処理をチェックポイントと呼ぶ。

## どこで出てくるか
JBD2は、`ps` や `iotop` で `jbd2/<デバイス名>` という名前のカーネルスレッドとして観測され、ext4の書き込みや[[fsync]]の性能を分析する際の着眼点となる。トランザクションは複数のファイルの更新をまとめて扱うため、あるファイルの `fsync()` が、無関係なファイルの更新を含むトランザクション全体のコミットを待つことがある。これを緩和するため、ext4には、変更の差分のみを記録する高速コミット（fast commit）が追加されている。ジャーナリングの方式とコストは、[[Crash Consistency|クラッシュ整合性]]に関する研究の主要な題材である。

## 関係
- 上位概念: [[Journaling File System]]
- 使う / 使われる: [[ext4]]（JBD2を使う）
- 関連: [[fsync]], [[Crash Consistency]], [[Metadata]]

## 出典
- [The Linux Journalling API - The Linux Kernel documentation](https://docs.kernel.org/filesystems/journalling.html)
- [Journal (jbd2) - The Linux Kernel documentation](https://docs.kernel.org/filesystems/ext4/journal.html)
- [ext4 General Information - The Linux Kernel documentation](https://docs.kernel.org/admin-guide/ext4.html)
