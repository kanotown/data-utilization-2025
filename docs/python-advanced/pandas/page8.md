# 8. データの整形・変換（欠損値処理、型変換、並べ替えなど）

pandasを使用してデータの整形や変換を行うことで、データの品質を向上させ、分析を効率的にできるようにします。このセクションでは、欠損値処理、型変換、並べ替えといった操作について説明します。

## 8.1 欠損値の処理

欠損値とは、データの中で値が存在しない箇所のことです。pandasでは、`NaN`（Not a Number）として扱われます。以下の方法で処理します。

### 8.1.1 欠損値の確認

まずはデータフレームにどこに欠損値があるか確認します。

```python
import pandas as pd

# データフレームの例を作成
data = {'A': [1, 2, None], 'B': [4, None, 6]}
df = pd.DataFrame(data)

# 欠損値を確認
print(df.isnull())
print(df.isnull().sum())  # 列ごとの欠損値の数を集計
```

### 8.1.2 欠損値の削除

欠損値を含む行または列を削除します。

```python
# 欠損値を含む行の削除
df_dropped_rows = df.dropna()

# 欠損値を含む列の削除
df_dropped_columns = df.dropna(axis=1)
```

### 8.1.3 欠損値の補完

欠損値を補完して埋めます。

```python
# 定数で埋める
df_filled_constant = df.fillna(0)

# 前の値で埋める
df_filled_ffill = df.fillna(method='ffill')

# 次の値で埋める
df_filled_bfill = df.fillna(method='bfill')
```

## 8.2 型変換

データの型を変換することで、計算や分析の効率を上げることができます。

```python
# データ型の確認
print(df.dtypes)

# 列 'A' を整数型に変換
df['A'] = df['A'].astype('Int64')

# 列 'B' を文字列型に変換
df['B'] = df['B'].astype(str)
```

## 8.3 データの並べ替え

データを特定の順序に並べ替えます。

### 8.3.1 単一の列で並べ替え

```python
# 列 'A' を昇順に並べ替え
df_sorted_A = df.sort_values(by='A')
```

### 8.3.2 複数列で並べ替え

```python
# 列 'A' を昇順、列 'B' を降順に並べ替え
df_sorted_multiple = df.sort_values(by=['A', 'B'], ascending=[True, False])
```

これらの操作を実践することで、データセットの準備と変換を効果的に行い、分析の基礎を固めることができます。プログラムを実行して手を動かし、実際の動作を確認してみてください。