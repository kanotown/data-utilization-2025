# 4. Seaborn のスタイル設定

Seaborn を使うと、データを視覚的にわかりやすく表示するために、多くのスタイルオプションが提供されています。スタイル設定を行うことで、グラフをより見やすく、理解しやすいものにできます。このセクションでは、Seaborn で利用できる基本的なスタイル設定について解説します。

## 4.1 Seaborn スタイルの設定方法

Seaborn には、あらかじめ用意されたスタイルがいくつかあります。スタイルを設定することで、全体のグラフの美観を統一することができます。以下は、スタイルの変更方法の基本です。

### 4.1.1 デフォルトのスタイルを使用する

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Seabornのデフォルトスタイル
sns.set_theme()

# サンプルデータのプロット
tips = sns.load_dataset("tips")
sns.histplot(data=tips, x="total_bill")

plt.show()
```

### 4.1.2 あらかじめ定義されたスタイルを使用する

Seaborn には以下の 5 つのスタイルが用意されています: "darkgrid", "whitegrid", "dark", "white", "ticks"。

```python
# スタイルを指定
sns.set_style("whitegrid")

sns.histplot(data=tips, x="total_bill")
plt.show()
```

## 4.2 スタイル要素のカスタマイズ

スタイルには以下のような要素が含まれており、細かくカスタマイズすることも可能です。

### 4.2.1 スケールとコンテキストの設定

`set_context()`関数を使うと、フォントサイズや図のサイズを変更して、異なるコンテキスト（e.g., 'paper', 'notebook', 'talk', 'poster'）に適応させることができます。

```python
# コンテキストを'talk'に設定
sns.set_context("talk")

sns.histplot(data=tips, x="total_bill")
plt.show()
```

### 4.2.2 背景色とグリッドのカスタマイズ

グラフの背景色やグリッドの表示/非表示もカスタマイズ可能です。

```python
# 背景色を白，グリッドを非表示に設定
sns.set_style("white")

# グリッド表示の有無の設定
sns.despine()

sns.histplot(data=tips, x="total_bill")
plt.show()
```

## 4.3 高度な視覚効果

Seaborn は視覚効果を向上するために、より高度な設定をサポートしています。

### 4.3.1 パレットの設定

データカテゴリーごとに異なる色を簡単に設定するために、色のパレットを利用することができます。

```python
# カスタムパレットを設定
sns.set_palette("pastel")

sns.countplot(data=tips, x="day")
plt.show()
```

これらの設定を利用することで、Seaborn を用いたグラフをより効果的にデザインすることが可能です。ぜひ自分のデータに合ったスタイルを発見してみてください！
