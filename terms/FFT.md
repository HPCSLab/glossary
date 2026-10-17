---
aliases: [高速フーリエ変換, Fast Fourier Transform, Cooley-Tukey, Cooley–Tukey, 3次元FFT, 3D FFT, 並列FFT]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-18
---
# FFT（高速フーリエ変換）

> N点の離散フーリエ変換（DFT）を、定義どおりに計算するとO(N²)となる演算を、O(N log N)で計算する算法の総称である。

## 概要
DFTは、N個の入力から、それぞれが全ての入力に回転因子（複素数の重み）を掛けて足し合わせたN個の出力を作る変換であり、定義どおりに計算すると演算量はN²に比例する。CooleyとTukeyは1965年に、Nが2のべき乗のとき、入力を添字の偶数番目と奇数番目に分けると、N点のDFTが二つのN/2点のDFTと、それらを組み合わせるN/2回の演算に分解できることを示した。この組み合わせの演算は、二つの値a, bから a + W·b と a − W·b を作るもので、図の形からバタフライと呼ぶ。分解を再帰的に繰り返すと、log₂N段のそれぞれでN/2個のバタフライを計算することになり、演算量はO(N log N)となる。

![[FFT Butterfly.excalidraw]]

段ごとに組になる要素の距離が変わるため、メモリへのアクセスは段によって飛び飛びになる。また、要素あたりの演算はlog N回程度にとどまり、データの再利用が少ない。このため、FFTは演算強度が低く、[[Roofline Model|ルーフラインモデル]]で言えばメモリの[[Bandwidth|バンド幅]]に[[Bottleneck|律速]]されやすい。多次元のFFTは、各軸に沿った1次元のFFTを軸ごとに順に行うことで計算する。

3次元のFFTを多数のプロセスで分担するとき、ある軸に沿った1次元のFFTを行うには、その軸の全ての要素が一つのプロセスに揃っていなければならない。このため、軸ごとのFFTの合間に、データの持ち方を入れ替える転置が必要となり、これを[[MPI]]の全対全通信（Alltoall）で行う。一つの軸だけで分割するslab分割では転置は一回で済むが、プロセス数は一辺の要素数Nを超えられない。二つの軸で分割するpencil分割では転置が二回となる一方、N²個までのプロセスを使える。転置では全てのプロセスが他の多くのプロセスとデータを交換するため、規模が大きくなるほど[[Collective Communication|集団通信]]の時間が全体の性能を左右し、ネットワークの[[Bisection Bandwidth|二分割帯域幅]]の影響を強く受ける。

## どこで出てくるか
乱流のシミュレーションのスペクトル法、[[N-Body Simulation|分子動力学計算]]の静電相互作用を格子上で求めるParticle Mesh Ewald（PME）法、画像や信号の処理、畳み込みの計算などで用いられる。CPU向けのライブラリにはFFTWがあり、MPIによる分散メモリの並列FFTも備える。FFTWのMPIのインタフェースは、データを先頭の軸に沿って分割するslab分割を用いる。[[GPU]]向けにはNVIDIAのcuFFTがあり、FFTWに倣ったAPIを持つ。3次元FFTのpencil分割を実装したライブラリとしてP3DFFTなどがある。スーパーコンピュータの性能評価では、HPC Challengeのベンチマークの競技部門の4項目の一つにGlobal FFTがあり、[[LINPACK]]（HPL）などと並べて評価される。

## 関係
- 使う / 使われる: [[Collective Communication]], [[MPI]], [[N-Body Simulation]]
- 関連: [[Roofline Model]], [[Bisection Bandwidth]], [[LINPACK]]

## 出典
- [An Algorithm for the Machine Calculation of Complex Fourier Series (Cooley and Tukey, Mathematics of Computation, 1965)](https://doi.org/10.1090/S0025-5718-1965-0178586-1)
- [FFTW: MPI Data Distribution (FFTW 3 Manual)](https://www.fftw.org/fftw3_doc/MPI-Data-Distribution.html)
- [cuFFT (NVIDIA Documentation)](https://docs.nvidia.com/cuda/cufft/)
- [P3DFFT: A Framework for Parallel Computations of Fourier Transforms in Three Dimensions (Pekurovsky, SIAM Journal on Scientific Computing, 2012)](https://arxiv.org/abs/1905.02803)
- [HPC Challenge](https://www.hpcchallenge.org/)
