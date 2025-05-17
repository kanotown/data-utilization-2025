# 3. SeriesとDataFrameの基本

pandasでのデータ操作の基礎を学ぶ最初のステップとして、SeriesとDataFrameについて理解することが重要です。ここでは、pandasの基本的なデータ構造であるこれら二つについて説明し、基礎的な使い方を学びましょう。

## 3.1 Seriesの基本

### 3.1.1 Seriesとは

Seriesは一列のデータを持つ一次元のラベル付き配列です。インデックスがラベルとして使用され、各要素に名前を付けることができます。

### 3.1.2 Seriesの作成

Seriesを作成するためには、`pandas.Series`を使用します。

```python
import pandas as pd

# リストからSeriesを作成
data = [10, 20, 30, 40]
s = pd.Series(data)
print(s)
```

このコードを実行すると、四つの数字がインデックス付きで表示されます。

### 3.1.3 インデックスを指定したSeriesの作成

```python
# インデックスを指定してSeriesを作成
data = [10, 20, 30, 40]
index = ['a', 'b', 'c', 'd']
s = pd.Series(data, index=index)
print(s)
```

指定したインデックスを活用してデータを参照することができます。

## 3.2 DataFrameの基本

### 3.2.1 DataFrameとは

DataFrameは、二次元データを扱うためのデータ構造で、行と列から成り立っています。Excelシートに似た構造を持ち、データの整形や処理に非常に便利です。

### 3.2.2 DataFrameの作成

DataFrameを作成するには、`pandas.DataFrame`を使用します。

```python
import pandas as pd

# 辞書からDataFrameを作成
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)
print(df)
```

データは列ごとに入力され、インデックスは自動的に生成されます。

### 3.2.3 インデックスと列の指定

```python
# インデックスと列を指定してDataFrameを作成
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
index = ['row1', 'row2', 'row3']
columns = ['A', 'B', 'C']
df = pd.DataFrame(data, index=index, columns=columns)
print(df)
```

作成時にインデックスや列名を独自に設定することも可能です。

これらの基本操作を理解すれば、pandasでのデータ操作がスムーズになります。次に進むための基礎をしっかりと身につけましょう。