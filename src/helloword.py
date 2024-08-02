import gymnasium as gym

ENV_NAME = 'CartPole-v1'
if __name__ == '__main__':
    env = gym.make(ENV_NAME, render_mode="human")
    for i_episode in range(20):  # run 20 episodes
        observation = env.reset()
        for t in range(1000):
            env.render()
            action = env.action_space.sample()
            observation, reward, terminated, truncated, info = env.step(action)
            if terminated or truncated:
                print("Episode finished after {} timesteps".format(t + 1))
                break
    env.close()
