---
aliases: [mercury, Mercury RPC, RPC, Remote Procedure Call, 遠隔手続き呼び出し, Bulk Transfer, NA Plugin]
tags: [term]
maps: ["[[HPC Storage]]", "[[Network]]"]
status: draft
updated: 2026-10-10
---
# Mercury

> 高速なネットワークを持つHPCシステムのために設計された、遠隔手続き呼び出し（RPC）のフレームワークである。

## 概要
RPCは、別の計算機上の関数を、あたかも手元の関数のように呼び出す仕組みである。呼び出し側は引数をメッセージにして送り、受け側は対応する処理（ハンドラ）を実行して結果を返す。Mercuryは、米国アルゴンヌ国立研究所とThe HDF Groupが共同で開発したRPCのフレームワークであり、HPCの高速なネットワークの能力を活かすことに重点を置いている。

Mercuryの特徴は、小さなRPCのメッセージと、大きなデータの転送を分けて扱う点にある。関数の引数のような小さなデータは、RPCのメッセージに含めて送る。一方、大きなデータは、送り手がそのメモリ領域を「バルク」として公開し、その記述子だけをRPCで送り、受け手が[[RDMA]]などの遠隔メモリアクセスによって必要なときに直接読み書きする。これにより、大きなデータを中継の複製なしに効率よく転送できる。ネットワークの違いは、NA（network abstraction）層のプラグインによって吸収され、libfabric（OFI）、[[UCX]]、共有メモリなどを同じ方法で利用できる。APIは非同期であり、要求の発行と完了の処理は、進行（progress）と完了の確認（trigger）を明示的に呼んでコールバックとして行う。

## どこで出てくるか
Mercuryは、HPC向けのストレージシステムやデータサービスの通信基盤として用いられており、[[DAOS]]もMercuryを用いている。アルゴンヌ国立研究所などが進めるMochiプロジェクトでは、Mercuryを基盤として、ストレージサービスを部品の組み合わせで構築する。ただし、Mercuryの非同期でコールバック中心のAPIを直接使って複雑なサービスを書くのは難しいため、Mochiでは、[[Argobots|ユーザレベルスレッド]]と組み合わせて逐次的な書き方を可能にした[[Margo]]を介して用いるのが一般的である。HPC向けの分散ストレージや、[[Parallel File System|並列ファイルシステム]]の代替となる仕組みを研究で試作する際の有力な基盤である。

## 関係
- 使う / 使われる: [[RDMA]], [[UCX]], [[Verbs]]（転送手段）, [[DAOS]], [[Margo]]（Mercuryを使う）
- 対比: [[MPI]]（並列計算のためのメッセージ通信）
- 関連: [[Parallel File System]], [[Latency]]

## 出典
- [Mercury](https://mercury-hpc.github.io/)
- [Mochi documentation](https://mochi.readthedocs.io/en/latest/)
