# robot-policy-learning-minimal

A minimal starter repository for robot / embodied-agent learning.

The goal is to run the smallest practical loop:

```text
observation -> policy -> action -> reward -> update
```

This repository starts with Gymnasium classic-control environments and Stable-Baselines3 PPO.  
After the basic loop works, you can move to MuJoCo environments such as `InvertedPendulum-v5`, `Reacher-v5`, or richer robotics stacks.

## What this repository includes

- Random policy execution
- PPO training
- PPO evaluation
- Video recording
- YAML config
- Minimal directory layout for future expansion

## What this repository intentionally avoids

- ROS 2
- Real robot control
- Isaac Sim / Isaac Lab
- Vision-language-action models
- Imitation learning
- Distributed training

Those are important, but not a good first step.

## Setup

Python 3.10 or newer is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

## 1. Run a random policy

```bash
python scripts/random_policy.py --env-id CartPole-v1 --episodes 3
```

Expected output:

```text
episode=1 steps=... reward=...
episode=2 steps=... reward=...
episode=3 steps=... reward=...
```

This confirms that Gymnasium is working.

## 2. Train PPO

```bash
python scripts/train_ppo.py --config configs/ppo.yaml
```

The default config trains `CartPole-v1` for 20,000 timesteps and saves:

```text
outputs/ppo_cartpole.zip
```

## 3. Evaluate the trained policy

```bash
python scripts/evaluate.py \
  --env-id CartPole-v1 \
  --model-path outputs/ppo_cartpole.zip \
  --episodes 5
```

## 4. Record a video

```bash
python scripts/record_video.py \
  --env-id CartPole-v1 \
  --model-path outputs/ppo_cartpole.zip \
  --video-dir outputs/videos
```

The video will be saved under:

```text
outputs/videos/
```

## Try a continuous-control environment

Edit `configs/ppo.yaml`:

```yaml
env_id: Pendulum-v1
model_path: outputs/ppo_pendulum.zip
```

Then run:

```bash
python scripts/train_ppo.py --config configs/ppo.yaml
python scripts/evaluate.py --env-id Pendulum-v1 --model-path outputs/ppo_pendulum.zip
```

## Try MuJoCo

The requirements include `gymnasium[mujoco]`, so you can try:

```bash
python scripts/random_policy.py --env-id InvertedPendulum-v5 --episodes 3
```

Or edit the config:

```yaml
env_id: InvertedPendulum-v5
model_path: outputs/ppo_inverted_pendulum.zip
```

Then train:

```bash
python scripts/train_ppo.py --config configs/ppo.yaml
```

## Concept map

```text
LLM post-training minimal:
  prompt -> model -> response -> preference/eval

Robot policy learning minimal:
  observation -> policy -> action -> reward
```

## Suggested next steps

Once this works, extend in this order:

1. Add more Gymnasium environments
2. Add MuJoCo continuous-control tasks
3. Add imitation learning from demonstration data
4. Add vision observations
5. Move to ManiSkill or Isaac Lab
6. Add ROS 2 only when you are ready to touch real robot conventions
```
