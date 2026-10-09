---
aliases: [mmap(), mmap(2), munmap, msync, Memory-mapped File, メモリマップドファイル, MAP_SHARED, MAP_PRIVATE, MAP_ANONYMOUS]
tags: [term]
maps: ["[[Storage]]", "[[Operating System]]"]
status: draft
updated: 2026-10-10
---
# mmap

> ファイルやデバイス、あるいは匿名のメモリ領域を、プロセスの仮想アドレス空間に写像する[[POSIX]]の関数である。

## 概要
`mmap()` でファイルを写像すると、プログラムはファイルの内容を通常のメモリと同じようにポインタで読み書きできる。[[read]]・[[write]]のようにデータをユーザのバッファへ複製する必要はなく、プロセスは[[Page Cache|ページキャッシュ]]上のページを直接参照する。写像は遅延的に行われ、まだ読み込まれていないページに初めてアクセスした時点でページフォルトが発生し、カーネルがそのページをページキャッシュに読み込んでプロセスの[[Virtual Memory|仮想記憶]]に結び付ける。写像するファイル上の開始位置は、ページサイズの倍数でなければならない。`MAP_POPULATE` を指定すると、写像の時点でページを先に読み込んでおける。

写像の種類は、変更の扱いによって二つに分かれる。`MAP_SHARED` では、変更は同じ領域を写像する他のプロセスから見え、基になるファイルにも反映される。ただし、反映の時期はカーネルの書き戻しに委ねられるため、確実に記憶装置へ書き出すには `msync()` を呼ぶ必要がある。`MAP_PRIVATE` では、変更は[[Copy-on-Write|コピーオンライト]]によってそのプロセス専用の複製に対して行われ、他のプロセスにもファイルにも反映されない。`MAP_ANONYMOUS` は、ファイルに対応しない、0で初期化されたメモリを確保する。glibcの `malloc` は、既定で128KiB以上の大きな確保にこの方式を用いる。写像の解除には `munmap()` を用いる。

## どこで出てくるか
mmapは、大きなファイルへの[[Access Pattern|ランダムアクセス]]を簡潔に記述でき、データの複製も省けるため、データの読み込みや、プロセス間でのメモリの共有に広く用いられる。実行ファイルや共有ライブラリも、ローダによってmmapで写像される。一方、I/Oの手段としてmmapを用いる場合には、性能と正しさの両面で注意を要する。I/Oはページフォルトという形で暗黙に発生するため、いつどれだけのI/Oが起きるかをプログラムが制御しにくい。I/Oのエラーは戻り値ではなく、SIGBUSなどのシグナルとして通知される。ファイル末尾を越えた領域へのアクセスもSIGBUSとなる。また、データベース管理システムが独自のバッファプールの代わりにmmapを用いることの問題点を論じた研究があり、いくつかのシステムがmmapの採用後に独自のI/O管理へ移行した経緯が報告されている。

## 関係
- 上位概念: [[POSIX]]
- 前提: [[Virtual Memory]], [[Page Cache]]
- 対比: [[read]], [[write]]（明示的な複製を伴うI/O）
- 使う / 使われる: [[address_space]]（写像の追跡）, [[File Descriptor]]
- 関連: [[fsync]], [[VFS]]

## 出典
- [mmap(2) - Linux manual page](https://man7.org/linux/man-pages/man2/mmap.2.html)
- [mallopt(3) - Linux manual page](https://man7.org/linux/man-pages/man3/mallopt.3.html)
- [Are You Sure You Want to Use MMAP in Your Database Management System? (CIDR 2022)](https://db.cs.cmu.edu/mmap-cidr2022/)
