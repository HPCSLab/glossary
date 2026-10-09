---
aliases: [indexfs, GIGA+, TableFS, Bulk Insertion, Stateless Caching]
tags: [term]
maps: ["[[HPC Storage]]"]
status: draft
updated: 2026-10-10
---
# IndexFS

> 既存の[[Parallel File System|並列ファイルシステム]]の上に重ねて、[[Metadata|メタデータ]]と小さなファイルの操作を多数のサーバに分散し、その性能を拡張する、カーネギーメロン大学のミドルウェアである。

## 概要
IndexFSは、Kai Ren、Qing Zheng、Swapnil Patil、Garth Gibsonが、2014年のSC（SC14）で発表した。多くの[[Distributed File System|分散ファイルシステム]]は、大きなファイルのデータを並列に読み書きする性能を重視して設計されており、メタデータは単一のメタデータサーバか、名前空間を静的に分割した少数のサーバで扱う。このため、全てのプロセスが自分のファイルを一斉に作成する[[Access Pattern|N-N]]型のチェックポイントや、ファイルシステム全体のメタデータの走査、大量の小さなファイルの扱いでは、メタデータの処理がボトルネックとなる。

IndexFSは、PVFS、[[Lustre]]、HDFSなどの既存のファイルシステムを改変せずに、その上に重ねて用いる。大きなファイルのデータは下位のファイルシステムで直接読み書きし、メタデータと小さなファイルはIndexFSのサーバが扱う。主な工夫は四つある。第一に、名前空間をディレクトリの単位で分割し、ディレクトリが大きくなるとGIGA+の手法で段階的に複数のサーバに分ける。小さなディレクトリは一つのサーバに置かれ、局所性が保たれる。第二に、ディレクトリのエントリ、属性、小さなファイルのデータを、[[LSM-Tree|LSM木]]（[[Key-Value Store|LevelDB]]）に格納し、その不変のファイル（SSTable）を下位のファイルシステムに置く。第三に、クライアントはパス名の要素と権限を、短い期限（リース）付きでキャッシュする。サーバはクライアントごとの状態を持たず、各エントリについて最も遅いリースの期限だけを記録し、変更をその期限まで待たせる。これにより、多数のクライアントへの無効化の通知が殺到することなく、パス名の解決の負荷を減らす。第四に、新しいディレクトリの下のファイルの作成をクライアント側でまとめ、SSTableとして一括して挿入する（bulk insertion）。これにより、ファイルの作成ごとのRPCが不要になる。

論文では、最大128台のメタデータサーバまでほぼ線形に性能が伸び、メタデータの負荷の多い処理で、下位のファイルシステムの性能を50%から2桁上回ったと報告している。

## どこで出てくるか
IndexFSは、HPCのストレージにおけるメタデータの拡張性の研究で、先行研究として参照される。論文が扱う、[[Metadata|メタデータ]]の負荷が少数のサーバに集中する問題、[[LSM-Tree|LSM木]]によるメタデータの格納、クライアントのキャッシュの一貫性を保つための通信の削減は、分散ファイルシステムのメタデータを設計する際の基本的な論点である。メタデータの性能は、[[mdtest]]などで測定される。

## 関係
- 上位概念: [[Distributed File System]]
- 前提: [[Metadata]]
- 使う / 使われる: [[LSM-Tree]], [[Lustre]]
- 関連: [[Parallel File System]], [[mdtest]], [[SC]]

## 出典
- [IndexFS: Scaling File System Metadata Performance with Stateless Caching and Bulk Insertion (SC14)](https://doi.org/10.1109/SC.2014.25)
- [論文PDF - Parallel Data Lab, CMU](https://www.pdl.cmu.edu/PDL-FTP/FS/IndexFS-SC14.pdf)
