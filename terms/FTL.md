---
aliases: [Flash Translation Layer, フラッシュ変換層, Page Mapping, Block Mapping, Hybrid Mapping, ページマッピング, ブロックマッピング]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# FTL（Flash Translation Layer）

> ホストから見た論理ブロックアドレスを、NANDフラッシュ上の物理的な位置に対応付け、上書きできないフラッシュを通常の[[Block Storage|ブロックデバイス]]として見せる層である。通常は[[SSD]]のコントローラのファームウェアとして実装される。

## 概要
NANDフラッシュは、書かれたページを上書きできず、消去は多数のページからなるブロックを単位としてしか行えず、ブロックごとに書き換え回数の上限がある。そのため、論理ブロックを常に同じ物理位置に置くことはできない。FTLは、更新のたびにデータを空いている別のページに書き、論理アドレスと物理位置の対応表（マッピングテーブル）を書き換える。この追記型の更新によって無効なページが生じるため、FTLはガベージコレクションで有効なページを移してからブロックを消去し、ウェアレベリングで書き込みを全ブロックに分散させ、不良ブロックを予備のブロックに置き換える。

対応付けの単位によって、ページ単位のページマッピング、ブロック単位のブロックマッピング、両者を組み合わせたハイブリッドマッピングがある。ページマッピングは性能が高いが、対応表が大きく、コストが高い。ブロックマッピングは対応表が小さく安価だが、性能が低い。SSDでは主にページマッピングが、USBメモリでは主にブロックマッピングが用いられる。ページマッピングの対応表の大きさは、容量のおよそ1/1000である。対応表はフラッシュ上にも保存されるため、電源断に備えて保護する必要がある。

## どこで出てくるか
SSDの性能の振る舞い（書き込みを続けたときの低下や、[[Latency|レイテンシ]]の突発的な増加）や書き込み増幅の原因を説明する際に、FTLのガベージコレクションが出てくる。[[QLC]]のSSDのように容量の大きな製品では、対応表を小さくするために対応付けの単位を大きくし、その単位にそろわない書き込みの性能が下がることがある。FTLの処理をホストに移す設計もあり、Open-Channel SSDはFTLをホスト側で担い、[[NVMe]]のZNSは順次書き込みのみを許すゾーンを設けてデータの配置をホストに委ねる。FTLの研究では、内部の振る舞いまで模擬する[[FEMU]]などのエミュレータが用いられる。ホストの側で書き込みを順次化する[[Log-Structured File System|ログ構造のファイルシステム]]は、FTLと同じ考え方をもう一段上の層で用いるものである。

## 関係
- 上位概念: [[SSD]]
- 使う / 使われる: [[FEMU]]（FTLを模擬する）
- 関連: [[QLC]], [[SLC Cache]], [[Log-Structured File System]], [[NVMe]]

## 出典
- [Flash memory controller - Wikipedia](https://en.wikipedia.org/wiki/Flash_memory_controller)
- [Platform Optimization for Performance and Endurance (QLC, CSAL) - Solidigm](https://www.solidigm.com/products/technology/platform-optimization-for-performance-and-endurance-qlc-csal.html)
