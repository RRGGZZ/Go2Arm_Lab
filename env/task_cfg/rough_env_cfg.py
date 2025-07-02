from omni.isaac.lab.utils import configclass

from ..agent_env.manager_env_cfg import LocomotionVelocityRoughEnvCfg

##
# Pre-defined configs
##
from ..usd_model.go2arm_articulation_cfg import UNITREE_GO2ARM_CFG  # isort: skip

@configclass
class UnitreeGo2ARMRoughEnvCfg(LocomotionVelocityRoughEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()

        self.scene.robot = UNITREE_GO2ARM_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")
        # # event
        self.events.push_robot = None #type :ignore

        self.events.reset_robot_joints.params["position_range"] = (1.0, 1.0)


@configclass
class UnitreeGo2ARMRoughEnvCfg_PLAY(UnitreeGo2ARMRoughEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()

        # make a smaller scene for play
        self.scene.num_envs = 50
        self.scene.env_spacing = 2.5
        # spawn the robot randomly in the grid (instead of their terrain levels)
        self.scene.terrain.max_init_terrain_level = None
        # reduce the number of terrains to save memory
        if self.scene.terrain.terrain_generator is not None:
            self.scene.terrain.terrain_generator.num_rows = 5
            self.scene.terrain.terrain_generator.num_cols = 5
            self.scene.terrain.terrain_generator.curriculum = False

        # disable randomization for play
        self.observations.policy.enable_corruption = False
        # remove random pushing event
        self.events.base_external_force_torque = None
        self.events.push_robot = None
