# 03 Policy — 方策とは何か

方策とは、観測から行動を決める関数です。

```text
policy(observation) -> action
```

CartPole では、観測は4次元の数値ベクトルです。

```text
[x, x_dot, theta, theta_dot]
```

方策は、この観測を受け取り、左に押すか右に押すかを決めます。

## ランダム方策

ランダム方策は、観測を使いません。

```text
Left  or  Right
50%       50%
```

そのため、CartPole はすぐ倒れます。

## 学習済み方策

学習済み方策は、観測に応じて行動を変えます。

例えば、棒が右に倒れそうなら右に押す、というような制御を学びます。

```text
observation
    ↓
MLP neural network
    ↓
action probability
    ↓
action
```

## MlpPolicy とは何か

Stable-Baselines3 の `MlpPolicy` は、多層パーセプトロンを使った方策です。

ここでの MLP は画像モデルではありません。

数値ベクトルを入力し、行動の確率分布や価値を出力します。

## 方策と価値関数

PPO では、方策だけでなく価値関数も使います。

| 要素 | 役割 |
|---|---|
| Policy | どの行動を選ぶか |
| Value Function | 今の状態がどれくらい良いか |

方策は「行動」を決めます。

価値関数は「状態の見込みの良さ」を推定します。

PPO は、この2つを使って方策を改善します。
