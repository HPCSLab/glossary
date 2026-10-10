---
aliases: [fstests, xfstests-dev, xfstests-bld, kvm-xfstests, gce-xfstests, ファイルシステム回帰テスト]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# xfstests

> Linuxの主要な[[File System|ファイルシステム]]に共通して使われる、回帰テストのためのテストスイートである。fstestsとも呼ばれる。

## 概要
xfstestsは、もともとSGIが[[XFS]]のために開発したテスト群であり、現在はLinux上で[[ext4]]、[[btrfs]]、XFS、[[NFS]]、tmpfsなど多くのファイルシステムの回帰テストに使われている。XFS専用ではなくなったため、fstestsとも呼ばれる。回帰テストとは、ある変更の前後で同じテスト群を実行し、以前は動いていた機能が壊れていないかを確かめることである。xfstestsは性能の測定を主な目的とするものではない。

テストを実行するには、`local.config` に二つの[[Block Storage|ブロックデバイス]]とそのマウント先を書く。`TEST_DEV`（`TEST_DIR` にマウント）は必須で、テストの間で再フォーマットされない、長く使われるファイルシステムとして扱われる。`SCRATCH_DEV`（`SCRATCH_MNT` にマウント）は、テストが必要に応じてmkfsし直すための領域であり、中身は上書きされる。対象のファイルシステムは `FSTYP` で指定するか、`TEST_DEV` から判定される。

テストはシェルスクリプトであり、`tests/generic/` にファイルシステムに依存しないテスト、`tests/xfs/`・`tests/ext4/`・`tests/btrfs/` などに各ファイルシステムに固有のテストが置かれる。`./check` が各スクリプトを実行し、終了コードを調べるとともに、出力を期待出力のファイル（例：`007.out`）と比較する。一致しなければ差分を表示し、`.out.bad` を残す。各テストは複数のグループに属し、`./check -g quick` のようにグループ単位で実行できる。既定ではauto（自動実行向け）グループのテストが実行され、quickは短時間の動作確認用、dangerousはカーネルをクラッシュさせうるテストである。

## どこで出てくるか
[[Linux Kernel|カーネル]]のファイルシステムの開発では、多くのメンテナが変更を送る前にxfstestsを一通り実行しており、大きな変更にはxfstestsでの確認を求めることが多い。対象のファイルシステムに厳密な制限はなく、[[FUSE]]で実装したファイルシステムも基本的な対応の水準で試験できる。

[[Crash Consistency|クラッシュ整合性]]のテストには[[Device Mapper|device mapper]]が使われる。dm-flakeyで書き込みを黙って捨ててから再マウントすることで、クラッシュや電源断を模擬する。dm-log-writesで書き込みをすべて記録し、印を付けた時点まで再生して、その時点のクラッシュ後の状態を確かめる。

実行環境を整えるラッパーとしてxfstests-bldがあり、[[QEMU]]/[[KVM]]の[[Virtual Machine|仮想マシン]]で実行するkvm-xfstests、Google Compute Engineで実行するgce-xfstestsを含む。本体はgit.kernel.orgの `fs/xfs/xfstests-dev.git` で管理され、パッチはfstests@vger.kernel.orgに送る。

## 関係
- 使う / 使われる: [[Device Mapper]], [[QEMU]]
- 対比: [[fio]]（性能の測定が目的で、正しさの回帰テストではない）
- 関連: [[XFS]], [[ext4]], [[btrfs]], [[Crash Consistency]], [[e2fsprogs]]

## 出典
- [README - xfstests-dev (kernel.googlesource.com mirror)](https://kernel.googlesource.com/pub/scm/fs/xfs/xfstests-dev/+/refs/heads/master/README)
- [What is xfstests? - xfstests-bld](https://kernel.googlesource.com/pub/scm/fs/ext2/xfstests-bld/+/HEAD/Documentation/what-is-xfstests.md)
- [xfstests-bld README](https://kernel.googlesource.com/pub/scm/fs/ext2/xfstests-bld/+/HEAD/README.md)
- [common/dmflakey - xfstests-dev](https://kernel.googlesource.com/pub/scm/fs/xfs/xfstests-dev/+/refs/heads/master/common/dmflakey)
- [common/dmlogwrites - xfstests-dev](https://kernel.googlesource.com/pub/scm/fs/xfs/xfstests-dev/+/refs/heads/master/common/dmlogwrites)
- [The 2010 Linux Storage and Filesystem Summit, day 1 - LWN.net](https://lwn.net/Articles/399148/)
