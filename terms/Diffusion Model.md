---
aliases: [拡散モデル, Diffusion Models, DDPM, Denoising Diffusion Probabilistic Models, DDIM, Latent Diffusion Model, 潜在拡散モデル, LDM, DiT, Diffusion Transformer]
tags: [term]
maps: ["[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-10
---
# Diffusion Model（拡散モデル）

> データに少しずつノイズを加えて壊していく過程を考え、その逆にノイズを少しずつ取り除く過程をニューラルネットワークに学習させることで、ノイズから新しいデータを生成するモデルである。画像の生成で広く用いられる。

## 概要
拡散モデルの考え方は、非平衡統計物理に着想を得て2015年にSohl-Dicksteinらが示した。データの分布の構造を、ノイズを加える前向きの拡散過程で段階的に壊し、その逆向きの過程を学習することで、構造を復元する生成モデルを得る。2020年にHoらが発表したDDPM（Denoising Diffusion Probabilistic Models）が、高品質な画像の生成を示した。学習では、ノイズを加えたデータから加えたノイズを予測するようにネットワークを訓練する。生成では、純粋なノイズから出発し、学習したネットワークでノイズを除く処理を多数の段階にわたって繰り返す。

この生成の手順は本質的に逐次的であり、ネットワークを何度も順に評価する必要があるため遅い。これを改善する研究が多い。DDIMは、DDPMと同じ学習の方法のまま、少ない段階で生成できるようにし、生成を10〜50倍速くした。潜在拡散モデル（Latent Diffusion Model）は、画素の空間で直接拡散を行う代わりに、事前に学習した自己符号化器（オートエンコーダ）で圧縮した潜在空間で拡散を行い、学習と生成の計算量を減らした。この論文は、クロスアテンションの層を加えることで、文章などを条件として生成を制御する方法も示した。ネットワークの構造は、当初はU-Netが標準であったが、DiTはこれを潜在空間のパッチに対して動く[[Transformer]]に置き換え、計算量を増やすほど生成の品質が上がることを示した。

## どこで出てくるか
文章などを条件として画像を生成する用途で出てくる。[[LLM]]が1トークンずつ順に生成するのに対し、拡散モデルは画像全体を段階的にノイズから仕上げていく点が異なるが、いずれも生成の際にモデルを何度も繰り返し実行する必要があり、推論の高速化がシステムの課題となる。[[AI for Science]]では、気象の予測への応用が進んでいる。例えば、GenCastは拡散モデルによって15日先までの全球の気象のアンサンブル予報を生成し、CorrDiffは粗い解像度の全球のデータから、km単位の細かな解像度の局所的な気象場を推定する（ダウンスケーリング）。

## 関係
- 上位概念: [[Generative Model]]
- 対比: [[LLM]]（トークンを一つずつ順に生成する自己回帰型のモデルである）
- 使う / 使われる: [[Transformer]], [[GPU]], [[PyTorch]]
- 関連: [[AI for Science]]

## 出典
- [Deep Unsupervised Learning using Nonequilibrium Thermodynamics (arXiv:1503.03585)](https://arxiv.org/abs/1503.03585)
- [Denoising Diffusion Probabilistic Models (arXiv:2006.11239)](https://arxiv.org/abs/2006.11239)
- [Denoising Diffusion Implicit Models (arXiv:2010.02502)](https://arxiv.org/abs/2010.02502)
- [High-Resolution Image Synthesis with Latent Diffusion Models (arXiv:2112.10752)](https://arxiv.org/abs/2112.10752)
- [Scalable Diffusion Models with Transformers (arXiv:2212.09748)](https://arxiv.org/abs/2212.09748)
- [GenCast: Diffusion-based ensemble forecasting for medium-range weather (arXiv:2312.15796)](https://arxiv.org/abs/2312.15796)
- [Residual Corrective Diffusion Modeling for Km-scale Atmospheric Downscaling (arXiv:2309.15214)](https://arxiv.org/abs/2309.15214)
