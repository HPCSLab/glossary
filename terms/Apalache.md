---
aliases: [APALACHE, apalache-mc, Symbolic Model Checker, 記号モデル検査器, Inductive Invariant, 帰納的不変条件, Snowcat]
tags: [term]
maps: ["[[Distributed Systems]]"]
status: draft
updated: 2026-10-11
---
# Apalache

> [[TLA+]]の仕様を[[SMT Solver|SMTソルバ]]が解ける論理式に変換し、状態を一つずつ列挙せずに記号的に検査する、TLA+のためのモデル検査器である。

## 概要
TLA+の標準のモデル検査器TLCは、到達しうる状態を一つずつ列挙して調べる明示的状態の[[Model Checking|モデル検査]]器であり、変数の取りうる値が多いと状態の数が爆発して検査が終わらなくなる。Apalacheは、仕様の遷移関係を量化子を含まないSMTの制約に変換し、Z3などのSMTソルバに「性質を破る実行が存在するか」を解かせる。状態を一つずつ列挙しないため、状態空間の大きな仕様ではTLCより速く検査できる場合がある。Igor Konnov、Jure Kukovec、Thanh-Hai TranがOOPSLA 2019で発表し、現在はLinux Foundation傘下のTLA+ Foundationに移管されている。TLCと同じく、定数などの仕様のパラメータは有限の値に固定する必要がある。

検査の方法は主に二つある。一つは有界モデル検査であり、`Next` の適用を指定した回数（既定では10回）までに限り、その長さまでの全ての実行で不変条件が成り立つかを調べる。もう一つは帰納的不変条件の検査である。帰納的不変条件とは、初期状態で成り立ち、成り立つ任意の状態から `Next` で一歩進んでも成り立ち続ける条件のことである。これを長さ0と1の検査に分けて確かめると、実行の長さに制限なく安全性が成り立つことを示せる。条件が帰納的でなければ反例が示され、利用者は条件を強めて検査を繰り返す。

SMTの制約に変換するために、Apalacheは変数の型を知る必要がある。TLA+自体は型を持たないため、`CONSTANTS` と `VARIABLES` の宣言には `\* @type: Int;` のような注釈を書き、型検査器Snowcatが残りの型を推論する。

## どこで出てくるか
状態の数が多くTLCでは扱いきれない分散プロトコルの検証で用いられる。開発の初期には、ブロックチェーンのTendermintの[[Consensus|合意]]プロトコルとライトクライアントの検査に用いられた。仕様記述言語Quintも、検査のバックエンドとしてApalacheを用いる。

## 関係
- 上位概念: [[Model Checking]]
- 前提: [[TLA+]], [[SMT Solver]]
- 対比: TLC（[[TLA+]]を参照。状態を一つずつ列挙するのに対し、Apalacheは制約として記号的に扱う）
- 関連: [[Alloy]], [[Consensus]]

## 出典
- [Apalache - apalache-mc.org](https://apalache-mc.org/)
- [apalache-mc/apalache - GitHub](https://github.com/apalache-mc/apalache)
- [Running the Tool - Apalache Manual](https://apalache-mc.org/docs/apalache/running.html)
- [How to write type annotations - Apalache Manual](https://apalache-mc.org/docs/HOWTOs/howto-write-type-annotations.html)
- [TLA+ Model Checking Made Symbolic (Konnov, Kukovec, Tran, OOPSLA 2019)](https://doi.org/10.1145/3360549)
