from __future__ import annotations

import argparse

import gymnasium as gym


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a random policy in a Gymnasium environment.")
    parser.add_argument("--env-id", default="CartPole-v1")
    parser.add_argument("--episodes", type=int, default=3)
    parser.add_argument("--render", action="store_true", help="Render to a window if supported.")
    args = parser.parse_args()

    render_mode = "human" if args.render else None
    env = gym.make(args.env_id, render_mode=render_mode)

    for episode in range(args.episodes):
        obs, info = env.reset()
        done = False
        total_reward = 0.0
        steps = 0

        while not done:
            action = env.action_space.sample()
            obs, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated
            total_reward += float(reward)
            steps += 1

        print(f"episode={episode + 1} steps={steps} reward={total_reward:.2f}")

    env.close()


if __name__ == "__main__":
    main()
