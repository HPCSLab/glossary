---
aliases: [N体シミュレーション, N体計算, N体問題, N-body, N-body Simulation, 多体計算, 粒子シミュレーション, ツリー法, Barnes-Hut, Barnes–Hut]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-18
---
# N-Body Simulation（N体シミュレーション）

> 互いに力を及ぼし合う多数の粒子（天体や原子など）の運動を、時刻ごとに各粒子にかかる力を求めて運動方程式を時間積分することで追う計算である。

## 概要
重力やクーロン力は距離の2乗に反比例して遠くまで及ぶため、各粒子は他の全ての粒子から力を受ける。全ての粒子の組について力を足し合わせる直接計算では、1ステップの演算量がN²に比例し、粒子数が大きい計算は現実的な時間で終わらない。直接計算は、読み込んだ粒子のデータを多数の相手との計算に再利用できるため[[Roofline Model|演算強度]]が高く、[[GPU]]や専用の計算機に向く。日本では重力のN体計算の専用計算機GRAPEが開発され、GRAPE-6はゴードン・ベル賞の性能部門を受賞した。

演算量を減らす代表的な方法が、遠くの粒子の集まりをまとめて近似するツリー法である。BarnesとHutは1986年に、粒子が2個以上入る立方体のセルを8個の子セルに再帰的に分割した木（2次元では四分木）を毎ステップ作り、十分遠いセルの粒子を、その重心に置いた一つの質点として扱う方法を示した。セルの大きさsと、力を求める粒子からの距離dの比が、あらかじめ決めた値θより小さければセルをまとめて扱い、そうでなければ子セルに降りる。これにより演算量はO(N log N)となり、θを小さくするほど精度が上がる代わりに計算が増える。GreengardとRokhlinの高速多重極展開法（FMM）は、セル同士の相互作用を多重極展開で表し、O(N)の演算量を達成した。

![[Barnes-Hut Quadtree.excalidraw]]

分子動力学計算では、ファンデルワールス力のような近距離の力は、一定の距離（カットオフ）より遠い粒子との相互作用を無視する。空間を格子状の小さな区画に分けて近くの区画だけを調べることで、相互作用する粒子の組（近接リスト）を粒子数に比例する手間で作れる。周期境界条件の下の静電相互作用は遠くまで及ぶため、Particle Mesh Ewald（PME）法で、近距離の部分を粒子の組ごとに、残りの部分を格子に割り当てた電荷から3次元の[[FFT]]で計算し、全体の演算量をO(N log N)に抑える。

多数の[[Compute Node|ノード]]で並列に計算するときは、空間を領域に分けて各プロセスに割り当てる[[Domain Decomposition|領域分割]]を用いる。各プロセスは、カットオフの範囲に入る隣の領域の粒子の写しを受け取って力を計算するため、近距離の力の計算に必要な通信は隣接する領域との間に限られる。一方、PMEの3次元FFTは全対全の転置を含むため、[[Collective Communication|集団通信]]の性能に左右される。

## どこで出てくるか
天文学の銀河、星団、宇宙の大規模構造の計算や、材料と生体分子の分子動力学計算（GROMACS、LAMMPSなど）で用いられる。[[AI for Science]]で、機械学習で求めた原子間の力を用いる分子動力学計算も、力を求めた後の時間積分と並列化の構造は同じである。LAMMPSは[[Kokkos]]によって多様なGPUに対応している。GPUや専用計算機の性能を示す題材として、[[SC]]のゴードン・ベル賞の受賞研究にもたびたび現れる。

## 関係
- 使う / 使われる: [[FFT]], [[Domain Decomposition]], [[GPU]]
- 関連: [[AI for Science]], [[Kokkos]], [[Collective Communication]]

## 出典
- [A Hierarchical O(N log N) Force-Calculation Algorithm (Barnes and Hut, Nature, 1986)](https://doi.org/10.1038/324446a0)
- [A Fast Algorithm for Particle Simulations (Greengard and Rokhlin, Journal of Computational Physics, 1987)](https://doi.org/10.1016/0021-9991(87)90140-9)
- [Particle Mesh Ewald: An N⋅log(N) Method for Ewald Sums in Large Systems (Darden, York, and Pedersen, The Journal of Chemical Physics, 1993)](https://doi.org/10.1063/1.464397)
- [Long Range Electrostatics (GROMACS Reference Manual)](https://manual.gromacs.org/current/reference-manual/functions/long-range-electrostatics.html)
- [Neighbor Lists (LAMMPS Developer Guide)](https://docs.lammps.org/Developer_par_neigh.html)
- [Space Researcher Using Prototype of World's Fastest Computer (MIT News, 2001)](https://news.mit.edu/2001/space-researcher-using-prototype-worlds-fastest-computer)
