---
aliases: [influxdb, InfluxDB 3, InfluxDB 3 Core, InfluxQL, Line Protocol, ラインプロトコル, Telegraf]
tags: [term]
maps: ["[[System Administration]]"]
status: draft
updated: 2026-10-10
---
# InfluxDB

> 時刻の付いた計測値やイベントの記録を大量に書き込み、時間の範囲で高速に問い合わせることに特化した時系列データベースである。InfluxData社が開発している。

## 概要
InfluxDBは、[[Time Series Database|時系列データベース]]の代表的な実装の一つである。データは外部のプログラムが書き込みのAPIを通じて送り込む。書き込みの形式であるラインプロトコルでは、一行が一つの記録であり、`cpu,host=node01 usage=42.5 1556813561098000000` のように、表の名前、タグ（`host=node01` のような、記録を区別するためのキーと値の組）、フィールド（計測値）、タイムスタンプを並べる。

版によって設計が大きく異なる。現行のInfluxDB 3では、オープンソース版のInfluxDB 3 Coreが提供されている。InfluxDB 3はデータを[[Parquet]]のファイルとして、ローカルのディスクまたは[[Object Storage|オブジェクトストレージ]]に保存し、問い合わせにはSQLと、旧版から引き継いだInfluxQLを使える。Coreは直近のデータを用いるリアルタイムの監視を主な用途とし、長期の履歴の分析などは商用のEnterprise版が担う。InfluxDB 1.xと2.xの書き込みのAPIとの互換性を持つ。

## どこで出てくるか
計測値を収集して送る道具としてInfluxData社のTelegrafを、可視化には[[Grafana]]などを組み合わせて、監視やダッシュボードの基盤として用いる。版ごとに問い合わせ言語や設定が異なるため、文書や記事を読む際には、どの版を対象としたものかを確かめる必要がある。

## 関係
- 上位概念: [[Time Series Database]]
- 使う / 使われる: [[Parquet]], [[Object Storage]], [[Grafana]]（可視化に用いる）
- 対比: [[Prometheus]]（監視対象からメトリクスを取りに行くプル型の監視システムである）

## 出典
- [InfluxDB 3 Core documentation](https://docs.influxdata.com/influxdb3/core/)
- [Get started with InfluxDB 3 Core](https://docs.influxdata.com/influxdb3/core/get-started/)
- [Line protocol reference - InfluxDB 3 Core](https://docs.influxdata.com/influxdb3/core/reference/line-protocol/)
