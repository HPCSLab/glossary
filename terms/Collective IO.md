---
aliases: [Collective I/O, 集団I/O, 集団的I/O, Two-phase I/O, 二段階I/O, Collective Buffering, Aggregator, アグリゲータ, 集約役, Data Sieving, データシービング, cb_nodes, cb_buffer_size, romio_cb_write, MPI_File_write_all]
tags: [term]
maps: ["[[Parallel Computing]]", "[[HPC Storage]]"]
status: draft
updated: 2026-10-11
---
# Collective I/O（集団I/O）

> 多数のプロセスが同時に呼び出す並列I/Oの操作であり、ライブラリが全プロセスのアクセスを把握して、細かい読み書きを少数の大きな読み書きにまとめることを可能にする。

## 概要
並列のプログラムのI/Oは、多数の小さく、飛び飛びの領域へのアクセスになることが多い。これを各プロセスが個別に発行すると、要求の数が膨大になり、性能が大きく低下する。[[MPI-IO]]では、全プロセスが同時に呼び出す集団的な操作（`MPI_File_write_all` のように名前に `_all` を含む）を用意しており、ライブラリは全プロセスがどこを読み書きするかを一度に知ることができる。

MPI-IOの代表的な実装であるROMIO（[[MPICH]]や[[Open MPI]]に含まれる）は、集団I/Oに二段階I/O（two-phase I/O、collective buffering）を用いる。まず、全プロセスのアクセスを解析し、転送すべきファイルの領域を、実際にファイルシステムとやり取りする少数の集約役（アグリゲータ）のプロセスに分担させる。書き込みでは、第一段階で各プロセスのデータを集約役に集め（プロセス間の通信）、第二段階で集約役が大きな連続した領域としてファイルに書く。読み込みでは逆に、集約役が大きく読み込んでから各プロセスに配る。小さな飛び飛びのI/Oが、ネットワークの通信と、少数の大きなI/Oに置き換わる。

![[Two-Phase IO.excalidraw]]

一つのプロセスの飛び飛びのアクセスに対しては、データシービング（data sieving）が用いられる。これは、隙間を含めた大きな領域をまとめて読み、必要な部分だけを取り出す手法であり、I/Oの呼び出しは一回で済むが、不要なデータも読むことになる。

## どこで出てくるか
二段階I/Oの振る舞いは、`MPI_Info` で渡すヒントで調整できる。ROMIOでは、集約役の最大の数を `cb_nodes`（既定はファイルを開いたプロセスのノードの数）、集約役の作業用のバッファの大きさを `cb_buffer_size`（既定は4MB）で指定し、集団書き込みで二段階I/Oを用いるかを `romio_cb_write`（`enable`、`disable`、`automatic`）で切り替える。使われているヒントの値は `MPI_File_get_info` で確かめられる。

[[Parallel File System|並列ファイルシステム]]の上で全プロセスが一つの共有ファイルに書くN-1の[[Access Pattern|アクセスパターン]]では、集団I/Oが性能を左右する。[[HDF5]]や[[netCDF|PnetCDF]]などの高水準のI/Oライブラリも、並列I/Oの下でMPI-IOを用いており、その集団I/Oの設定の影響を受ける。

## 関係
- 上位概念: [[MPI-IO]]
- 使う / 使われる: [[Collective Communication]]（第一段階のデータの集約）, [[HDF5]]
- 関連: [[Access Pattern]], [[Parallel File System]], [[Lustre]], [[Distributed Lock Manager]], [[MPICH]]

## 出典
- [Data Sieving and Collective I/O in ROMIO (Thakur, Gropp, Lusk, Frontiers '99)](https://doi.org/10.1109/FMPC.1999.750599)
- [Data sieving and collective I/O in ROMIO - UNT Digital Library](https://digital.library.unt.edu/ark:/67531/metadc722449/)
- [ROMIO Users Guide (users-guide.tex) - pmodels/mpich GitHub](https://github.com/pmodels/mpich/blob/main/src/mpi/romio/doc/users-guide.tex)
