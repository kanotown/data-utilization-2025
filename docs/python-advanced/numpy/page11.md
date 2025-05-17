# 11. 乱数の生成と利用

NumPy には乱数を手軽に生成する機能が備わっています。この章では NumPy を用いて乱数を生成し、どのように応用できるかを学びましょう。乱数はシミュレーションやデータの初期化、統計的なサンプリングなどで非常に役立ちます。

## 11.1 乱数生成の基本

NumPy の`numpy.random`モジュールを使用すると、様々な分布から乱数を生成することができます。

### 11.1.1 一様分布からの乱数生成

まずは、一様分布からの乱数を生成してみましょう。一様分布とは、指定した範囲内でどの値も等しく選ばれる分布です。

```python
import numpy as np

# 0以上1未満の一様分布の乱数を生成
random_values = np.random.rand(5)
print("一様分布の乱数:\n", random_values)

# 2以上5未満の範囲で一様分布の乱数を生成
random_integers = np.random.randint(2, 5, size=5)
print("指定範囲の整数乱数:\n", random_integers)
```

### 11.1.2 正規分布からの乱数生成

正規分布も頻繁に使われる分布です。次に、平均 0、標準偏差 1 の正規分布から乱数を生成してみましょう。

```python
# 平均0、標準偏差1の正規分布から5つの乱数を生成
normal_random_values = np.random.randn(5)
print("正規分布の乱数:\n", normal_random_values)
```

## 11.2 再現可能な乱数生成

実験やテストにおいて、同じ乱数を再現可能にしたい場合があるでしょう。そのためには、乱数のシードを設定することができます。

```python
# シードを設定して乱数を生成
np.random.seed(42)
consistent_random_values = np.random.rand(5)
print("再現可能な乱数:\n", consistent_random_values)
```

シード値を設定すると、同じ処理を何度実行しても同じ乱数が生成されるため、実験結果の再現性が得られます。

## 11.3 応用例

乱数生成の知識を応用して、ランダムなデータを使用するシンプルなシミュレーションを行ってみましょう。

### 11.3.1 モンテカルロ法による円周率の近似

ランダムな点を生成し、それを使って円の面積比から円周率を近似するモンテカルロ法を実装します。

```python
import numpy as np

# 点の数
num_points = 10000
np.random.seed(0)

# [0,1)の範囲で乱数を生成
x = np.random.rand(num_points)
y = np.random.rand(num_points)

# 原点からの距離が1以下の点を数える
inside_circle = (x ** 2 + y ** 2) <= 1

# 円周率を近似
pi_approx = (inside_circle.sum() / num_points) * 4
print("円周率の近似値:", pi_approx)
```

このように、乱数を活用することで様々なシミュレーションや計算を行うことができます。以上の内容を自分でも試して理解を深めておきましょう。
