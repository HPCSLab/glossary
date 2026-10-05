---
aliases: ["To FUSE or Not to FUSE: Performance of User-Space File Systems", FUSE or not FUSE, Stackfs, Vangoor FAST 2017]
tags: [term, paper]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-06
---
# To FUSE or Not to FUSE

> [[FUSE]]によるユーザ空間のファイルシステムの性能を、多様な負荷と記憶装置で体系的に測定し、その負担がどこから生じるかを分析した、[[FAST]] 2017の論文である。

## 概要
著者は、Stony Brook UniversityのBharath Kumar Reddy Vangoor、Erez Zadokと、IBM Research-AlmadenのVasily Tarasovである。ファイルシステムは伝統的にカーネルの中で実装されてきたが、ユーザ空間のファイルシステムを試作にとどめるべきか、実運用に用いてよいかについては議論があった。著者らは、ストレージの研究者の間でFUSEの性能が、その後の改良を考慮されないまま、低いと決めつけられがちであると指摘し、その性能を初めて網羅的に評価した。

評価のために、著者らはStackfsという、FUSEの要求をそのまま下位の[[ext4]]に渡すだけのファイルシステムを作り、ext4を直接用いた場合と比べた。FUSEの最適化を有効にしない基本の構成（StackfsBase）と、ライトバックキャッシュ、要求の最大の大きさの拡大（4KiBから128KiB）、デーモンのマルチスレッド化、spliceによるデータの複製の削減を全て有効にした構成（StackfsOpt）を、[[HDD]]と[[SSD]]の上で、45種類の負荷で比べた。また、FUSEのカーネルモジュールとlibfuseに、要求の種類ごとの数や待ち行列の状態を記録する計測の仕組みを加え、性能の低下の原因を分析した。

結果は、負荷と装置によって大きく異なった。ext4と比べた性能は、最良で+6.2%（Webサーバの負荷）、最悪で−83.1%（一つのスレッドで大量の小さなファイルを作成する負荷）であり、CPUの使用率は相対的に最大31%増えた。最適化は多くの負荷で性能を大きく改善した一方、一部の負荷では逆に低下させた。二つの構成のうち良い方を選んだ場合、性能が半分以下に落ちたのは、45種類のうちファイルの作成の二つの負荷だけであった。一般に、記憶装置が速いほど、FUSE自体の負担が目立つ。

## どこで出てくるか
FUSEでファイルシステムを試作する研究では、FUSE自体の負担を議論する際に、この論文が参照される。論文の結論は、FUSEの負担は一律に大きいわけではなく、負荷の種類とFUSEの設定に強く依存するということである。自らの評価でも、どの最適化を有効にしたかを明記し、特にメタデータの操作の多い負荷で、FUSEの寄与を分けて議論する必要がある。

ただし、この論文の測定は2017年当時のFUSEと、HDDおよび当時のSATAのSSDを用いたものである。その後、FUSEには、カーネル内で下位のファイルに直接読み書きするパススルーモード（Linux 6.9）や、[[io_uring]]を用いた要求の受け渡し（Linux 6.14）が加わっている。また、[[NVMe]] SSDのような高速な装置では、FUSEの負担がさらに目立つ可能性がある。現在の環境での性能は、改めて測定する必要がある。

## 関係
- 上位概念: [[FUSE]]
- 関連: [[ext4]], [[FAST]], [[SSD]], [[HDD]], [[Metadata]]

## 出典
- [To FUSE or Not to FUSE: Performance of User-Space File Systems - USENIX FAST 2017](https://www.usenix.org/conference/fast17/technical-sessions/presentation/vangoor)
- [論文PDF](https://www.usenix.org/system/files/conference/fast17/fast17-vangoor.pdf)
