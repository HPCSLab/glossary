---
aliases: [Linux, Linuxカーネル, カーネル, Kernel, mainline, LTS, Longterm Kernel, Kernel Module, カーネルモジュール]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-06
---
# Linux Kernel（Linuxカーネル）

> 1991年にLinus Torvaldsが開発を始めた、オープンソースのUnix系オペレーティングシステムカーネルである。

## 概要
カーネルは、ハードウェアを管理し、その上で動作するプログラムに資源を配分する、OSの中核部分である。Linuxカーネルは、プロセスのスケジューリング、[[Virtual Memory|仮想記憶]]によるメモリ管理、[[VFS]]を中心とするファイルシステム、[[blk-mq]]を基盤とするブロック層、ネットワーク、デバイスドライバなどの機能を担う。アプリケーションはユーザ空間で動作し、これらの機能を[[System Call|システムコール]]を通じて利用する。Linuxカーネルの上にCライブラリ、シェル、各種ツールなどを組み合わせて配布したものがLinuxディストリビューションであり、日常的に「Linux」と呼ばれるのはこの全体であることが多い。

設計上は、主要な機能のすべてが一つのアドレス空間内で特権モードで動作するモノリシックカーネルである。ただし、デバイスドライバやファイルシステムなどの多くは、実行中に読み込みと取り外しが可能なカーネルモジュールとして構成できる。主にC言語で書かれており、Linux 6.1以降はRustによる記述も導入されている。ライセンスはGPLv2である。TOP500の上位500台のスーパーコンピュータは、すべてLinuxで動作している。

開発は時間に基づく周期で進む。新しい版の開発は、約2週間のマージウィンドウで新機能を取り込むことから始まる。その後、毎週のリリース候補（-rc）による安定化の期間を経て、2〜3か月ごとに新しい版が公開される。新機能はLinus Torvaldsが管理するmainlineのツリーにのみ入る。リリース後の版には、mainlineで修正済みの不具合修正のみが取り込まれる（stable）。一部の版は長期保守版（longterm、LTS）として数年間保守される。変更はパッチとしてメーリングリストに投稿され、サブシステムごとのメンテナが審査して自身のツリーに取り込み、マージウィンドウにmainlineへ統合される。

## どこで出てくるか
カーネルの機能や挙動は版によって大きく異なるため、OSやストレージの研究では、使用したカーネルの版を実験条件として明記する必要がある。版は `uname -r` で確認できる。[[io_uring]]（5.1）、sched_ext（6.12）など、新しい機能の多くは特定の版以降でしか使えない。また、ディストリビューションのカーネルは、LTSを基に独自の修正や機能の取り込み（バックポート）を加えていることが多く、版番号だけでは機能の有無を判断できない場合がある。

研究目的でカーネルを改変する場合、カーネル内部のAPIは安定性が保証されず、版が変わると関数やデータ構造が変更されうることに注意を要する。一方、ユーザ空間に対するシステムコールのインタフェースは極めて安定しており、既存のアプリケーションを壊さないことが開発の強い原則となっている。カーネルを改変・再構築せずに機能を追加・観測する手段として、[[BPF]]、カーネルモジュール、ユーザ空間で処理を担う[[FUSE]]や[[ublk]]などが用いられる。ソースコードの調査にはElixir Cross Referencerが、各版の変更点の把握にはKernel Newbiesのまとめが、公式の解説には docs.kernel.org が便利である。

## 関係
- 使う / 使われる: [[System Call]]（ユーザ空間へのインタフェース）, [[VFS]], [[Page Cache]], [[blk-mq]], [[Virtual Memory]]
- 関連: [[POSIX]], [[BPF]], [[io_uring]], [[FUSE]], [[ublk]]

## 出典
- [Linux kernel - Wikipedia](https://en.wikipedia.org/wiki/Linux_kernel)
- [How the development process works - The Linux Kernel documentation](https://docs.kernel.org/process/2.Process.html)
- [Releases - The Linux Kernel Archives](https://www.kernel.org/category/releases.html)
- [The Linux Kernel Driver Interface - The Linux Kernel documentation](https://docs.kernel.org/process/stable-api-nonsense.html)
- [Elixir Cross Referencer - Bootlin](https://elixir.bootlin.com/linux/latest/source)
- [Kernel Newbies](https://kernelnewbies.org/)
