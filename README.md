# dmcgym

A fork of [dmc2gym](https://github.com/denisyarats/dmc2gym) refactored to remove parts implemented in other gym wrappers and add support for interactive rendering.

## Installation

```bash
pip install git+https://github.com/ikostrikov/dmcgym.git
```

## Usage
```python
import gym
import dmcgym

env = gym.make('cheetah-run-v0')
```

### Manipulation Tasks
For manipulation tasks, only `features` versions are loaded. To get pixel observations, please call a pixel wrapper, such as [`PixelObservationWrapper`](https://github.com/openai/gym/blob/1061949d0ca951518275f7fd5944ca52e3af8b9d/gym/wrappers/pixel_observation.py#L15).

To load a manipulation task, specify the environment as follows: `env = gym.make('reach_duplo-v0')`.
