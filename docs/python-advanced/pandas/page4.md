# 4. データの読み込みと書き出し（CSV, Excel, 他）

pandas を使用すると、CSV や Excel ファイルをはじめとする多様な形式のデータを手軽に扱うことができます。このセクションでは、pandas を使ってデータを読み込み、そして書き出す方法について学びます。

## 4.1 CSV ファイルの読み込み

CSV（Comma-Separated Values）は最も一般的なテキストデータ形式の一つです。pandas には、この形式のデータを読み込むための`read_csv`関数があります。

### コード例

```python
import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('sample.csv')

# データフレームの内容を確認
print(df.head())
```

このコードは`sample.csv`という名前の CSV ファイルを読み込み、データフレームとして表示します。

## 4.2 Excel ファイルの読み込み

Excel ファイルの読み込みには`read_excel`関数を使用します。この関数は、単一のシートだけでなく複数シートを含む Excel ファイルにも対応しています。

### コード例

```python
# Excelファイルを読み込む
df = pd.read_excel('sample.xlsx', sheet_name='Sheet1')

# データフレームの内容を確認
print(df.head())
```

このコードは`sample.xlsx`という Excel ファイルの`Sheet1`シートからデータを読み込みます。

## 4.3 データの書き出し

データの書き出しも簡単に行えます。データを CSV ファイルや Excel ファイルとして保存するための関数を見ていきましょう。

### 4.3.1 CSV ファイルへの書き出し

pandas では、`to_csv`関数を使ってデータを CSV ファイルとして保存することができます。

#### コード例

```python
# データフレームをCSVファイルとして保存
df.to_csv('output.csv', index=False)
```

このコードは、データフレーム`df`を`output.csv`として保存します。`index=False`は、データフレームのインデックスをファイルに含めないようにしています。

### 4.3.2 Excel ファイルへの書き出し

データを Excel ファイルとして保存するには`to_excel`関数を使用します。

#### コード例

```python
# データフレームをExcelファイルとして保存
df.to_excel('output.xlsx', sheet_name='Results', index=False)
```

このコードは、`df`を`output.xlsx`という名前で保存し、`Results`というシート名を指定しています。

## 4.4 その他のデータ形式

pandas は、JSON や SQL データベース、Parquet ファイルなど、他の多くの形式にも対応しています。詳細は、pandas の公式ドキュメントで確認してみてください。

これで、pandas を使った基本的なデータの読み込みと書き出しの方法をマスターできました。実際に手を動かしながら進めると、感覚がつかみやすくなるので、ぜひ練習してみてくださいね。
