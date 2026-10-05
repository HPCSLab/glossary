---
aliases: [一貫性モデル, 整合性モデル, Memory Consistency Model, メモリ一貫性モデル, Eventual Consistency, 結果整合性, Causal Consistency, 因果一貫性, Sequential Consistency, 逐次一貫性, Read Your Writes, TSO, Close-to-Open Consistency]
tags: [term]
maps: ["[[Distributed Systems]]", "[[Storage]]"]
status: draft
updated: 2026-10-06
---
# Consistency Model（一貫性モデル）

> 複数の主体が共有データを並行に読み書きするとき、どの読み込みがどの書き込みの結果を返しうるかを定める規則である。

## 概要
共有データの複製やキャッシュが存在するシステムでは、ある書き込みの結果がいつ、誰から見えるようになるかは自明ではない。一貫性モデルは、システムが取りうる実行の履歴のうち、どれを正しいものとして許すかを定める。強いモデルほど利用者にとって直感的であるが、実装には複製間の協調が必要となり、性能と可用性が低下する。弱いモデルほど実装は高速で可用性も高いが、利用者は古い値を読む可能性を考慮してプログラムを書く必要がある。

代表的なモデルを強い順に挙げる。[[Linearizability|線形化可能性]]は、各操作が呼び出しから応答までの間の一瞬で実行されたかのように見え、その順序が実時間と一致することを要求する。逐次一貫性（sequential consistency）は、全操作が各プロセスのプログラム順序を保った一つの順序で実行されたように見えることを要求するが、実時間との一致は問わない。因果一貫性（causal consistency）は、因果関係のある操作の順序のみを全員が同じように観測することを要求し、無関係な操作の順序は観測者ごとに異なってよい。さらに弱いモデルとして、自分の書き込みは以後の自分の読み込みに必ず反映されるread-your-writesなどのセッション保証や、更新が止まればいずれ全複製が同じ値に収束することのみを保証する結果整合性（eventual consistency）がある。複数の操作をまとめたトランザクションについては、直列化可能性（serializability）やスナップショット分離などの、別系統の基準がある。

ネットワークの分断が起きても全ノードが応答し続ける（可用性を保つ）ことと両立できるのは、因果一貫性程度までの弱いモデルに限られ、逐次一貫性以上の強いモデルとは両立しない。これは、CAP定理として知られる制約を一般化したものである。

## どこで出てくるか
一貫性モデルは、分野ごとに異なる名前で現れるが、問いは共通である。CPUでは、メモリ一貫性モデルとして現れる。x86は、各プロセッサの書き込みがいったんストアバッファに置かれるため、逐次一貫性より弱いTSO（Total Store Order）を採用しており、ARMなどはさらに弱いモデルを採る。並行プログラムでメモリバリアやアトミック操作が必要となるのはこのためである。

ストレージでは、[[POSIX]]が `write()` の完了後のすべての `read()` にその結果を反映することを求める強い意味論を定めている。これに対し、[[NFS]]は、ファイルを閉じた時点で書き込みをサーバに反映し、開いた時点でキャッシュの有効性を確かめるclose-to-open一貫性を採用する。[[MPI-IO]]は、既定では衝突するアクセスの順序を保証せず、sync-barrier-syncの手順か、アトミックモードを要求する。[[Object Storage|オブジェクトストレージ]]のAmazon S3は、キー単位の強い一貫性を提供する一方、複数のキーにまたがる不可分な更新は提供しない。[[Parallel File System|並列ファイルシステム]]がPOSIXの強い意味論を維持するためのロックのコストは、HPCストレージ研究の主要な論点であり、意味論を緩和した設計が数多く提案されている。システムを使う側としては、どのモデルが提供されているかを把握しなければ、正しいプログラムを書くことも、性能の数値を公平に比較することもできない。

## 関係
- 使う / 使われる: [[Linearizability]]（代表的な強いモデル）
- 関連: [[POSIX]], [[MPI-IO]], [[Object Storage]], [[Parallel File System]], [[Lustre]], [[Raft]], [[Consensus]]

## 出典
- [Consistency Models - Jepsen](https://jepsen.io/consistency/models)
- [Sequential Consistency - Jepsen](https://jepsen.io/consistency/models/sequential)
- [x86-TSO: A Rigorous and Usable Programmer's Model for x86 Multiprocessors (Sewell et al., CACM 2010)](https://www.cl.cam.ac.uk/~pes20/weakmemory/cacm.pdf)
- [RFC 7530: Network File System (NFS) Version 4 Protocol, Section 10.3.1](https://datatracker.ietf.org/doc/html/rfc7530#section-10.3.1)
- [write, pwrite - The Open Group Base Specifications Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/functions/write.html)
- [What is Amazon S3? - Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
