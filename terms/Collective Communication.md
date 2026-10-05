---
aliases: [集団通信, Collective, Collective Operation, 集団操作, Allreduce, MPI_Allreduce, Broadcast, Bcast, Alltoall, Allgather, Reduce-Scatter, Barrier, NCCL, Ring Allreduce]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-06
---
# Collective Communication（集団通信）

> 通信に参加するプロセスの集団の全員が関与して、データの配布、収集、集約、交換を行う通信である。

## 概要
集団通信は、一対一の送受信を組み合わせれば実現できる通信パターンのうち、並列プログラムで頻繁に現れるものを、まとまった操作として提供するものである。[[MPI]]では、コミュニケータに属する全プロセスが同じ関数を呼び出すことで実行される。主な操作は次のとおりである。

| 操作 | 内容 |
|---|---|
| Barrier | 全員が到達するまで待つ（同期） |
| Bcast | 一つのプロセスのデータを全員に配る |
| Scatter / Gather | 一つのプロセスのデータを分割して配る / 全員のデータを一つのプロセスに集める |
| Allgather | 全員のデータを集めて、全員が全体を受け取る |
| Reduce / Allreduce | 全員の値を総和などで集約し、一つのプロセス / 全員が結果を受け取る |
| Reduce-scatter | 集約した結果を分割して全員に配る |
| Alltoall | 全員が全員と異なるデータを交換する |

集団通信をまとめた操作として提供することには、記述の簡潔さに加えて、実装がプロセス数、データ量、ネットワークの構成に応じて最適なアルゴリズムを選べるという利点がある。例えば、Bcastを根のプロセスから全員へ順に送る素朴な方法では、$p$ 個のプロセスに対して $p-1$ 回の送信が逐次に必要となる。二分木状に送り先を倍々に増やす方法（二項木）を用いれば、約 $\log_2 p$ 段で完了する。Allreduceでは、データが小さい場合は段数を少なくして[[Latency|レイテンシ]]を抑えるアルゴリズムが、データが大きい場合は各プロセスが送受信するデータ量を抑えて[[Bandwidth|バンド幅]]を有効に使うアルゴリズムが有利となる。後者の代表例であるリング型のAllreduceは、プロセスを環状に並べ、データを分割して隣へ順に送りながら集約と配布を行う。これにより、各プロセスが送受信する量は、プロセス数によらずデータの約2倍に抑えられる。

## どこで出てくるか
集団通信は、並列プログラムの性能を大きく左右する。多くの集団通信は、全員の参加を必要とするため、実質的な同期点として働く。一つのプロセスでも到着が遅れると全員が待たされるため、負荷の不均衡やシステムのノイズによる遅れが、集団通信の待ち時間として表面化する。[[Weak Scaling|弱スケーリング]]では、プロセス数が増えるにつれて集団通信のコストが増大し、効率を低下させる主要な要因となる。[[Strong Scaling|強スケーリング]]では、プロセスあたりのデータが小さくなるため、レイテンシが支配的となる。

機械学習の分散学習では、各GPUが計算した勾配の総和をAllreduceで求める処理が中心となり、GPU向けの集団通信ライブラリNCCLが広く用いられている。性能の分析では、集団通信の呼び出し回数とデータ量、各プロセスの到着時刻のばらつきを計測することが基本となる。また、ノンブロッキング集団通信（`MPI_Iallreduce` など）を用いて、集団通信と計算を重ね合わせる手法もある。

## 関係
- 上位概念: [[MPI]]
- 使う / 使われる: [[InfiniBand]], [[RDMA]]
- 関連: [[Latency]], [[Bandwidth]], [[Weak Scaling]], [[Strong Scaling]], [[Parallel Efficiency]], [[MPI-IO]]

## 出典
- [MPI: A Message-Passing Interface Standard Version 4.1, Chapter 7 Collective Communication - MPI Forum](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node114.htm)
- [Collective Operations - NCCL documentation](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html)
