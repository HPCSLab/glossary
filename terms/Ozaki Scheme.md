---
aliases: [Ozakiスキーム, ozakiスキーム, オザキスキーム, Ozaki Scheme I, Ozaki Scheme II, Ozaki-I, Ozaki-II, FP64 Emulation, FP64エミュレーション, DGEMM Emulation, Error-free Transformation of Matrix Multiplication, 行列積の無誤差変換]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-06
---
# Ozaki Scheme（Ozakiスキーム）

> 行列を精度の低い複数の行列に分割し、それらの行列積を組み合わせることで、高い精度（例えばFP64）の行列積を、低精度の高速な行列演算器の上で再現する手法である。

## 概要
元となる手法（Ozaki Scheme I）は、Katsuhisa Ozaki、Takeshi Ogita、Shin'ichi Oishi、Siegfried M. Rumpが、2012年に Numerical Algorithms 誌で、行列積の無誤差変換として発表した。浮動小数点数の行列AとBを、仮数部の上位から少しずつのビットを持つ複数の行列（スライス）の和に分解する（Aをk個、Bをl個）。各スライスのビット数は、行列の大きさに応じて、スライス同士の積とその和が丸め誤差なしに計算できるように選ばれる。すると、ABは、丸め誤差のない k×l 個の行列積の和に変換される。各行列積には、高速な既存の行列積のルーチン（GEMM）をそのまま使える。また、和をとる順序を固定すれば、結果は計算の環境によらず再現可能になる。

この手法は、近年、GPUのテンソルコアの活用で注目されている。機械学習向けのGPUでは、低精度の行列演算器の性能がFP64の演算器を大きく上回る。例えば、FP64の性能に対するINT8のテンソルコアの性能の比は、NVIDIA B200で約121倍、一般向けのRTX 5090では約1,020倍である。スライスを適切に拡大縮小して型を変換すれば、各スライスの行列積をFP16やINT8のテンソルコアで計算でき、FP64の行列積（DGEMM）を、FP64の演算器を使うよりも速く再現できる場合がある。

スライスの数を増やすと、行列積の回数は k×l に比例して増える。2025年に、Ozaki、Uchino、Imamuraが提案したOzaki Scheme IIは、中国剰余定理を用い、行列を互いに素な複数の法による剰余の行列に分解する。法の数に比例する回数のINT8の行列積で済むため、従来の手法より少ない計算で同等の精度が得られる。論文では、FP64の行列積の再現でNVIDIA GH200において56.6〜80.2 TFLOPSを達成し、FP64の演算器による実測の性能を上回ったと報告している。

## どこで出てくるか
AI向けのGPUでFP64の演算器の性能が相対的に低くなる中、科学技術計算に必要なFP64の行列積をどう確保するかという議論で用いられる。NVIDIAの数値計算ライブラリcuBLASは、Ozaki-IとOzaki-IIに基づく固定小数点のエミュレーションによってFP64の行列積を計算する機能を備える。理化学研究所の次期のスーパーコンピュータ（FugakuNEXT）に向けたセミナーでも取り上げられている。

スーパーコンピュータの評価の文脈でも、FP64のエミュレーションによる行列積や[[LINPACK|HPL]]の性能と電力あたりの性能を、FP64の演算器を用いる場合と比べる発表が行われている（ISC 2024）。エミュレーションで得られる精度はスライスや法の数で決まるため、利用する際には、必要な精度に対してその数がどう設定されているかを確かめる必要がある。

## 関係
- 使う / 使われる: [[GPU]], [[CUDA]]
- 関連: [[LINPACK]], [[TOP500]], [[Roofline Model]], [[HBM]]

## 出典
- [Error-free transformations of matrix multiplication by using fast routines of matrix multiplication and its applications (Ozaki, Ogita, Oishi, Rump, Numerical Algorithms 59, 2012)](https://doi.org/10.1007/s11075-011-9478-1)
- [Ozaki Scheme I: Emulation method for Matrix Multiplication (Katsuhisa Ozaki, The 4th FugakuNEXT Application Seminar, 2025) - RIKEN R-CCS](https://www.r-ccs.riken.jp/assets/uploads/2025/12/FugakuNEXT_4th_ApplicationSeminar.pdf)
- [Ozaki Scheme II: A GEMM-oriented emulation of floating-point matrix multiplication using an integer modular technique (Ozaki, Uchino, Imamura) - arXiv](https://arxiv.org/abs/2504.08009)
- [cuBLAS - NVIDIA Documentation](https://docs.nvidia.com/cuda/cublas/index.html)（Fixed-Point Emulation）
