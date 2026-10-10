---
aliases: [cublas, cuBLASLt, cuBLASXt]
tags: [term]
maps: ["[[Parallel Computing]]", "[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-10
---
# cuBLAS

> 基本的な線形代数の演算の標準的なインタフェースであるBLASを、NVIDIAの[[GPU]]上で[[CUDA]]を用いて実装したライブラリである。

## 概要
[[BLAS]]（Basic Linear Algebra Subprograms）は、ベクトルと行列の基本的な演算を定めた標準のルーチン群であり、ベクトル同士の演算（レベル1）、行列とベクトルの演算（レベル2）、行列と行列の演算（レベル3）に分けられる。LAPACKなどの多くの数値計算ソフトウェアはBLASの上に作られており、計算機ごとに最適化したBLASの実装を差し替えることで、同じプログラムで高い性能を得られる。cuBLASは、そのNVIDIAのGPU向けの実装である。

中でも最も重要なのは行列積（GEMM）である。cuBLASは、Fortranとの互換性のために行列を列優先（column-major）で格納するとみなすため、行優先の配列を扱うC/C++のプログラムでは、添字の対応や転置に注意を要する。使う際は、`cublasCreate()` でハンドルを作り、以後の呼び出しにそれを渡す。データはあらかじめGPUのメモリに置いておく。cuBLASは、速いと判断した場合にはTensor Coreを自動的に用いる。行列積に特化し、データの配置や精度、アルゴリズムを細かく指定できるcuBLASLtと、複数のGPUに処理を分配するcuBLASXtのAPIもある。

## どこで出てくるか
深層学習のフレームワークの内部で用いられる。[[PyTorch]]は、NVIDIAのGPUで行列積などのBLASの演算を行う際、既定でcuBLASを用い、`torch.backends.cuda.preferred_blas_library()` でcuBLASLtに切り替えることもできる。また、AI向けのGPUではFP64の性能が相対的に低いため、cuBLASは[[Ozaki Scheme|Ozakiスキーム]]に基づき、低精度の演算器を用いてFP64の行列積をエミュレーションする機能を備えている。

## 関係
- 上位概念: [[BLAS]]
- 前提: [[CUDA]], [[GPU]]
- 使う / 使われる: [[PyTorch]], [[Ozaki Scheme]]
- 関連: [[cuDNN]], [[Transformer]]

## 出典
- [cuBLAS - NVIDIA Documentation](https://docs.nvidia.com/cuda/cublas/index.html)
- [BLAS (Basic Linear Algebra Subprograms) - Netlib](https://www.netlib.org/blas/)
- [torch.backends - PyTorch documentation](https://docs.pytorch.org/docs/2.14/backends.html)
