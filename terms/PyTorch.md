---
aliases: [pytorch, torch, Tensor, テンソル, autograd, Autograd, 自動微分, torch.compile, torch.distributed, DistributedDataParallel, DDP, PyTorch Foundation]
tags: [term]
maps: ["[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-06
---
# PyTorch

> [[Python]]から使う、オープンソースの深層学習のフレームワークであり、[[GPU]]で動く多次元配列（テンソル）の演算と、自動微分を中心とする。

## 概要
PyTorchは、Meta AI（旧Facebook AI Research）が開発し、2016年9月に公開された。Luaを用いた機械学習のライブラリTorchの後継である。2018年3月にはCaffe2を統合し、2022年9月にLinux FoundationのもとのPyTorch Foundationに移管された。Python、C++、CUDAで書かれ、BSDライセンスで公開されている。

PyTorchの基本のデータ構造はテンソル（多次元の配列）であり、CPUやGPUの上で扱う。GPUでの演算には[[CUDA]]などを用いる。自動微分の機能（autograd）は、演算を実行するたびにその履歴をグラフとして記録し、出力から入力へとたどって連鎖律により勾配を計算する（逆方向の自動微分）。演算を実行しながらグラフを作るため、Pythonの通常の制御構文をそのまま使ってモデルを書ける。2023年3月のPyTorch 2.0では、Pythonのコードを解析してモデルを最適化し、コンパイルする `torch.compile` が導入された。

## どこで出てくるか
深層学習の研究では、モデルの記述と学習に広く用いられている。[[Hugging Face]]のTransformersなどのライブラリもPyTorchの上で動く。複数のGPUやノードを用いる学習では、`torch.distributed` が通信の機能を提供し、その通信の実装（バックエンド）として、NVIDIAのGPUの間の通信ライブラリNCCL、Gloo、[[MPI]]などを選べる。`DistributedDataParallel`（DDP）は、各GPUがモデルの複製を持ち、それぞれのデータで計算した勾配を[[Collective Communication|集団通信]]で同期するデータ並列の学習を提供する。学習したモデルは、[[ONNX]]の形式に書き出して他の環境で推論することもできる。

## 関係
- 使う / 使われる: [[Python]], [[CUDA]], [[GPU]], [[Collective Communication]], [[MPI]]
- 関連: [[Hugging Face]], [[ONNX]], [[LLM]]

## 出典
- [PyTorch - PyTorch Foundation](https://pytorch.org/projects/pytorch/)
- [PyTorch - Wikipedia](https://en.wikipedia.org/wiki/PyTorch)
- [Autograd mechanics - PyTorch documentation](https://docs.pytorch.org/docs/stable/notes/autograd.html)
- [torch.compile - PyTorch documentation](https://docs.pytorch.org/docs/stable/generated/torch.compile.html)
- [Distributed communication package - torch.distributed - PyTorch documentation](https://docs.pytorch.org/docs/stable/distributed.html)
- [DistributedDataParallel - PyTorch documentation](https://docs.pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html)
