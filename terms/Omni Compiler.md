---
aliases: [Omni, omni-compiler, XcodeML, XcalableMP, XMP, XcalableACC, xmpcc, xmpf90, ompcc]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-10
---
# Omni Compiler

> 並列化の指示文を含むCとFortranのプログラムを、通常のコンパイラが扱えるプログラムに変換する、ソースからソースへの変換コンパイラを作るための基盤であり、XcalableMPなどの処理系を提供する。

## 概要
Omni Compilerは、[[RIKEN|理化学研究所計算科学研究センター（R-CCS）]]のプログラミング環境研究チームと、筑波大学のHPCS研究室が開発しているオープンソースのソフトウェアであり、[[GitHub]]で公開されている。CとFortranのプログラムを、XMLで書かれた中間表現であるXcodeMLに変換し、XcodeMLの上で指示文を解釈してプログラムを書き換え、再びCやFortranのプログラムに戻す。変換後のプログラムは、それぞれの計算機の通常のコンパイラ（ネイティブコンパイラ）でコンパイルされる。

Omni Compilerは、次の言語の処理系を提供する。XcalableMP（XMP）は、分散メモリの計算機向けの並列プログラムを、逐次のプログラムに指示文を加えることで書けるようにする、CとFortranの言語拡張である。全体のデータを一つの配列として扱い、指示文でその分割や並列化を指定する global-view のモデルと、各プロセスの持つデータを coarray の記法で一方向の通信によって読み書きする local-view のモデルを持つ。XMPの規格は、日本のPCクラスタコンソーシアムの支援を受けた作業部会が策定しており、Omni CompilerはXMPの参照実装である。このほか、GPUなどのアクセラレータ向けの[[OpenACC]]と、XMPとOpenACCを組み合わせてアクセラレータを持つクラスタを対象とするXcalableACCにも対応する。

## どこで出てくるか
XMPのプログラムは、Cの場合は `xmpcc`、Fortranの場合は `xmpf90` でコンパイルし、`mpirun` で[[MPI]]のプログラムと同じように起動する。XMPは、MPIのインタフェースや、[[OpenMP]]との組み合わせ（ハイブリッド並列）とも連携できる。並列プログラミング言語の処理系の研究では、指示文を解釈してプログラムを書き換える部分を、Omni Compilerの基盤の上に実装できる。

## 関係
- 使う / 使われる: [[MPI]], [[OpenACC]], [[C]]
- 関連: [[OpenMP]]

## 出典
- [Omni Compiler](https://omni-compiler.org/)
- [omni-compiler/omni-compiler - GitHub](https://github.com/omni-compiler/omni-compiler)
- [XcalableMP](https://xcalablemp.org/)
