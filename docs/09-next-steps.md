# 09 Next Steps — 次に進む方向

CartPole で最小ループを理解したら、次は段階的に複雑さを上げます。

## Step 1: 他の Gymnasium 環境を試す

まずは Gymnasium の classic-control 環境を試します。

- CartPole-v1
- Pendulum-v1
- Acrobot-v1
- MountainCar-v0

CartPole は離散行動です。

Pendulum は連続行動です。

この違いは、ロボット制御に進むうえで重要です。

## Step 2: MuJoCo 環境に進む

MuJoCo では、よりロボット制御に近い環境を扱えます。

- InvertedPendulum-v5
- Reacher-v5
- Hopper-v5
- HalfCheetah-v5

ここでは、関節、トルク、物理シミュレーションがより重要になります。

## Step 3: 模倣学習を学ぶ

強化学習だけでなく、デモデータから学ぶ方法も重要です。

代表例は Behavior Cloning です。

```text
human/expert demonstration
↓
observation-action pairs
↓
supervised learning
↓
policy
```

## Step 4: 視覚入力を扱う

CartPole では数値ベクトルを観測として使いました。

実ロボットでは、カメラ画像が重要になります。

```text
image
↓
CNN / Vision Transformer
↓
policy
↓
action
```

## Step 5: Diffusion Policy / VLA に進む

近年のロボット学習では、次のような方向が重要です。

- Diffusion Policy
- Transformer policy
- Vision-Language-Action model
- World model

ただし、これらを理解するためにも、最小ループの理解が先に必要です。

## 学習の順番

おすすめの順番は次の通りです。

```text
CartPole PPO
↓
Pendulum PPO
↓
MuJoCo Reacher
↓
Behavior Cloning
↓
Vision-based Policy
↓
Diffusion Policy
↓
VLA / Physical AI
```
