---
aliases: [cudnn, CUDA Deep Neural Network library]
tags: [term]
maps: ["[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-10
---
# cuDNN

> 畳み込みや[[Attention|アテンション]]など、深層学習でよく使われる演算を、NVIDIAの[[GPU]]向けに高度に最適化して提供するライブラリである。

## 概要
cuDNNは、深層ニューラルネットワークのための基本的な演算（プリミティブ）を集めた、[[CUDA]]の上のライブラリである。対象となる演算は、畳み込み、アテンション（scaled dot-product attention）、行列積、正規化、softmax、プーリング、要素ごとの演算などである。畳み込みなどの演算には複数のアルゴリズムが用意されている。また、複数の演算を一つにまとめて実行する融合（fusion）にも対応する。現在のAPIでは、演算をグラフとして表し、[[Python]]またはC++から指定する。

## どこで出てくるか
利用者がcuDNNを直接呼ぶことは少なく、[[PyTorch]]などのフレームワークの下で使われる。PyTorchでは、`torch.backends.cudnn.benchmark = True` とすると、cuDNNが複数の畳み込みのアルゴリズムを試して最も速いものを選ぶ。ただし、実行のたびに異なるアルゴリズムが選ばれうるため、結果の再現性が必要な場合は `benchmark` を無効にし、`torch.backends.cudnn.deterministic = True` で決定的なアルゴリズムだけを使わせる。性能を比較する実験では、この設定が速度と結果の再現性の両方に影響する点に注意を要する。行列積などの線形代数の演算は、[[cuBLAS]]が担う。

## 関係
- 前提: [[CUDA]], [[GPU]]
- 使う / 使われる: [[PyTorch]]
- 対比: [[cuBLAS]]（線形代数の汎用の演算を提供する）
- 関連: [[Transformer]], [[Attention]]

## 出典
- [NVIDIA cuDNN Documentation](https://docs.nvidia.com/deeplearning/cudnn/latest/)
- [torch.backends - PyTorch documentation](https://docs.pytorch.org/docs/2.14/backends.html)
- [Reproducibility - PyTorch documentation](https://docs.pytorch.org/docs/2.14/notes/randomness.html)
