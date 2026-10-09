---
aliases: [draw.io, diagrams.net, ドローアイオー]
tags: [term]
maps: ["[[Research]]"]
status: draft
updated: 2026-10-10
---
# draw.io

> システム構成図や流れ図などの図を、マウス操作で描くための無料の作図ツールである。

## 概要
draw.ioは、draw.io Ltd（旧称JGraph）とdraw.io AGが開発する作図ツールであり、ソースコードはApache 2.0ライセンスで公開されている。アカウントの登録なしに、Webブラウザ（app.diagrams.net）またはデスクトップアプリで利用でき、図のファイルは利用者が選んだ場所（手元のディスク、Google Drive、[[GitHub]]のリポジトリなど）に保存される。VS Codeの拡張もあり、エディタの中で図を編集できる。

図は、箱や矢印などの図形をキャンバスに配置し、図形同士を接続線でつないで描く。保存形式の `.drawio` はXMLのテキストであり、[[Git]]で版を管理できる。PNG、SVG、PDFに書き出す際に「Include a copy of my diagram」を選ぶと、画像の中に図のデータが埋め込まれ、書き出した画像を後からdraw.ioで開いて編集し直せる。

## どこで出てくるか
論文や発表のスライドに載せる、提案手法の構成図、ソフトウェアの層の図、処理の流れ図を描くときに用いる。[[LaTeX]]の論文に載せる場合は、PDFやSVGなどのベクタ形式で書き出して取り込むと、拡大しても線や文字がぼやけない。PNGはラスタ形式であり、拡大するとぼやける。

同じく図を作る[[TikZ]]は図をコードで記述するのに対し、draw.ioは画面上で直接配置するため、試行錯誤しながら配置を決める構成図に向く。一方、実験結果のグラフはデータから作るものであり、draw.ioではなく[[Matplotlib]]などで描く。

## 関係
- 対比: [[TikZ]]（図をコードで記述する）, [[Matplotlib]]（データからグラフを描く）
- 使う / 使われる: [[LaTeX]], [[Beamer]]
- 関連: [[Git]]

## 出典
- [draw.io](https://www.drawio.com/)
- [jgraph/drawio - GitHub](https://github.com/jgraph/drawio)
- [Export diagrams - draw.io FAQ](https://www.drawio.com/doc/faq/export-diagram)
