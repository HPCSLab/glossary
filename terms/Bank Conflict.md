---
aliases: [バンク競合, バンクコンフリクト, バンク衝突, Shared Memory Bank Conflict, 共有メモリのバンク競合, Memory Bank, メモリバンク, N-way Bank Conflict]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-17
---
# Bank Conflict（バンク競合）

> GPUの共有メモリで、ワープ内の複数のスレッドが同じバンクの異なるアドレスに同時にアクセスし、そのアクセスが順番に処理されて遅くなる現象である。

## 概要
[[CUDA]]の共有メモリ（shared memory）は、[[GPU]]のSMの中にある[[SRAM]]であり、同じスレッドブロックのスレッドがデータを受け渡すのに用いる。共有メモリは、同時にアクセスできる等しい大きさの区画（バンク）に分かれている。compute capability 5.x以降では、バンクは32個あり、各バンクは1クロックに32ビットを読み書きできる。連続する4バイトの語は順に隣のバンクに置かれるため、語の番号を32で割った余りがバンクの番号になる。ワープの32個のスレッドが全て異なるバンクにアクセスすれば一度に処理されるが、n個のスレッドが同じバンクの異なる語にアクセスすると、アクセスはn回に分けて順に処理され（n-wayの競合）、実効的なバンド幅は1/nになる。複数のスレッドが同じ語を読む場合は、値が全員に配られる（broadcast）ため競合にならない。

![[Shared Memory Bank Conflict.excalidraw]]

典型的な例は、32×32の二次元配列を共有メモリに置き、列の方向に読む場合である。一行がちょうど32語であるため、一つの列の要素は全て同じバンクに入り、32-wayの競合となる。行の長さを33語にする（`tile[32][33]` のように一列の詰め物を加える）と、行ごとにバンクが一つずれ、競合が無くなる。一般に、スレッドtが語 s×t にアクセスする場合、競合の度合いはsと32の最大公約数となり、sが奇数なら競合しない。

## どこで出てくるか
行列の転置や行列積、ステンシル計算のように、[[Bandwidth|バンド幅]]を稼ぐためにデータをタイルに分けて共有メモリに置くカーネルを最適化するときに問題となる。NVIDIAのブログの行列転置の例では、詰め物によって競合を除くと、転置の性能が単純なコピーの約95%まで上がった。プロファイラのNsight Computeのメモリの解析には共有メモリのバンク競合が示されるため、共有メモリを用いるカーネルが期待より遅い場合に確認する項目の一つとなる。全体のメモリ（グローバルメモリ）でのアクセスをまとめる条件（coalescing）とは別の問題であり、両方を満たすように配置を考える必要がある。

## 関係
- 前提: [[CUDA]], [[GPU]]
- 関連: [[SRAM]]

## 出典
- [CUDA C++ Best Practices Guide: Shared Memory and Memory Banks (NVIDIA)](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html)
- [An Efficient Matrix Transpose in CUDA C/C++ (NVIDIA Technical Blog)](https://developer.nvidia.com/blog/efficient-matrix-transpose-cuda-cc/)
