---
aliases: [excalidraw, エクスカリドロー]
tags: [term]
maps: ["[[Research]]"]
status: draft
updated: 2026-10-10
---
# Excalidraw

> 手描き風の線で図を描く、Webブラウザで動作するオープンソースのホワイトボードである。

## 概要
Excalidrawは、MITライセンスで公開されているオープンソースの作図ツールであり、Webブラウザで excalidraw.com を開けばすぐに利用できる。描いた図は、箱や矢印、文字などがあえて手で描いたような揺らぎのある線で表示される。図は自動的にブラウザに保存され、オフラインでも動作する。

保存形式の `.excalidraw` はJSONのテキストであり、図をPNGやSVGの画像として書き出すこともできる。excalidraw.com には、複数人が同じキャンバスに同時に描き込めるリアルタイム共同編集の機能があり、その通信はエンドツーエンドで暗号化される。また、エディタはReactの部品（npmパッケージ）として提供されており、[[Obsidian]]のプラグインなど、他のアプリケーションに組み込まれて使われている。Obsidianのプラグインでは、図はMarkdownのファイルとして保管され、ノートと相互にリンクできる。

## どこで出てくるか
オンラインの打ち合わせで、システムの構成やデータの流れを全員で同じ画面に描き込みながら議論するホワイトボードとして用いる。また、Obsidianでノートを取る場合に、ノートの中に図を描く手段として用いる。同じく構成図を描く[[drawio|draw.io]]が整った直線で図を描くのに対し、Excalidrawの図は手描き風の見た目になる点が異なる。

## 関係
- 対比: [[drawio|draw.io]]（整った線で図を描く）, [[TikZ]]（図をコードで記述する）
- 関連: [[Obsidian]]

## 出典
- [excalidraw/excalidraw - GitHub](https://github.com/excalidraw/excalidraw)
- [zsviczian/obsidian-excalidraw-plugin - GitHub](https://github.com/zsviczian/obsidian-excalidraw-plugin)
