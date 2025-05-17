# 6. カテゴリ変数の可視化（棒グラフ・箱ひげ図・バイオリンプロット）

カテゴリ変数の可視化は、データの特徴や傾向を理解する上で非常に重要です。このセクションでは、Seaborn を使用してカテゴリ変数を可視化する方法を詳しく学びましょう。具体的には、棒グラフ、箱ひげ図、およびバイオリンプロットを取り上げます。

## 6.1 棒グラフ（Bar plot）

棒グラフは、カテゴリごとの数値を比較するのに適しています。Seaborn では`barplot()`関数を使って簡単に作成できます。

### 6.1.1 基本的な棒グラフの作成

以下は、カテゴリ変数の棒グラフを作成するための基本的なコードです。

```python
import seaborn as sns
import matplotlib.pyplot as plt

# サンプルデータ
data = sns.load_dataset('tips')

# 棒グラフの作成
sns.barplot(x='day', y='total_bill', data=data)

# グラフを表示
plt.show()
```

### 6.1.2 色を指定した棒グラフ

色をカスタマイズしたいときは、引数`palette`を使います。

```python
sns.barplot(x='day', y='total_bill', data=data, palette='Blues')
plt.show()
```

## 6.2 箱ひげ図（Box plot）

箱ひげ図は、データの分布、中央値や外れ値を視覚的に表現するのに適しています。

### 6.2.1 基本的な箱ひげ図の作成

```python
# 箱ひげ図の作成
sns.boxplot(x='day', y='total_bill', data=data)

# グラフを表示
plt.show()
```

### 6.2.2 色を指定した箱ひげ図

```python
sns.boxplot(x='day', y='total_bill', data=data, palette='Set2')
plt.show()
```

## 6.3 バイオリンプロット（Violin plot）

バイオリンプロットは、データの分布を視覚的に理解するための強力な方法です。密度情報を含むため、特にサンプル数が少ない場合でも役立ちます。

### 6.3.1 基本的なバイオリンプロットの作成

```python
# バイオリンプロットの作成
sns.violinplot(x='day', y='total_bill', data=data)

# グラフを表示
plt.show()
```

### 6.3.2 色を指定したバイオリンプロット

```python
sns.violinplot(x='day', y='total_bill', data=data, palette='muted')
plt.show()
```

## 6.4 まとめ

Seaborn を使うと、カテゴリ変数を視覚的に解析することが簡単にできます。棒グラフはカテゴリごとの比較に、箱ひげ図とバイオリンプロットはデータの分布を理解するのに役立ちます。それぞれのプロットで色やスタイルを変えることで、よりわかりやすくデータを伝えることができます。ぜひ自分のデータセットでもこれらの可視化を試してみてください。
