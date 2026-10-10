---
aliases: [Dynamic Host Configuration Protocol, BOOTP, DHCPリレー, DHCP Relay Agent, DHCPリース, DHCP Lease, DORA]
tags: [term]
maps: ["[[System Administration]]"]
status: draft
updated: 2026-10-10
---
# DHCP（Dynamic Host Configuration Protocol）

> ネットワークに接続した計算機に、IPアドレスなどのネットワークの設定をサーバから自動で配布するプロトコルである。

## 概要
DHCPは、RFC 2131で定められている。それ以前のBOOTPのメッセージの形式を引き継ぎ、アドレスを期限付きで貸し出して再利用する仕組みと、多くの設定項目（オプション）を加えた。サーバは、IPアドレスに加えて、サブネットマスク、デフォルトゲートウェイ、DNSサーバのアドレスなどを配布する。

アドレスの割り当て方には三種類がある。期限付きで貸し出して返却後に再利用する動的な割り当て、恒久的なアドレスを与える自動的な割り当て、管理者が決めたアドレスをDHCPで届けるだけの手動の割り当てである。貸し出しの期間をリースと呼び、クライアントは期限の前に延長を求める。実際のサーバでは、クライアントのMACアドレスごとに決まったアドレスを与える設定（予約、固定割り当て）が用いられる。

まだアドレスを持たないクライアントは、ブロードキャストで要求を送る。手順は、クライアントがサーバを探すDHCPDISCOVER、サーバがアドレスを提示するDHCPOFFER、クライアントが一つを選ぶDHCPREQUEST、サーバが確定するDHCPACKの四段階であり、頭文字からDORAと呼ばれる。通信は[[UDP]]で行い、サーバは67番、クライアントは68番のポートを用いる。ブロードキャストはルータを越えないため、別のサブネットのサーバに要求を中継するリレーエージェントを置くことで、サブネットごとにサーバを置かずに済む。

## どこで出てくるか
家庭や大学のネットワークに計算機をつなぐと自動でアドレスが設定されるのは、DHCPによる。研究室のサーバやクラスタの管理では、[[Compute Node|計算ノード]]のMACアドレスごとに固定のアドレスとホスト名を割り当てたり、[[PXE]]による起動のために起動用のサーバとファイル名を通知したりする。クライアントはDHCPサーバが正規のものかを確かめられないため、同じネットワークに意図しないDHCPサーバがあると、計算機が誤った設定を受け取る。

## 関係
- 使う / 使われる: [[UDP]], [[PXE]]（起動時の設定の取得に用いる）
- 関連: [[NIC]]

## 出典
- [RFC 2131 - Dynamic Host Configuration Protocol](https://datatracker.ietf.org/doc/html/rfc2131)
- [Dynamic Host Configuration Protocol - Wikipedia](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol)
- [Preboot Execution Environment - Wikipedia](https://en.wikipedia.org/wiki/Preboot_Execution_Environment)
