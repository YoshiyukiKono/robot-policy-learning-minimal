# 02 Environment — CartPole 環境を理解する

CartPole は、台車の上に棒が立っている環境です。

目的は、台車を左右に動かしながら、棒を倒さないようにすることです。

## 環境とは何か

強化学習における環境とは、エージェントが行動を与える対象です。

環境は、行動を受け取ると、次の情報を返します。

```text
observation, reward, terminated, truncated, info
```

Gymnasium では典型的に次のように使います。

```python
observation, info = env.reset()
observation, reward, terminated, truncated, info = env.step(action)
```

## CartPole の観測

CartPole-v1 の観測は4次元です。

| 要素 | 意味 |
|---|---|
| cart position | 台車の位置 |
| cart velocity | 台車の速度 |
| pole angle | 棒の角度 |
| pole angular velocity | 棒の角速度 |

つまり、方策は画像を見ているわけではありません。

数値ベクトルを見ています。

```text
observation = [x, x_dot, theta, theta_dot]
```

## CartPole の行動

CartPole-v1 の行動は2種類です。

| action | 意味 |
|---|---|
| 0 | 左に押す |
| 1 | 右に押す |

これは離散行動空間です。

一方で、Pendulum や MuJoCo の多くの環境では、連続値の行動を使います。

## 報酬

CartPole では、基本的に棒が倒れずに1ステップ進むたびに報酬が入ります。

```text
1 step 生き残るごとに +1
```

したがって、長く倒れない方策ほど高い報酬を得ます。

## Episode

Episode とは、1回の試行です。

CartPole では、次のような条件で episode が終わります。

- 棒が大きく傾く
- 台車が範囲外に出る
- 最大ステップ数に達する

学習前はすぐに倒れます。

学習後は、長くバランスを保てるようになります。
