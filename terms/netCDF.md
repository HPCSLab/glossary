---
aliases: [NetCDF, network Common Data Form, netCDF-4, PnetCDF, CF Conventions, CF規約, .nc]
tags: [term]
maps: ["[[Scientific Data]]"]
status: draft
updated: 2026-10-10
---
# netCDF

> 配列形式の科学データを、自己記述的かつ計算機に依存しない形で格納・共有するための、データ形式とライブラリの総体である。

## 概要
netCDF（network Common Data Form）は、米国大気研究大学連合（UCAR）のUnidataが開発・配布している。気象、気候、海洋などの地球科学の分野で特に広く用いられている。

データモデルは三つの要素からなる。次元（dimension）は、緯度、経度、時刻のような名前の付いた軸である。変数（variable）は、次元によって添字付けられた配列である。属性（attribute）は、変数やファイル全体に付ける単位や説明などの[[Metadata|メタデータ]]である。例えば、気温を表す変数 `temperature(time, lat, lon)` は、三つの次元を持つ三次元配列として表される。データが自身の構造と意味の説明を含むため、異なる計算機や言語の間でも変換なしに読み書きできる。

ファイル形式には複数の版がある。1989年からの古典形式（CDF-1）、より大きなファイルを扱える64ビットオフセット形式（CDF-2）、変数あたりの要素数の制限を緩めた64ビットデータ形式（CDF-5）、および[[HDF5]]を基盤とするnetCDF-4形式である。netCDF-4は、HDF5の機能を利用して、圧縮、チャンク、グループ、より豊富なデータ型を提供する。

ライブラリの利用者には、データの意味付けに関する共通の取り決めも重要である。CF（Climate and Forecast）規約は、変数の名前、単位、座標の表し方などの属性の付け方を定めており、これに従ったファイルは、多くの解析・可視化ツールでそのまま扱える。

## どこで出てくるか
気候モデルや気象シミュレーションの入出力、観測データの配布では、netCDFが事実上の標準である。並列環境での読み書きには、netCDF-4形式に対してはParallel HDF5を経由する方法が、古典形式系に対しては[[MPI-IO]]を直接用いるPnetCDF（Parallel netCDF）がある。Pythonでは、xarrayを用いると、次元の名前と座標を伴った配列としてnetCDFのデータを扱え、同じ操作で[[Zarr]]形式のデータも扱える。ファイルの構造は `ncdump -h` で確認できる。

## 関係
- 使う / 使われる: [[HDF5]]（netCDF-4の基盤）, [[MPI-IO]]（PnetCDF）
- 対比: [[Zarr]]
- 関連: [[NumPy]], [[Python]]

## 出典
- [NetCDF FAQ - Unidata](https://docs.unidata.ucar.edu/netcdf-c/current/faq.html)
