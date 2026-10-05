---
aliases: [Multi-Queue Block IO Queueing Mechanism, Multi-Queue Block Layer, ブロック層, Block Layer, I/O Scheduler, I/Oスケジューラ, mq-deadline]
tags: [term]
maps: ["[[Storage]]", "[[Operating System]]"]
status: draft
updated: 2026-10-05
---
# blk-mq

> Linuxカーネルのブロック層において、CPUごとの複数のキューを用いてI/O要求をデバイスドライバへ渡す仕組みである。

## 概要
ブロック層は、[[File System|ファイルシステム]]などから発行されたI/O要求を受け取り、[[Block Storage|ブロックデバイス]]のドライバに渡す、カーネル内の層である。従来のブロック層は、デバイスごとに単一の要求キューと一つのロックを持っていた。HDDの時代には、デバイスの機械的な遅延が支配的であったため問題にならなかったが、[[NVMe]]などの高速なSSDの登場により、ボトルネックはデバイスからOS側に移った。多数のCPUコアが一つのキューのロックを奪い合い、キャッシュの競合も生じたためである。blk-mqは、この問題を解消するために導入された。

blk-mqは二段のキューを持つ。第一段のソフトウェアステージングキューは、CPUごと（あるいはCPUの集合ごと）に置かれ、ロックの競合なしに要求を受け付ける。ここで、隣接するセクタへの要求の併合や、I/Oスケジューラによる並べ替えが行われる。第二段のハードウェアディスパッチキューは、デバイスが持つ投入キューに対応し、ここからドライバに要求が渡される。NVMeのように多数のハードウェアキューを持つデバイスでは、CPUごとのキューを専用のハードウェアキューに直接対応付けられる。デバイスが要求をすぐに受け付けられない場合は、待機リストに置かれて後で送られる。

I/Oスケジューラは差し替え可能であり、`/sys/block/<デバイス名>/queue/scheduler` で確認・変更できる。選択肢には、並べ替えを行わず先着順に渡す `none`、要求の待ち時間に期限を設ける `mq-deadline`、プロセス間で帯域を公平に配分する `bfq`、遅延目標に基づいて流量を制御する `kyber` がある。

## どこで出てくるか
高速なNVMe SSDでは、スケジューラによる並べ替えの効果よりもその処理のコストが目立つため、`none` が選ばれることが多い。一方、HDDや複数のプロセスが帯域を奪い合う環境では、`mq-deadline` や `bfq` が有効な場合がある。ストレージの性能評価では、どのスケジューラが設定されているかで結果が変わるため、実験条件として記録しておく必要がある。[[io_uring]]や[[ublk]]、各種ファイルシステムから発行されたI/Oは、最終的にこの層を通ってデバイスに届く。

## 関係
- 上位概念: [[Block Storage]]
- 使う / 使われる: [[NVMe]]（ハードウェアキューを対応付ける）, [[ext4]], [[io_uring]], [[ublk]]
- 関連: [[Latency]], [[Bandwidth]]

## 出典
- [Multi-Queue Block IO Queueing Mechanism (blk-mq) - The Linux Kernel documentation](https://docs.kernel.org/block/blk-mq.html)
- [Switching Scheduler - The Linux Kernel documentation](https://docs.kernel.org/block/switching-sched.html)
