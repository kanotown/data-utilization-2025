# 10. データの可視化（pandas の plot 機能）

データの可視化は、データ分析において非常に重要なステップです。`pandas`には、データを簡単に可視化するための便利な plot 機能が備わっています。このセクションでは、pandas の plot 機能を使ってデータを視覚化する方法について学びます。

## 10.1 pandas.plot の概要

pandas の`plot`機能は、`matplotlib`ライブラリを基に構築されており、基本的なグラフをシンプルなコードで作成することができます。`Series`や`DataFrame`オブジェクトに直接メソッドとして`plot`を使うことで、様々なタイプのグラフを描画できます。

## 10.2 基本的なプロット方法

以下に、pandas の`plot`機能で利用できる基本的なプロットをいくつか紹介します。

### 10.2.1 ラインプロット

ラインプロット（線グラフ）は、データの傾向を示すのに便利です。以下のコードは、`DataFrame`のデータをラインプロットで表示する方法です。

```python
import pandas as pd
import matplotlib.pyplot as plt

# サンプルデータの作成
data = {'Year': [2018, 2019, 2020, 2021],
        'Sales': [200, 220, 250, 300]}
df = pd.DataFrame(data)

# ラインプロットの作成
df.plot(x='Year', y='Sales', kind='line')
plt.title('Sales Over Years')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.show()
```

### 10.2.2 バープロット

バープロット（棒グラフ）は、カテゴリ別のデータを比較するのに適しています。

```python
# バープロットの作成
df.plot(x='Year', y='Sales', kind='bar')
plt.title('Sales Comparison by Year')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.show()
```

### 10.2.3 ヒストグラム

ヒストグラムは、データの分布を視覚化するのに用いられます。

```python
# サンプルデータの作成
data = {'Age': [23, 25, 29, 30, 31, 35, 37, 42, 45, 49]}
df = pd.DataFrame(data)

# ヒストグラムの作成
df['Age'].plot(kind='hist', bins=5)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
```

### 10.2.4 散布図

散布図は、2 つの数値データの関係を視覚化するのに役立ちます。

```python
# サンプルデータの作成
data = {'Height': [150, 160, 170, 180, 190],
        'Weight': [50, 60, 70, 80, 90]}
df = pd.DataFrame(data)

# 散布図の作成
df.plot(x='Height', y='Weight', kind='scatter')
plt.title('Height vs Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()
```

## 10.3 グラフのカスタマイズ

pandas の plot 機能をカスタマイズして、見た目や特徴を変更することが可能です。

### 10.3.1 軸ラベルとタイトルの設定

既に紹介したように、`xlabel`、`ylabel`、`title`を使ってグラフの軸ラベルやタイトルを設定できます。

### 10.3.2 色の設定

`color`引数を使って、グラフの色を指定できます。

```python
df.plot(x='Year', y='Sales', kind='line', color='green')
plt.title('Sales Over Years')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.show()
```

### 10.3.3 複数のシリーズを同時にプロット

1 つのグラフに複数のシリーズを重ねて表示することもできます。

```python
# サンプルデータの作成
data = {'Year': [2018, 2019, 2020, 2021],
        'Sales_A': [200, 220, 250, 300],
        'Sales_B': [150, 180, 210, 240]}
df = pd.DataFrame(data)

# 複数のシリーズのプロット
df.plot(x='Year', y=['Sales_A', 'Sales_B'])
plt.title('Sales Over Years')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.show()
```

## 10.4 まとめ

pandas の plot 機能は、データの視覚化を簡単に行える強力なツールです。このセクションでは、基本的なプロット方法やカスタマイズの方法について学びました。次にデータを分析する際には、ぜひ pandas を活用してビジュアルに訴える洞察を引き出してください。
