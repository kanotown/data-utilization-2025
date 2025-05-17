# 8. 日本語表示とフォント設定

Matplotlibでグラフを描く際、日本語のラベルを追加したい場合があります。しかし、そのままでは日本語が正しく表示されないことがあります。ここでは、日本語を正しく表示するための設定方法とフォントのカスタマイズについて説明します。

## 8.1 日本語フォントのインストール

最初に、日本語を表示するために必要なフォントをインストールします。以下では、一般的な方法を紹介します。

1. **IPythonまたはPython環境の確認**: Jupyter Notebookなどを利用している場合は、インストール済みのフォントを確認することができます。
2. **フォントのインストール**: システムにインストールされている日本語フォントを確認します。Windowsなら「Meiryo」、Macなら「Hiragino」、Linuxなら「Noto Sans CJK」などがよく使われます。

## 8.2 日本語の表示設定

### 8.2.1 フォントの設定方法

Matplotlibのフォント設定で、日本語フォントを使用する方法を以下に示します。

```python
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# フォントプロパティの設定
font_path = '/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc'  # お使いの環境に合わせて変更してください
font_prop = fm.FontProperties(fname=font_path)

# サンプルデータの準備
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y)

# グラフのタイトルとラベルに日本語を設定
plt.title('素数のグラフ', fontproperties=font_prop)
plt.xlabel('見出し', fontproperties=font_prop)
plt.ylabel('値', fontproperties=font_prop)

plt.show()
```

### 8.2.2 フォントキャッシュのクリア

新しいフォントをインストールした後は、フォントキャッシュをクリアする必要があります。以下のコマンドをPython環境で実行してください。

```python
import matplotlib as mpl

# フォントキャッシュの削除
mpl.font_manager._rebuild()
```

## 8.3 フォントサイズとスタイルのカスタマイズ

フォントサイズやスタイルを変更するには、`FontProperties`を利用します。以下はその例です。

```python
# フォントプロパティを使ったカスタマイズ
font_prop_large = fm.FontProperties(fname=font_path, size=14, style='italic')

plt.title('拡大されたフォント', fontproperties=font_prop_large)
plt.xlabel('横軸ラベル', fontproperties=font_prop)
plt.ylabel('縦軸ラベル', fontproperties=font_prop)

plt.plot(x, y)
plt.show()
```

このようにして、Matplotlibで日本語を表示しつつ、フォントのスタイルやサイズを調整することができます。プログラムを実際に試しながら、設定を自在に変えてみましょう。