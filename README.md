# 為替レート配信パッケージ
[![test](https://github.com/inochida/robosys2025/actions/workflows/sinsu_test.yml/badge.svg)](https://github.com/inochida/robosys2025/actions/workflows/sinsu_test.yml)

## パッケージ概要
このROS2パッケージは為替レート（USD / EUR / GBP）をリアルタイムで取得し、日本円に換算して配信します。

## ノードの説明
### exchange_rate_talker.py
- 役割：[ExchangeRate-API](https://app.exchangerate-api.com/dashboard) から最新の為替データを取得し、各通貨の日本円（JPY）換算レートをパブリッシュします。
- ノード名：`currency_talker`
- パブリッシュするトピック：`/dollar_rate`、`/euro_rate`、`/pound_rate`
- 更新時間：15秒
### exchange_rate_listener.py
- 役割：各通貨トピックを受信し、表示します。
- ノード名：`currency_listener`
- サブスクライブするトピック：`/dollar_rate`、`/euro_rate`、`/pound_rate`
- 表示：「USD: 123.45 JPY」のようにUSD、EUR、GBPを日本円に換算して表示します。

##トピックの説明
### /dollar_rate
- 型：`std_msgs/Float64`
- 内容：1米ドル（USD）あたりの日本円（JPY）価格。
### /euro_rate
- 型：`std_msgs/Float64`
- 内容：1ユーロ（EUR）あたりの日本円（JPY）価格。
### /pound_rate
- 型：`std_msgs/Float64`
- 内容: 1英ポンド（GBP）あたりの日本円（JPY）価格。

## 実行方法
### まとめてUSD、EUR、GBPを日本円に換算する場合。
```
$ ros2 launch  mypkg rate.launch.py
[INFO] [launch]: All log files can be found below /home/inochi/.ros/log/2025-12-27-22-19-51-033350-LAPTOP-4K8M6V7V-155106
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [155108]
[INFO] [listener-2]: process started with pid [155110]
[talker-1] [INFO] [1766841592.241212872] [talker_node]: Sent USD rate
[listener-2] [INFO] [1766841592.241212864] [listener_node]: USD: 156.47 JPY
[talker-1] [INFO] [1766841592.685930060] [talker_node]: Sent EUR rate
[listener-2] [INFO] [1766841592.686215411] [listener_node]: EUR: 184.26 JPY
[talker-1] [INFO] [1766841593.239517128] [talker_node]: Sent GBP rate
[listener-2] [INFO] [1766841593.239832824] [listener_node]: GBP: 211.24 JPY
```
USD、EUR、GBPがまとめて日本円に換算されます。
### 別々にUSD、EUR、GBPを日本円に換算する場合。
- 端末1でtalkerを立ち上げます。
```
$ ros2 run mypkg talker
[INFO] [1766842491.982019430] [currency_talker]: Sent USD rate
[INFO] [1766842492.565577726] [currency_talker]: Sent EUR rate
[INFO] [1766842493.067461444] [currency_talker]: Sent GBP rate
```
talkerを立ち上げるとUSD、EUR、GBPが配信されます。

- 端末2でトピックを直接確認します。
```
$ ros2 topic echo /dollar_rate
data: 156.47
---
```
```
$ ros2 topic echo /euro_rate
data: 184.26
---
```
```
$ ros2 topic echo /pound_rate
data: 211.24
---
```
それぞれ直接確認することができます。

## 必要なソフトウェア
### 本パッケージの実行には、以下の環境およびライブラリが必要です。
- OS: Ubuntu 22.04.3 LTS
- ROS2 Humble Hawksbill
- Python 3.13.9
- Pythonライブラリ: `requests`
  - インストール方法: `pip install requests`

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。
- ©2025 Sota Ino

## 参考文献
- [ExchangeRate-API](https://app.exchangerate-api.com/dashboard)
- [Requestsの使い方](https://note.nkmk.me/python-requests-usage/)
- [response.jsonとは？](https://pythonaiclarifydoubts.com/response-json/)
