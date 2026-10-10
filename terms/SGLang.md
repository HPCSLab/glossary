---
aliases: [sglang, RadixAttention]
tags: [term]
maps: ["[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-10
---
# SGLang

> [[LLM]]とマルチモーダルモデルの推論とサービングのためのオープンソースのフレームワークであり、RadixAttentionによる要求間での[[KV Cache|KVキャッシュ]]の再利用を特徴とする。

## 概要
SGLangは、Zhengらの論文 "SGLang: Efficient Execution of Structured Language Model Programs" として2023年にarXivで公開され、2024年のNeurIPSで発表された。現在は非営利組織LMSYSのもとでオープンソースとして開発されている。論文が対象としたのは、一回の生成で終わらず、複数回の生成呼び出し、制御フロー、JSONのような構造を持つ入出力を組み合わせるLLMのプログラム（エージェント、少数例を与える推論、[[RAG]]、複数ターンの対話など）である。このようなプログラムでは、同じシステムプロンプトや会話の履歴といった共通の接頭辞を持つ要求が繰り返し発行される。

SGLangは、このプログラムを書くためのフロントエンドの言語と、それを実行するランタイムから成る。ランタイムの中心であるRadixAttentionは、過去の要求のKVキャッシュを捨てずにradix tree（基数木）で管理し、新しい要求の接頭辞と一致する部分のキャッシュを再利用して、その部分のプリフィルの計算を省く。また、JSONなどの決まった形式に従う構造化出力のデコードを、圧縮した有限状態機械で高速化する。論文は、既存の推論システムに比べてスループットが最大6.4倍に向上したと報告している。現在のSGLangは、プレフィックスキャッシュに加え、複数の[[GPU]]への並列化、プリフィルとデコードの分離、投機的デコード、[[Quantization|量子化]]を備え、OpenAI互換のAPIを提供する。NVIDIAとAMDのGPUのほか、Google TPUなどにも対応している。

## どこで出てくるか
SGLangは、[[vLLM]]と並ぶ代表的なLLMの推論エンジンであり、LLMの推論システムの研究で比較対象（ベースライン）として用いられることがある。両者の出発点となった論文は、KVキャッシュに関する着眼点が異なる。vLLMのPagedAttentionは、KVキャッシュをブロック単位で割り当ててメモリの無駄を減らすことを主眼とした。SGLangのRadixAttentionは、要求の間で共通の接頭辞のキャッシュを再利用し、計算を省くことを主眼とした。LLMを自前で動かして評価する際には、両方を試し、[[TTFT]]やスループットを比べることになる。

## 関係
- 上位概念: [[LLM]]
- 対比: [[vLLM]]（PagedAttentionでKVキャッシュのメモリの無駄を減らすことを主眼とした）
- 使う / 使われる: [[KV Cache]], [[GPU]]
- 関連: [[TTFT]], [[RAG]], [[Quantization]]

## 出典
- [SGLang Documentation](https://docs.sglang.io/)
- [SGLang: Efficient Execution of Structured Language Model Programs (Zheng et al.) - arXiv](https://arxiv.org/abs/2312.07104)
- [SGLang: Efficient Execution of Structured Language Model Programs - NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/724be4472168f31ba1c9ac630f15dec8-Abstract-Conference.html)
