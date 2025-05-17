# 6. 配列の形状操作（reshape, flatten など）

NumPy配列は、その形状（サイズや次元）を柔軟に操作することが可能です。この章では、配列の形状を操作する基本技術を学びます。これらの操作は、データの整形や解析において非常に役立ちます。

## 6.1 配列のshape属性

NumPy配列の`shape`属性を使えば、配列の形状を確認できます。また、配列の形状を変更する際の目安ともなります。

```python
import numpy as np

# 3x4の配列を作成
array = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8], 
                  [9, 10, 11, 12]])

# 配列の形状を確認
print("Original shape:", array.shape)
```

## 6.2 reshapeによる形状変更

`reshape`メソッドを使うと、配列の要素数を変えずに形状を変更できます。

```python
import numpy as np

# 3x4の配列を1x12に変形
reshaped_array = array.reshape(1, 12)
print("Reshaped to 1x12:")
print(reshaped_array)

# 2x6に再度変形
reshaped_array = array.reshape(2, 6)
print("Reshaped to 2x6:")
print(reshaped_array)
```

## 6.3 flattenによる一次元化

`flatten`メソッドを使うと、配列を一次元に平坦化できます。これは、データの簡単な処理や保存に便利です。

```python
# 配列を一次元に平坦化
flattened = array.flatten()
print("Flattened array:")
print(flattened)
```

## 6.4 その他の形状変更操作

### 6.4.1 ravelメソッド

`ravel`メソッドも配列を一次元にしますが、オリジナルのデータとのリンクを保持する場合があります。

```python
# ravelによる一次元化
raveled = array.ravel()
print("Raveled array:")
print(raveled)
```

### 6.4.2 newaxisによる次元追加

新たに次元を追加して配列を拡張することも可能です。

```python
# newaxisを使って次元を追加
expanded = array[:, np.newaxis, :]
print("Expanded array shape:", expanded.shape)
```

## 6.5 実際に試してみよう

皆さんもぜひ上記のコードを実行してみてください。試行錯誤を通じて、配列の形状操作を直感的に理解できるようになることを目指しましょう。実際に手を動かすことが習得への一番の近道です。