# 08 Code Walkthrough — コード全体を読む

この章では、リポジトリのファイルを教育的に読みます。

## ディレクトリ構成

```text
robot-policy-learning-minimal/
├── README.md
├── requirements.txt
├── configs/
│   └── ppo.yaml
├── scripts/
│   ├── random_policy.py
│   ├── train_ppo.py
│   ├── evaluate.py
│   └── record_video.py
└── outputs/
    ├── ppo_cartpole.zip
    └── videos/
```

## README.md

README は、最短で動かすための入口です。

教育用ドキュメントを追加した後は、README は「5分で動かす」ことに集中させるとよいです。

## requirements.txt

必要な Python パッケージを定義します。

代表的には以下が含まれます。

```text
gymnasium
stable-baselines3
pyyaml
moviepy
```

## configs/ppo.yaml

PPO の設定を外部化するファイルです。

コードを変えずに、環境や学習ステップ数、保存先を変更できます。

## scripts/random_policy.py

ランダム方策を実行します。

このスクリプトの目的は、学習ではなく、環境が動くことを確認することです。

## scripts/train_ppo.py

PPO を学習します。

重要な処理は次の3つです。

```python
env = gym.make(env_id)
model = PPO("MlpPolicy", env, ...)
model.learn(total_timesteps=total_timesteps)
```

## scripts/evaluate.py

保存済みモデルを読み込み、複数 episode で性能を確認します。

```python
model = PPO.load(model_path)
action, _ = model.predict(observation)
```

## scripts/record_video.py

保存済みモデルを読み込み、環境の描画を動画に保存します。

動画生成は、学習済み方策のふるまいを人間が目で確認するためのものです。

## outputs/

`outputs/` は生成物を置く場所です。

| ファイル | 意味 |
|---|---|
| `ppo_cartpole.zip` | 学習済みモデル |
| `videos/` | 動画出力先 |

`outputs/` は Git で管理しない方がよい場合が多いです。
