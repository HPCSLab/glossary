---
aliases: [ansible, ansible-playbook, Playbook, プレイブック, Ansible Inventory, Ansible Role, 構成管理]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-10
---
# Ansible

> 計算機のあるべき状態をYAMLで記述し、SSHで接続した多数の計算機に対して、その設定やソフトウェアの導入を自動で行う、オープンソースの構成管理ツールである。

## 概要
Ansibleは、Michael DeHaanが開発し、2012年2月に最初の版が公開された。2015年10月にRed Hatが買収している。主にPythonで書かれており、GPLv3のもとで公開されている。

Ansibleを実行する計算機を制御ノード、設定の対象となる計算機を管理対象ノード（ホスト）と呼ぶ。管理対象ノードの一覧はインベントリに記述し、ノードをグループに分けて、グループごとに変数を与えることができる。行う作業は、YAMLで書かれたプレイブックに記述する。プレイブックは、どのノードにどのタスクを適用するかを定めたプレイからなり、一つのタスクは、パッケージの導入やファイルの配置といった一つの操作を表す。タスクの実体はモジュールと呼ばれるプログラムであり、制御ノードから管理対象ノードに送られて実行される。再利用できるタスクや変数、テンプレートの組はロールとしてまとめる。

Ansibleはエージェントを持たない。管理対象ノードに専用のソフトウェアを導入する必要はなく、Unix系のノードにはSSHで、Windowsのノードには Windows Remote Management で接続する。Unix系のノードでは、モジュールの実行のためにPythonが必要である。また、Ansibleは冪等性を重視しており、ノードがすでにプレイブックに記述された状態にあれば、何度実行しても何も変更しない。

## どこで出てくるか
複数の計算機に同じ環境を用意する場面で用いられる。例えば、複数の[[Compute Node|計算ノード]]に同じパッケージや設定ファイルを導入する作業を、手作業で一台ずつ行う代わりにプレイブックとして記述しておけば、同じ手順を何度でも正確に再現できる。プレイブックはテキストであるため、[[Git|git]]で版を管理でき、環境を構築した手順の記録にもなる。[[Ubuntu]]と[[Rocky Linux]]のように、ディストリビューションによってパッケージの名前やパッケージを導入するモジュールが異なる点には注意を要する。

## 関係
- 使う / 使われる: [[Python]], [[Ubuntu]], [[Rocky Linux]]
- 関連: [[Incus]], [[Compute Node]], [[Spack]]

## 出典
- [Introduction to Ansible - Ansible Documentation](https://docs.ansible.com/ansible/latest/getting_started/introduction.html)
- [Ansible concepts - Ansible Documentation](https://docs.ansible.com/ansible/latest/getting_started/basic_concepts.html)
- [Ansible (software) - Wikipedia](https://en.wikipedia.org/wiki/Ansible_(software))
