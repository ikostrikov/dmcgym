import gym
from dm_control import suite
from gym.envs.registration import register

from dmcgym.env import DMCGYM


def create_dm_control_env(domain_name: str, task_name: str) -> gym.Env:
    env = suite.load(domain_name=domain_name, task_name=task_name)
    return DMCGYM(env)


create_dm_control_env.metadata = DMCGYM.metadata

for (domain_name, task_name) in suite.ALL_TASKS:
    register(id=f"{domain_name}-{task_name}-v0",
             entry_point="dmcgym:create_dm_control_env",
             max_episode_steps=1000,
             kwargs=dict(domain_name=domain_name, task_name=task_name))
