# 7. 複数グラフのレイアウト（サブプロット・複合グラフ）

Plotlyを使用すると、一つの図面内に複数のグラフを配置することができます。これにより、異なるデータセットを比較したり、複雑なデータを視覚的に表現したりすることが可能になります。本章では、サブプロットと複合グラフの作成方法について学びます。

## 7.1 サブプロットの作成

サブプロットを使用すると、異なる種類のグラフを一つの図面に並べて比較することができます。ここでは、例として折れ線グラフと棒グラフを横に並べたサブプロットを作成します。

### 7.1.1 必要なライブラリのインポート

まず、必要なPythonライブラリをインポートします。

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots
```

### 7.1.2 基本的なサブプロット作成

次に、サブプロットを作成するための基本的なコードを示します。

```python
# サブプロットの設定
fig = make_subplots(rows=1, cols=2, subplot_titles=("折れ線グラフ", "棒グラフ"))

# 折れ線グラフ
fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[10, 11, 12], mode='lines', name='折れ線グラフ'),
    row=1, col=1
)

# 棒グラフ
fig.add_trace(
    go.Bar(x=[1, 2, 3], y=[1, 3, 2], name='棒グラフ'),
    row=1, col=2
)

# サブプロットのレイアウト設定
fig.update_layout(title_text="サブプロットの例")
fig.show()
```

### 7.1.3 サブプロットのカスタマイズ

サブプロットのそれぞれのグラフに対して、タイトルや軸ラベルを設定できます。

```python
# タイトルと軸ラベルのカスタマイズ
fig.update_xaxes(title_text="X軸", row=1, col=1)
fig.update_yaxes(title_text="Y軸", row=1, col=1)
fig.update_xaxes(title_text="X軸", row=1, col=2)
fig.update_yaxes(title_text="Y軸", row=1, col=2)

# 再度レンダリング
fig.show()
```

## 7.2 複合グラフの作成

複合グラフでは、同じグラフに異なるデータ系列を重ねることができます。これにより、異なるデータポイントの関係を視覚的に理解できます。

### 7.2.1 同じグラフに複数データ系列を追加

以下の例では、折れ線グラフと棒グラフを重ねて表示します。

```python
# グラフの初期化
fig = go.Figure()

# 折れ線グラフ
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[3, 2, 1], mode='lines', name='折れ線グラフ'))

# 棒グラフ
fig.add_trace(go.Bar(x=[1, 2, 3], y=[2, 3, 1], name='棒グラフ'))

# グラフのレイアウトを調整
fig.update_layout(title_text="複合グラフの例")
fig.show()
```

### 7.2.2 複合グラフのカスタマイズ

それぞれのデータ系列に対して色を変更するなどのカスタマイズが可能です。

```python
# 折れ線グラフの色をカスタマイズ
fig.update_traces(line=dict(color='blue'), selector=dict(mode='lines'))

# 棒グラフの色をカスタマイズ
fig.update_traces(marker_color='green', selector=dict(type='bar'))

# 再度レンダリング
fig.show()
```

Plotlyを用いたサブプロットや複合グラフは、視覚的にデータを比較しやすく非常に有用です。この章で学んだ知識を基に、様々なデータを扱ってみましょう。