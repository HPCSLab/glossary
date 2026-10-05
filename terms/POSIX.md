---
aliases: [Portable Operating System Interface, IEEE Std 1003.1, POSIX.1, ポジックス]
tags: [term]
maps: ["[[Storage]]", "[[Operating System]]"]
status: draft
updated: 2026-10-05
---
# POSIX

> Unix系オペレーティングシステム間でアプリケーションの移植性を確保するために、OSが提供すべきインタフェースとその振る舞いを定めた標準規格群である。

## 概要
POSIX（Portable Operating System Interface）は、Unixから派生した各種OSの間で、同一のソースコードが同じように動作することを目的として、1988年に最初の版が制定された。現行の中核規格は POSIX.1-2024 であり、これは IEEE Std 1003.1-2024 であると同時に The Open Group Base Specifications Issue 8 でもあり、ISO/IEC 9945 としても扱われる。策定はIEEE、The Open Group、ISO/IECの合同作業部会であるAustin Groupが担う。

規格は、用語や共通の概念を定める Base Definitions、C言語から呼び出す関数群を定める System Interfaces、シェルと `ls` や `cp` などのコマンドを定める Shell and Utilities、および設計根拠を述べる Rationale の4巻で構成される。[[File System|ファイルシステム]]の操作に関しては、[[open|open()]]・[[read|read()]]・[[write|write()]]・[[lseek|lseek()]]・[[fsync|fsync()]]・[[rename|rename()]] などの関数、[[File Descriptor|ファイルディスクリプタ]]とファイルオフセットの扱い、ディレクトリ操作、権限やタイムスタンプなどのファイル属性が定められている。

POSIXが定めるのはインタフェースと観測可能な振る舞いであり、内部の実装方式は定めない。そのため、Linuxではこれらの関数の多くが[[System Call|システムコール]]を薄く包んだライブラリ関数として実装され、カーネル内の[[VFS]]を経て各ファイルシステムの実装に到達する。正式な認証を受けたOSにはmacOSやAIXなどがあり、Linuxの各ディストリビューションは認証を受けていないものの、その大部分に準拠している。

## どこで出てくるか
HPCのストレージ研究では、「POSIX I/O」あるいは「POSIXの意味論」という形でこの語に頻繁に出会う。POSIXは、`write()` が成功して戻った後は、その位置に対する後続の `read()` が書き込まれたデータを返すことを要求し、ある `read()` が `write()` の後に起きたことが何らかの手段で示せるならば、別スレッドからの呼び出しであってもその結果を反映しなければならないと定めている。この強い一貫性は単一ノードでは自然に満たされるが、多数のクライアントが同一ファイルを共有する[[Parallel File System|並列ファイルシステム]]では、ロックなどの協調機構を必要とし、性能上の制約となる。このため、POSIXに完全準拠することの是非や、一貫性を緩和した独自のインタフェース・意味論の設計が、研究上の主要な論点となっている。[[NFS]]がPOSIXより弱いclose-to-open一貫性を採用していることも、この緊張関係の一例である。

## 関係
- 対比: [[Object Storage]]（POSIXの意味論を持たない、異なるアクセスモデル）
- 使う / 使われる: [[File System]], [[File Descriptor]], [[VFS]]（POSIXのインタフェースを実装・提供する側）
- 関連: [[System Call]], [[Parallel File System]], [[Consistency Model]]

## 出典
- [POSIX - Wikipedia](https://en.wikipedia.org/wiki/POSIX)
- [Preface - The Open Group Base Specifications Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/frontmatter/preface.html)
- [write, pwrite - The Open Group Base Specifications Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/functions/write.html)
