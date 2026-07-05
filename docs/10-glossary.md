# 10 Glossary — 用語集

## Agent

環境に対して行動を選ぶ主体です。

このリポジトリでは、PPO で学習される方策が Agent の中核です。

## Environment

Agent が相互作用する対象です。

CartPole-v1 では、台車と棒のシミュレーションが Environment です。

## Observation

環境から Agent に渡される情報です。

CartPole では、台車の位置、速度、棒の角度、角速度です。

## Action

Agent が環境に対して行う操作です。

CartPole では、左に押す／右に押すの2種類です。

## Reward

行動の結果として得られる評価値です。

CartPole では、倒れずに1ステップ進むごとに報酬が得られます。

## Policy

観測から行動を決める関数です。

```text
policy(observation) -> action
```

## Value Function

ある状態がどれくらい良いかを推定する関数です。

## Episode

環境を reset してから終了条件に達するまでの1回の試行です。

## Timestep

環境との1回の相互作用です。

```text
action -> env.step(action) -> next observation
```

## PPO

Proximal Policy Optimization の略です。

方策を急激に変えすぎないようにしながら、安定的に改善する強化学習アルゴリズムです。

## Rollout

現在の方策で環境を動かして集めた経験のまとまりです。

## Advantage

ある行動が期待よりどれくらい良かったかを表す値です。

## Inference

学習済みモデルを使って行動を選ぶことです。

評価や動画生成では inference を行います。
