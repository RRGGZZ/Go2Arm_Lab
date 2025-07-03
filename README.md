# Go2Arm_Lab
## Overview

[中文文档](https://github.com/zzzJie-Robot/Go2Arm_Lab/blob/main/README_CN.md "中文文档")  

Go2Arm_Lab is a reinforcement learning training framework for legged manipulation robots based on the IsaacLab platform.

Go2Arm consists of a Unitree Go2 quadruped robot + an Interbotix WidowX 250s robotic arm.

> Version  
> This framework is compatible with IsaacLab v1.4.1. Support for v2.00 and above will be updated in the future.

> Recommendation  
> If you want to deploy policies in Gazebo, please use [Go2Arm_sim2sim](https://github.com/zzzJie-Robot/Go2Arm_Lab "Go2Arm_sim2sim").

| IsaacLab  | Gazebo |
| ---------- | ----------- |
| Image   | Image   |

## Installation
Follow the installation guide to install IsaacLab v1.4.1: [IsaacLab v1.4.1](https://isaac-sim.github.io/IsaacLab/v1.4.1/source/setup/installation/index.html "IsaacLab").

Install the Go2Arm_Lab environment:
* Clone or copy this repository into the Isaac Lab installation directory, at the same level as the `source` folder.
    ```
    git clone xxx
    ```

## Training and Inference
* You can train Go2Arm using the following command:

    ```
    conda activate your_isaaclab_env
    cd /your_path/IsaacLab
    isaaclab.sh -p /Go2Arm_main/train.py --num_envs 4096 --max_iterations 10000 --headless
    ```
    Here, `headless` indicates headless mode, which closes the IsaacSim window and significantly improves training efficiency.

* You can use the following command to run inference with a trained agent:

    ```
    conda activate your_isaaclab_env
    cd /your_path/IsaacLab
    isaaclab.sh -p /Go2Arm_main/play.py --num_envs 1
    ```
