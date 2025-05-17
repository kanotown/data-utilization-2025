# 7. 散布図と回帰分析の可視化

この章では、Seaborn を用いた散布図と回帰分析の可視化方法について学びます。散布図は二変量の関係を視覚的に確認するのに優れており、回帰分析はその関係を数値的に把握するための手法です。

## 7.1 散布図の作成

Seaborn には、散布図を作成するための関数`scatterplot`があります。この関数を使用して、二変数間の関係を可視化できます。

### 例: 基本的な散布図

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# データセットの読み込み
tips = sns.load_dataset('tips')

# 散布図の作成
sns.scatterplot(x='total_bill', y='tip', data=tips)

# グラフの表示
plt.title('Total Bill vs Tip')
plt.show()
```

## 7.2 散布図行列の作成

複数の変数間の関係を同時に確認したい場合、Seaborn の`pairplot`関数を利用できます。これにより、複数の変数間の散布図を一度に表示することが可能です。

### 例: 散布図行列

```python
# 散布図行列の作成
sns.pairplot(tips)

# グラフの表示
plt.show()
```

## 7.3 回帰分析の可視化

Seaborn には、回帰分析を可視化するための`regplot`関数があります。この関数を使用すると、散布図上に回帰線を引くことができます。

### 例: 散布図と回帰線

```python
# 散布図と回帰線の作成
sns.regplot(x='total_bill', y='tip', data=tips)

# グラフの表示
plt.title('Regression Line for Total Bill vs Tip')
plt.show()
```

## 7.4 カテゴリ別の回帰分析

場合によっては、特定のカテゴリごとに回帰分析を行いたいことがあります。`lmplot`を利用すると、カテゴリごとに色分けした散布図と回帰線を描くことができます。

### 例: 性別ごとの回帰分析

```python
# 性別ごとの回帰分析
sns.lmplot(x='total_bill', y='tip', hue='sex', data=tips)

# グラフの表示
plt.title('Regression by Sex')
plt.show()
```

これらのツールを活用することで、データ中の関係性を視覚的に確認することができます。ぜひ、お手元の環境でコードを実行し、理解を深めてください。
