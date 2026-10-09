---
aliases: [Distributed Namespace, Distributed Namespace Environment, Lustre DNE, Remote Directory, リモートディレクトリ, Striped Directory, ストライプディレクトリ, "lfs mkdir -i", "lfs mkdir -c", MDT, MDT0000]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-09
---
# DNE（Distributed Namespace）

> [[Lustre]]のファイルシステムの名前空間を、複数のメタデータサーバ（MDSとそのMDT）に分けて置き、[[Metadata|メタデータ]]の処理を分散させる機能である。

## 概要
Lustreでは、ファイルのデータは多数のOSTに分散されるが、ディレクトリやファイルの名前などのメタデータはMDT（メタデータのターゲット）が保持する。DNEを用いると、ファイルシステムの根を持つ最初のMDT（MDT0000）のほかに、それぞれのMDTを持つMDSを加え、名前空間の一部をそこに置ける。

DNEには二つの形がある。一つはリモートディレクトリであり、あるディレクトリとその下の全てを、指定したMDTに置く。`lfs mkdir -i <MDTの番号> <ディレクトリ>` で作成する。利用者やプロジェクトごとに異なるMDTを割り当てるといった使い方ができる。ただし、そのMDTが使えなくなると、その下のディレクトリにはアクセスできなくなる。もう一つは、Lustre 2.8で導入されたストライプディレクトリであり、一つの大きなディレクトリの中のファイルを、ファイル名のハッシュによって複数のMDTに分散させる。`lfs mkdir -c <ストライプの数> <ディレクトリ>` で作成し、ストライプの数にはMDTの数を指定することが多い。

## どこで出てくるか
一つのディレクトリに大量のファイルを作成するアプリケーションでは、一つのMDTの処理能力がボトルネックとなる。ストライプディレクトリは、このような用途のために用意されており、一つのディレクトリに置けるエントリの数の上限も、ストライプの数の倍に増える。ただし、通常のディレクトリより処理の負担が増えるため、全てのディレクトリをストライプにすべきではないとされている。

## 関係
- 上位概念: [[Lustre]]
- 前提: [[Metadata]]
- 関連: [[Parallel File System]], [[IndexFS]], [[mdtest]], [[EXAScaler]]

## 出典
- [Lustre Software Release 2.x Operations Manual](https://doc.lustre.org/lustre_manual.xhtml)（DNE、Creating a sub-directory on a specific MDT、striped directory）
