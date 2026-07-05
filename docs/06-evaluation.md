# 06 Evaluation — 評価とは何か

評価は、学習済みモデルを使って、どの程度うまく動くかを確認する工程です。

実行例は次の通りです。

```bash
python scripts/evaluate.py \
  --env-id CartPole-v1 \
  --model-path outputs/ppo_cartpole.zip \
  --episodes 5
```

## 評価では学習しない

評価時には、ニューラルネットワークの重みを更新しません。

評価で行うことは、次の通りです。

```text
モデルを読み込む
↓
環境を reset する
↓
observation を受け取る
↓
model.predict(observation) で action を選ぶ
↓
env.step(action) を実行する
↓
episode が終わるまで繰り返す
```

## Training と Evaluation の違い

| 項目 | Training | Evaluation |
|---|---|---|
| 目的 | 方策を改善する | 方策の性能を見る |
| 重み更新 | あり | なし |
| 使用メソッド | `model.learn()` | `model.predict()` |
| 出力 | 学習済みモデル | 報酬・ステップ数 |

## 評価結果の見方

CartPole-v1 では、episode reward が高いほど良いです。

報酬は概ね「倒れずに続いたステップ数」と対応します。

学習前は短い episode で終わることが多く、学習後は最大ステップ近くまで続くようになります。
