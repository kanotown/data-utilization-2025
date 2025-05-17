# 9. グラフのカスタマイズ（色・ラベル・凡例など）

Seaborn を使ってデータを視覚化する際、グラフのカスタマイズを行うことで、より見やすく、情報を効果的に伝えることができます。この章では、Seaborn で用意されているカスタマイズ方法を説明し、実践的なコード例を使って解説していきます。

## 9.1 色のカスタマイズ

Seaborn では簡単に色を変更することが可能です。適切な色を選ぶことでデータの特徴を際立たせることができます。

### 9.1.1 パレットによる色の設定

Seaborn には様々なカラーパレットが用意されています。`palette`パラメータを利用して設定することができます。

```python
import seaborn as sns
import matplotlib.pyplot as plt

# データセットの読み込み
tips = sns.load_dataset('tips')

# 色を "pastel" パレットに設定
sns.set_palette("pastel")
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day")

plt.title("Scatter plot with Pastel Palette")
plt.show()
```

### 9.1.2 色の指定

カスタムカラーを指定することも可能です。

```python
# カスタムカラーを指定
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", palette={"Thur": "blue", "Fri": "green", "Sat": "red", "Sun": "purple"})

plt.title("Scatter plot with Custom Colors")
plt.show()
```

## 9.2 ラベルのカスタマイズ

グラフには通常、軸のラベルやタイトルを設定することが重要です。これにより、グラフの目的やデータの詳細が一目でわかるようになります。

### 9.2.1 軸ラベルとタイトルの設定

`matplotlib.pyplot`の機能を使って Seaborn プロットにラベルやタイトルを追加できます。

```python
# 軸ラベルとタイトルの設定
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")

plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Total Bill vs. Tip by Time of Day")
plt.show()
```

## 9.3 凡例のカスタマイズ

凡例はデータのカテゴリを区別するのに役立ちます。表現を変えるだけでなく、凡例を削除することもできます。

### 9.3.1 凡例の位置と表示設定

`legend`パラメータや`matplotlib.pyplot`の`legend`関数を使用して、凡例をカスタマイズできます。

```python
# 凡例の位置を設定
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")

plt.legend(title="Meal", loc='upper left', fontsize='small')
plt.title("Scatter plot with Legend Customization")
plt.show()
```

### 9.3.2 凡例の削除

場合によっては、凡例を削除した方がスッキリすることがあります。

```python
# 凡例を削除
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", legend=False)

plt.title("Scatter plot without Legend")
plt.show()
```

これで、Seaborn を用いたグラフのカスタマイズ方法についての解説は終了です。実際にコードを書いて試しながら、全体の見た目や情報の伝え方を調整してみましょう。関心のあるデザインでグラフをカスタマイズすることで、データの印象を大きく変えることができます。
