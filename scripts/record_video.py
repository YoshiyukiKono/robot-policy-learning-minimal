from __future__ import annotations

import argparse
from pathlib import Path

import gymnasium as gym
from gymnasium.wrappers import RecordVideo
from stable_baselines3 import PPO


def main() -> None:
    parser = argparse.ArgumentParser(description="Record a trained policy as video.")
    parser.add_argument("--env-id", default="CartPole-v1")
    parser.add_argument("--model-path", default="outputs/ppo_cartpole.zip")
    parser.add_argument("--video-dir", default="outputs/videos")
    parser.add_argument("--episodes", type=int, default=1)
    args = parser.parse_args()

    Path(args.video_dir).mkdir(parents=True, exist_ok=True)

    env = gym.make(args.env_id, render_mode="rgb_array")
    env = RecordVideo(
        env,
        video_folder=args.video_dir,
        episode_trigger=lambda episode_id: True,
        name_prefix=args.env_id.replace("/", "-").lower(),
    )

    model = PPO.load(args.model_path, env=env)

    for _ in range(args.episodes):
        obs, info = env.reset()
        done = False
        while not done:
            action, _state = model.predict(obs, deterministic=True)
            obs, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated

    env.close()
    print(f"Saved videos under {args.video_dir}")


if __name__ == "__main__":
    main()
