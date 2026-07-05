# Learning Journal — robot-policy-learning-minimal

Date: 2026-07-05
Repository: robot-policy-learning-minimal

## 1. 実行したこと

- Python 仮想環境を作成した
- requirements.txt をインストールした
- random_policy.py を実行した
- train_ppo.py を実行した
- evaluate.py を実行した
- record_video.py で動画を生成した

## 2. 確認できたこと

- Gymnasium 環境が動作した
- PPO 学習が完了した
- 学習済みモデルが `outputs/ppo_cartpole.zip` に保存された
- 動画が `outputs/videos/` に生成された

## 3. 理解したこと

- CartPole は観測・行動・報酬を持つ強化学習環境である
- PPO は方策を少しずつ改善するアルゴリズムである
- 学習と評価は異なる
- 動画生成は学習ではなく、可視化である

## 4. まだ曖昧なこと

- PPO の Advantage 計算
- 方策ネットワークと価値関数の関係
- CartPole と実ロボット制御の距離
- 連続制御環境への拡張

## 5. 次に試すこと

- `total_timesteps` を変えて比較する
- `Pendulum-v1` を試す
- `InvertedPendulum-v5` を試す
- 学習ログを保存する
- 評価結果を表にする
