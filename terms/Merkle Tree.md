---
aliases: [マークル木, マークルツリー, Hash Tree, ハッシュ木, Merkle Hash Tree, Merkle DAG]
tags: [term]
maps: ["[[Data Structures]]", "[[Distributed Systems]]"]
status: draft
updated: 2026-10-17
---
# Merkle Tree（マークル木）

> 葉にデータのブロックのハッシュ値を置き、内部節点に子のハッシュ値をまとめたハッシュ値を置く木であり、根のハッシュ値だけでデータ全体が同じかを確かめ、異なる部分を少ない比較で特定できる。

## 概要
暗号学的なハッシュ関数（SHA-256など）は、任意の長さのデータから固定長の値を計算し、異なるデータから同じ値が得られることは事実上ない。Merkle木は、データをブロックに分けて各ブロックのハッシュ値を葉とし、子のハッシュ値を連結してさらにハッシュをとった値を親に置く操作を根まで繰り返したものである。Ralph Merkleがデジタル署名の方式のために考案した。どのブロックが変わっても、その葉から根までの経路上のハッシュ値が全て変わるため、根のハッシュ値一つがデータ全体の要約となる。一つのブロックが正しいことは、根のハッシュ値と、経路の各段の兄弟の節点のハッシュ値（ブロック数nに対して約 log n 個）だけで確かめられる。

![[Merkle Tree Comparison.excalidraw]]

二つの複製を比べるときは、まず根のハッシュ値を交換し、等しければ全体が同一であるため終わる。異なれば子のハッシュ値を交換し、異なる子の部分木だけを下りていく。等しい部分木はその下を調べずに済むため、少数のブロックだけが異なる場合、データ全体を送らずに異なるブロックを特定できる。

## どこで出てくるか
[[Key-Value Store|キーバリューストア]]のDynamoは、複製の間の食い違いを背後で見つけて揃える反エントロピー（anti-entropy）の処理に用い、各ノードが担当するキーの範囲ごとにMerkle木を保持して、根から順にハッシュ値を比べる。[[ZFS]]は、各ブロックのチェックサムをそのブロックを指す親のブロックに格納しており、根まで同じ形の木をなす。このため、記憶装置が誤ったデータを返しても、親の持つチェックサムとの不一致として検出できる。[[Git]]は、ファイルの内容（blob）とディレクトリ（tree）をその内容のハッシュ値で名付け、treeは子のハッシュ値を並べたものであるため、コミットが指す最上位のtreeのハッシュ値はスナップショット全体を表す。いずれも、ハッシュ値を比べるだけで大きなデータの同一性を判断するという、同じ考え方に基づく。

## 関係
- 使う / 使われる: [[ZFS]], [[Git]], [[Key-Value Store]]

## 出典
- [A Digital Signature Based on a Conventional Encryption Function (Merkle, CRYPTO '87)](https://doi.org/10.1007/3-540-48184-2_32)
- [Dynamo: Amazon's Highly Available Key-value Store (DeCandia et al., SOSP 2007)](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf)
- [Git Internals - Git Objects (Pro Git)](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)
