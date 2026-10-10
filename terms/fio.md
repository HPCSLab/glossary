---
aliases: [Flexible I/O Tester, fio benchmark, ioengine, iodepth]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# fio（Flexible I/O Tester）

> 読み書きの種類、大きさ、並行度、I/Oの発行方法を指定して記憶装置やファイルシステムに負荷をかけ、その[[Bandwidth|帯域]]、[[IOPS]]、[[Latency|レイテンシ]]を測るベンチマークツールである。

## 概要
fioは、Jens Axboeが、[[Linux Kernel|Linux]]のI/Oの仕組みやスケジューラを試すたびに専用の試験プログラムを書く手間を省くために作ったツールである。負荷は、`[ジョブ名]` で区切ったiniファイル形式のジョブファイル、またはコマンドラインのオプションで記述する。主なオプションは次のとおりである。

| オプション | 意味 |
|---|---|
| `rw` | 読み書きの種類。`read`、`write`、`randread`、`randwrite`、`randrw` など |
| `bs` | 一回のI/Oの大きさ（既定は4096バイト） |
| `ioengine` | I/Oの発行方法。`psync`（既定、`pread`/`pwrite`）、`sync`、`libaio`、`io_uring` など |
| `iodepth` | 非同期のエンジンで同時に発行しておくI/Oの数（キューの深さ） |
| `numjobs` | 同じジョブを複製して並行に動かすスレッドまたはプロセスの数 |
| `direct` | `1` で[[Direct IO\|Direct I/O]]（多くは `O_DIRECT`）を用いる |
| `size` / `runtime` / `time_based` | 読み書きする量、実行時間、量を終えても時間まで繰り返すか |

結果としては、IOPS、帯域、レイテンシが報告される。レイテンシは、I/Oの発行までの時間（slat）、発行から完了までの時間（clat）、全体（lat）に分けて示され、clatは百分位数（99パーセンタイルなど）でも示される。

## どこで出てくるか
[[SSD]]や[[NVMe]]の装置、単一ノードのファイルシステムの性能を測るときに用いる。多数のノードから[[Parallel File System|並列ファイルシステム]]を測る場合には、[[MPI]]で多数のプロセスを協調させる[[IOR]]を用いる。

測定では、設定によって測っているものが変わることに注意を要する。`direct=1` を付けなければ[[Page Cache|ページキャッシュ]]の効果を測ることになる。同期のエンジン（`psync` など）では `iodepth` を増やしても効果がなく、並行度を上げるには `numjobs` を増やすか、`libaio` や[[io_uring]]などの非同期のエンジンを用いる。また、`libaio` はDirect I/Oでないと実質的に非同期に動かない。論文では、`rw`、`bs`、`ioengine`、`iodepth`、`numjobs`、`direct` を明記すると、結果を再現・比較できる。

## 関係
- 対比: [[IOR]]（MPIで多数のノードから並列ファイルシステムを測る）
- 使う / 使われる: [[io_uring]], [[Direct IO]]
- 関連: [[SSD]], [[NVMe]], [[Latency]], [[Bandwidth]], [[Page Cache]]

## 出典
- [fio - Flexible I/O tester documentation](https://fio.readthedocs.io/en/latest/fio_doc.html)
