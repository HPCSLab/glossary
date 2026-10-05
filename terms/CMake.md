---
aliases: [cmake, CMakeLists.txt, CMakeCache.txt, Ninja, Out-of-source Build, ビルドシステム生成]
tags: [term]
maps: ["[[Programming]]"]
status: draft
updated: 2026-10-06
---
# CMake

> プロジェクトのビルド方法を一度記述しておけば、各環境に合わせたビルドファイル（Makefileなど）を生成する、クロスプラットフォームのビルドシステム生成ツールである。

## 概要
CMakeは、それ自体がコンパイルを行うのではなく、[[Make]]やNinjaなどの実際のビルドツールが用いるファイルを生成する。ビルドの方法は、プロジェクトのディレクトリに置いた `CMakeLists.txt` に記述する。ここでは、作成する実行ファイルやライブラリ、そのソースファイル、依存する外部ライブラリ、コンパイラのオプションなどを、ツールや環境に依存しない形で書く。CMakeは、この記述と、実行する計算機で見つかったコンパイラやライブラリの情報をもとに、その環境に適したビルドファイルを生成する。

CMakeでは、ソースコードを置くソースツリーと、生成物を置くビルドツリーを分けるのが原則である（out-of-sourceビルド）。基本的な手順は次のとおりである。

```sh
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release   # 構成（ビルドファイルの生成）
cmake --build build -j                            # ビルド
cmake --install build                             # インストール
```

構成の段階で決まった設定は、ビルドツリーの `CMakeCache.txt` に保存され、以後のビルドで再利用される。生成するビルドファイルの種類は、ジェネレータ（Unix Makefiles、Ninjaなど）として選べる。

## どこで出てくるか
[[MPI]]や[[HDF5]]を用いるHPCのアプリケーションやライブラリの多くは、CMakeでビルドされる。外部のライブラリは `find_package` で探索されるため、ライブラリを標準外の場所に入れた場合は、その場所をCMakeに教える必要がある。新メンバーがつまずきやすいのは、一度構成したビルドツリーに古い設定が `CMakeCache.txt` として残り、オプションやコンパイラを変えても反映されない場合である。設定を大きく変えるときは、ビルドツリーを削除して構成し直すのが確実である。性能を評価する際には、最適化の有無を決めるビルドの種類（`CMAKE_BUILD_TYPE`）を確認しておく必要がある。

## 関係
- 使う / 使われる: [[Make]]（生成するビルドファイルの一つ）, [[C]]
- 関連: [[Spack]]（CMakeを用いるパッケージを自動でビルドする）, [[MPI]], [[HDF5]]

## 出典
- [cmake(1) - CMake documentation](https://cmake.org/cmake/help/latest/manual/cmake.1.html)
