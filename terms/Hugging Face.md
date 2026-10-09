---
aliases: [huggingface, HuggingFace, Hugging Face Hub, HF Hub, Transformers, transformers, huggingface_hub, HF_HOME, HF_HUB_CACHE, Model Card, モデルカード]
tags: [term]
maps: ["[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-10
---
# Hugging Face

> 機械学習のモデル、データセット、デモのアプリケーションを共有するためのプラットフォーム（Hugging Face Hub）と、それを利用するためのライブラリ群を提供する企業およびそのサービスの総称である。

## 概要
Hugging Face Hubは、オープンな機械学習のための共有の場であり、200万を超えるモデル、150万のデータセット、150万のデモのアプリケーション（Spaces）が公開されている。これらは、[[Git|git]]に基づく版管理されたリポジトリとして置かれ、コミットの履歴、差分、ブランチを持つ。大きなファイルは、Xetと呼ばれる仕組みによって、ファイルを固有の断片（チャンク）に分けて効率よく格納・転送される。モデルのリポジトリには、そのモデルの用途、限界、偏りなどを記したモデルカードが付けられる。一部のモデルやデータセットは、利用の条件に同意した利用者にのみ公開される（gated）。

Hubのモデルを利用する代表的なライブラリがTransformersである。Transformersは、テキスト、画像、音声、動画、マルチモーダルの最新のモデルの定義を提供する枠組みであり、推論と学習の両方に用いられる。モデルの定義を一か所にまとめることで、[[vLLM]]などの推論エンジンや、各種の学習の枠組みが、同じモデルの定義を利用できるようにしている。簡単に推論を行うためのPipeline、学習のためのTrainer、[[LLM]]による文章の生成のためのgenerateなどの機能を持つ。データセットの利用には `datasets` ライブラリを用いる。

## どこで出てくるか
LLMをはじめとする公開のモデルを研究で用いる際には、Hugging Face Hubからモデルの重みと設定のファイルを取得できる。取得したファイルは、既定ではホームディレクトリの下の `~/.cache/huggingface/hub` にキャッシュされ、再び用いる際には取得し直さずに済む。キャッシュでは、ファイルの実体（blobs）を、版ごとのフォルダ（snapshots）からシンボリックリンクで参照する構造をとるため、同じファイルを複数の版で共有できる。古い版のファイルは自動では削除されないため、`hf cache ls` で使用量を確認し、`hf cache rm` や `hf cache prune` で削除する。

大きなモデルの重みは数十GB以上になることがある（例えば、あるモデルの量子化した重みの一つのファイルが16.5GBである）。計算機センターでは、ホームディレクトリの容量に上限（クォータ）が設けられていることが多いため、キャッシュの場所を環境変数 `HF_HOME` や `HF_HUB_CACHE` で作業用の大きな領域に移しておく必要がある。シンボリックリンクをうまく扱えない共有のファイルシステムでは、環境変数 `HF_HUB_DISABLE_SYMLINKS` によって、シンボリックリンクを使わない方式に切り替えられる。

## 関係
- 使う / 使われる: [[LLM]], [[vLLM]]（Transformersのモデル定義を利用する）, [[Python]], [[GPU]]
- 関連: [[KV Cache]], [[Parallel File System]], [[Node-local Storage]]

## 出典
- [Hugging Face Hub documentation](https://huggingface.co/docs/hub/index)
- [Transformers documentation](https://huggingface.co/docs/transformers/index)
- [Understand caching - huggingface_hub documentation](https://huggingface.co/docs/huggingface_hub/guides/manage-cache)
- [File System Separation (Admin Guide) - HPC Wiki](https://hpc-wiki.info/hpc/Admin_Guide_File_System_Separation)（ホームディレクトリのクォータについて）
