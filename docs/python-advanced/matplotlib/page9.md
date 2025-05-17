# 9. 実践例：データ分析への応用

この章では、Matplotlib を使用したデータ分析の実践例を見ていきます。実際にコードを試しながら、どのようにデータを可視化し分析に役立てるかを学びましょう。

## 9.1 データセットの準備

まずは、データ分析に使用するデータセットを準備します。ここでは、Python の一般的なライブラリである Pandas を使って CSV データを読み込みます。以下のコードを実行して、データセットを読み込んでみましょう。

```python
import pandas as pd

# CSVファイルを読み込む
data = pd.read_csv('sample_data.csv')
print(data.head())  # 最初の5行を表示
```

## 9.2 基本的なデータ可視化

データを視覚化することで、より良い洞察を得ることができます。ここでは、データセットの基本統計量をヒストグラムで表示します。

```python
import matplotlib.pyplot as plt

# 特定のカラム（ここでは'sales'）のヒストグラムを描画
plt.hist(data['sales'], bins=10, color='skyblue')
plt.title('Sales Distribution')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()
```

## 9.3 時系列データの可視化

時系列データを扱うことは多く、これを効率的に視覚化することが重要です。以下のコードでは、売上データを時系列でプロットしています。

```python
# 'date'を時系列データとしてプロット
data['date'] = pd.to_datetime(data['date'])
plt.plot(data['date'], data['sales'], marker='o', linestyle='-')
plt.title('Sales over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
```

## 9.4 相関関係の可視化

複数の変数間の相関を散布図で可視化します。ここでは、売上と広告費との関係を見てみましょう。

```python
# 散布図の作成
plt.scatter(data['advertising'], data['sales'], color='green')
plt.title('Sales vs. Advertising')
plt.xlabel('Advertising')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
```

## 9.5 結論と次のステップ

これらの視覚化技術を使用することで、データに潜むパターンや異常値を見つけ出す手助けになります。次のステップとしては、これらのビジュアルを基にした更なる詳細な分析や機械学習モデルの作成に進むことができます。

この実践例を通じて、Matplotlib を使った効果的なデータ可視化の基本を学びました。これからも実際のデータを使って練習を重ね、分析スキルを高めていきましょう。
