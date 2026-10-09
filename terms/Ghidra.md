---
aliases: [ギドラ, Software Reverse Engineering, SRE, リバースエンジニアリング, Reverse Engineering, Decompiler, 逆コンパイラ, デコンパイラ, Disassembler, 逆アセンブラ]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-10
---
# Ghidra（ギドラ）

> コンパイル済みの実行ファイルを逆アセンブル・逆コンパイルし、ソースコードなしでその動作を読み解くための、米国国家安全保障局（NSA）が開発したソフトウェアリバースエンジニアリングのフレームワークである。

## 概要
ソフトウェアリバースエンジニアリング（SRE）とは、コンパイル済みのバイナリから、元のプログラムの構造や動作を復元して理解することである。Ghidraはその作業のための道具一式であり、機械語を命令列に戻す逆アセンブル、命令列から[[C]]に近い疑似コードを復元する逆コンパイル、関数呼び出しや制御フローのグラフ表示などを備える。多数のプロセッサの命令セットと実行ファイルの形式に対応し、Windows、macOS、Linuxで動作する。

GhidraはNSAの研究部門が内部で用いてきたものであり、2019年3月のRSA Conferenceでバイナリが公開され、約1か月後にソースコードがApache License 2.0で[[GitHub]]に公開された。本体はJavaで書かれ、逆コンパイラはC++で書かれている。解析の自動化はJavaまたは[[Python]]のスクリプトで行える。GUIを使わずに多数のバイナリを一括で取り込み・解析し、スクリプトを適用するためのヘッドレス解析器（`analyzeHeadless`）もある。デバッガ機能も持ち、[[gdb]]などを背後で用いて実行中のプログラムを調べられる。

[[gdb]]が主にデバッグ情報付きでコンパイルした自分のプログラムを実行しながら調べる道具であるのに対し、Ghidraはソースコードやデバッグ情報が手元にないバイナリを静的に読み解くことを主な用途とする。

## どこで出てくるか
マルウェアの解析や脆弱性の調査など、セキュリティの分野で広く用いられる。ソースコードが手に入らないファームウェアなどの動作を確かめる場面でも用いられ、例えばオープンソースのファームウェアを開発するcorebootプロジェクトはファームウェアの解析にGhidraを用いている。商用の同種のツールにIDA Proがあり、Ghidraは無償で使える代替として比較されることが多い。

## 関係
- 対比: [[gdb]]（実行中のプログラムを調べるのに対し、Ghidraは主にバイナリを静的に解析する）
- 関連: [[C]], [[Python]]

## 出典
- [NationalSecurityAgency/ghidra - GitHub](https://github.com/NationalSecurityAgency/ghidra)
- [Ghidra - Wikipedia](https://en.wikipedia.org/wiki/Ghidra)
- [NSA will demonstrate a free and open source tool for reverse engineering malware - SC Media](https://www.scworld.com/news/nsa-will-demonstrate-a-free-and-open-source-tool-for-reverse-engineering-malware-with-the-hopes-of-improving-security-rather-than-undermining-it)
- [Headless Analyzer README (Ghidra 12.0)](https://www.ghidradocs.com/12.0_PUBLIC/support/analyzeHeadlessREADME.html)
- [AnalyzeHeadless - Ghidra API](https://ghidra.re/ghidra_docs/api/ghidra/app/util/headless/AnalyzeHeadless.html)
