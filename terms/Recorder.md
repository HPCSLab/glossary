---
aliases: [Recorder 2.0, recorder-viz, recorder-report, I/O Tracing, I/Oトレース]
tags: [term]
maps: ["[[HPC Storage]]", "[[Parallel Computing]]"]
status: draft
updated: 2026-10-10
---
# Recorder

> HPCのアプリケーションが発行したI/Oの関数の呼び出しを、I/Oスタックの複数の層にわたって一つずつ記録（トレース）する、並列I/Oのトレースのツールである。

## 概要
HPCのアプリケーションのI/Oは、[[HDF5]]や[[netCDF]]（PnetCDF）のような高水準のライブラリ、その下の[[MPI-IO]]、さらにその下の[[POSIX]]のファイルの操作という層を順に通る。Recorderは、これらの層の呼び出しを同時に記録し、呼び出しごとに関数名、引数、開始と終了の時刻、呼び出しの深さを残す。深さから、ある層の呼び出しがその下の層でどの呼び出しになったかを読み取れる。[[DAOS]]のAPIや、I/O以外の[[MPI]]の呼び出しも記録でき、層ごとに環境変数（`RECORDER_POSIX_TRACING` など）で記録の有無を切り替える。

使い方は `LD_PRELOAD` で共有ライブラリ `librecorder.so` を読み込ませてアプリケーションを実行するだけであり、アプリケーションの改変も再コンパイルも要らない。トレースは実行したディレクトリの下に、ホスト名、ユーザ名、アプリケーション名、PID、開始時刻からなる名前のフォルダとして書き出される。全ての呼び出しを記録するとトレースはプロセス数と実行時間に比例して大きくなるため、Recorderは呼び出しの規則的な繰り返しを見つけて圧縮する。論文では、典型的な並列I/Oのパターンであれば、トレースの大きさが実行の規模によらず一定になると報告されている。

[[Darshan]]がファイルごとの集計値（カウンタ）として要約を残すプロファイラであるのに対し、Recorderは個々の呼び出しを残すトレーサである。Darshanも拡張機能のDXTで呼び出しを記録できるが、その対象はPOSIXとMPI-IOの層に限られる。

## どこで出てくるか
並列I/Oの[[Access Pattern|アクセスパターン]]の研究で、アプリケーションが実際に発行した呼び出しの列そのものが必要なときに使われる。例えば、Recorderの開発者らは17個のHPCのアプリケーションのトレースを解析し、POSIXの厳密な一貫性はHPCのアプリケーションにはほとんど必要とされないと報告した（[[HPDC]] 2021）。このようにトレースは、[[Parallel File System|並列ファイルシステム]]がどの程度の[[Consistency Model|一貫性モデル]]を提供すべきかを、実際のアプリケーションから確かめる材料になる。

トレースは、[[Python]]のrecorder-vizに含まれる `recorder-report` でHTMLの報告書にするか、`recorder2parquet` で[[Parquet]]の形式に、`recorder2timeline` で[[Perfetto]]で表示できるタイムラインの形式に変換して調べる。

## 関係
- 対比: [[Darshan]]（集計値を残すプロファイラであるのに対し、Recorderは個々の呼び出しを残すトレーサである）
- 使う / 使われる: [[POSIX]], [[MPI-IO]], [[HDF5]], [[netCDF]], [[DAOS]]
- 関連: [[Access Pattern]], [[strace]], [[Consistency Model]]

## 出典
- [uiuc-hpc/Recorder - GitHub](https://github.com/uiuc-hpc/Recorder)
- [Recorder documentation](https://recorder.readthedocs.io/latest/index.html)
- [Usage - Recorder documentation](https://recorder.readthedocs.io/latest/usage.html)
- [Post-processing and Visualization - Recorder documentation](https://recorder.readthedocs.io/latest/postprocessing.html)
- [Recorder: Comprehensive Parallel I/O Tracing and Analysis (Wang et al., arXiv:2501.04654)](https://arxiv.org/abs/2501.04654)
