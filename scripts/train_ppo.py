from __future__ import annotations

import argparse
from pathlib import Path

import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.utils import set_random_seed

from common import ensure_parent, load_config


def main() -> None:
    parser = argparse.ArgumentParser(description="Train a PPO policy with Stable-Baselines3.")
    parser.add_argument("--config", default="configs/ppo.yaml")
    args = parser.parse_args()

    cfg = load_config(args.config)
    env_id = cfg.get("env_id", "CartPole-v1")
    seed = int(cfg.get("seed", 42))
    total_timesteps = int(cfg.get("total_timesteps", 20_000))
    model_path = cfg.get("model_path", "outputs/ppo_model.zip")
    log_dir = cfg.get("log_dir", "outputs/logs")
    ppo_cfg = cfg.get("ppo", {})

    Path(log_dir).mkdir(parents=True, exist_ok=True)
    ensure_parent(model_path)
    set_random_seed(seed)

    env = Monitor(gym.make(env_id), filename=str(Path(log_dir) / "monitor.csv"))
    env.reset(seed=seed)

    model = PPO(
        policy="MlpPolicy",
        env=env,
        verbose=1,
        tensorboard_log=log_dir,
        seed=seed,
        **ppo_cfg,
    )
    model.learn(total_timesteps=total_timesteps)
    model.save(model_path)
    env.close()

    print(f"Saved model to {model_path}")


if __name__ == "__main__":
    main()
