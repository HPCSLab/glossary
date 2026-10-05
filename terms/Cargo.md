---
aliases: [cargo, Cargo.toml, Cargo.lock, crates.io, Crate, クレート]
tags: [term]
maps: ["[[Programming]]"]
status: draft
updated: 2026-10-06
---
# Cargo

> [[Rust]]の標準のビルドツール兼パッケージマネージャであり、依存するライブラリの取得、コンパイル、テスト、パッケージの公開を一つのコマンドで扱う。

## 概要
Cargoは、Rustの処理系とともに配布される公式のツールである。Rustのプロジェクトは、`Cargo.toml` というマニフェストファイルに、パッケージの名前と版、依存するライブラリとその版の範囲などを記述する。Rustのライブラリやプログラムの単位はクレート（crate）と呼ばれ、公開されたクレートは公式のレジストリであるcrates.ioから取得できる。

Cargoは、`Cargo.toml` に従って依存するクレートを自動的に取得してビルドし、実際に用いた依存関係の正確な版を `Cargo.lock` に記録する。`Cargo.lock` を保存しておけば、別の計算機でも全く同じ版の組み合わせでビルドを再現できる。主なコマンドとして、プロジェクトを作る `cargo new`、ビルドする `cargo build`、ビルドして実行する `cargo run`、テストを実行する `cargo test`、ベンチマークを実行する `cargo bench`、クレートを公開する `cargo publish` がある。`cargo build` の既定はデバッグ用のビルドであり、最適化したビルドには `--release` を付ける。

## どこで出てくるか
[[C]]言語のプロジェクトでは、ビルドに[[Make]]や[[CMake]]、依存ライブラリの導入にOSのパッケージや[[Spack]]など、複数のツールを組み合わせる必要がある。これに対し、Rustでは、ほぼすべてをCargoだけで扱える点が大きな利点である。性能を評価する際に `--release` を付け忘れると、最適化されていないプログラムを計測してしまい、桁違いに遅い結果となるため注意を要する。また、論文の実装を公開する際には、`Cargo.lock` を含めておくことで、他者が同じ構成で再現できるようにする。

## 関係
- 上位概念: [[Rust]]
- 対比: [[Make]], [[CMake]], [[Spack]]
- 関連: [[C]]

## 出典
- [The Cargo Book](https://doc.rust-lang.org/cargo/)
