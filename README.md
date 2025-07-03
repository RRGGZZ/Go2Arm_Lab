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
    git clone https://github.com/zzzJie-Robot/Go2Arm_Lab.git
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


# Go2Arm_Lab  
**A Reinforcement-Learning(RL) Training Framework for Legged Manipulation Robots**  
Built on [IsaacLab v1.4.1](https://isaac-sim.github.io/IsaacLab/v1.4.1)  

<p align="center">
  <img src="https://img.shields.io/badge/IsaacLab-v1.4.1-blue" alt="IsaacLab v1.4.1" />
  <img src="https://img.shields.io/badge/Python-3.10-blue" alt="Python 3.10" />
  <img src="https://img.shields.io/badge/Platform-Linux--64-orange" alt="Linux-64" />
  <img src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" />
</p>

---

## 🚀 Overview  
Go2Arm_Lab enables end-to-end RL training for the **Go2Arm** robot:  
- **Base platform**: Unitree Go2 quadruped  
- **Manipulator**: Interbotix WidowX 250s robotic arm  

> **Version compatibility**  
> Current release targets IsaacLab **v1.4.1**. Support for v2.00+ is planned in a future update.

> **Gazebo deployment**  
> Prefer Gazebo? Use the companion repo:  
> [Go2Arm_sim2sim](https://github.com/zzzJie-Robot/Go2Arm_Lab)  

| IsaacLab Simulation | Gazebo Simulation |
|---------------------|-------------------|
| ![IsaacLab](https://via.placeholder.com/300x150/0a84ff/ffffff?text=IsaacLab) | ![Gazebo](https://via.placeholder.com/300x150/ff6b6b/ffffff?text=Gazebo) |

---

## 📦 Installation  
1. Install IsaacLab v1.4.1 following the [official guide](https://isaac-sim.github.io/IsaacLab/v1.4.1/source/setup/installation/index.html).  
2. Clone this repository into your IsaacLab root (same level as `source/`):

```
git clone https://github.com/zzzJie-Robot/Go2Arm_Lab.git
```


### ⚙️ Training & Inference  

#### Training  
Run distributed RL training in headless mode for maximum throughput:

```
# Activate IsaacLab environment
conda activate your_isaaclab_env

# Navigate to IsaacLab root
cd /path/to/IsaacLab

# Launch training (headless)
isaaclab.sh -p Go2Arm_main/train.py \
            --num_envs 4096 \
            --max_iterations 10000 \
            --headless
```

#### Inference  
Deploy a trained policy in a single environment:

# Activate IsaacLab environment  

```
conda activate your_isaaclab_env
```

# Navigate to IsaacLab root  

```
cd /path/to/IsaacLab

# Run inference
isaaclab.sh -p Go2Arm_main/play.py \
            --num_envs 1
```
