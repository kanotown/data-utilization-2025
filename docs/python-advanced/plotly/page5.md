# 5. グラフのカスタマイズ（タイトル・軸ラベル・色など）

Plotly を使ってデータを視覚化する際、グラフを見やすく、解釈しやすくするためにカスタマイズが重要です。このセクションでは、Plotly のグラフをカスタマイズする方法について学習します。

## 5.1 タイトルの追加

グラフにタイトルを追加することで、グラフの内容を簡潔に伝えることができます。

```python
import plotly.express as px

# サンプルデータの生成
df = px.data.iris()

# 散布図の作成とタイトルの設定
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
fig.update_layout(title='アイリスの花びらの幅と長さの関係')
fig.show()
```

## 5.2 軸ラベルの変更

軸ラベルを設定することで、プロットされたデータが何を示しているか明確にすることができます。

```python
# 軸ラベルの設定
fig.update_xaxes(title_text='花びらの幅 (cm)')
fig.update_yaxes(title_text='花びらの長さ (cm)')
fig.show()
```

## 5.3 グラフの色の変更

グラフの色は視覚的な印象を大きく左右します。デフォルトの色設定を変更することで、より魅力的なグラフを作成することができます。

```python
# 色の変更
fig = px.scatter(
    df,
    x='sepal_width',
    y='sepal_length',
    color='species',
    color_discrete_sequence=['#FF5733', '#33FF57', '#3357FF']
)
fig.show()
```

## 5.4 凡例のカスタマイズ

凡例をカスタマイズして、データのカテゴリをより分かりやすく表示することができます。

```python
# 凡例の設定
fig.update_layout(
    legend_title_text='種別',
    legend=dict(
        x=0.1,
        y=0.9,
        bgcolor='rgba(255, 255, 255, 0.5)',
        bordercolor='Black',
        borderwidth=1
    )
)
fig.show()
```

## 5.5 テーマの適用

Plotly には複数の内蔵テーマがあり、これらを適用することでグラフの外観を劇的に変えることができます。

```python
# テーマの適用
fig.update_layout(template='plotly_dark')
fig.show()
```

これらのカスタマイズのテクニックを活用して、魅力的で情報量の多いグラフを作成してください。実際にコードを実行して、どのようにグラフが変化するかを観察してみましょう。
