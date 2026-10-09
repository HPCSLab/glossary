---
aliases: [onnx, Open Neural Network Exchange, ONNX Runtime, onnxruntime, ORT, Execution Provider, opset, torch.onnx.export]
tags: [term]
maps: ["[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-10
---
# ONNX（Open Neural Network Exchange）

> 機械学習のモデルを、学習に用いたフレームワークに依存しない共通の形式で表すための、開かれた規格である。

## 概要
ONNXは、2017年にFacebookとMicrosoftが始め、現在はLinux FoundationのLF AI & Dataのもとで運営されている。機械学習の開発者は、一つのフレームワークやその周辺の道具に縛られがちである。ONNXは、モデルを共通の形式で表すことで、あるフレームワークで作ったモデルを、別のフレームワークや推論の環境で使えるようにする。

ONNXのモデルは、演算子（オペレータ）を表すノードからなる、循環のない計算のグラフである。グラフは、入力、出力、学習済みの重みなどの定数（イニシャライザ）を持ち、Protocol Buffersの形式でファイルに保存される。演算子には、加算や乗算などの数学の演算、ReLUなどの活性化関数、畳み込み（Conv）やLSTMなどのニューラルネットワークの層、[[Quantization|量子化]]のための演算などがある。演算子は版によって定義が変わることがあり、モデルはどの版の演算子の集合（opset）を用いるかを持つ。ONNXに対応するフレームワークは、これらの演算子の実装を提供する。

## どこで出てくるか
[[PyTorch]]では `torch.onnx.export()` でモデルをONNXの形式に書き出せる。書き出したモデルは、Microsoftが開発するONNX Runtimeなどで実行できる。ONNX Runtimeは、モデルのグラフを最適化し、利用できるハードウェアに応じて部分グラフに分け、それぞれを実行プロバイダ（execution provider）と呼ばれる、ハードウェアごとのライブラリに割り当てる。実行プロバイダには、CPUのほか、NVIDIAの[[CUDA]]とTensorRT、IntelのOpenVINO、AMDのROCmなどがある。ONNX Runtimeは、クラウドからモバイル、ブラウザまで多くの環境で動作する。

学習はPyTorchで行い、推論はONNXに書き出して別の環境で行う、というように、学習と推論の環境を分けたい場合に用いられる。

## 関係
- 使う / 使われる: [[GPU]], [[CUDA]]

## 出典
- [About ONNX - ONNX](https://onnx.ai/about.html)
- [ONNX Concepts - ONNX documentation](https://onnx.ai/onnx/intro/concepts.html)
- [ONNX Runtime documentation](https://onnxruntime.ai/docs/)
- [microsoft/onnxruntime - GitHub](https://github.com/microsoft/onnxruntime)
- [torch.onnx - PyTorch documentation](https://docs.pytorch.org/docs/stable/onnx.html)
