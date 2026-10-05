---
aliases: [rdtsc, RDTSCP, rdtscp, TSC, Time Stamp Counter, タイムスタンプカウンタ, Invariant TSC, __rdtsc, vDSO, clock_gettime, CLOCK_MONOTONIC]
tags: [term]
maps: ["[[Operating System]]", "[[Parallel Computing]]"]
status: draft
updated: 2026-10-06
---
# RDTSC

> x86のプロセッサが持つ64ビットのカウンタ（タイムスタンプカウンタ、TSC）の値を読み出す命令であり、短い処理の時間を少ない負担で測るために用いられる。

## 概要
TSCは、Pentiumで導入された、プロセッサのリセット時に0になり、その後単調に増え続けるカウンタである。RDTSC命令は、その値の上位32ビットをEDXに、下位32ビットをEAXに読み込む。[[C]]/C++からは、コンパイラの組込み関数 `__rdtsc()`（GCCでは `<x86intrin.h>`、MSVCでは `<intrin.h>`）で呼び出せる。[[System Call|システムコール]]を経ずにユーザ空間で直接実行でき、一回の読み出しの負担が小さい（ただし、OSが制御レジスタCR4のTSDフラグを立てると、ユーザ空間からは実行できなくなる）。

TSCの値をそのまま時間として扱うには、いくつか注意を要する。第一に、近年のIntelとAMDのプロセッサのTSCは、ターボブーストや省電力による実際の動作周波数の変化に関わらず、一定の公称周波数で増える（invariant TSC）。このため、TSCの増分はCPUの実際のクロックサイクル数とは一致せず、時間に換算するにはTSCの周波数で割る必要がある。第二に、RDTSCは直列化命令ではない。アウトオブオーダ実行によって、前の命令が終わる前や後の命令が始まった後にカウンタが読まれることがある。測定の範囲を正しく区切るには、RDTSCの直前と直後にLFENCE命令を置く。RDTSCPは、前の全ての命令の実行が終わるのを待ってからカウンタを読み、あわせてプロセッサを識別する値をECXに返すが、後の命令が先に始まることは防がないため、直後にLFENCEを置く。第三に、古いプロセッサや一部の環境では、コアの間でTSCの値がずれることがある。

## どこで出てくるか
[[Latency|レイテンシ]]がナノ秒からマイクロ秒の単位の処理（例えば、[[Mutex|ロック]]の取得、メモリへのアクセス、[[NVMe]]や[[RDMA]]の一回の操作）を測るマイクロベンチマークで用いられる。測定したい処理が短いほど、時刻を読む操作自体の負担と誤差が無視できなくなるためである。

一般的な時間の計測には、OSが提供する `clock_gettime()`（`CLOCK_MONOTONIC` など）を用いる方が安全である。Linuxでは、`clock_gettime()` はvDSOと呼ばれる仕組みによって、カーネルに入らずユーザ空間で実行されるため、負担も小さい。RDTSCを直接用いる場合は、上記の注意点を踏まえ、プロセッサがinvariant TSCに対応しているかを確認し、TSCの周波数による換算の方法を論文などに明記する必要がある。

## 関係
- 関連: [[Latency]], [[perf]], [[System Call]], [[Linux Kernel]]

## 出典
- [RDTSC — Read Time-Stamp Counter (x86 Instruction Set Reference)](https://www.felixcloutier.com/x86/rdtsc)
- [RDTSCP — Read Time-Stamp Counter and Processor ID (x86 Instruction Set Reference)](https://www.felixcloutier.com/x86/rdtscp)
- [Time Stamp Counter - Wikipedia](https://en.wikipedia.org/wiki/Time_Stamp_Counter)
- [vdso(7) - Linux manual page](https://man7.org/linux/man-pages/man7/vdso.7.html)
- [__rdtsc - Microsoft Learn](https://learn.microsoft.com/en-us/cpp/intrinsics/rdtsc)
- [ia32intrin.h - GCC source (gcc-mirror)](https://github.com/gcc-mirror/gcc/blob/master/gcc/config/i386/ia32intrin.h)
