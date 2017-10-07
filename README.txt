GVAR model推計用のデータをつくるプログラム
GVAR modelとはGlobal Vector Auto Regressive modelのこと。各国のマクロ変数の時間を通した動的な関係を調べることができる。
GVAR modelの推計はMatlabを用いて行っているが、これまでは推計するためのデータを手作業で作成していた。このプログラムはその作業を自動化するものである。
主に以下の二つの部分からなる。
１. IMFのデータベースから最新のデータをとってきてAWS RDBに格納する。
２. AWS RDBからデータを成形し、出力する。
