---
aliases: [MLCommons, MLPerf Training, MLPerf Inference, MLPerf Storage, MLPerf HPC, MLPerf Training HPC, LoadGen]
tags: [term]
maps: ["[[Machine Learning Systems]]", "[[HPC Storage]]"]
status: draft
updated: 2026-10-16
---
# MLPerf

> 機械学習の学習と推論を行う計算機システムの性能を、共通の規則の下で測り比べるためのベンチマーク群であり、業界団体MLCommonsが策定し、結果を定期的に公表している。

## 概要
機械学習のシステムは、ハードウェアとソフトウェアの組み合わせが多く、[[GPU]]の理論性能などの単一の数値では実際の速さを比較できない。MLPerfは、実際のモデルとデータセットを用いた課題を定め、達成すべき品質と実行の規則を揃えることで、異なる構成のシステムを比較可能にする。学習のMLPerf Trainingと推論のMLPerf Inferenceが中心であり、その方法論は論文（MLSys 2020、ISCA 2020）として発表されている。このほかに、スーパーコンピュータでの学習を測るMLPerf Training: HPCや、ストレージを測るMLPerf Storageなどがある。

MLPerf Trainingは、モデルを定められた品質（例えば言語モデルのlog perplexity）に達するまで学習させる時間を測る。学習は確率的で結果がばらつくため、各課題を複数回実行し、最速と最遅を除いて平均する。MLPerf Inferenceは、すべての提出者が共通の負荷生成器LoadGenを用い、利用の場面を模した4つのシナリオで測る。Offlineは全データを一度に与えて処理能力を、Single Streamは一件ずつ処理したときの[[Latency|レイテンシ]]を、ServerとInteractiveはポアソン分布に従って到着する要求を、レイテンシの制約を守りながら処理できる最大の速さを測る。[[LLM]]の課題では、制約は[[TTFT]]と1トークンあたりの時間（TPOT）で与えられる。推論の精度は、基準となるFP32などの精度の99%または99.9%以上を保つことが求められ、その範囲で[[Quantization|量子化]]などの最適化が許される。

結果は、基準の実装と同じモデルを用いて装置とソフトウェアを比較するClosed部門と、モデルの変更を認めて新しい手法を示すOpen部門に分けて公表される。さらに、市販品のみからなるAvailable、次の回に市販となるPreview、開発中のものを含むRDIの区分がある。

## どこで出てくるか
GPUやAI向けの計算機の発表、ベンダの性能の主張、[[MLSys]]などの論文で、性能の根拠として頻繁に引用される。結果を読む際には、部門と区分、シナリオ、使用した加速器の数を確かめる必要がある。Closed部門の同じ課題どうしでなければ数値は比較できない。また、[[TOP500]]や[[IO500]]と同様に、公表される課題での性能が自分の負荷での性能を表すとは限らない（[[Goodhart's Law|グッドハートの法則]]）。

ストレージの研究では、MLPerf Storageに出会う。これは、GPUを実際には用いず、学習のデータ読み込みのI/Oを[[DLIO]]で模擬し、模擬した加速器の稼働率を一定以上（例えば3D U-Netで90%）に保てる加速器の数と読み込みの[[Bandwidth|帯域]]を報告する。近年は、学習のチェックポイント、[[Vector Database|ベクトル検索]]、[[KV Cache|KVキャッシュ]]の課題も加わっている。

## 関係
- 対比: [[TOP500]]（単一の課題LINPACKで順位を付ける）, [[IO500]]（HPCストレージのベンチマーク）
- 関連: [[GPU]], [[LLM]], [[TTFT]], [[Quantization]], [[Goodhart's Law]], [[MLSys]]

## 出典
- [Benchmarks - MLCommons](https://mlcommons.org/benchmarks/)
- [MLPerf Training - MLCommons](https://mlcommons.org/benchmarks/training/)
- [MLPerf Storage - MLCommons](https://mlcommons.org/benchmarks/storage/)
- [MLPerf Inference Rules - mlcommons/inference_policies](https://github.com/mlcommons/inference_policies/blob/master/inference_rules.adoc)
- [mlcommons/storage - GitHub](https://github.com/mlcommons/storage)
- [MLPerf Training Benchmark (Mattson et al.) - arXiv](https://arxiv.org/abs/1910.01500)
- [MLPerf Inference Benchmark (Reddi et al.) - arXiv](https://arxiv.org/abs/1911.02549)
