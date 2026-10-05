---
aliases: [DLM, DLM Lock, DLMロック, 分散ロックマネージャ, 分散ロック, Distributed Lock, LDLM, Lustre Distributed Lock Manager, Extent Lock, エクステントロック, Inodebits Lock, Blocking AST, Completion AST, Glimpse AST, Lock Mode, ロックモード]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-06
---
# Distributed Lock Manager（分散ロックマネージャ）

> クラスタの複数の計算機の間で、共有する資源へのアクセスをロックによって調停する仕組みであり、[[Lustre]]ではLDLMとしてクライアントのキャッシュの一貫性を保つ。

## 概要
分散ロックマネージャ（DLM）は、一つの計算機の中の[[Mutex|ミューテックス]]と同様のロックを、ネットワークでつながった複数の計算機の間で提供する。起源はVAX/VMSのクラスタのロックマネージャであり、ロックは名前の付いた資源に対して取得される。ロックには六つのモードがある。NL（関心のみを示す）、CR（並行読み出し）、CW（並行書き込み）、PR（保護された読み出し、通常の共有ロック）、PW（保護された書き込み、他者の読み出しのみを許す）、EX（排他）である。二つのロックが同時に成立するかは、モードの組合せの互換性の表で決まり、例えばPR同士は両立するが、PRとPWは両立しない。

ロックを持つ側は、他者が衝突するロックを要求したときに通知を受け取る。この通知は、VMSの用語を引き継いでAST（Asynchronous System Trap）と呼ばれ、通知を受けた側は、ロックで守っていた作業を終えてロックを解放する。

## Lustre の LDLM
[[Lustre]]のロックマネージャ（LDLM）は、VAXのDLMの設計を基にしている。ロックは、サーバのサービス（各OST、MDSなど）ごとの名前空間の中の資源に対して取得され、OSTのオブジェクトのロックはそのOSTが、ファイルの[[Metadata|メタデータ]]のロックはMDSが管理する。ロックの種類には、OSTのデータのバイト範囲を守るエクステントロックと、[[Inode|inode]]の属性の一部を守るinodebitsロックなどがある。エクステントロックでは、要求された範囲が他のロックと重ならなければ衝突しない。衝突がなければ、後の要求を減らすために、ストライプの大きさの範囲内で、要求よりできるだけ大きな範囲のロックを与える。

クライアントは、データやメタデータをキャッシュする前に対応するロックを取得し、衝突する要求が来るまでロックを保持し続ける。他のクライアントが衝突するロックを要求すると、サーバはロックを持つクライアントにblocking ASTを送る。そのクライアントは、ロックの下での入出力を終え、キャッシュの内容を書き戻すか破棄してからロックを解放する。その後、サーバは待っていた要求にロックを与え、completion ASTで通知する。ファイルの大きさは、各OSTが持つオブジェクトの大きさから決まるため、glimpse ASTによって、ロックを解放させずに大きさの情報だけを問い合わせる仕組みもある。

## どこで出てくるか
並列ファイルシステムで一つの共有ファイルに多数のプロセスが書き込む場合、各プロセスの書き込みの範囲がストライプの中で重なったり交互に並んだりすると、エクステントロックの奪い合いが起きる。ロックが解放されるたびにキャッシュの書き戻しが必要になるため、性能が大きく低下する。[[MPI-IO]]の集団I/Oで書き込みを集約し、各プロセスの書き込みの範囲をストライプの境界にそろえるのは、この競合を避けるためでもある。[[IBM Storage Scale]]も、トークンと呼ばれる分散ロックによって、同じようにキャッシュの一貫性を保っている。

## 関係
- 使う / 使われる: [[Lustre]], [[IBM Storage Scale]]
- 関連: [[Mutex]], [[Parallel File System]], [[MPI-IO]], [[Consistency Model]]

## 出典
- [Distributed lock manager - Wikipedia](https://en.wikipedia.org/wiki/Distributed_lock_manager)
- [Understanding Lustre Filesystem Internals (ORNL/TM-2009/117)](https://wiki.lustre.org/images/d/da/Understanding_Lustre_Filesystem_Internals.pdf)（4章 LDLM。Lustre 1.6のコードに基づく）
