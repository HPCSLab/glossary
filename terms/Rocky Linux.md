---
aliases: [rocky linux, Rocky, RHEL, Red Hat Enterprise Linux, CentOS, CentOS Stream, dnf, RPM, Rocky Enterprise Software Foundation]
tags: [term]
maps: ["[[System Administration]]"]
status: draft
updated: 2026-10-10
---
# Rocky Linux

> Red Hat Enterprise Linux（RHEL）のソースコードから作られ、RHELとバイナリの互換性を持つ、コミュニティによるLinuxのディストリビューションである。

## 概要
Rocky Linuxは、CentOSの共同創設者であるGregory Kurtzerが始めたディストリビューションであり、Rocky Enterprise Software Foundationが保守している。名前は、CentOSの初期の協力者で、その成功を見ることなく亡くなったRocky McGaughにちなむ。

CentOSは、RHELと互換の、本番の環境で利用できる無償のディストリビューションであった。しかし、2020年12月にRed Hatが、CentOSの開発を終え、継続的に更新される開発版のCentOS Streamに移行することを決めた。Rocky Linuxは、これを受けて、RHELと互換の安定したディストリビューションを提供するために作られ、2021年6月に最初の安定版（8.4）が公開された。RHELのソースコードを用いて作られ、RHELとバイナリの互換性を持つことを目標としている。パッケージの管理には、RPM形式のパッケージと `dnf` コマンドを用いる。

| 版 | 名前 | 公開日 | 積極的なサポートの終了 | 保守の終了 |
|---|---|---|---|---|
| Rocky Linux 8 | Green Obsidian | 2021年6月 | 2024年5月 | 2029年5月 |
| Rocky Linux 9 | Blue Onyx | 2022年7月 | 2027年5月 | 2032年5月 |
| Rocky Linux 10 | Red Quartz | 2025年6月 | 2030年5月 | 2035年5月 |

それぞれの主要な版は、新しい機能が加わる5年間の積極的なサポートと、その後のセキュリティの修正のみの5年間の保守を合わせた、10年間にわたって保守される。各主要な版の中では、最新の小さな版（例えば8.10）のみが保守の対象となる。

## どこで出てくるか
Rocky Linuxは、デスクトップ、サーバ、ワークステーションのほか、スーパーコンピュータも対象としている。RHEL系のディストリビューションは、[[Ubuntu]]とは、パッケージを導入するコマンド（`dnf` と `apt`）、パッケージの名前、標準で用いられる[[Linux Kernel|カーネル]]の版が異なる。手順書やエラーの情報を参照する際、また実験の条件を記録する際には、ディストリビューションとその版を確認する必要がある。

## 関係
- 上位概念: [[Linux Kernel]]（Rocky Linuxが用いるカーネル）
- 対比: [[Ubuntu]]（Debian系のディストリビューション）
- 関連: [[Spack]], [[Compute Node]]

## 出典
- [About Rocky Linux - Rocky Linux](https://rockylinux.org/about)
- [Rocky Releases - Rocky Linux Documentation](https://docs.rockylinux.org/10/releases/)
- [Rocky Linux - Wikipedia](https://en.wikipedia.org/wiki/Rocky_Linux)
