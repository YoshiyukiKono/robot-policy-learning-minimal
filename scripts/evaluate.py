from __future__ import annotations

import argparse

import gymnasium as gym
from stable_baselines3 import PPO


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate a trained PPO policy.")
    parser.add_argument("--env-id", default="CartPole-v1")
    parser.add_argument("--model-path", default="outputs/ppo_cartpole.zip")
    parser.add_argument("--episodes", type=int, default=5)
    parser.add_argument("--render", action="store_true")
    args = parser.parse_args()

    render_mode = "human" if args.render else None
    env = gym.make(args.env_id, render_mode=render_mode)
    model = PPO.load(args.model_path, env=env)

    rewards: list[float] = []
    for episode in range(args.episodes):
        obs, info = env.reset()
        done = False
        total_reward = 0.0
        steps = 0

        while not done:
            action, _state = model.predict(obs, deterministic=True)
            obs, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated
            total_reward += float(reward)
            steps += 1

        rewards.append(total_reward)
        print(f"episode={episode + 1} steps={steps} reward={total_reward:.2f}")

    env.close()
    avg = sum(rewards) / len(rewards)
    print(f"average_reward={avg:.2f}")


if __name__ == "__main__":
    main()
