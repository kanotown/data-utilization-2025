# 4. 配列の生成と初期化

NumPy を活用する上で、配列の生成と初期化は基本的かつ重要なステップです。このセクションでは、NumPy の配列をどのように生成し、初期化するかについて学習します。皆さんが実際にコードを試すことで、理解を深めましょう。

## 4.1 NumPy 配列の生成

NumPy では、様々な方法で配列を生成することができます。以下に代表的な方法を示します。

### 4.1.1 配列をリストから生成

Python のリストを変換して NumPy 配列を生成します。

```python
import numpy as np

# リストから配列を生成
list_data = [1, 2, 3, 4, 5]
array_from_list = np.array(list_data)

print(array_from_list)
```

### 4.1.2 ゼロで初期化された配列を生成

全ての要素がゼロの配列を生成します。主に初期値が意味を持たないときに使います。

```python
# 5つの要素を持つゼロ初期化された配列
zeros_array = np.zeros(5)

print(zeros_array)
```

### 4.1.3 任意の形状のゼロ配列を生成

任意の形状（dimensions）のゼロ配列を作成することができます。

```python
# 2x3のゼロ行列
zeros_matrix = np.zeros((2, 3))

print(zeros_matrix)
```

### 4.1.4 任意の数で初期化された配列を生成

特定の値で全ての要素を初期化します。

```python
# 4つの要素を持つ配列を7で初期化
filled_array = np.full(4, 7)

print(filled_array)
```

## 4.2 数列を用いた配列の生成

数列を生成するための便利な関数を紹介します。

### 4.2.1 arange()関数で等差数列を生成

`arange()`関数を使って、開始点、終了点、ステップを指定して数列を生成します。

```python
# 0から始まり10未満まで2刻みで増加する配列
seq_array = np.arange(0, 10, 2)

print(seq_array)
```

### 4.2.2 linspace()関数で等間隔な数列を生成

`linspace()`関数を使うと、指定した範囲を等間隔に分割した数値の配列を得ることができます。

```python
# 0から1までを5つに等間隔で分割した配列
linspace_array = np.linspace(0, 1, 5)

print(linspace_array)
```

## 4.3 配列の初期化によく使われる関数

初期化時によく利用される関数について紹介します。

### 4.3.1 ones()関数で 1 の配列を生成

全ての要素が 1 の配列を生成します。

```python
# 3x3の1行列を生成
ones_matrix = np.ones((3, 3))

print(ones_matrix)
```

### 4.3.2 eye()関数で単位行列を生成

単位行列を生成する際に用います。

```python
# 4x4の単位行列
identity_matrix = np.eye(4)

print(identity_matrix)
```

## 4.4 まとめ

配列の生成と初期化に関して、NumPy が提供する便利な方法を学びました。これらの知識は、データ分析や多くの科学技術計算の基礎になりますので、しっかりと理解しておきましょう。皆さんの実践によって、さらに深く理解できることを期待しています。
