---
aliases: [ローカルストレージ, ノードローカルストレージ, Local Storage, Node-local SSD, ローカルディスク, /scratch, Local File System, ローカルファイルシステム]
tags: [term]
maps: ["[[HPC Storage]]"]
status: draft
updated: 2026-10-10
---
# Node-local Storage（ローカルストレージ）

> [[Compute Node|計算ノード]]に搭載され、そのノードからのみ読み書きできる記憶装置と、その上のファイルシステムである。

## 概要
HPCのクラスタでは、ノード間で共有されるファイルシステムとして、ホームディレクトリ（`/home`）と、[[Parallel File System|並列ファイルシステム]]による作業用の領域（`/work` など）が提供されることが多い。これに加えて、各計算ノードが、ノードごとに独立した一時的なデータのための領域（`/scratch` など）を持つ場合がある。このようなノードに閉じた領域は、通常、[[ext4]]、XFS、[[btrfs]]などのローカルファイルシステムで構成され、他のノードからは読み書きできない。

並列計算機のクラスタでは、共有のファイルシステムの背後の記憶装置が主に磁気ディスクであるのに対し、計算ノードの中には、[[SSD]]や不揮発性メモリといった、より高速な記憶装置が搭載されるようになった。

## どこで出てくるか
ローカルストレージは、そのノードからしか読み書きできず、一時的なデータのための領域である。ノードローカルな記憶装置を科学技術計算の作業の流れに組み込むための手法として、複数のノードのローカルストレージを束ねて一時的な共有のファイルシステムを作る[[Ad Hoc File System|アドホックファイルシステム]]（[[GekkoFS]]、[[CHFS]]、[[UnifyFS]]など）や、並列ファイルシステムのファイルをクライアントのローカルな記憶装置にキャッシュする[[Lustre PCC]]がある。[[Fugaku|富岳]]の[[LLIO]]も、計算ノードの近くのSSDを第1階層のストレージとして用いる。ローカルストレージを用いる際には、ジョブの終了後にデータが消えるかどうか、ほかのノードから見えるかどうかを、所属する計算機センターの案内で確認する必要がある。

## 関係
- 上位概念: [[Block Storage]]（ローカルストレージの記憶装置）
- 対比: [[Parallel File System]]（ノード間で共有される）
- 使う / 使われる: [[Ad Hoc File System]], [[Lustre PCC]], [[LLIO]]（ローカルストレージを用いる仕組み）
- 関連: [[Compute Node]], [[SSD]], [[NVMe]], [[ext4]]

## 出典
- [File System Separation (Admin Guide) - HPC Wiki](https://hpc-wiki.info/hpc/Admin_Guide_File_System_Separation)
- [HPC-Dictionary - HPC Wiki](https://hpc-wiki.info/hpc/HPC-Dictionary)
- [Ad Hoc File Systems for High-Performance Computing (Brinkmann et al., Journal of Computer Science and Technology, 2020)](https://jcst.ict.ac.cn/EN/10.1007/s11390-020-9801-1)
