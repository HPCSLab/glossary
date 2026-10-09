---
aliases: [Lustre File System, ラスター, LNet, ldiskfs, MDS, MDT, OSS, OST]
tags: [term]
maps: ["[[HPC Storage]]"]
status: draft
updated: 2026-10-10
---
# Lustre

> HPCで最も広く用いられているオープンソースの[[Parallel File System|並列ファイルシステム]]であり、[[POSIX]]準拠の単一の名前空間を多数のサーバ上に構築する。

## 概要
Lustreの名称は Linux と cluster を組み合わせた造語である。1999年にカーネギーメロン大学で設計が始まり、その後の開発主体は Cluster File Systems、Sun Microsystems、Oracle、Whamcloud、Intel を経て、現在はDDNのWhamcloud部門が中心となっている。ライセンスはGPLv2である。2005年以降、世界の上位スーパーコンピュータの過半で採用されてきた。

Lustreは、役割の異なる3種類のサーバと、クライアントから構成される。MGS（管理サーバ）はファイルシステムの構成情報を保持し、配布する。MDS（メタデータサーバ）は、ディレクトリ、ファイル名、権限などの名前空間と[[Metadata|メタデータ]]を、記憶領域であるMDTに格納する。OSS（オブジェクトストレージサーバ）は、ファイルの内容を記憶領域であるOSTに格納する。一つのファイルシステムは数百台のOSSと数千のOSTまで拡張できる。MDTとOSTの実体は、[[ext4]]を基にしたldiskfs、または[[ZFS]]でフォーマットされた[[Block Storage|ブロックデバイス]]である。サーバ間とクライアントとの通信には、InfiniBandやEthernetなどを抽象化し、RDMAによるゼロコピー転送を提供する独自のネットワーク層LNetを用いる。

クライアントがファイルを開くと、MDSからそのファイルのレイアウト、すなわち内容がどのOST上のどのオブジェクトに、どのストライプサイズで分割されているかを受け取る。以後の読み書きは、MDSを介さずに各OSSと直接行う。レイアウトは `lfs setstripe` で設定し、`lfs getstripe` で確認する。Lustre 2.10で導入されたPFL（Progressive File Layout）は、ファイル内の位置に応じて異なるレイアウトを適用する。例えば、先頭部分は少数のOSTに置き、ファイルが大きくなるにつれてより多くのOSTに分散させる。2.11で導入されたDoM（Data on MDT）は、小さなファイルの内容をMDTに直接格納し、OSSへのアクセスを省く。また、DNEにより名前空間を複数のMDTに分散させ、メタデータ性能を拡張できる。

複数のクライアントが同じファイルをキャッシュしつつ並列に読み書きするため、Lustreは[[Distributed Lock Manager|分散ロックマネージャ]]（LDLM）によってキャッシュの一貫性を保つ。クライアントはデータやメタデータをキャッシュする前に対応するロックを取得し、他のクライアントが衝突するロックを要求すると、ロックを返却する前にキャッシュを書き戻すか破棄する。これにより、複数のクライアントにまたがってもPOSIXの意味論が維持される。サーバの障害に備えて、記憶装置を複数のサーバに接続し、一方の障害時に他方が引き継ぐフェイルオーバ構成が一般的である。

## どこで出てくるか
多くのスーパーコンピュータで、`/scratch` や `/work` などの共有作業領域としてLustreが提供されている。利用者は、大きなファイルに対してはストライプ数を増やし、小さなファイルが多いディレクトリでは既定のまま、あるいはDoMを用いる、というようにレイアウトを調整することで性能を改善できる。`lfs df` でOSTごとの使用量を確認でき、特定のOSTが満杯になるとそこにストライプされるファイルへの書き込みが失敗する点にも注意を要する。研究の文脈では、メタデータサーバの性能限界、LDLMのロック競合、共有ファイルへのN-1書き込みの性能などが、Lustreを題材とした代表的な論点である。

## 関係
- 上位概念: [[Parallel File System]]
- 前提: [[POSIX]], [[Metadata]]
- 使う / 使われる: [[ext4]]（ldiskfsの基盤）, [[ZFS]], [[Block Storage]]
- 対比: [[IBM Storage Scale]], [[BeeGFS]]
- 関連: [[MPI-IO]], [[Consistency Model]], [[Lustre PCC]], [[EXAScaler]], [[DNE]]

## 出典
- [Introduction to Lustre - Lustre Wiki](https://wiki.lustre.org/Introduction_to_Lustre)
- [Lustre Software Release 2.x Operations Manual](https://doc.lustre.org/lustre_manual.xhtml)
- [Lustre (file system) - Wikipedia](https://en.wikipedia.org/wiki/Lustre_(file_system))
