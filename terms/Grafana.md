---
aliases: [grafana, Grafana Labs, ダッシュボード, Dashboard]
tags: [term]
maps: ["[[System Administration]]"]
status: draft
updated: 2026-10-10
---
# Grafana

> さまざまなデータベースに保存されたデータを問い合わせ、グラフを並べたダッシュボードとして可視化し、条件に応じて警報を出すオープンソースのツールである。

## 概要
Grafanaは、自らはデータを保存せず、データソースと呼ばれる外部のデータベースに問い合わせて結果を表示する。データソースには、[[Prometheus]]や[[InfluxDB]]などの[[Time Series Database|時系列データベース]]のほか、PostgreSQLやMySQLなどのSQLのデータベースがあり、プラグインによって追加できる。このため、収集と保存を担うシステムと、表示を担うGrafanaとを分けて組み合わせる構成が一般的である。複数のグラフをまとめた画面をダッシュボードと呼び、表示する時間の範囲を変えながら、複数の指標を並べて見比べられる。警報の機能も持ち、指標が条件を満たすとメールやSlackなどに通知する。Grafana Labs社が開発し、オープンソース版のライセンスはAGPL-3.0である。

## どこで出てくるか
計算機やクラスタの監視で、Prometheusなどが収集したCPU、メモリ、ネットワーク、ストレージの使用状況を表示する画面として出てくる。

## 関係
- 使う / 使われる: [[Prometheus]], [[InfluxDB]]（データソース）
- 関連: [[Time Series Database]]

## 出典
- [Introduction to Grafana - Grafana documentation](https://grafana.com/docs/grafana/latest/introduction/)
- [grafana/grafana - GitHub](https://github.com/grafana/grafana)
