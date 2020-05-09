# cibook-study-python

効果検証入門の学習のため、テキストに乗っている図や分析結果をPythonで実装していったコード群です。  
`notebook/`以下に章別に.ipynbファイルをまとめています。  
実装していく際に、nekoumeiさんのpythonでの実装を何度も参考にさせて頂きました。この場を借りてお礼申し上げます。

## How to use

自分の学習の際はpipenvを使用しました。pipenvを使用されている場合は次のコマンド群を実行してください。

```{shell}
git clone https://github.com/shyaginuma/cibook-study-python.git
cd cibook-study-python
pipenv install
pipenv shell
jupyter lab
```

それ以外を利用されている方は、requirements.txtを含めていますのでそちらから依存関係をインストールしてください。

### 書籍内で使用されているデータについて

書籍内ではいくつかのサンプルデータを例に分析をしていますが、中にはRのライブラリ内にのみ存在するデータがあるので、以下手順で事前にダウンロードし、`data/`配下に置いてください。

* 2.3.2節で使用する`vouvhers`データ：[ここ](https://github.com/itamarcaspi/experimentdatar/blob/master/data/vouchers.rda)からrdaファイルをダウンロード
* 4.3.1節で使用する`Cigar`データ：[ここ](https://cran.r-project.org/src/contrib/Ecdat_0.3-7.tar.gz)からEcdatライブラリをダウンロードし展開、`data/`から`Cigar`を取り出す。

※nekoumeiさんの実装では、`rpy2`というライブラリを使ってpythonからRのライブラリを使用する方法で行われていました。そちらの方がスマートなやり方かもしれません。

## Cautions

* 書籍で利用されているコードはRであり、Pythonには無いライブラリもいくつかあったので代替ライブラリを使うか直接実装しています。そのため分析結果の数値が書籍のものと異なる部分があります。

* 書籍の中の図などはnekoumeiさんのPython実装で完璧に再現されているので、そちらを参照されることをお勧めします。
* 書籍に乗っている一部の図は実装できていません。（以下）
  * 図3.10 IPWの共変量のバランス
  * 図5.6 rddパッケージによる分析結果の可視化

## References

* [効果検証入門](https://www.amazon.co.jp/dp/4297111179)
* [著者の方によるRのサンプルコード](https://github.com/ghmagazine/cibook)
* [サンプルコードのpython版実装](https://github.com/nekoumei/cibook-python) by [@nekoumei](https://twitter.com/nekoumei)さん

## Libraries

普段あまり使わないライブラリも多く使用しています。下記リンクをご参照下さい。

|name|homepage|
|---|---|
|rdata|https://github.com/vnmabus/rdata|
|rdd|https://github.com/evan-magnusson/rdd|
|pycausalimpact|https://github.com/dafiti/causalimpact|
