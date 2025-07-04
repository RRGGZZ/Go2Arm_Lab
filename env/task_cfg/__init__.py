# Copyright (c) 2025-2026 Junjie Zhu
# SPDX-License-Identifier: Apache-2.0

import gymnasium as gym

from . import flat_env_cfg, rough_env_cfg
from . import rsl_rl_ppo_cfg

##
# Register Gym environments.
##

gym.register(
    id="Isaac-Flat-Go2Arm",
    entry_point="env.agent_env.manager_env:ManagerRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": flat_env_cfg.UnitreeGo2ARMFlatEnvCfg,
        "rsl_rl_cfg_entry_point": rsl_rl_ppo_cfg.Go2ArmFlatPPORunnerCfg,
    },
)

gym.register(
    id="Isaac-Flat-Go2Arm-Play",
    entry_point="env.agent_env.manager_env:ManagerRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": flat_env_cfg.UnitreeGo2ARMFlatEnvCfg_PLAY,
        "rsl_rl_cfg_entry_point": rsl_rl_ppo_cfg.Go2ArmFlatPPORunnerCfg,
    },
)

gym.register(
    id="Isaac-Rough-Go2Arm",
    entry_point="env.agent_env.manager_env:ManagerRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": rough_env_cfg.UnitreeGo2ARMRoughEnvCfg,
        "rsl_rl_cfg_entry_point": rsl_rl_ppo_cfg.Go2ArmRoughPPORunnerCfg,
    },
)

gym.register(
    id="Isaac-Rough-Go2Arm-Play",
    entry_point="env.agent_env.manager_env:ManagerRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": rough_env_cfg.UnitreeGo2ARMRoughEnvCfg_PLAY,
        "rsl_rl_cfg_entry_point": rsl_rl_ppo_cfg.Go2ArmRoughPPORunnerCfg,
    },
)