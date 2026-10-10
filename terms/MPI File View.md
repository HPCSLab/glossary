---
aliases: [File View, ファイルビュー, MPI_File_set_view, etype, filetype]
tags: [term]
maps: ["[[Parallel Computing]]", "[[HPC Storage]]"]
status: draft
updated: 2026-10-11
---
# MPI File View（ファイルビュー）

> [[MPI-IO]]において、各プロセスがファイルのどの部分をどのような並びとして見るかを定める設定であり、開始位置（displacement）、etype、filetype、データ表現の四つからなる。

## 概要
[[POSIX]]のファイルは一続きのバイト列であり、多数のプロセスがファイルを分担して読み書きするには、各プロセスが自分の担当する位置を計算し、飛び飛びの領域ごとに `lseek` と `write` を繰り返す必要がある。MPI-IOのファイルビューは、この分担を[[MPI]]の派生データ型で一度に宣言できるようにしたものである。規格の定義では、ビューは、オープンしたファイルのうち現在見えてアクセスできるデータを、etypeの順序付きの集まりとして定める。

ビューは `MPI_File_set_view` で設定する。displacementは、ビューが始まる位置をファイル先頭からのバイト数で表し、ファイルのヘッダを読み飛ばすのに用いる。etype（elementary datatype）は、データのアクセスと位置指定の単位であり、オフセットやファイルポインタはバイトではなくetypeの個数で数える。filetypeは、etypeの並びと穴（hole）からなる型紙であり、displacementから始めて繰り返し敷き詰められてビューを形づくる。穴の部分のデータはそのプロセスからは見えない。そのため、各プロセスが互いに補い合うfiletypeを設定すると、全体として一つのファイルをプロセス間で分割する配置を表現できる。例えば、二次元配列をブロックに分けた場合、各プロセスは `MPI_Type_create_subarray` で作った自分のブロックの型をfiletypeとし、ファイル上では飛び飛びの領域を、連続したデータとして一回の呼び出しで読み書きできる。データ表現（datarep）は、メモリ上の表現をそのまま書く `"native"` のほか、実装に依存しない `"external32"` などを文字列で指定する。

![[MPI File View Tiling.excalidraw]]

`MPI_File_set_view` は、ファイルをオープンしたプロセス群の[[Collective Communication|集団操作]]である。datarepは全プロセスで同じでなければならないが、displacementとfiletypeはプロセスごとに異なってよい。呼び出すと、各プロセスのファイルポインタと共有ファイルポインタは0に戻る。filetypeの変位は負でなく、単調非減少でなければならず、書き込み用のファイルでは一つのfiletypeの中に重なる領域を含めてはならない。一方、異なるプロセスのfiletypeどうしが重なることは許される。

## どこで出てくるか
ファイルビューは、MPI-IOで共有ファイルに書くN-1型の[[Access Pattern|アクセスパターン]]を記述する基本の手段である。各プロセスの要求が小さく飛び飛びである場合でも、ビューによって全プロセスのアクセス範囲をライブラリに伝えることができ、これが[[Collective IO|集団I/O]]の二段階I/Oやデータシービングによる最適化の前提となる。[[HDF5]]や[[netCDF|PnetCDF]]のような高水準I/Oライブラリを用いる場合は、ビューを直接書くことはないが、これらはMPI-IOを下位層として用いるため、配列の一部を並列に読み書きする要求は最終的にMPI-IOへのアクセスとして発行される。プログラムを読む際には、`MPI_File_write_at` などに渡すオフセットがバイト単位ではなく、ビューに対するetype単位である点に注意が要る。

## 関係
- 上位概念: [[MPI-IO]]
- 前提: [[MPI]]
- 使う / 使われる: [[Collective IO]]
- 関連: [[Access Pattern]], [[POSIX]]

## 出典
- [15.3. File Views - MPI 4.1 Standard](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node361.htm)
- [Definitions (I/O) - MPI 3.1 Standard](https://www.mpi-forum.org/docs/mpi-3.1/mpi31-report/node306.htm)
- [15.5.2. External Data Representation: "external32" - MPI 4.1 Standard](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node377.htm)
- [MPI_File_set_view - Open MPI documentation](https://docs.open-mpi.org/en/v5.0.x/man-openmpi/man3/MPI_File_set_view.3.html)
