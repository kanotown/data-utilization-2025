# 4. データの準備と読み込み（Pandas との連携）

このセクションでは、Plotly でグラフを作成するために必要なデータの準備と読み込みについて学びます。特に、Pandas ライブラリを使ってデータを効率的に扱う方法を紹介します。以下のステップを順に進めていくことで、Pandas を用いたデータ操作の基礎を理解し、実際に Plotly を使ったグラフ作成の準備を整えましょう。

## 4.1 Pandas の基本

### 4.1.1 Pandas とは

Pandas は、Python でデータを操作するためのライブラリで、特に表形式のデータを効率的に扱うことができます。Plotly と組み合わせることで、データを視覚化する際に非常に便利です。

### 4.1.2 Pandas のインストール

まず、Pandas をインストールする必要があります。以下のコマンドをターミナルまたはコマンドプロンプトで実行してください。

```bash
pip install pandas
```

## 4.2 データの読み込み

Pandas を使うと、CSV ファイルや Excel ファイルなどから簡単にデータを読み込むことができます。

### 4.2.1 CSV ファイルの読み込み

CSV ファイルは、最も一般的なデータ保存形式の一つです。以下のコードで、CSV ファイルを Pandas の DataFrame として読み込むことができます。

```python
import pandas as pd

# CSVファイルのパスを指定
file_path = 'example.csv'

# CSVファイルを読み込む
df = pd.read_csv(file_path)

# データの最初の5行を表示
print(df.head())
```

### 4.2.2 Excel ファイルの読み込み

Excel ファイルを読み込む方法も CSV に非常に似ています。

```python
# Excelファイルのパスを指定
file_path = 'example.xlsx'

# Excelファイルを読み込む
df = pd.read_excel(file_path)

# データの最初の5行を表示
print(df.head())
```

## 4.3 データの準備

データを読み込んだ後、グラフを描画する準備として、必要に応じてデータを加工・変換します。

### 4.3.1 データの選択とフィルタリング

特定の列や行を選択し、必要なデータだけに絞り込みます。

```python
# 特定の列を選択
selected_columns = df[['column1', 'column2']]

# 条件に基づくフィルタリング
filtered_data = df[df['column1'] > threshold_value]
```

### 4.3.2 データの集計

データを集計して、グラフ作成に適した形に整えます。

```python
# グループ化と平均値の計算
grouped_data = df.groupby('category_column').mean()

# 結果を表示
print(grouped_data)
```

## 4.4 Pandas と Plotly の連携

準備したデータを Plotly に渡してグラフを作成する方法を確認します。

```python
import plotly.express as px

# DataFrameからPlotlyのグラフを作成
fig = px.line(df, x='date', y='value', title='Sample Line Graph')

# グラフを表示
fig.show()
```

これで、Pandas を使ってデータを準備し、Plotly でグラフを描画するための基本的なスキルを身につけました。これらを活用して、さまざまなデータを視覚化してみましょう。
