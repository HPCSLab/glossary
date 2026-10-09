---
aliases: [mke2fs, mkfs.ext4, e2fsck, fsck.ext4, tune2fs, dumpe2fs, debugfs, resize2fs, libext2fs]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# e2fsprogs

> [[ext4]]をはじめとするext2・ext3・ext4の[[File System|ファイルシステム]]を作成・検査・修復・調整・調査するための、ユーザ空間のツール群である。

## 概要
e2fsprogsは、ext系のファイルシステムを[[Linux Kernel|カーネル]]の外から操作するためのパッケージであり、Theodore Ts'oが開発している。ライセンスはGPLである。多くのツールは、ディスク上の構造を読み書きするライブラリlibext2fsの上に作られており、マウントしていない[[Block Storage|ブロックデバイス]]やディスクイメージのファイルを直接扱う。カーネル内のext4の実装とは別に、同じディスク上の形式を解釈する実装がユーザ空間にあることになる。

主なツールは次のとおりである。`mke2fs`（`mkfs.ext4` などの名前でも呼ばれる）はファイルシステムを作成し、既定のパラメータは `/etc/mke2fs.conf` で定める。`e2fsck` は構造の矛盾を検査・修復し、ジャーナルを持つファイルシステムでは、まずジャーナルの記録を再適用する。`tune2fs` は予約ブロックの割合、ラベル、機能フラグなどの設定を変更し、`resize2fs` は大きさを変更する。`dumpe2fs` は[[Superblock|スーパーブロック]]とブロックグループの情報を表示し、`debugfs` は[[Inode|inode]]やジャーナルの中身を対話的に調べる。`debugfs` は既定では読み取り専用で開き、`-w` を付けたときだけ書き換えができる。

作成時にしか決められないパラメータがある点に注意を要する。`mke2fs` の `-i` は何バイトごとにinodeを一つ用意するかを指定し、`-I` はinodeの大きさを指定するが、いずれも作成後には変更できない。小さなファイルが極めて多い用途では、作成時にinodeの数を十分に確保しておく必要がある。

## どこで出てくるか
実験用のディスクやパーティションを用意するときに `mkfs.ext4` を実行するのが最も典型的な場面である。ファイルシステムの性能評価では、`mke2fs` のオプションでジャーナルの有無や機能を変えて条件を揃えることがある。クラッシュや異常終了の後には、`e2fsck` で[[Crash Consistency|一貫性]]を確認する。`e2fsck` をマウント中のファイルシステムに対して実行するのは安全でなく、修復は必ずアンマウントしてから行う。ext4の内部構造を学ぶとき、あるいは自作のツールやファイルシステムが書いたイメージを確かめるときには、`dumpe2fs` や `debugfs` の `stat`・`logdump` で、スーパーブロック、inode、[[JBD2]]のジャーナルの実際の内容を見ることができる。

## 関係
- 使う / 使われる: [[ext4]]
- 関連: [[Superblock]], [[Inode]], [[JBD2]], [[Crash Consistency]]

## 出典
- [E2fsprogs: Ext2/3/4 Filesystem Utilities](https://e2fsprogs.sourceforge.net/)
- [e2fsprogs - Wikipedia](https://en.wikipedia.org/wiki/E2fsprogs)
- [mke2fs(8) - Linux manual page](https://man7.org/linux/man-pages/man8/mke2fs.8.html)
- [e2fsck(8) - Linux manual page](https://man7.org/linux/man-pages/man8/e2fsck.8.html)
- [tune2fs(8) - Linux manual page](https://man7.org/linux/man-pages/man8/tune2fs.8.html)
- [dumpe2fs(8) - Linux manual page](https://man7.org/linux/man-pages/man8/dumpe2fs.8.html)
- [debugfs(8) - Linux manual page](https://man7.org/linux/man-pages/man8/debugfs.8.html)
- [resize2fs(8) - Linux manual page](https://man7.org/linux/man-pages/man8/resize2fs.8.html)
