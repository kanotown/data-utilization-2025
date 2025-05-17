# 5. 単変量データの可視化（ヒストグラム・カーネル密度推定）

このセクションでは、Seabornを用いて単変量データの可視化を行う方法について解説します。ヒストグラムとカーネル密度推定（KDE）の2つの代表的な手法を学んでいきましょう。

## 5.1 ヒストグラム

ヒストグラムは、データの分布を視覚的に理解するための基本的なツールです。Seabornでは `displot` 関数を利用して簡単に作成できます。

### 5.1.1 ヒストグラムの作成

まず、SeabornとMatplotlib、さらにデータ操作ライブラリのPandasを使ってデータを読み込み、ヒストグラムを描画してみましょう。

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# データセットの読み込み
data = sns.load_dataset("tips")

# ヒストグラムの作成
sns.displot(data['total_bill'], kde=False)

# グラフの表示
plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()
```

上記のコードは、"tips" データセットの`total_bill`列に対するヒストグラムを表示します。

## 5.2 カーネル密度推定（KDE）

カーネル密度推定とは、データの確率密度関数を推定する方法です。滑らかな曲線でデータの分布を示すことができ、ヒストグラムと組み合わせて使われることが多いです。

### 5.2.1 KDEの追加

ヒストグラムにKDEを追加することで、データの分布をより詳細に理解できます。

```python
# KDEの追加
sns.displot(data['total_bill'], kde=True)

# グラフの表示
plt.title("Distribution of Total Bill with KDE")
plt.xlabel("Total Bill")
plt.ylabel("Density")
plt.show()
```

このコードでは、`kde=True` とすることでヒストグラムにKDE曲線を重ねて表示しています。

## 5.3 ヒストグラムとKDEのカスタマイズ

Seabornでは、ヒストグラムとKDEのスタイルや色をカスタマイズするための多くのオプションが用意されています。

### 5.3.1 スタイルと色のカスタマイズ

以下の例では、色やスタイルを変更してみます。

```python
# ヒストグラムとKDEのカスタマイズ
sns.displot(data['total_bill'], kde=True, color='purple', bins=30)

# グラフの表示
plt.title("Customized Histogram and KDE of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Density")
plt.show()
```

この例では、`color='purple'` で色を指定し、`bins=30` でヒストグラムのビンの数を調整しています。

以上のステップを通じて、Seabornによる単変量データの可視化について基本的な理解が得られることでしょう。実際に手を動かして、さまざまなデータセットで試してみてくださいね。