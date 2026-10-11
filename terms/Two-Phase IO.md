---
aliases: [Two-Phase I/O, Two-phase I/O, 二段階I/O, 2段階I/O, ツーフェーズI/O, Collective Buffering, File Domain, ファイルドメイン, Aggregator, アグリゲータ, 集約役, cb_nodes, cb_buffer_size, cb_config_list, romio_cb_write, romio_cb_read]
tags: [term]
maps: ["[[Parallel Computing]]", "[[HPC Storage]]"]
status: draft
updated: 2026-10-11
---
# Two-Phase I/O（二段階I/O）

> 集団I/Oで、多数のプロセスの細かく飛び飛びのアクセスを、プロセス間の通信と、少数の集約役による大きく連続したファイルアクセスの二段階に分けて実行する最適化である。

## 概要
並列のプログラムでは、各プロセスが受け持つデータがファイル上で小さく飛び飛びの位置に対応することが多い。例えば、行優先でファイルに格納された二次元配列を、行と列の両方向にブロック分割して読み込むと、各プロセスの局所配列の各行は、他のプロセスの行に挟まれてファイル上に散らばる。各プロセスがこれを一行ずつ読むと、小さなI/Oの要求が大量に発生し、性能が大きく低下する。しかし、全プロセスを合わせればファイル全体を読むことになる。二段階I/Oはこの事実を利用する。第一段階では、各プロセスがファイル上の大きく連続した領域を読み、第二段階では、プロセス間の通信でデータを本来の分割に配り直す。I/Oが大きく連続したものになることによる時間の短縮は、通信の追加の費用を大きく上回る。この方法は、del Rosarioらが1993年に分散配列の読み書きについて提案した。書き込みでは順序が逆になり、まず通信でデータを集め、次にファイルに書く。

![[Two-Phase IO.excalidraw]]

[[MPI-IO]]の代表的な実装であるROMIOは、これを一般化し、[[MPI]]の派生データ型で表せる任意の飛び飛びのアクセスに適用している。[[Collective IO|集団I/O]]の呼び出しで、各プロセスはまず自分のアクセスの開始と終了のオフセットを他のプロセスと交換する。全プロセスの要求の最小の開始オフセットから最大の終了オフセットまでの範囲を、I/Oを行うプロセス（集約役、アグリゲータ）の数で等分し、それぞれをその集約役のファイルドメインとする。各プロセスは、自分の要求のどの部分がどのファイルドメインに入るかを計算し、その部分を担当の集約役と交換する。集約役は、自分のファイルドメインを作業用のバッファの大きさごとに区切って処理する。書き込む範囲に隙間がある場合は、読み込んでから書き戻す（read-modify-write）が、ファイルドメインは互いに重ならないため、このとき領域をロックする必要はない。なお、ROMIOの論文によれば、隣り合うランクのどのプロセスの組でもアクセスの範囲が交錯していない場合には、集団I/Oにしても要求をまとめられないと判断し、各プロセスの独立I/Oで処理する。

![[Two-Phase IO File Domains.excalidraw]]

## どこで出てくるか
`MPI_File_write_all` などの集団I/Oの性能を調べるときに、その中身として現れる。ROMIOでは、二段階I/Oをcollective bufferingとも呼び、`MPI_Info` で渡すヒントで調整できる。集約役の最大の数は `cb_nodes`（既定は、ファイルを開いたコミュニケータに含まれるホストの数）、どのホストを集約役にするかは `cb_config_list`、集約役の作業用のバッファの大きさは `cb_buffer_size`（既定は4MB）で指定し、集団読み込みと集団書き込みで二段階I/Oを使うかを `romio_cb_read` と `romio_cb_write`（`enable`、`disable`、`automatic`）で切り替える。使われているヒントの値は `MPI_File_get_info` で確かめられる。

ROMIOは、[[Parallel File System|並列ファイルシステム]]ごとの専用のヒントも持つ。例えば[[Lustre]]向けの `romio_lustre_co_ratio` は、一つのOST（Lustreでデータを格納する記憶対象）に同時にアクセスするクライアントの数の上限を指定する。[[HDF5]]や[[netCDF|PnetCDF]]などの高水準のI/Oライブラリで集団I/Oを有効にしたときも、下ではこの二段階I/Oが動いている。

## 関係
- 上位概念: [[Collective IO]]
- 前提: [[MPI-IO]], [[Access Pattern]]
- 使う / 使われる: [[Collective Communication]]（プロセス間のデータの交換）, [[MPICH]]（ROMIOを含む）
- 関連: [[Parallel File System]], [[Lustre]], [[MPI File View]]

## 出典
- [Data Sieving and Collective I/O in ROMIO (Thakur, Gropp, Lusk, Frontiers '99)](https://www.mcs.anl.gov/~thakur/papers/romio-coll.pdf)
- [Data Sieving and Collective I/O in ROMIO - DOI](https://doi.org/10.1109/FMPC.1999.750599)
- [ROMIO Users Guide (users-guide.tex) - pmodels/mpich GitHub](https://github.com/pmodels/mpich/blob/main/src/mpi/romio/doc/users-guide.tex)
