---
aliases: [ADIOS, ADIOS 2, Adaptable Input Output System, Adaptable I/O System, BP5, BP4]
tags: [term]
maps: ["[[Scientific Data]]", "[[HPC Storage]]"]
status: draft
updated: 2026-10-10
---
# ADIOS2

> 自己記述的な変数と属性を、一つのAPIでファイル、ネットワーク、メモリ上のステージングのいずれにも読み書きできるようにする、科学技術データのためのI/Oフレームワークである。

## 概要
ADIOS2はAdaptable Input Output Systemの現行の実装であり、[[ORNL|Oak Ridge National Laboratory]]、Kitware、Lawrence Berkeley National Laboratory、Georgia Institute of Technology、Rutgers Universityが共同で開発している。資金は米国エネルギー省がExascale Computing Projectを通じて提供している。[[MPI]]を前提とし、ライセンスはApache 2.0である。本体は[[C++]]で実装され、[[Python]]、[[C|C言語]]、Fortran、Matlabから利用できる。

データは、名前を持つ多次元配列である変数（Variable）と、補足情報である属性（Attribute）として記述する。シミュレーションの時間ステップのような論理的な区切りを `BeginStep` と `EndStep` で囲み、その間で `Put`（書き込み）と `Get`（読み込み）を呼ぶ。既定の遅延（deferred）モードでは、データは `EndStep` などの時点でまとめて転送されるため、それまでアプリケーションはバッファを変更してはならない。

実際の転送を担うのはエンジン（Engine）であり、ADIOS2の要点はこれを差し替えられることにある。ファイル用には独自のバイナリ形式であるBP5、BP4などのエンジンがあり、ADIOS 2.9以降はBP5が既定のファイル形式である。HDF5エンジンを選べば[[HDF5]]ファイルを読み書きでき、[[DAOS]]エンジンはDAOSの[[Object Storage|オブジェクトストア]]に直接読み書きする。一方、SSTエンジンはファイルを介さず、書き込み側が渡したデータを読み込み側のプログラムへ直接届けるストリーミングを行い、通信にはTCP、[[RDMA]]、MPIを用いる。エンジンは `SetEngine` で指定するほか、XMLまたはYAMLの設定ファイルで実行時に指定でき、再コンパイルせずにファイル出力とストリーミングを切り替えられる。`BeginStep`/`EndStep` を用いて書いたコードは、ファイルとストリーミングのどちらのエンジンでも同じように動く。

変数には、圧縮などの変換を行うオペレータ（Operator）を `AddOperation` で付けられる。ZFP、SZ3、MGARDといった誤差を制御できる非可逆圧縮のほか、BZip2やBlosc2などを利用できる。

## どこで出てくるか
ADIOS2は、大規模シミュレーションのデータ出力のほか、シミュレーションの実行中にファイルを介さずデータを解析側へ渡すin situ解析やin transit解析、複数のプログラムを結合する連成計算で用いられる。[[HDF5]]や[[netCDF]]が「どのようなファイルを作るか」を定めるのに対し、ADIOS2は「データをどこへどう運ぶか」をエンジンとして切り替えられる点で性格が異なる。これにより、同じアプリケーションのコードのまま、[[Parallel File System|並列ファイルシステム]]へのファイル出力と、ファイルシステムを経由しないストリーミングとを設定で選べる。出力ファイル（BPおよびHDF5）の中身は `bpls` で確認できる。

## 関係
- 対比: [[HDF5]]（ファイル形式とライブラリであり、転送方式は差し替えない）, [[netCDF]]
- 使う / 使われる: [[MPI]], [[HDF5]]（HDF5エンジン）, [[DAOS]], [[RDMA]]（SSTの通信）
- 関連: [[Parallel File System]], [[Zarr]]

## 出典
- [Introduction - ADIOS2 documentation](https://adios2.readthedocs.io/en/latest/introduction/introduction.html)
- [Interface Components - ADIOS2 documentation](https://adios2.readthedocs.io/en/latest/components/components.html)
- [Supported Engines - ADIOS2 documentation](https://adios2.readthedocs.io/en/latest/engines/engines.html)
- [Supported Operators - ADIOS2 documentation](https://adios2.readthedocs.io/en/latest/operators/operators.html)
- [Installation (CMake options) - ADIOS2 documentation](https://adios2.readthedocs.io/en/latest/setting_up/setting_up.html)
- [Utilities - ADIOS2 documentation](https://adios2.readthedocs.io/en/latest/ecosystem/utilities.html)
- [ornladios/ADIOS2 - GitHub](https://github.com/ornladios/ADIOS2)
