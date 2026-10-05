---
aliases: [openacc, OpenACC Directives, "#pragma acc", "#pragma acc parallel", "#pragma acc kernels", "#pragma acc data", "nvc -acc", "-fopenacc"]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-06
---
# OpenACC

> C、C++、Fortranのプログラムに指示文（ディレクティブ）を書き加えることで、ループなどの処理を、ホストのCPUから[[GPU]]などのアクセラレータに移して実行させるための、プログラミングの規格である。

## 概要
OpenACCは、Cray、CAPS、NVIDIA、PGIが開発し、2011年11月に発表された。現在は、学術機関と企業の会員からなる非営利の団体が規格を策定しており、最新の版は3.4である。

OpenACCは、[[OpenMP]]と同じく、元のプログラムに指示文を加えることで並列化する。C/C++では `#pragma acc` で始まる指示文を用いる。`parallel` や `kernels` は、アクセラレータで実行する領域を示し、`loop` は、その中のループをどう並列化するかを示す。`data` は、ホストのメモリとアクセラレータのメモリの間で、どのデータをいつ転送するかを示す。[[CUDA]]のように、GPUで動く関数（カーネル）とメモリの管理を明示的に書く方法と比べ、元のプログラムの構造を保ったまま移植できる。

対応するコンパイラには、NVIDIAのHPC SDKのコンパイラ（`nvc -acc` など。既定ではNVIDIAのGPUに処理を移し、`-acc=multicore` を指定するとCPUの多数のコアで並列に実行する）や、GCC（`-fopenacc`。NVIDIAのGPUとAMDのGPUに対応）がある。

## どこで出てくるか
既存のC、C++、Fortranの科学技術計算のプログラムを、GPUで動かすために用いられ、OpenACCの団体によれば400を超えるアプリケーションが用いている。OpenACCの会員は、OpenMPの団体と協力して、アクセラレータへの対応をOpenMPの規格にも取り入れており、OpenMP 4.0以降では、同様の目的に `target` の指示文を用いることもできる。

## 関係
- 対比: [[OpenMP]]（target指示文によるオフロード）, [[CUDA]]（明示的にGPUのカーネルを書く）
- 使う / 使われる: [[GPU]]
- 関連: [[MPI]]

## 出典
- [About OpenACC - OpenACC](https://www.openacc.org/about)
- [OpenACC Specification - OpenACC](https://www.openacc.org/specification)
- [OpenACC - Wikipedia](https://en.wikipedia.org/wiki/OpenACC)
- [NVIDIA HPC Compilers User's Guide - NVIDIA Documentation](https://docs.nvidia.com/hpc-sdk/compilers/hpc-compilers-user-guide/index.html)
- [OpenACC - GCC Wiki](https://gcc.gnu.org/wiki/OpenACC)
