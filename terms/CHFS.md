---
aliases: [chfs, Consistent Hashing File System, CHFS-zpoline]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-06
---
# CHFS

> 計算ノードのローカルな永続メモリやNVMe SSDを用いて即座に構築できる、コンシステントハッシュに基づく並列キャッシュファイルシステムである。

## 概要
CHFSは、筑波大学の建部修見らが開発し、2022年の[[HPC Asia]]で論文 "CHFS: Parallel Consistent Hashing File System for Node-local Persistent Memory" として発表された。計算ノードのローカルな記憶装置（[[Intel Optane Persistent Memory|永続メモリ]]や[[NVMe]] SSD）を束ね、ジョブなどの単位で即座に作成できる、アドホックな並列ファイルシステムである。

CHFSの設計は、コンシステントハッシュを用いた、拡張性の高い分散[[Key-Value Store|キーバリューストア]]に全面的に基づいている。ファイルのデータと[[Metadata|メタデータ]]は、コンシステントハッシュによって各ノードのサーバに分散して置かれる。専用のメタデータサーバ、逐次的な処理、中央集権的なデータ管理を排除することで、ノード数に応じたデータアクセスとメタデータの性能の拡張性を高めている。永続メモリの低遅延と高帯域を活かすため、永続メモリ上のキーバリューストアであるpmemkvを用い、ノード間の通信には[[Margo]]と[[RDMA]]を用いる。論文では、BeeONDや[[GekkoFS]]と比べて、帯域とメタデータの両方で、よりよい拡張性と性能を示したと報告している。

CHFSは `chfsctl start` によって各ノードでサーバを起動して作成する。アクセスの方法は、[[FUSE]]によるマウント（`chfuse`）、専用のライブラリのAPI、そしてプログラムを改変せずにシステムコールを横取りするライブラリ（CHFS-zpoline）の三つがある。また、背後の[[Parallel File System|並列ファイルシステム]]に対するキャッシュとして動作させることもでき、ファイルは必要に応じて、あるいは `chstagein` によって明示的にキャッシュに読み込まれ、変更は背後のファイルシステムへ書き戻される。

## どこで出てくるか
CHFSは、[[GekkoFS]]や[[UnifyFS]]と同じく、計算ノードのローカルな記憶装置を用いるアドホックファイルシステムであり、GitHubでオープンソースとして公開されている。専用のメタデータサーバを置かずにメタデータをコンシステントハッシュで分散させる点が、設計上の特徴である。

## 関係
- 対比: [[GekkoFS]], [[UnifyFS]]（同じくアドホックファイルシステム）, [[Parallel File System]]
- 使う / 使われる: [[Margo]], [[RDMA]], [[Intel Optane Persistent Memory]], [[NVMe]], [[FUSE]], [[Key-Value Store]]
- 関連: [[Metadata]], [[LLIO]], [[HPC Asia]]

## 出典
- [CHFS: Parallel Consistent Hashing File System for Node-local Persistent Memory - 筑波大学 HPCS研究室](https://www.hpcs.cs.tsukuba.ac.jp/publications/2022/hpcasia2022tatebe/)
- [CHFS: Parallel Consistent Hashing File System for Node-local Persistent Memory - ACM Digital Library](https://dl.acm.org/doi/fullHtml/10.1145/3492805.3492807)
- [otatebe/chfs - GitHub](https://github.com/otatebe/chfs)
