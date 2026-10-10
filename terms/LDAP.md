---
aliases: [Lightweight Directory Access Protocol, OpenLDAP, slapd, ディレクトリサービス, Directory Service, DN, Distinguished Name, posixAccount, posixGroup, StartTLS, LDAPS, SSSD, NIS]
tags: [term]
maps: ["[[System Administration]]"]
status: draft
updated: 2026-10-10
---
# LDAP（Lightweight Directory Access Protocol）

> ユーザやグループなどの情報を木構造で保持するディレクトリサービスに、ネットワーク越しに問い合わせ・更新するためのプロトコルである。

## 概要
複数の計算機で同じユーザが作業するには、どのノードでも同じユーザ名とUID・GIDの番号が見えている必要がある。[[NFS]]で用いられるRPCの認証方式AUTH_SYSでは、クライアントは要求に数値のUIDとGIDを付けて送り、その番号は同じ番号の体系を共有する範囲でしか意味を持たない。そのため、各ノードの `/etc/passwd` に別々にユーザを登録して番号が食い違うと、共有したホームディレクトリのファイルが別のユーザの所有に見えたり、権限のエラーが起きたりする。これを避けるため、ユーザとグループの情報を一か所のサーバに置き、全ノードがそこを参照する。LDAPはそのようなサーバとの通信に用いられるプロトコルであり、RFC 4511で定められている。

ディレクトリは、検索と閲覧に特化したデータベースである。データはエントリの木として格納され、各エントリは祖先の名前をつないだDN（Distinguished Name）で識別される（例：`uid=babs,ou=People,dc=example,dc=com`）。エントリは属性の集まりであり、特別な属性 `objectClass` が、必須の属性と許される属性を定める。UNIXのアカウントの表現はRFC 2307が定めており、`posixAccount` は `uid`、`uidNumber`、`gidNumber`、`homeDirectory` を必須とし、`loginShell` などを任意とする。`posixGroup` は `gidNumber` を必須とし、所属するユーザを `memberUid` に列挙する。

通信はTCPで行い、389番が割り当てられたポートである。クライアントはBindで認証し、Search、Add、Modify、Deleteなどの操作を要求する。通信を暗号化するには、平文の接続を確立した後にTLSを開始するStartTLS操作か、最初からTLSで接続する `ldaps://` の方式を用いる。

## どこで出てくるか
サーバの実装として、オープンソースのOpenLDAPがあり、そのサーバのプログラムは `slapd` である。OpenLDAPが推奨するデータベースのバックエンドは、[[LMDB]]を用いるMDBである。Windowsの環境で用いられるActive Directoryも、LDAPによるアクセスに対応している。

クライアント側では、[[Compute Node|計算ノード]]などの各ノードで、名前の解決をNSS（Name Service Switch）に、ログイン時の認証をPAMに任せ、その先でSSSDなどがLDAPのサーバに問い合わせる。SSSDは、サーバから得た情報をキャッシュし、サーバと通信できないときでも、以前にログインしたユーザのログインを許すことができる。ユーザがLDAPから見えているかは、`getent passwd <ユーザ名>` や `getent group <グループ名>` で確かめられる。これらはNSSの設定（`/etc/nsswitch.conf`）に従って検索するため、ローカルのファイルにないユーザも表示される。

LDAPより古い方式として、Sun Microsystemsが開発したNIS（旧称Yellow Pages）があり、コマンド名の `yp` はその名残である。NISは、拡張性と安全性に限界があるとされ、置き換えが進んでいる。

## 関係
- 対比: NIS（より古い集中管理の方式）, `/etc/passwd`（ノードごとのローカルな管理）
- 使う / 使われる: [[LMDB]]（OpenLDAPのバックエンド）
- 関連: [[NFS]], [[Compute Node]]

## 出典
- [RFC 4511: Lightweight Directory Access Protocol (LDAP): The Protocol](https://www.rfc-editor.org/rfc/rfc4511.html)
- [RFC 2307: An Approach for Using LDAP as a Network Information Service](https://www.rfc-editor.org/rfc/rfc2307.html)
- [RFC 1813: NFS Version 3 Protocol Specification](https://www.rfc-editor.org/rfc/rfc1813.html)
- [RFC 5531: RPC: Remote Procedure Call Protocol Specification Version 2](https://www.rfc-editor.org/rfc/rfc5531.html)
- [OpenLDAP Software 2.6 Administrator's Guide: Introduction to OpenLDAP Directory Services](https://www.openldap.org/doc/admin26/intro.html)
- [OpenLDAP Software 2.6 Administrator's Guide: Using TLS](https://www.openldap.org/doc/admin26/tls.html)
- [SSSD: Introduction](https://sssd.io/docs/introduction.html)
- [sssd(8) - Arch manual pages](https://man.archlinux.org/man/sssd.8)
- [getent(1) - Arch manual pages](https://man.archlinux.org/man/getent.1)
- [Active Directory Domain Services - Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/ad/active-directory-domain-services)
- [Network Information Service - Wikipedia](https://en.wikipedia.org/wiki/Network_Information_Service)
