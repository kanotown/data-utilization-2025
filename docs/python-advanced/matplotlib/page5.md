# 5. グラフのカスタマイズ（色・線種・マーカー）

Matplotlib では、グラフの見た目を様々な方法でカスタマイズすることができます。このセクションでは、グラフをより魅力的に、そして分かりやすくするための色、線種、マーカーの設定方法について学びます。

## 5.1 色のカスタマイズ

グラフの色は、データの視覚的な区別を容易にするために重要です。Matplotlib では、色を柔軟に指定することができます。

### 5.1.1 線の色を指定する

線の色を変更するには、`color`引数を使用します。色は名前、RGB、16 進数などで指定可能です。

```python
import matplotlib.pyplot as plt

# データを定義
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

# グラフを描画
plt.plot(x, y, color='blue')  # 青色のライン
plt.title('Line Graph with Custom Color')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
```

### 5.1.2 複数の線に異なる色を設定する

異なるデータに異なる色を設定することで、視覚的な区別が明確になります。

```python
# 複数のデータを用意
y1 = [0, 1, 2, 3, 4]
y2 = [0, 1, 4, 9, 16]

plt.plot(x, y1, color='green', label='y = x')
plt.plot(x, y2, color='red', label='y = x^2')

plt.title('Multiple Lines with Different Colors')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.show()
```

## 5.2 線種のカスタマイズ

線種は、`linestyle`引数で指定します。通常使う線種には、`'-'`(実線)、`'--'`(破線)、`'-.'`(点線-破線)、`':'`(点線)などがあります。

```python
plt.plot(x, y, color='black', linestyle='--')  # 破線を使用
plt.title('Line Graph with Custom Linestyle')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
```

## 5.3 マーカーのカスタマイズ

データポイントを強調するために、マーカーを使用することができます。マーカーは、`marker`引数で指定します。たとえば、`'o'`(円)、`'s'`(四角)、`'^'`(三角)などがあります。

```python
plt.plot(x, y, color='purple', marker='o', linestyle='-')  # 丸いマーカーを使用
plt.title('Line Graph with Markers')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
```

## 5.4 色、線種、マーカーの組み合わせ

色、線種、マーカーを組み合わせることで、データを視覚的にわかりやすく表現できます。

```python
plt.plot(x, y1, color='blue', linestyle='-', marker='x', label='Linear')
plt.plot(x, y2, color='orange', linestyle='--', marker='s', label='Quadratic')

plt.title('Customized Graph with Colors, Linestyles, and Markers')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.show()
```

ここまでで、Matplotlib を用いたグラフの色、線種、マーカーのカスタマイズについて学びました。これらのテクニックを使いこなすことで、見やすく、情報を伝えるのに効果的なグラフを作成できるようになります。ぜひ自分のデータで試してみてください。
