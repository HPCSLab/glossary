---
aliases: [Network File System, NFSv3, NFSv4, NFSv4.1, pNFS, Parallel NFS, Close-to-Open, close-to-open一貫性, actimeo]
tags: [term]
maps: ["[[Storage]]", "[[Network]]"]
status: draft
updated: 2026-10-06
---
# NFS

> ネットワーク越しに、リモートのサーバ上のファイルを、ローカルのファイルと同様に扱えるようにする分散ファイルシステムのプロトコルである。

## 概要
NFS（Network File System）は、1980年代にSun Microsystemsが開発し、現在まで最も広く用いられているネットワークファイルシステムである。クライアントは、サーバが公開（エクスポート）したディレクトリを自分のディレクトリにマウントし、以後はその下のファイルを通常の[[POSIX]]のインタフェースで読み書きする。クライアント側では、NFSは[[VFS]]の下の一つのファイルシステムの実装として動作する。

広く使われている版は二つある。NFSv3（RFC 1813、1995年）は、サーバがクライアントの状態を保持しないステートレスな設計を採り、サーバが再起動してもクライアントは要求を再送するだけで済む。ファイルのロックは、状態を伴うため、NLMという別のプロトコルに分離されている。NFSv4（RFC 7530）は、ロックや開いているファイルの状態をプロトコル本体で扱うステートフルな設計に改められた。NFSv4.1（RFC 8881）は、pNFS（parallel NFS）を導入した。pNFSでは、メタデータへのアクセスとデータへのアクセスを分離し、クライアントはサーバから受け取ったレイアウトに従って、複数のデータサーバに並列にアクセスする。これは[[Parallel File System|並列ファイルシステム]]と同様の構造である。

NFSの一貫性は、[[POSIX]]の要求より弱い。クライアントは性能のためにファイルの内容と属性をキャッシュし、close-to-open一貫性と呼ばれる規則に従う。すなわち、ファイルを閉じる時点で未反映の書き込みをサーバへ送り、ファイルを開く時点でサーバ上のファイルが変更されていないかを確かめてキャッシュの有効性を判断する。したがって、あるクライアントが書いて閉じたファイルを、別のクライアントが後から開けば変更が見えるが、両者が同時にファイルを開いたまま読み書きする場合、変更がいつ見えるかは保証されない。属性のキャッシュの有効期間は、マウントオプション（`actimeo`、`acregmin` など）で調整できる。

## どこで出てくるか
多くの計算機クラスタや研究室のサーバでは、ホームディレクトリやソフトウェアの置き場がNFSで共有されている。そのため、複数のノードから同じファイルを同時に書き込む処理や、一方のノードで書いたファイルを別のノードですぐに読む処理では、close-to-open一貫性と属性のキャッシュによって、古い内容やサイズが見えることがある。また、NFSは単一のサーバに要求が集中するため、多数の計算ノードから大量のI/Oを行う用途には向かない。大規模な並列I/Oには、[[Lustre]]などの並列ファイルシステム上の作業領域を用いるのが原則である。I/O性能を測定する際には、測定対象のディレクトリがNFS上にあるのか、ローカルディスクや並列ファイルシステム上にあるのかを `df -T` や `mount` で確認しておく必要がある。

## 関係
- 上位概念: [[Distributed File System]]
- 対比: [[Parallel File System]], [[Lustre]]（多数のサーバに分散する）
- 関連: [[Consistency Model]], [[POSIX]], [[VFS]], [[Metadata]]

## 出典
- [RFC 1813: NFS Version 3 Protocol Specification](https://www.rfc-editor.org/rfc/rfc1813.html)
- [RFC 7530: Network File System (NFS) Version 4 Protocol](https://datatracker.ietf.org/doc/html/rfc7530)
- [RFC 8881: Network File System (NFS) Version 4 Minor Version 1 Protocol](https://www.rfc-editor.org/rfc/rfc8881.html)
- [nfs(5) - Linux manual page](https://man7.org/linux/man-pages/man5/nfs.5.html)
