# 6. 複数グラフの描画（サブプロット）

Matplotlib では、1 つの(図)の中に複数のグラフ（プロット）を描画することができます。これを「サブプロット」と呼び、異なるデータセットを比較する際に非常に便利です。この章では、サブプロットを用いた複数グラフの描画方法について学びます。

## 6.1 サブプロットの基本

`matplotlib.pyplot` には `subplot()` や `subplots()` 関数が用意されており、簡単にサブプロットを作成することができます。

### 6.1.1 `subplot()` 関数

`subplot()` 関数は、図をグリッド状に分割して複数のプロットを配置します。

```python
import matplotlib.pyplot as plt
import numpy as np

# データ準備
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# サブプロット描画
plt.subplot(2, 1, 1)  # 2行1列目のグリッドの1番目にサイン波をプロット
plt.plot(x, y1)
plt.title('Sine Wave')

plt.subplot(2, 1, 2)  # 2行1列目のグリッドの2番目にコサイン波をプロット
plt.plot(x, y2)
plt.title('Cosine Wave')

plt.tight_layout()
plt.show()
```

### 6.1.2 `subplots()` 関数

`subplots()` 関数を使うと、グリッドを指定して一度にすべてのサブプロットを管理できます。

```python
import matplotlib.pyplot as plt
import numpy as np

# データ準備
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# subplotsでサブプロット用の領域を用意
fig, ax = plt.subplots(2, 1)

# 各サブプロットにプロット
ax[0].plot(x, y1)
ax[0].set_title('Sine Wave')

ax[1].plot(x, y2)
ax[1].set_title('Cosine Wave')

plt.tight_layout()
plt.show()
```

## 6.2 サブプロットのカスタマイズ

サブプロットの形や間隔は簡単に調整することができます。

### 6.2.1 サブプロットのサイズ変更

`subplots()` 関数の引数として `figsize` を指定することで、図全体の大きさを指定できます。

```python
fig, ax = plt.subplots(2, 2, figsize=(10, 5))
```

### 6.2.2 サブプロット間のスペース調整

`plt.tight_layout()` のほかに、`subplots_adjust()` 関数を使って、サブプロット同士の距離を細かく調整できます。

```python
plt.subplots_adjust(hspace=0.5, wspace=0.3)
```

## 6.3 複数のグラフを視覚的に整理する

サブプロットを利用して、異なるデータセットを一つの視点でまとめることができるため、複雑なデータセットを分かりやすく表示する効果的な手段となります。

### 6.3.1 具体的な例

以下に、異なる種類のデータを一つの図にまとめて表示する例を示します。

```python
import matplotlib.pyplot as plt
import numpy as np

# データ準備
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# サブプロット描画
fig, ax = plt.subplots(3, 1, figsize=(8, 10))

ax[0].plot(x, y1)
ax[0].set_title('Sine Wave')

ax[1].plot(x, y2)
ax[1].set_title('Cosine Wave')

ax[2].plot(x, y3)
ax[2].set_ylim(-10, 10)  # タンジェントのプロット範囲制限
ax[2].set_title('Tangent Wave')

plt.tight_layout()
plt.show()
```

これで、複数のグラフを描画するための基本的な方法を理解しました。サブプロットを用いることで、データの理解を効果的に深めることができるでしょう。生徒の皆さんもこれらの方法を自分のデータに応用してみてくださいね。
