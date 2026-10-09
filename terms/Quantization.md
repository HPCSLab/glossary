---
aliases: [量子化, Model Quantization, モデルの量子化, Weight-only Quantization, Post-training Quantization, PTQ, INT8, INT4, FP8, GPTQ, AWQ, bitsandbytes, GGUF]
tags: [term]
maps: ["[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-10
---
# Quantization（量子化）

> 機械学習のモデルの重みなどを、より少ないビット数の数値表現（例えばINT8やINT4）で表すことで、メモリの使用量と計算の負担を減らす手法である。

## 概要
モデルの重みは、もとは32ビットの浮動小数点数（FP32）で表され、現在の大きなモデルでは16ビットのFP16やBF16で保持することが多い。量子化は、これをさらに8ビットや4ビットの整数（INT8、INT4）などに変換し、精度をできるだけ保ちながらモデルを小さくする。例えば、70億パラメータのモデルの重みは、16ビットでは約14GBであるが、4ビットでは約3.5GBになる。

量子化の方法は、何を量子化するかと、いつ量子化するかで分けられる。重みだけを低いビット数にする重みのみの量子化（weight-only）と、重みに加えて計算途中の値（活性化）も量子化する方式がある。また、学習を終えたモデルを後から量子化する学習後量子化（PTQ）が広く用いられる。代表的な手法に、近似的な二次の情報を用いて重みを3〜4ビットに量子化し、1750億パラメータのモデルを約4 GPU時間で量子化したGPTQ（ICLR 2023）や、活性化の分布から重要な約1%の重みを見つけて保護するAWQ（[[MLSys]] 2024の最優秀論文）がある。手法によっては、少量のデータで量子化の誤差を補正する較正（calibration）を要する。

## どこで出てくるか
[[LLM]]の推論で、モデルを限られた[[GPU]]のメモリに収める、あるいはより安価なGPUで動かすために用いられる。推論のデコードの段階は、トークンごとに全ての重みを読み出すため、メモリの[[Bandwidth|帯域]]で律速される。重みのビット数を減らすと読み出す量が減るため、メモリの節約だけでなく速度の向上にもつながる。GPTQの論文は、FP16に比べて高性能なGPUで約3.25倍の推論の高速化を報告している。

[[Hugging Face]]のTransformersは、bitsandbytes、GPTQ、AWQなど多数の量子化の方式に対応しており、[[vLLM]]も各種の量子化に対応する。Hubには量子化済みの重みも公開されている。量子化したモデルを評価に用いる際には、ビット数と手法によって精度と速度が変わるため、どの方式で量子化したかを明記する必要がある。

## 関係
- 使う / 使われる: [[LLM]], [[vLLM]], [[Hugging Face]]
- 関連: [[GPU]], [[Bandwidth]], [[KV Cache]], [[Ozaki Scheme]]（低精度の演算器で高精度の計算を再現する）, [[MLSys]]

## 出典
- [Quantization overview - Hugging Face Transformers](https://huggingface.co/docs/transformers/main/en/quantization/overview)
- [GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers (Frantar et al., ICLR 2023) - arXiv](https://arxiv.org/abs/2210.17323)
- [AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration (Lin et al., MLSys 2024) - arXiv](https://arxiv.org/abs/2306.00978)
