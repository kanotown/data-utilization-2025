# 13. NumPyの応用例（簡単なデータ分析・可視化への応用）

NumPyはデータ分析や可視化といった分野でも広く利用されています。このセクションでは、NumPyを用いたデータ分析の基礎的な流れと、それに関連した簡単な可視化を例に説明します。

## 13.1 簡単なデータ分析の流れ

ここでは、NumPyを用いて実際にデータの集計や分析を行う手順を示します。

### 13.1.1 データの準備

まずは仮のデータセットを用意します。この例では、ある商品が5日間に売れた数を記録したデータを使用します。

```python
import numpy as np

# ある商品の5日間の売上データ
sales = np.array([15, 22, 19, 14, 29])
```

### 13.1.2 基本的な集計操作

NumPyを用いると簡単にデータの集計を行うことができます。以下は基本的な集計処理です。

```python
# 各値の総計
total_sales = np.sum(sales)
print(f"総売上: {total_sales}")

# 平均
average_sales = np.mean(sales)
print(f"平均売上: {average_sales:.2f}")

# 最大値・最小値
max_sales = np.max(sales)
min_sales = np.min(sales)
print(f"最大売上: {max_sales}, 最小売上: {min_sales}")
```

## 13.2 データの可視化

データを可視化することで、より直感的にその特徴を捉えることができるようになります。ここではMatplotlibを使用して簡単なグラフを作成してみましょう。

### 13.2.1 Matplotlibによるグラフ作成

Matplotlibを用いて売上データの折れ線グラフを作成します。

```python
import matplotlib.pyplot as plt

# x軸の日数
days = np.array([1, 2, 3, 4, 5])

# 折れ線グラフを描画
plt.plot(days, sales, marker='o', linestyle='-')
plt.title("5日間の売上")
plt.xlabel("日")
plt.ylabel("売上")
plt.grid(True)
plt.show()
```

## 13.3 応用例

これまでに学んだことに基づいて、NumPyを活用したデータ分析と可視化の応用例を紹介します。

### 13.3.1 複数商品の売上分析

ここでは、複数の商品をまとめたデータを解析し、その結果を可視化します。

```python
# 各商品ごとの5日間の売上データ
sales_data = np.array([
    [15, 22, 19, 14, 29],  # 商品A
    [10, 15, 25, 10, 30],  # 商品B
    [5, 8, 12, 15, 20]     # 商品C
])

# 各商品の合計売上を計算
total_sales_per_product = np.sum(sales_data, axis=1)
print(f"商品の総売上: {total_sales_per_product}")

# グラフで表示
for i, product_sales in enumerate(sales_data):
    plt.plot(days, product_sales, marker='o', linestyle='-', label=f"商品{i+1}")

plt.title("各商品の5日間の売上")
plt.xlabel("日")
plt.ylabel("売上")
plt.legend()
plt.grid(True)
plt.show()
```

この例では、3つの商品に対して5日間の売上データを整理・分析し、その結果をグラフとして可視化しています。NumPyとMatplotlibを組み合わせることで、より複雑なデータの分析・可視化が可能となります。高校生や大学生の皆さんが、日々のデータ分析に役立ててくださることを期待しています。