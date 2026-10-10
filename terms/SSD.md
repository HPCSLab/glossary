---
aliases: [Solid State Drive, ソリッドステートドライブ, NAND Flash, NANDフラッシュ, Write Amplification, 書き込み増幅, Garbage Collection, TRIM, ZNS, Zoned Namespaces]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# SSD（ソリッドステートドライブ）

> NANDフラッシュメモリを記憶媒体とし、機械的な可動部を持たない記憶装置である。

## 概要
SSDは、外部に対しては[[HDD]]と同じく[[Block Storage|ブロックデバイス]]として振る舞い、任意の論理ブロックを読み書きできるように見える。しかし、内部のNANDフラッシュメモリには、HDDとは大きく異なる制約がある。フラッシュは、ページ（数KiB〜十数KiB）を単位として読み書きするが、既に書かれたページをそのまま上書きすることはできず、書き直すには事前に消去が必要である。しかも消去は、多数のページからなるはるかに大きなブロックを単位としてしか行えない。さらに、各ブロックが耐えられる書き込みと消去の回数には上限がある。

この制約を隠すのが、SSDのコントローラ上で動作する[[FTL]]（Flash Translation Layer）である。FTLは、ホストから見た論理ブロックアドレスと、フラッシュ上の物理的な位置との対応表を管理する。論理ブロックが更新されると、新しいデータを空いている別のページに書き、対応表を書き換えて、古いページを無効とする（追記型の更新）。無効なページが増えると、FTLはガベージコレクションによって、ブロック内のまだ有効なページを別の場所へ移してから、そのブロックを消去し、空き領域として回収する。また、書き込みが特定のブロックに集中しないよう、ウェアレベリングによって書き込み先を分散させる。

ガベージコレクションやウェアレベリングによる移動のため、フラッシュへ実際に書き込まれるデータ量は、ホストが書き込んだ量より大きくなる。この比を書き込み増幅（write amplification）と呼ぶ。書き込み増幅は、性能を低下させ、寿命を縮める。これを抑える手段として、利用者に見せない予備の容量を確保するオーバープロビジョニングと、ファイルシステムが削除済みの領域をSSDに通知するTRIM（Linuxでは `fstrim` やマウントオプション `discard`）がある。[[NVMe]]のZNS（Zoned Namespaces）は、記憶領域を順次書き込みのみを許すゾーンに分割し、データの配置をホストに委ねることで、デバイス側の書き込み増幅とオーバープロビジョニングを削減する。

## どこで出てくるか
SSDの性能は、書き込みの履歴に強く依存する。新品や全領域を消去した直後は、ガベージコレクションが不要なため高い書き込み性能を示すが、書き込みを続けると空きブロックが枯渇し、ガベージコレクションが前面のI/Oと競合して性能が低下する。そのため、性能評価では、事前に十分な量を書き込んで定常状態に到達させてから測定する（プレコンディショニング）必要がある。この手順を省いた測定結果は、実運用での性能を過大に示すことがある。また、ガベージコレクションは不規則に生じるため、平均値よりもテール[[Latency|レイテンシ]]に影響が現れやすい。ストレージシステムやファイルシステムの研究では、ログ構造化の設計によって書き込みを順次化し、書き込み増幅を減らす手法が多く提案されている。

## 関係
- 上位概念: [[Block Storage]]
- 使う / 使われる: [[NVMe]]（SSDを接続するインタフェース）
- 対比: [[HDD]]
- 関連: [[Latency]], [[Bandwidth]], [[blk-mq]]

## 出典
- [Write amplification - Wikipedia](https://en.wikipedia.org/wiki/Write_amplification)
- [Flash memory controller - Wikipedia](https://en.wikipedia.org/wiki/Flash_translation_layer)
- [NVMe Zoned Namespaces (ZNS) Command Set Specification - NVM Express](https://nvmexpress.org/specification/nvme-zoned-namespaces-zns-command-set-specification/)
