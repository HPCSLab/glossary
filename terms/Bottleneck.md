---
aliases: [ボトルネック, 律速, 律速段階, 律速要因, Rate-Limiting Step, Rate-Determining Step, Bound, バウンド, I/O-bound, I/O律速, CPU-bound, Communication-bound, 通信律速]
tags: [term]
maps: ["[[Parallel Computing]]", "[[Storage]]"]
status: draft
updated: 2026-10-11
---
# Bottleneck（ボトルネック、律速）

> システムを構成する資源や処理段階のうち、その処理能力がシステム全体の性能の上限を決めているものである。

## 概要
処理は、CPUの演算、メモリの読み書き、ネットワークの通信、記憶装置へのI/Oなど、複数の資源や段階を経て進む。データが段階を順に流れる処理では、全体のスループットは最も遅い段階の処理能力を超えられない。この段階がボトルネックである。ボトルネックとなった資源は[[Saturation|飽和]]しており、他の資源には余裕がある。そのため、ボトルネック以外の資源をいくら速くしても全体の性能は上がらず、性能を改善するには、まずボトルネックを特定する必要がある。ボトルネックを解消すると、次に遅い資源が新たなボトルネックとなる。

日本語では、ボトルネックによって性能が制限されることを「律速」と言い、「メモリ律速」「I/O律速」のように制限している資源の名で呼ぶ。英語では memory-bound、I/O-bound のように bound を付ける。律速は、化学反応の全体の速さが最も遅い段階（律速段階、rate-determining step）で決まることに由来する語である。

## どこで出てくるか
性能の分析と論文の議論の中心である。単一のノードでは、[[Roofline Model|ルーフラインモデル]]によって、計算が演算性能で律速される（演算律速）か、メモリの[[Bandwidth|バンド幅]]で律速される（メモリ律速）かを見積もる。多くのHPCのアプリケーションや、[[LLM]]の推論のデコードの段階は、メモリ律速である。並列計算では、プロセス数を増やすと、通信や同期、[[Amdahl's Law|逐次部分]]が律速となりやすい。ストレージでは、大量の小さなファイルを扱うときに[[Metadata|メタデータ]]の処理がボトルネックとなることが多い。また、[[NVMe]]の[[SSD]]のように装置が速くなると、ボトルネックが装置からOSのソフトウェアに移り、[[blk-mq]]などの設計の見直しにつながった。

ボトルネックを特定するには、[[perf]]などのツールで時間の使われ方を計測し、[[Systems Performance|USEメソッド]]のように資源ごとの使用率と飽和度を点検する。論文で手法の効果を示すときも、従来の方式では何が律速となっていて、提案手法がそれをどう解消したかを示すのが基本である。

## 関係
- 前提: [[Saturation]], [[Bandwidth]], [[Latency]]
- 使う / 使われる: [[Roofline Model]]（演算律速とメモリ律速を見分ける）
- 関連: [[Amdahl's Law]], [[perf]], [[Systems Performance]], [[Metadata]]

## 出典
- [The USE Method - Brendan Gregg](https://www.brendangregg.com/usemethod.html)
- [Rate-determining step - Wikipedia](https://en.wikipedia.org/wiki/Rate-determining_step)
- [Roofline: An Insightful Visual Performance Model for Multicore Architectures (Williams, Waterman, Patterson, CACM 2009)](https://doi.org/10.1145/1498765.1498785)
