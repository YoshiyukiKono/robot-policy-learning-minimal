# 05 Training — 学習スクリプトを理解する

学習スクリプトの役割は、環境を作り、PPO モデルを作り、一定ステップ学習し、モデルを保存することです。

代表的な実行コマンドは次の通りです。

```bash
python scripts/train_ppo.py --config configs/ppo.yaml
```

## 設定ファイル

`configs/ppo.yaml` には、学習に必要な設定が入っています。

典型的には次のような項目です。

```yaml
env_id: CartPole-v1
total_timesteps: 20000
model_path: outputs/ppo_cartpole.zip
```

この設定により、コードを直接書き換えずに実験条件を変更できます。

## 学習で起きていること

学習中、PPO は次のことを繰り返しています。

```text
環境を reset する
↓
現在の方策で action を選ぶ
↓
env.step(action) を実行する
↓
reward を受け取る
↓
経験を保存する
↓
一定量たまったら方策を更新する
```

## total_timesteps の意味

`total_timesteps` は、環境との相互作用回数です。

20,000 timesteps なら、環境で 20,000 回程度のステップを進めます。

これは episode 数ではありません。

## 保存されるモデル

学習が終わると、モデルが保存されます。

```text
outputs/ppo_cartpole.zip
```

この zip には、学習済みニューラルネットワークの重みや設定が含まれます。

動画ではなく、方策そのものです。

## 学習ログの読み方

Stable-Baselines3 は、学習中に次のような情報を出すことがあります。

| 項目 | 意味 |
|---|---|
| ep_rew_mean | 直近 episode の平均報酬 |
| ep_len_mean | 直近 episode の平均長さ |
| fps | 学習速度 |
| total_timesteps | これまでの総ステップ数 |

CartPole では、`ep_rew_mean` が上がれば、倒れずに長く維持できていると考えられます。
