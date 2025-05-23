# 9. グラフの保存と共有（画像・HTML ファイルとして出力）

Plotly で作成したグラフやビジュアライゼーションを他の人と共有するためには、グラフを画像や HTML ファイルとして保存・出力する方法を理解することが重要です。この章では、具体的なコード例を交えて、グラフを保存・共有する方法を紹介します。

## 9.1 画像として保存

Plotly のグラフを画像ファイルとして保存する場合、`write_image`関数を使用します。この関数では、PNG、JPEG、PDF などの形式でグラフを保存することができます。以下は、PNG 形式でグラフを保存する例です。

```python
import plotly.express as px

# サンプルデータとグラフの作成
df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')

# グラフをPNG形式で保存
fig.write_image("figure.png")
```

### 9.1.1 必要なライブラリのインストール

Plotly の画像出力には、`kaleido`というライブラリが必要になります。以下のコマンドでインストールしてください。

```sh
pip install -U kaleido
```

## 9.2 HTML ファイルとして保存

グラフを HTML ファイルとして保存すると、インタラクティブな要素をそのまま保った状態で Web 上で共有することができます。以下は、HTML 形式でグラフを保存する方法です。

```python
import plotly.express as px

# サンプルデータとグラフの作成
df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')

# グラフをHTML形式で保存
fig.write_html("figure.html")
```

## 9.3 グラフの共有

保存した画像や HTML ファイルは、以下の方法で共有することができます。

### 9.3.1 メールで送信

保存したファイルをメールの添付ファイルとして送信することで、簡単に人と共有することができます。HTML ファイルの場合、受け手がファイルを開けば、インタラクティブなグラフをその場で確認できます。

### 9.3.2 クラウドストレージサービス

Google Drive や Dropbox といったクラウドストレージサービスを利用してファイルをアップロードし、共有リンクを生成することでスムーズに他者と共有することができます。

### 9.3.3 GitHub Pages の利用

GitHub Pages を利用すると、自分のリポジトリ上で HTML ファイルを公開し、静的サイトとして他の人にアクセスさせることができます。特に長期間共有したい場合に便利です。

このように、Plotly のグラフはさまざまな形式で保存・共有することができ、相手に合わせた方法での共有が可能です。ぜひ、活用してみてください！
