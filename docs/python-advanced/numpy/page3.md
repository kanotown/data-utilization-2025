# 3. NumPy 配列（ndarray）の基礎

NumPy の配列（ndarray）はデータを効率よく扱うための強力なツールです。このセクションでは、ndarray の基本概念と操作方法について学びます。

## 3.1 ndarray の特徴

### 3.1.1 固定サイズの配列

NumPy の ndarray は、固定サイズの多次元配列です。全ての要素は同じデータ型で格納されます。

### 3.1.2 メモリ効率

ndarray は C の配列に似たメモリ効率の良い方法でデータを格納し、高速演算が可能です。

## 3.2 ndarray の基本操作

### 3.2.1 ndarray の作成

最も基本的な方法はリストから配列を作成することです。

```python
import numpy as np

# リストからndarrayを作成
array1 = np.array([1, 2, 3, 4, 5])
print(array1)
```

### 3.2.2 ndarray の型確認と型変換

```python
# 配列のデータ型を確認
print(array1.dtype)

# データ型を浮動小数点に変換
array2 = np.array([1, 2, 3, 4, 5], dtype=float)
print(array2)
```

### 3.2.3 ndarray の次元と形状の確認

```python
# 次元数を確認
print(array1.ndim)

# 形状を確認
print(array1.shape)
```

## 3.3 ndarray の基本的なプロパティ

### 3.3.1 配列のサイズと要素数

ndarray 自体が持つ要素数やメモリの大きさを簡単に確認できます。

```python
# 要素の総数を確認
print(array1.size)

# 配列のメモリバイト数を確認
print(array1.nbytes)
```

### 3.3.2 インデックスを使用した要素のアクセス

配列の要素にインデックスを使用してアクセスできます。

```python
# 特定の要素へのアクセス
print(array1[0])  # 1番目の要素

# スライスを使ったアクセス
print(array1[1:4])  # 2番目から4番目の要素
```

### 3.3.3 Boolean インデックスを使った操作

特定の条件に基づいた要素を簡単に取得できます。

```python
# 偶数の要素を取得
even_elements = array1[array1 % 2 == 0]
print(even_elements)
```

このパートでは、NumPy の ndarray の基礎について学びました。これにより、配列を使ったデータ操作の基本が身についたはずです。次の章以降で、さらに配列を応用した高度な操作方法を学んでいきましょう。
