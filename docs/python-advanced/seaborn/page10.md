# 10. Seaborn と Matplotlib の連携

Seaborn は Matplotlib のラッパーライブラリとして知られており、データの可視化を簡略化するのに役立ちます。Seaborn と Matplotlib を連携させることで、よりカスタマイズされたグラフを作成できます。本節では、Seaborn と Matplotlib を組み合わせて効果的なデータビジュアライゼーションを行う方法を学びます。

## 10.1 Seaborn と Matplotlib の基礎

Seaborn と Matplotlib はそれぞれ独立して動作しますが、Seaborn のグラフを Matplotlib でさらに調整することが可能です。まずは両方のライブラリをインポートし、基本的な使用法を示します。

### 10.1.1 ライブラリのインポート

```python
import matplotlib.pyplot as plt
import seaborn as sns
```

### 10.1.2 基本的な使い方

Seaborn で作成したグラフを Matplotlib の機能でカスタマイズする基本的な例です。

```python
# サンプルデータの読み込み
tips = sns.load_dataset("tips")

# Seabornで基本的なグラフ作成
sns.set(style="whitegrid")
ax = sns.boxplot(x="day", y="total_bill", data=tips)

# Matplotlibでグラフにカスタマイズを追加
ax.set_title('Day-wise Box Plot of Total Bill')
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill')
plt.show()
```

## 10.2 グラフのカスタマイズ

Matplotlib の強力なカスタマイズ機能を用いて Seaborn のプロットに付加価値を与えることができます。

### 10.2.1 色のカスタマイズ

Matplotlib では Seaborn のプロットに対して色をカスタマイズできます。

```python
# 色のカスタマイズ
sns.set_palette("pastel")
sns.boxplot(x="day", y="total_bill", data=tips)

# Matplotlibでさらにカスタマイズ
plt.title('Custom Color for Box Plot')
plt.show()
```

### 10.2.2 グリッド線の調整

Seaborn のグリッドスタイルを調整する例を示します。

```python
# グリッド線の調整
sns.set(style="darkgrid")
sns.boxplot(x="day", y="total_bill", data=tips)

# Matplotlibでグリッドの色を変更
plt.grid(color='gray', linestyle='--', linewidth=0.7)
plt.title('Adjusted Grid Lines on Box Plot')
plt.show()
```

## 10.3 複合プロットの作成

Seaborn と Matplotlib を組み合わせて複合的なプロットを作成する例です。

### 10.3.1 FacetGrid と Matplotlib

Seaborn の`FacetGrid`を使い、Matplotlib で調整を行う例です。

```python
# FacetGridの作成
g = sns.FacetGrid(tips, col="sex", height=4, aspect=1)
g.map(sns.histplot, "total_bill", kde=True)

# Matplotlibで全体にタイトルを追加
plt.subplots_adjust(top=0.8)
g.fig.suptitle('Total Bill Distribution by Sex')
plt.show()
```

このように Seaborn と Matplotlib を連携させることで、視覚的に訴求力のあるグラフを作成できます。自分自身で様々なカスタマイズを試してみてください。
