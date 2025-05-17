# 10. よくあるエラーとその対処法

Plotly を使っているときに遭遇しがちなエラーとその対処法を以下に示します。エラーはプログラミングの一部ですが、恐れずに的確な対処を身に付けましょう。

## 10.1 モジュールが見つからないエラー

### 症状
`ModuleNotFoundError: No module named 'plotly'` と表示される。

### 対処法
Plotly がインストールされていない可能性があります。以下のコマンドを実行してインストールしてください。

```bash
pip install plotly
```

## 10.2 データフレームに指定されたカラムがないエラー

### 症状
`KeyError: 'column_name'` と表示される。

### 対処法
指定したカラムが実際にデータフレームに存在するか確認してください。カラム名には誤字がないか、またデータが想定通りに読み込まれているかを確認しましょう。例えば、Pandasデータフレームのカラムを確認するコードは以下の通りです。

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# カラム名の確認
print(df.columns)
```

## 10.3 グラフが表示されないエラー

### 症状
コードは実行されるが、グラフが表示されない。

### 対処法
Jupyter Notebook や Google Colab で実行している場合、Plotly で生成したグラフを表示するために `plotly.io.renderers.default='notebook'` を指定する必要があります。また、`plotly.offline.plot` も利用可能です。

例：

```python
import plotly.express as px
import plotly.io as pio

# Jupyter Notebook 用
pio.renderers.default = 'notebook'

df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length')

# グラフを表示
fig.show()
```

## 10.4 Jupyter Notebook でのエクスポートエラー

### 症状
`ValueError: Figures created using the 'notebook_connected' renderer cannot be used with to_image` と表示される。

### 対処法
Jupyter Notebook でグラフをエクスポートするときは、`plotly.io.to_image` 関数を用います。ただし、デフォルトのレンダラー設定が問題となる場合があります。その場合、このレンダラー設定を適切に調整してください。

```python
import plotly.io as pio

# 'notebook'から 'png'や'jpeg'などの静的レンダラーに変更する
pio.renderers.default = 'png'

# グラフのエクスポート
img_bytes = pio.to_image(fig, format='png')

# 保存する場合
with open('plot.png', 'wb') as f:
    f.write(img_bytes)
```

様々なエラーに遭遇することはありますが、試行錯誤を重ねて対処できるようになると、プログラミングがより楽しくなってくるはずです。困ったときはエラーメッセージをしっかり読み、インターネットや公式ドキュメントを活用して解決策を探しましょう。