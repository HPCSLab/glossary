---
aliases: [close-to-open, Close-to-Open, close-to-open一貫性, CTO, cto, nocto, close-to-open cache consistency]
tags: [term]
maps: ["[[HPC Storage]]"]
status: draft
updated: 2026-10-16
---
# Close-to-Open Consistency（close-to-open一貫性）

> クライアントがファイルを閉じる時点で変更をサーバへ書き戻し、ファイルを開く時点でキャッシュの有効性を確かめることで、「閉じてから開いた」場合に限り他のクライアントの変更が見えることを保証する、[[NFS]]の[[Cache|キャッシュ]]の一貫性の規則である。

## 概要
[[Distributed File System|分散ファイルシステム]]のクライアントは、ネットワーク越しのアクセスの[[Latency|遅延]]を避けるため、ファイルの内容と属性を手元にキャッシュする。しかし、すべての `read()` と `write()` のたびに他のクライアントのキャッシュとの一貫性を保つことは高価である。close-to-open一貫性は、ファイルの共有は多くの場合、一方が書いて閉じた後に他方が開いて読むという逐次的な形で行われることに着目し、一貫性を確かめる時点を [[close|close()]] と [[open|open()]] の二つに限ったものである。これにより、[[POSIX]]が求める強い意味論より弱いが、日常的なファイル共有には十分な一貫性を、小さな通信の量で実現する。

規則は二つからなり、互いに補い合う。一つは、書き込み用に開いたファイルを閉じる前に、変更されたデータをサーバへ送り、サーバの永続的な記憶装置に反映させることである。もう一つは、ファイルを開いた後に、サーバからファイルの属性（NFSv4ではchange属性、NFSv3では更新時刻など）を取得し、キャッシュした値と異なればキャッシュを無効とすることである。閉じる時点で書き戻さなければ、開く時点の検査は意味をなさない。[[Linux Kernel|Linux]]のクライアントは、閉じた直後と次に開いたときの GETATTR の結果を比較することでこれを実装している。

この規則が保証するのは、閉じてから開くという順序がある場合だけである。複数のクライアントが同時にファイルを開いたまま読み書きする場合、他方の書き込みがいつ見えるかは保証されない。このような共有を正しく行うには、ファイルロックを用いる必要がある。NFSv4では、ロックの取得時にその範囲のキャッシュを再検証し、書き込みロックの解放前に変更を書き戻すことが定められている。

## どこで出てくるか
NFSで共有されたホームディレクトリなどで、ある[[Compute Node|ノード]]が書き続けているファイルを別のノードで読むと、古い内容やサイズが見えることがある。これは、書き手が閉じていない間の変更の可視性が close-to-open一貫性では保証されず、さらに属性のキャッシュの有効期間（マウントオプションの `actimeo`、`acregmin` など）の間は古い属性が使われるためである。Linuxのマウントオプション `cto`（既定）と `nocto` は、この規則を使うかどうかを切り替え、`noac` は属性のキャッシュを無効にする。ただし、`noac` を指定してもデータのキャッシュの一貫性が保証されるわけではない。

研究の文脈では、[[Parallel File System|並列ファイルシステム]]の多くがPOSIXの強い意味論を[[Distributed Lock Manager|分散ロックマネージャ]]で維持しているのに対し、close-to-open一貫性は、意味論を緩めて性能を得る設計の代表例として[[Consistency Model|一貫性モデル]]の比較に現れる。

## 関係
- 上位概念: [[Consistency Model]]
- 前提: [[Cache]], [[open]], [[close]]
- 対比: [[POSIX]]（すべての `write()` の結果を後続の `read()` に反映することを求める）
- 使う / 使われる: [[NFS]]
- 関連: [[Distributed File System]], [[Distributed Lock Manager]], [[Metadata]]

## 出典
- [RFC 7530: Network File System (NFS) Version 4 Protocol, Section 10.3](https://datatracker.ietf.org/doc/html/rfc7530#section-10.3.1)
- [nfs(5) - Linux manual page](https://man7.org/linux/man-pages/man5/nfs.5.html)
- [Linux NFS FAQ（A8. What is close-to-open cache consistency?）](https://nfs.sourceforge.net/)
