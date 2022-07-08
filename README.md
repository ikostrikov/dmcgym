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
