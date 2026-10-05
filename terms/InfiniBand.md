---
aliases: [インフィニバンド, IB, HCA, Subnet Manager, サブネットマネージャ, Fat Tree, ファットツリー]
tags: [term]
maps: ["[[Parallel Computing]]", "[[Network]]"]
status: draft
updated: 2026-10-05
---
# InfiniBand

> 高いスループットと低いレイテンシを特徴とし、HPCのノード間接続に広く用いられるネットワークの規格である。

## 概要
InfiniBandは、1999年に競合していた二つの規格（IntelらのNGIOと、IBMらのFuture I/O）が統合されて生まれ、業界団体InfiniBand Trade Association（IBTA）が仕様を策定している。現在の主要な製造元は、NVIDIAに買収されたMellanoxである。[[RDMA]]をネットワークの基本機能として備えており、CPUの負荷を抑えつつ低遅延の通信を実現する。HPCの用途では、アダプタ単体のレイテンシはマイクロ秒未満に達する。2014年から2016年にかけては、TOP500のスーパーコンピュータで最も多く用いられた接続方式であった。

速度の世代は、SDR、DDR、QDR、FDR、EDR、HDR、NDR、XDRという三文字の略号で呼ばれる。通常は4本のレーンを束ねた4xリンクで用いられ、例えばHDRは200Gbit/s、2024年に登場したXDRは800Gbit/sである。速度はビット毎秒で表記されるため、バイト単位の[[Bandwidth|バンド幅]]と比較する際には8で割る必要がある。

ネットワークは、各ノードに搭載したアダプタ（HCA: Host Channel Adapter）とスイッチから構成されるスイッチドファブリックである。サブネット内の経路設定やアドレスの割り当ては、サブネットマネージャと呼ばれるソフトウェアが集中的に行う。また、受信側の空き容量を確認してから送信するクレジットベースのフロー制御により、混雑時にもパケットを破棄しない。HPCシステムでは、スイッチを多段に組み合わせ、上位の階層ほど多くの帯域を持たせるファットツリーなどのトポロジで接続されることが多い。

## どこで出てくるか
多くのスーパーコンピュータとHPCクラスタで、計算ノード間の[[MPI]]通信と、[[Parallel File System|並列ファイルシステム]]へのアクセスの両方にInfiniBandが用いられる。通信性能の評価では、ネットワークの世代、リンクの本数、トポロジ、ノード間のスイッチの段数を把握する必要がある。同じスイッチに接続されたノード同士と、上位のスイッチを経由するノード同士とでは、レイテンシや競合の程度が異なるためである。状態の確認には `ibstat` や `ibv_devinfo` を、性能の測定にはperftestの `ib_write_bw`・`ib_write_lat` や、MPIレベルのOSU Micro-Benchmarksを用いる。Ethernet上でRDMAを行う[[RoCE]]は、InfiniBandと同じ[[Verbs|verbs]]のインタフェースを用いるため、ソフトウェアの多くを共通に利用できる。

## 関係
- 使う / 使われる: [[RDMA]], [[MPI]], [[Lustre]]
- 関連: [[Latency]], [[Bandwidth]], [[Collective Communication]]

## 出典
- [InfiniBand - Wikipedia](https://en.wikipedia.org/wiki/InfiniBand)
- [Remote direct memory access - Wikipedia](https://en.wikipedia.org/wiki/Remote_direct_memory_access)
