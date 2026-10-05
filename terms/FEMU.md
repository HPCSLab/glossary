---
aliases: [femu, Flash Emulator, SSD Emulator, SSDエミュレータ]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-06
---
# FEMU

> [[QEMU]]とKVMを基盤とし、SSDの内部構造と振る舞いまでを模擬する、研究用のNVMe SSDエミュレータである。

## 概要
FEMUは、シカゴ大学のHuaicheng Liらが開発し、2018年のFAST（USENIX Conference on File and Storage Technologies）で発表された。論文の題名は "The CASE of FEMU: Cheap, Accurate, Scalable and Extensible Flash Emulator" であり、安価（オープンソースで無償）、正確、スケーラブル、拡張可能であることを掲げている。現在はバージニア工科大学のMoatLabが保守している。

[[SSD]]の研究には二つの障壁がある。市販のSSDは、FTLやガベージコレクションなどの内部の処理が非公開で変更できない。一方、内部を変更できる研究用のハードウェアは高価で入手が難しい。また、SSDのシミュレータの多くは、アプリケーションやOSを実際に動かさずに、記録したI/Oの系列を入力として内部の振る舞いだけを計算するものであった。FEMUは、仮想マシンのNVMeデバイスとしてSSDを模擬し、フラッシュメモリの読み書きと消去の遅延、チャネルやチップの並列性を再現する。そのため、ゲストの中で実際のアプリケーション、ファイルシステム、カーネルを動作させたまま、SSDの内部の設計を変更して、その影響を全体として評価できる。

FEMUには複数の動作形態がある。BlackBox（BBSSD）は、FTLとガベージコレクションを内部に持つ一般的な市販のSSDを模擬する。WhiteBox（OCSSD）は、FTLをホスト側が担うOpen-Channel SSDを模擬する。ZNSは、[[NVMe]]のZoned Namespacesに対応した装置を模擬する。NoSSDは、遅延を最小限にしたメモリ上の装置として動作する。

## どこで出てくるか
FEMUは、FTL、ガベージコレクション、書き込み増幅、ZNSなど、SSD内部の設計と、それがファイルシステムやアプリケーションの性能に与える影響を調べる研究で用いられる。ホスト側の改変だけで済む研究でも、特定の内部特性を持つSSDを再現したい場合に有用である。ただし、FEMUの性能は、ホスト計算機の性能と設定（CPUの割り当て、メモリの量など）に依存し、模擬の正確さにも限界がある。そのため、論文では、模擬のパラメータ（ページの読み書きと消去の遅延、チャネル数など）と実行環境を明記し、絶対的な性能値よりも、設計間の相対的な比較として結果を解釈するのが一般的である。

## 関係
- 上位概念: [[QEMU]]（FEMUはQEMUを拡張したものである）
- 使う / 使われる: [[NVMe]], [[SSD]]（模擬の対象）
- 関連: [[Block Storage]], [[blk-mq]]

## 出典
- [FEMU - GitHub](https://github.com/MoatLab/FEMU)
- [The CASE of FEMU: Cheap, Accurate, Scalable and Extensible Flash Emulator - USENIX FAST 2018](https://www.usenix.org/conference/fast18/presentation/li)
