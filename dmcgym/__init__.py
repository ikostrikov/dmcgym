import gym
from dm_control import suite, manipulation
from gym.envs.registration import register

from dmcgym.env import DMCGYM


def create_dm_control_env(domain_name: str, task_name: str) -> gym.Env:
    env = suite.load(domain_name=domain_name, task_name=task_name)
    return DMCGYM(env)


def create_dm_control_env_manipulation(environment_name: str) -> gym.Env:
    env = manipulation.load(environment_name=environment_name)
    return DMCGYM(env)


create_dm_control_env.metadata = DMCGYM.metadata
create_dm_control_env_manipulation.metadata = DMCGYM.metadata

for (domain_name, task_name) in suite.ALL_TASKS:
    register(id=f"{domain_name}-{task_name}-v0",
             entry_point="dmcgym:create_dm_control_env",
             max_episode_steps=1000,
             kwargs=dict(domain_name=domain_name, task_name=task_name))

for environment_name in manipulation.ALL:
    # only load proprioceptive versions
    if 'features' in environment_name:
        env_name = environment_name[:-(1 + len('features'))]
        register(id=f"{env_name}-v0",
                 entry_point="dmcgym:create_dm_control_env_manipulation",
                 max_episode_steps=1000,
                 kwargs=dict(environment_name=environment_name))
