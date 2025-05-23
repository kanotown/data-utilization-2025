# 8. さまざまなグラフタイプ（散布図・ヒートマップ・3D グラフなど）

Plotly は様々なグラフタイプをサポートしており、データ解析から可視化まで広範囲にわたって利用可能です。この章では、最も一般的なグラフタイプである散布図、ヒートマップ、3D グラフを取り上げ、それぞれの特徴や作成方法を詳しく解説します。

## 8.1 散布図

散布図は、データの分布や関係性を視覚化するのに非常に適したグラフです。ここでは、Plotly を用いた基本的な散布図の作成方法を紹介します。

### 8.1.1 基本的な散布図の作成

```python
import plotly.express as px

# サンプルデータを生成
df = px.data.iris()

# 散布図を作成
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species',
                 title="Irisデータセットの散布図")

# グラフを表示
fig.show()
```

このコードを実行すると、`sepal_width` と `sepal_length` に基づく Iris データセットの散布図が表示されます。`color` 引数を用いて、各データポイントに異なる色を付けることで、視覚的に種を分けていることが見てとれます。

## 8.2 ヒートマップ

ヒートマップは、行列形式のデータを色彩によって視覚化するのに役立ちます。次に、ヒートマップの作成方法を示します。

### 8.2.1 基本的なヒートマップの作成

```python
import plotly.express as px
import numpy as np

# サンプルデータを生成
data = np.random.rand(10, 10)

# ヒートマップを作成
fig = px.imshow(data, color_continuous_scale='Viridis', title="ランダムデータのヒートマップ")

# グラフを表示
fig.show()
```

このコードでは、10x10 のランダムな数値行列を視覚化する基本的なヒートマップを作成しています。デフォルトの色彩スケールによって、データの多様な範囲を色で表すことができます。

## 8.3 3D グラフ

3D グラフは、データの多次元性を表現する場合に有効です。ここでは、Plotly を用いた基礎的な 3D 散布図の作成方法を紹介します。

### 8.3.1 基本的な 3D 散布図の作成

```python
import plotly.express as px

# サンプルデータを生成
df = px.data.iris()

# 3D散布図を作成
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width', color='species',
                    title="Irisデータセットの3D散布図")

# グラフを表示
fig.show()
```

このコードを実行すると、`sepal_length`、`sepal_width`、`petal_width`に基づく Iris データセットの 3D 散布図が表示されます。`color` 引数を使うことで、3D 空間においてもデータのグルーピングが視覚的に表現されます。

---

以上、各グラフタイプの基本的な作成方法を解説しました。これらのサンプルコードを実際に試しながら、Plotly のもつ多様な可視化機能を体験してみてください。各グラフは多くのオプションを持っており、カスタマイズによってさらに多様な表現が可能です。興味を持った方は、公式ドキュメントや様々なチュートリアルも活用し、理解を深めていきましょう。
