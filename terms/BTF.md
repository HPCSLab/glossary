---
aliases: [BPF Type Format, CO-RE, BPF CO-RE, Compile Once Run Everywhere, vmlinux.h, /sys/kernel/btf/vmlinux, CONFIG_DEBUG_INFO_BTF, pahole]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-06
---
# BTF（BPF Type Format）

> カーネルや[[BPF]]のプログラムが持つ構造体や関数の型の情報を、コンパクトに表すための形式である。

## 概要
BTFは、当初はBPFのプログラムとマップのデバッグ情報を表すために作られ、後に関数の型や、ソースコードの行の情報も表せるように拡張された。整数、構造体、関数の型など、19種類の型を表す。BTFは、コンパイラが出力するDWARFのデバッグ情報から、paholeなどの道具で変換して作られ、DWARFに比べてはるかに小さい（最大で100分の1程度）。カーネルを `CONFIG_DEBUG_INFO_BTF` を有効にしてビルドすると、カーネル自身の型の情報が `/sys/kernel/btf/vmlinux` に置かれる。

BTFの最も重要な用途は、CO-RE（Compile Once – Run Everywhere）である。BPFのプログラムはカーネルの内部の構造体を読むことが多いが、構造体のメンバの配置は、カーネルの版や設定によって変わる。従来のbccでは、この問題を避けるために、プログラムを実行する計算機の上で、そのカーネルのヘッダを用いて毎回コンパイルしていた。そのため、対象の計算機にコンパイラとカーネルのヘッダが必要で、起動にも時間がかかった。CO-REでは、Clangが「どの構造体のどのメンバを読むか」を名前と型で記録しておき（BTFの再配置の情報）、読み込み時にlibbpfが実行中のカーネルのBTFと照らし合わせて、実際の位置に書き換える。これにより、一度コンパイルしたプログラムを、異なる版のカーネルでそのまま動かせる。`bpftool btf dump` で、カーネルの全ての型を含むヘッダ `vmlinux.h` を生成でき、カーネルのヘッダのパッケージは不要になる。

## どこで出てくるか
[[bpftrace]]は、カーネルがBTFを持っていれば、カーネルの全ての構造体を参照できる。BPFの道具を使う、あるいは作る際には、まず `/sys/kernel/btf/vmlinux` があるか、すなわち利用するカーネルがBTFを有効にしてビルドされているかを確かめる。BTFはまた、BPFのマップの内容を型に沿って表示したり、検証器のログにソースコードの行を示したりするためにも用いられる。

## 関係
- 上位概念: [[BPF]]
- 使う / 使われる: [[bpftrace]], [[Linux Kernel]]
- 関連: [[gdb]]（DWARFのデバッグ情報を用いる）, [[drgn]]

## 出典
- [BPF Type Format (BTF) - The Linux Kernel documentation](https://docs.kernel.org/bpf/btf.html)
- [BPF CO-RE (Compile Once – Run Everywhere) - Andrii Nakryiko's Blog](https://nakryiko.com/posts/bpf-portability-and-co-re/)
