---
aliases: [darshan, darshan-runtime, darshan-util, darshan-parser, darshan-job-summary, PyDarshan, DXT, Darshan eXtended Tracing, I/O Characterization, I/Oの特性評価]
tags: [term]
maps: ["[[HPC Storage]]", "[[Parallel Computing]]"]
status: draft
updated: 2026-10-10
---
# Darshan

> HPCのアプリケーションが行ったI/Oの[[Access Pattern|アクセスパターン]]を、アプリケーションを改変せずに小さな負担で記録する、アルゴンヌ国立研究所などが開発する特性評価のツールである。

## 概要
Darshanは、Carnsらが2009年のIEEE Clusterで、ペタスケールの計算機のI/Oの負荷を常時記録するために発表した。記録を取る部分（darshan-runtime）と、記録を解析する部分（darshan-util）からなる。

darshan-runtimeは、コンパイル時のラッパか、実行時の `LD_PRELOAD` による共有ライブラリの読み込みによって、アプリケーションのI/Oの関数の呼び出しを捕まえる。当初は[[MPI]]のアプリケーションのみが対象であったが、3.2.0以降はMPIを用いないアプリケーションも記録できる（この場合は `LD_PRELOAD` を用いる）。記録の対象は、[[POSIX]]のファイルの操作のほか、MPIのアプリケーションでは[[MPI-IO]]と[[HDF5]]、限定的にPnetCDFの操作であり、stdio（`fopen()` や `fread()` など）や、[[Lustre]]のストライプの設定を記録するモジュールもある。アプリケーションを一回実行するごとに一つのログのファイルが作られる。

ログは、全ての呼び出しを記録するのではなく、ファイルごとの集計値（カウンタ）として要約される。例えば、読み書きの回数とバイト数、直前のアクセスのすぐ後ろへの連続したアクセスの回数、直前より後ろへの順方向のアクセスの回数、読み書きの大きさのヒストグラム、よく現れるアクセスの大きさとストライド、区切りにそろわないアクセスの回数、読み込みと書き込みが切り替わった回数などである。集計ではなく個々の呼び出しを記録（トレース）したい場合には、DXT（Darshan eXtended Tracing）を用いる。DXTはPOSIXとMPI-IOの層を対象とする。

## どこで出てくるか
ログは、`darshan-parser` で全てのカウンタをテキストとして出力するか、`darshan-job-summary.pl` やPythonのPyDarshan（`pip install darshan`）で、I/Oの活動を図にした報告書として見る。アプリケーションのI/Oが遅い場合に、小さな読み書きが多いのか、ランダムなアクセスが多いのか、どのファイルに時間がかかっているのかを、まずDarshanで調べ、その結果をもとに[[IOR]]などで同じパターンを再現して性能を評価する、という使い方がある。

## 関係
- 使う / 使われる: [[POSIX]], [[MPI-IO]], [[HDF5]], [[Lustre]]
- 関連: [[Access Pattern]], [[IOR]], [[strace]], [[Parallel File System]]

## 出典
- [darshan-hpc/darshan - GitHub](https://github.com/darshan-hpc/darshan)
- [darshan-runtime documentation - GitHub](https://github.com/darshan-hpc/darshan/blob/main/darshan-runtime/doc/darshan-runtime.rst)
- [darshan-util documentation - GitHub](https://github.com/darshan-hpc/darshan/blob/main/darshan-util/doc/darshan-util.rst)
- [24/7 Characterization of Petascale I/O Workloads (Carns et al., IEEE Cluster 2009)](https://doi.org/10.1109/CLUSTR.2009.5289150)
