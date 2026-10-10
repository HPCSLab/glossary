---
aliases: [PromQL, Node Exporter, node_exporter, Exporter, エクスポータ, Alertmanager, Pushgateway]
tags: [term]
maps: ["[[System Administration]]"]
status: draft
updated: 2026-10-10
---
# Prometheus

> 監視対象から数値の指標（メトリクス）を定期的に収集して時系列として蓄積し、問い合わせと警報を行うオープンソースの監視システムである。

## 概要
Prometheusは、2012年ごろにSoundCloudで開発が始まり、2016年にCloud Native Computing Foundation（CNCF）に、Kubernetesに次ぐ二番目のプロジェクトとして加わった。データは[[Time Series Database|時系列]]として格納され、各時系列は、メトリクスの名前と、`instance="node01"` のようなキーと値の組（ラベル）で識別される。ラベルによって、同じ指標をノードやデバイスごとに区別しつつ、まとめて集計できる。

収集は、Prometheusのサーバが監視対象のHTTPのエンドポイントを定期的に取りに行くプル型で行う。監視対象のソフトウェアが自らメトリクスを公開しない場合は、エクスポータと呼ばれる仲介のプログラムを置く。例えば、Node Exporterは、CPU、メモリ、ファイルシステム、ネットワークなどの[[Linux Kernel|カーネル]]の統計を、ポート9100の `/metrics` で公開する。収集したデータはPromQLという問い合わせ言語で集計し、条件を満たしたときの通知はAlertmanagerが担う。短時間で終わるジョブのためには、メトリクスを押し込むPushgatewayがある。

## どこで出てくるか
計算機やクラスタの稼働状況を継続的に記録・監視する場面で用いられ、可視化には[[Grafana]]などを組み合わせる。各ノードでNode Exporterを動かし、Prometheusの設定ファイル `prometheus.yml` の `scrape_configs` に収集先を、`scrape_interval` に収集の間隔を書く。収集の間隔より短い変動は記録されないため、[[perf]]などによる細かな性能解析の代わりにはならない。また、公式の文書は、課金のように完全な正確さを要する用途には向かないとしている。

## 関係
- 上位概念: [[Time Series Database]]
- 使う / 使われる: [[Grafana]]（可視化に用いる）
- 対比: [[InfluxDB]]（データを書き込んでもらうプッシュ型を基本とする時系列データベースである）

## 出典
- [Overview - Prometheus](https://prometheus.io/docs/introduction/overview/)
- [Monitoring Linux host metrics with the Node Exporter - Prometheus](https://prometheus.io/docs/guides/node-exporter/)
