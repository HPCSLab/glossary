---
aliases: [詳解 システム・パフォーマンス, 詳解システム・パフォーマンス, Systems Performance Enterprise and the Cloud, USE Method, USEメソッド, Brendan Gregg]
tags: [term, book]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-06
---
# Systems Performance（詳解 システム・パフォーマンス）

> Brendan Greggによる、OS、カーネル、ハードウェア、アプリケーションにわたるシステムの性能分析の方法論とツールを体系的に解説した書籍である。

## 概要
原著は *Systems Performance: Enterprise and the Cloud* であり、第2版が2020年にAddison-Wesleyから刊行された。日本語訳は『詳解 システム・パフォーマンス 第2版』（西脇靖紘 監訳、長尾高弘 訳、オライリー・ジャパン、2023年）である。著者はNetflixなどで性能エンジニアを務め、[[BPF]]を用いた観測ツールやフレームグラフの開発で知られる。

本書の特徴は、個々のツールの使い方よりも、性能問題に取り組む方法論を重視する点にある。その代表がUSEメソッドであり、「すべての資源について、使用率（Utilization）、飽和度（Saturation）、エラー（Errors）を確認する」という手順である。使用率は資源が仕事をしていた時間の割合、飽和度は資源が処理しきれずに待たされている仕事の程度（多くは待ち行列の長さ）、エラーはエラーの発生回数を指す。CPU、メモリ、ディスク、ネットワークなどの資源を網羅的に点検することで、思い付きで計測を始めるよりも確実にボトルネックを特定できる。

内容は、方法論、OSの基礎、観測ツールの概説に続いて、アプリケーション、CPU、メモリ、ファイルシステム、ディスク、ネットワーク、クラウドの各章で、それぞれの仕組み、方法論、ツールを解説する。第2版では、[[perf]]、Ftrace、BPFを用いたツールの解説が大幅に拡充され、Linuxを中心とした内容となっている。ベンチマークの正しい行い方を論じた章も含まれる。

## どこで出てくるか
本書は、Linuxシステムの性能を分析するための標準的な参考書として広く読まれている。新メンバーが全体を通読する必要はないが、方法論の章と、自分の研究に関係する資源（例えばストレージであればファイルシステムとディスクの章）の章を読んでおくと、[[strace]]や[[perf]]などの個々のツールの位置付けが明確になる。ベンチマークの章は、実験を設計し結果を解釈する際の落とし穴を把握するのに役立つ。[[Page Cache|ページキャッシュ]]の影響、[[Latency|レイテンシ]]の分布、[[Little's Law|リトルの法則]]など、このノート群で扱う多くの概念が本書でも扱われている。

## 関係
- 関連: [[perf]], [[BPF]], [[strace]], [[ltrace]], [[Latency]], [[Bandwidth]], [[Page Cache]]

## 出典
- [詳解 システム・パフォーマンス 第2版 - オライリー・ジャパン](https://www.oreilly.co.jp/books/9784814400072/)
- [Systems Performance: Enterprise and the Cloud, 2nd Edition - Brendan Gregg](https://www.brendangregg.com/systems-performance-2nd-edition-book.html)
- [The USE Method - Brendan Gregg](https://www.brendangregg.com/usemethod.html)
