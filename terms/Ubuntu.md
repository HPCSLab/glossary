---
aliases: [ubuntu, Ubuntu LTS, Canonical, apt, APT, deb, Ubuntu Pro]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-10
---
# Ubuntu

> Canonicalが開発する、Debianを基にしたLinuxのディストリビューションであり、デスクトップ、サーバ、クラウドで広く用いられている。

## 概要
Ubuntuは、主に自由ソフトウェアとオープンソースソフトウェアからなる、Debianを基にした[[Linux Kernel|Linux]]のディストリビューションであり、Canonicalが開発し、2004年10月に最初の版が公開された。パッケージの管理には、Debianの仕組みであるAPT（`apt` コマンド）と `.deb` 形式のパッケージを用いる。パソコン向けのDesktop、サーバ向けのServer、組込み機器向けのCoreなどの版がある。Webサーバに用いられるLinuxのディストリビューションとして最も広く用いられている。

Ubuntuは、毎年4月と10月の6か月ごとに新しい版を公開し、版の番号は「年.月」で表される（例えば、2026年4月の版は26.04である）。このうち2年に一度、偶数年の4月に公開される版は長期サポート版（LTS）であり、5年間のセキュリティの保守が提供される。Ubuntu Pro（個人の利用では5台まで無償）による延長保守（ESM）を用いると、保守の期間は10年まで、さらに追加の契約で15年まで延びる。LTS以外の版は、9か月間だけ更新が提供される。

## どこで出てくるか
研究室の計算機や、クラウドの[[Virtual Machine|仮想マシン]]、個人の開発環境では、Ubuntuが用いられることが多い。サーバや実験の環境には、保守の期間が長いLTSの版を用いるのが一般的である。ディストリビューションごとに、パッケージを導入するコマンド（Ubuntuの `apt` と、[[Rocky Linux]]などの `dnf`）、パッケージの名前、標準で用いられる[[Linux Kernel|カーネル]]の版が異なるため、手順書やエラーの情報を参照する際には、どのディストリビューションのどの版についてのものかを確認する必要がある。実験の条件としても、使用したディストリビューションとその版、カーネルの版を記録しておく。

## 関係
- 上位概念: [[Linux Kernel]]（Ubuntuが用いるカーネル）
- 対比: [[Rocky Linux]]（Red Hat Enterprise Linuxと互換のディストリビューション）
- 関連: [[Spack]], [[Python]]

## 出典
- [Ubuntu release cycle - Ubuntu](https://ubuntu.com/about/release-cycle)
- [Ubuntu - Wikipedia](https://en.wikipedia.org/wiki/Ubuntu)
