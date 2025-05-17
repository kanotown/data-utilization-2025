# 12. NumPy 配列と Python 標準リストの違い

NumPy 配列（ndarray）と Python の標準リスト（list）はどちらも複数の要素を扱うためのデータ構造ですが、それらには重要な違いがあります。この章では、NumPy 配列と標準リストの違いを理解し、最適なデータ構造を選択できるようにするためのポイントを紹介します。

## 12.1 データのタイプと一貫性

### 12.1.1 NumPy 配列

NumPy 配列は同じデータ型（例えばすべて整数、すべて浮動小数点数など）の要素を格納します。これにより、計算が効率的に行われます。

```python
import numpy as np

# 整数型のNumPy配列を作成
numpy_array = np.array([1, 2, 3, 4])
print(numpy_array.dtype)  # 出力: int64
```

### 12.1.2 Python 標準リスト

Python の標準リストは、異なるデータ型の要素を持つことができます。

```python
# 異なるデータ型が混在したリスト
python_list = [1, 2.5, 'three', [4, 5]]
print(type(python_list[0]))  # 出力: <class 'int'>
print(type(python_list[1]))  # 出力: <class 'float'>
print(type(python_list[2]))  # 出力: <class 'str'>
```

## 12.2 メモリとパフォーマンス

### 12.2.1 NumPy 配列の効率性

NumPy 配列は、データがメモリ上に連続して格納されるため、要素の更新や数値計算が高速です。

```python
import numpy as np

# 大きな配列を作成して要素を一括更新
large_array = np.arange(1000000)
large_array *= 2
```

### 12.2.2 Python 標準リストの柔軟性

Python のリストは内部的にポインタの集合であり、要素への直接アクセスは遅くなりますが、要素の追加や削除がしやすいです。

```python
# 要素の追加
python_list = [1, 2, 3]
python_list.append(4)

# 要素の削除
del python_list[0]
```

## 12.3 要素の操作

### 12.3.1 ベクトル演算

NumPy はベクトル演算をサポートし、効率的に大規模な計算を行うことができます。

```python
import numpy as np

array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])

# 要素ごとの加算
result = array_a + array_b
print(result)  # 出力: [5 7 9]
```

### 12.3.2 リストのループによる操作

Python のリストでは、ループを使って要素を一つずつ処理する必要があります。

```python
python_list_a = [1, 2, 3]
python_list_b = [4, 5, 6]

# 要素ごとの加算
result_list = [a + b for a, b in zip(python_list_a, python_list_b)]
print(result_list)  # 出力: [5, 7, 9]
```

## 12.4 総括

NumPy 配列は数値計算に特化しており、一様なデータ型で大量のデータを効率的に処理するのに向いています。一方、Python 標準リストは異種データ型を扱う柔軟性があります。特定の用途に合わせて、どちらのデータ構造を用いるべきかを判断するために、これらの違いを理解しておくことが重要です。
