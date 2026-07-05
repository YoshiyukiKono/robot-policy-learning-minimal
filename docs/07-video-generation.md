# 07 Video Generation — 動画生成を理解する

動画生成は、学習済み方策がどのように動くかを人間が確認するための工程です。

実行例は次の通りです。

```bash
python scripts/record_video.py \
  --env-id CartPole-v1 \
  --model-path outputs/ppo_cartpole.zip \
  --video-dir outputs/videos
```

## 動画生成で起きていること

動画生成では、学習済みモデルを使って環境を動かし、その描画結果を保存します。

```text
model.load()
↓
env.reset()
↓
model.predict(observation)
↓
env.step(action)
↓
env.render()
↓
mp4 として保存
```

## 動画生成は学習ではない

動画生成時には、モデルは改善されません。

動画は、結果を確認するための観察手段です。

## outputs/videos の意味

動画は通常、次のようなディレクトリに保存されます。

```text
outputs/videos/
```

ファイル名は Gymnasium の RecordVideo wrapper により生成されます。

## よくある誤解

### 誤解1: 動画を作ると学習が進む

進みません。

動画生成は評価・可視化です。

### 誤解2: 動画が良ければ必ず学習が成功している

1本の動画だけでは判断できません。

複数 episode の評価報酬も確認する必要があります。

### 誤解3: CartPole はロボットではないので意味がない

CartPole は実ロボットではありません。

しかし、観測・方策・行動・報酬・更新という最小構造を理解するには十分に有効です。
