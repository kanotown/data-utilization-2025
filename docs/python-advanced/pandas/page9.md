# 9. データの結合・マージ・連結

データ分析を行う際には、複数のデータセットを組み合わせることが必要になることがよくあります。pandasは、データの結合やマージ、連結を行うための強力な機能を提供しています。この章では、それらの基本操作について学びましょう。

## 9.1 データフレームの結合（merge）

pandasでは、SQLのJOINと同様の操作を行うことができます。`merge`関数を使うことで、2つのDataFrameをキーに基づいて結合することができます。

### 9.1.1 基本的な使い方

```python
import pandas as pd

# サンプルデータ
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value1': [1, 2, 3]
})

df2 = pd.DataFrame({
    'key': ['A', 'B', 'D'],
    'value2': [4, 5, 6]
})

# 結合
result = pd.merge(df1, df2, on='key', how='inner')
print(result)
```

### 9.1.2 結合方法の指定

結合方法には以下の種類があります：

- `inner`（内部結合、共通キーのみ）
- `outer`（外部結合、全てのキー）
- `left`（左外部結合、左のデータフレームを基準）
- `right`（右外部結合、右のデータフレームを基準）

以下は例です：

```python
# 外部結合の例
result_outer = pd.merge(df1, df2, on='key', how='outer')
print(result_outer)
```

## 9.2 データフレームの連結（concat）

複数のDataFrameを上下または左右に連結することができます。

### 9.2.1 縦方向に連結

```python
df3 = pd.DataFrame({
    'key': ['E', 'F'],
    'value1': [7, 8]
})

result_concat = pd.concat([df1, df3], ignore_index=True)
print(result_concat)
```

### 9.2.2 横方向に連結

```python
result_concat_axis1 = pd.concat([df1, df2], axis=1)
print(result_concat_axis1)
```

## 9.3 インデックスを用いた結合

インデックスを用いて結合を行うこともできます。`merge`や`concat`のオプションを使うことで、インデックスをキーとして指定することが可能です。

### 9.3.1 インデックスでの結合

```python
# インデックスを指定した結合
result_index = pd.merge(df1.set_index('key'), df2.set_index('key'), left_index=True, right_index=True, how='inner')
print(result_index)
```

これらの操作を通じて、異なるデータフレームを効果的に結合・マージ・連結するスキルを身につけることができます。それぞれの操作方法は、データ分析の場面で非常に役立つでしょう。ぜひ手を動かして試してみてください。