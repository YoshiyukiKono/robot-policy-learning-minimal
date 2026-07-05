# Exercises — 演習

この演習は、リポジトリを「動かした」状態から「理解した」状態へ進むためのものです。

## Exercise 1: total_timesteps を変える

`configs/ppo.yaml` の `total_timesteps` を変えて、学習結果を比較してください。

例:

```yaml
total_timesteps: 5000
```

```yaml
total_timesteps: 20000
```

```yaml
total_timesteps: 100000
```

観察する点:

- 評価報酬は上がるか
- 動画の安定性は変わるか
- 学習時間はどれくらい増えるか

## Exercise 2: ランダム方策と学習済み方策を比較する

次の2つを比較してください。

```bash
python scripts/random_policy.py --env-id CartPole-v1 --episodes 5
```

```bash
python scripts/evaluate.py --env-id CartPole-v1 --model-path outputs/ppo_cartpole.zip --episodes 5
```

考える点:

- 報酬はどれくらい違うか
- ランダム方策はなぜすぐ倒れるのか
- 学習済み方策は何を利用しているのか

## Exercise 3: Pendulum-v1 を試す

`configs/ppo.yaml` を変更します。

```yaml
env_id: Pendulum-v1
model_path: outputs/ppo_pendulum.zip
```

実行:

```bash
python scripts/train_ppo.py --config configs/ppo.yaml
python scripts/evaluate.py --env-id Pendulum-v1 --model-path outputs/ppo_pendulum.zip --episodes 5
```

考える点:

- CartPole と Pendulum の action space は何が違うか
- 報酬の意味はどう違うか

## Exercise 4: 評価 episode 数を変える

```bash
python scripts/evaluate.py --env-id CartPole-v1 --model-path outputs/ppo_cartpole.zip --episodes 1
python scripts/evaluate.py --env-id CartPole-v1 --model-path outputs/ppo_cartpole.zip --episodes 20
```

考える点:

- 1 episode だけで性能を判断してよいか
- 平均を見る意味は何か

## Exercise 5: 動画と数値評価を比較する

動画だけでなく、評価報酬も見てください。

考える点:

- 見た目では良さそうでも、報酬は低いことがあるか
- 逆に、報酬は高いが人間には不自然に見えることがあるか
