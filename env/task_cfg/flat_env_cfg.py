# Copyright (c) 2025-2026 Junjie Zhu
# SPDX-License-Identifier: Apache-2.0

from omni.isaac.lab.utils import configclass


from ..agent_env.manager_env_cfg import LocomotionVelocityRoughEnvCfg

##
# Pre-defined configs
##

from ..usd_model.go2arm_articulation_cfg import UNITREE_GO2ARM_CFG  # isort: skip


@configclass
class UnitreeGo2ARMFlatEnvCfg(LocomotionVelocityRoughEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()
        self.scene.robot = UNITREE_GO2ARM_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")

        # no terrain curriculum
        self.curriculum.terrain_levels = None

        self.scene.terrain.terrain_type = "plane"
        self.scene.terrain.terrain_generator = None

class UnitreeGo2ARMFlatEnvCfg_PLAY(UnitreeGo2ARMFlatEnvCfg):
    def __post_init__(self) -> None:
        # post init of parent
        super().__post_init__()

        # make a smaller scene for play
        self.scene.num_envs = 50
        self.scene.env_spacing = 2.5
        # disable randomization for play
        self.observations.policy.enable_corruption = False
        # remove random pushing event
        self.events.base_external_force_torque = None
        self.events.push_robot = None
        # self.events.reset_base = None
        self.commands.ee_pose.is_Go2ARM = False
        self.commands.base_velocity.is_Go2ARM = False
        self.commands.ee_pose.is_Go2ARM_Play = True
        
        # self.commands.base_velocity.resampling_time_range = (5.0,10.5)
        # self.commands.base_velocity.rel_standing_envs = 0.2
        # self.commands.base_velocity.ranges.ang_vel_z = (0.0, 0.0)
        # self.commands.base_velocity.ranges.lin_vel_y = (-0.0, 0.0)
       
        # self.commands.ee_pose.resampling_time_range = (2.0,5.0)
        # self.commands.ee_pose.ranges.pos_x = (0.45, 0.45)
        # self.commands.ee_pose.ranges.pos_y = (0.0, 0.0)
        # self.commands.ee_pose.ranges.pos_z = (0.3, 0.3)