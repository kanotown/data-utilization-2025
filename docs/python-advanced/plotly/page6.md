# 6. インタラクティブな機能の活用

Plotly の大きな特徴の一つに、インタラクティブなグラフを作成できるという点があります。このセクションでは、大学生の皆さんが Plotly を使ってインタラクティブなグラフをどのように作成し、その機能を活用するかについて学んでいきましょう。

## 6.1 インタラクティブグラフの基礎

Plotly のインタラクティブグラフでは、ホバー、ズーム、パンなどの操作が可能です。これにより、グラフ上のデータポイントを詳細に確認することができます。

### 6.1.1 準備

まずは、Jupyter Notebook または任意の Python 環境で以下の準備を行ってください。

```python
# Plotlyのインポート
import plotly.express as px
```

### 6.1.2 基本的なインタラクティブグラフの作成

以下は、基本的なインタラクティブな折れ線グラフを作成するコードです。

```python
# サンプルデータの準備
import pandas as pd

data = {
    'year': [2010, 2011, 2012, 2013, 2014],
    'value': [10, 20, 15, 25, 30]
}
df = pd.DataFrame(data)

# 折れ線グラフの作成
fig = px.line(df, x='year', y='value', title='Sample Interactive Line Chart')

# グラフの表示
fig.show()
```

このコードを実行すると、インタラクティブにデータを探索できるグラフが表示されます。

## 6.2 ホバー情報のカスタマイズ

Plotly では、デフォルトでホバー時にデータポイントの情報が表示されますが、この情報をカスタマイズすることも可能です。

### 6.2.1 カスタマイズ方法

以下のコードでは、ホバー情報をカスタマイズする方法を示しています。

```python
fig = px.line(df, x='year', y='value', title='Customized Hover Info')

# ホバー情報のカスタマイズ
fig.update_traces(hovertemplate='Year: %{x}<br>Value: %{y}<extra></extra>')

fig.show()
```

このようにすれば、ホバー情報をより見やすく、必要な情報だけを表示することが可能です。

## 6.3 アニメーションの追加

Plotly では、時間の経過やカテゴリの変化を視覚化するためにアニメーションを追加することができます。

### 6.3.1 アニメーションの作成

次に、アニメーションの基本的な例を示します。

```python
df_anim = px.data.gapminder().query("country=='Japan'")

# アニメーション付きの散布図を作成
fig = px.scatter(df_anim, x='gdpPercap', y='lifeExp', size='pop', color='year',
                 hover_name='year', log_x=True, size_max=60, title='Japan over Time',
                 animation_frame='year', animation_group='country')

fig.show()
```

この例では、年ごとに日本の GDP と平均寿命の変化を視覚化することができます。

## 6.4 まとめ

インタラクティブな機能を活用することで、データの探索性や視覚的な訴求力を高めることができます。大学生の皆さんには、ここで学んだ内容を元に、さまざまなデータセットに自分自身でインタラクティブなグラフを作成することをお勧めします。これにより、より深いデータの理解と洞察を得ることができるでしょう。
