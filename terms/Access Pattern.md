---
aliases: [I/O Access Pattern, IO Access Pattern, アクセスパターン, I/Oパターン, I/Oのアクセスパターン, Sequential Access, 逐次アクセス, シーケンシャルアクセス, Random Access, ランダムアクセス, N-N, N-1, File-per-process, Shared File, 共有ファイル, N-1 Strided, Strided Access, ストライドアクセス, PLFS]
tags: [term]
maps: ["[[HPC Storage]]", "[[Parallel Computing]]"]
status: draft
updated: 2026-10-10
---
# Access Pattern（I/Oのアクセスパターン）

> アプリケーションがファイルや記憶装置を読み書きする際の、位置の順序、一回の大きさ、読み書きの割合、複数のプロセスによるファイルの分け方などの特徴の総称である。

## 概要
I/Oの性能は、同じ量のデータでも、アクセスパターンによって大きく変わる。主な観点は次のとおりである。

第一は位置の順序である。直前のアクセスのすぐ後ろを読み書きする連続（consecutive）なアクセス、直前より後ろの位置に飛びながら進む順方向（sequential）のアクセス、位置が無作為に変わるランダムなアクセスがある。一定の間隔で飛び飛びにアクセスする場合を、ストライド（strided）のアクセスと呼ぶ。[[HDD]]ではランダムなアクセスのたびにヘッドの移動が必要になるため、連続したアクセスとの性能の差が特に大きい。

第二は一回のアクセスの大きさである。小さな読み書きを多数行うと、[[System Call|システムコール]]や要求の処理の負担が相対的に大きくなり、[[Bandwidth|バンド幅]]を使い切れない。第三は、読み込みと書き込みの割合と、その切り替えの頻度である。第四は、ファイルの中の位置が、記憶装置やファイルシステムの区切り（ブロックや[[Lustre]]のストライプ）にそろっているか（アラインメント）である。また、大量の小さなファイルの作成や削除のように、データよりも[[Metadata|メタデータ]]の操作が中心となるパターンもある。

## 並列I/Oのパターン
多数のプロセスが並列にファイルを書く場合、各プロセスが自分のファイルに書くN-N（file-per-process）と、全プロセスが一つの共有ファイルに書くN-1がある。N-1のうち、各プロセスの書き込みがファイル全体にわたって他のプロセスの書き込みと交互に並ぶものをN-1 stridedと呼ぶ。この場合、各プロセスは小さく、区切りにそろわない書き込みを、他のプロセスと入り混じって行うことになる。利用者に好まれるN-1のパターンは、並列ファイルシステムで性能が極めて悪くなることがある。複数のプロセスが同じストライプに書き込むと、[[Distributed Lock Manager|ロック]]の奪い合いも起きる。一方、N-Nは、全てのプロセスが一斉にファイルを作成するため、[[Metadata|メタデータ]]の処理に大きな負荷がかかる（[[IndexFS]]を参照）。

このような問題に対して、[[MPI-IO]]の[[Collective IO|集団I/O]]は、多数の小さな書き込みを少数の大きな書き込みにまとめる。チェックポイント向けの仮想的なファイルシステムPLFS（SC09）は、アプリケーションの悪いアクセスパターンを、並列ファイルシステムが得意とするアクセスパターンに変換し、アプリケーションを改変せずに、複数のアプリケーションとベンチマークで桁違いの改善を得た。

## どこで出てくるか
I/Oの性能を測る際には、対象のアプリケーションのアクセスパターンに合わせてベンチマークを設定する必要がある。[[IOR]]では、一回の転送の大きさ（`-t`）、ブロックの大きさ（`-b`）、N-NとN-1の切り替え（`-F`）、ランダムな位置（`-z`）などを指定できる。実際のアプリケーションのアクセスパターンは、HPCのI/Oの特性を記録するツールである[[Darshan]]で調べられる。Darshanは、ファイルごとに、連続なアクセスと順方向のアクセスの回数、読み書きの大きさのヒストグラム、よく現れるストライドとアクセスの大きさ、区切りにそろわないアクセスの回数などを記録する。

## 関係
- 関連: [[IOR]], [[MPI-IO]], [[Parallel File System]], [[Lustre]], [[HDD]], [[SSD]], [[Metadata]], [[mdtest]], [[Distributed Lock Manager]], [[IndexFS]], [[Darshan]], [[Collective IO]]

## 出典
- [PLFS: A Checkpoint Filesystem for Parallel Applications (Bent et al., SC09)](https://doi.org/10.1145/1654059.1654081)
- [File Systems for the World's Fastest Computer (PDSW09) - LANL](https://www.pdsw.org/pdsw09/resources/LANL.pdf)
- [Petascale Data Storage Institute Final Report - OSTI](https://www.osti.gov/servlets/purl/1150023)（N-1 stridedの書き込みの例）
- [IndexFS (SC14) - Parallel Data Lab, CMU](https://www.pdl.cmu.edu/PDL-FTP/FS/IndexFS-SC14.pdf)（N-N型のチェックポイントのファイル作成）
- [darshan-hpc/darshan - GitHub](https://github.com/darshan-hpc/darshan)
- [darshan-util documentation (Guide to darshan-parser output) - GitHub](https://github.com/darshan-hpc/darshan/blob/main/darshan-util/doc/darshan-util.rst)
- [hpc/ior - GitHub](https://github.com/hpc/ior)
