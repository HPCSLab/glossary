---
aliases: [Low-Rank Adaptation, 低ランク適応, LoRAアダプタ, LoRA Adapter, QLoRA]
tags: [term]
maps: ["[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-17
---
# LoRA（低ランク適応）

> 事前学習したモデルの重みを凍結したまま、層ごとに小さな低ランクの行列の組を加えてその行列だけを学習することで、少ないメモリでモデルを特定の用途に適応させる手法である。

## 概要
事前学習したモデルを特定の課題やデータに合わせて追加で学習すること（ファインチューニング）は、全ての重みを更新すると、重みに加えて勾配とオプティマイザの状態（Adamでは重み一つにつき二つの値）を[[GPU]]のメモリに置く必要があり、用途ごとにモデル全体の複製も保存することになる。LoRA（Low-Rank Adaptation）は、Microsoftの研究者らが2021年に提案した手法であり、適応による重みの変化は低いランクの行列で近似できるという仮定に立つ。d×dの重みWを凍結し、その変化をd×rの行列Bとr×dの行列Aの積BAで表して、AとBだけを学習する。rはdより十分小さく（例えば8や16）、学習する値の数はWの数百分の一程度になる。論文は、GPT-3 175BをAdamで全て学習する場合に比べ、学習する値の数が約1万分の1、GPUのメモリが約3分の1になると報告している。

![[LoRA Low-Rank Update.excalidraw]]

Bを0で初期化するため、学習の開始時の出力は元のモデルと一致する。学習を終えたら W + BA を一つの行列にまとめられるため、層を追加する他の手法と異なり、推論の計算と[[Latency|レイテンシ]]は増えない。まとめずに保存すれば、一つの基盤モデルに用途ごとの小さなアダプタを付け替えて使える。LoRAは主に[[Transformer]]のアテンションの射影の行列などに適用される。

## どこで出てくるか
[[LLM]]を手元のデータに合わせて調整するときの標準的な方法であり、[[Hugging Face]]のPEFTライブラリでは、ランク `r`、出力の倍率 `lora_alpha`、適用する層 `target_modules` を指定して用いる。学習したアダプタは基盤モデルより桁違いに小さいファイルとしてHubで配布される。基盤モデルの重みを4ビットに[[Quantization|量子化]]して凍結し、その上でLoRAのアダプタを学習するQLoRAは、65Bパラメータのモデルを48GBのGPU一台で調整できることを示した。[[DGX Spark]]のようにメモリの限られた一台の計算機で大きなモデルを調整する場合にも、全ての重みを学習する方法より必要なメモリが少ないことが利点となる。

## 関係
- 前提: [[Transformer]]
- 使う / 使われる: [[Hugging Face]]
- 関連: [[Quantization]]

## 出典
- [LoRA: Low-Rank Adaptation of Large Language Models (Hu et al., arXiv:2106.09685)](https://arxiv.org/abs/2106.09685)
- [QLoRA: Efficient Finetuning of Quantized LLMs (Dettmers et al., arXiv:2305.14314)](https://arxiv.org/abs/2305.14314)
- [LoRA - PEFT documentation (Hugging Face)](https://huggingface.co/docs/peft/main/en/developer_guides/lora)
