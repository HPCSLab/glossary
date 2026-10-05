---
aliases: [MPI I/O, MPI_File, ROMIO, 並列I/O]
tags: [term]
maps: ["[[Parallel Computing]]", "[[Storage]]"]
status: draft
updated: 2026-10-05
---
# MPI-IO

> [[MPI]]規格の一部として定められた並列ファイルI/Oのインタフェースであり、多数のプロセスが一つのファイルを協調して読み書きするための機能を提供する。

## 概要
MPI-IOはMPI-2.0で導入された。規格自身が述べるとおり、[[POSIX]]のインタフェースは、ファイルを複数のプロセスで分担する記述や、全プロセスが協調して行う集団的な転送を表現できないため、並列I/Oに必要な最適化の余地が乏しい。MPI-IOはこれを補うため、プロセス群によるファイルの共同オープン、データ型を用いたファイルの分割の記述、集団的I/O、非同期I/O、ファイルの物理配置の制御を提供する。

ファイルは `MPI_File_open` により、コミュニケータに属する全プロセスが集団的にオープンする。各プロセスは `MPI_File_set_view` でファイルのビューを設定する。ビューは、ファイル先頭からの開始位置（displacement）、アクセスの単位となるデータ型（etype）、ファイル上で自分が担当する部分の型紙となるデータ型（filetype）からなる。例えば、行列をブロックに分けて各プロセスが担当する場合、filetypeに飛び飛びの領域を表す派生データ型を指定すれば、各プロセスは自分の担当部分だけを連続したデータとして読み書きできる。読み書きの位置の指定には、明示的なオフセット（`MPI_File_write_at` のように名前に `_at` を含む）、プロセスごとのファイルポインタ、全プロセスで共有するファイルポインタの三方式がある。

各操作には、プロセスが個別に行う独立I/Oと、全プロセスが同時に呼び出す集団I/O（`MPI_File_write_at_all` のように名前に `_all` を含む）がある。集団I/Oでは、ライブラリが全プロセスのアクセスを把握できるため、最適化が可能となる。代表的な実装であるROMIOは、一部のプロセスを集約役（アグリゲータ）としてデータを集め、大きな連続領域としてまとめてファイルに書く二段階I/O（two-phase I/O、collective buffering）を行う。また、細かく飛び飛びの領域へのアクセスを、隙間を含めた大きな連続アクセスに置き換えるデータシービング（data sieving）も行う。これらの挙動は、`MPI_Info` によるヒントで調整できる。規格は、集約役の数を指定する `cb_nodes`、その作業用バッファの大きさを指定する `cb_buffer_size`、ファイルを分散させるI/O装置の数と単位を指定する `striping_factor`・`striping_unit` などを予約している。

一貫性の意味論はPOSIXより弱い。既定の非アトミックモードでは、異なるプロセスが同じ領域に衝突するアクセスを行った場合、結果の逐次一貫性は保証されない。あるプロセスが書いたデータを別のプロセスが確実に読むには、`MPI_File_sync`、`MPI_Barrier`、`MPI_File_sync` の順に呼ぶ「sync-barrier-sync」の手順を踏むか、`MPI_File_set_atomicity` でアトミックモードを有効にする必要がある。この緩和は、実装がPOSIXの厳密な一貫性を維持するコストを避けられるようにするためのものである。

## どこで出てくるか
[[Parallel File System|並列ファイルシステム]]上で全プロセスが一つの共有ファイルに書くN-1型のI/Oでは、各プロセスの書き込みが小さく飛び飛びであると、[[Distributed Lock Manager|ロック]]の競合と細かいI/Oにより性能が大きく低下する。集団I/Oによる集約は、これを少数の大きな書き込みに変換する代表的な手段であり、集約役の数や配置を[[Lustre]]のストライプ構成に合わせることが性能上の要点となる。科学技術計算で広く用いられるHDF5やPnetCDFなどの高水準I/Oライブラリは、並列I/Oの下位層としてMPI-IOを用いている。そのため、アプリケーションがMPI-IOを直接呼ばない場合でも、その性能特性がI/O性能を左右する。

## 関係
- 上位概念: [[MPI]]
- 前提: [[POSIX]], [[Parallel File System]]
- 使う / 使われる: [[Lustre]], [[HDF5]]（MPI-IOを使う）
- 対比: [[POSIX]]（一貫性の意味論が強い）
- 関連: [[Collective Communication]], [[Consistency Model]], [[write]]

## 出典
- [MPI: A Message-Passing Interface Standard Version 4.1, Chapter 14 I/O - MPI Forum](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report.pdf)
- [MPI Documents - MPI Forum](https://www.mpi-forum.org/docs/)
