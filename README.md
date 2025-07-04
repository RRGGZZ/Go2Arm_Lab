# Go2Arm_Lab

**A Reinforcement-Learning(RL) Training Framework for Legged Manipulation Robots**
  
<img src="https://img.shields.io/badge/IsaacSim-v4.0.0-blue" alt="IsaacSim-v4.0.0" /> <img src="https://img.shields.io/badge/IsaacLab-v1.4.1-blue" alt="IsaacLab v1.4.1" /> <img src="https://img.shields.io/badge/Python-3.10-blue" alt="Python 3.10" /> <img src="https://img.shields.io/badge/Platform-Linux--64-orange" alt="Linux-64" /> <img src="https://img.shields.io/badge/License-Apache2.0-yellow" alt="Apache2.0T License" />

[中文文档](https://github.com/zzzJie-Robot/Go2Arm_Lab/blob/main/README_CN.md "中文文档")

## 🚀 Overview

Go2Arm_Lab enables RL training for the **Go2Arm** robot:

- **Base platform**: Unitree Go2 quadruped
- **Manipulator**: Interbotix WidowX 250s robotic arm

> **Version compatibility**  
> Current release targets [IsaacLab v1.4.1](https://isaac-sim.github.io/IsaacLab/v1.4.1). Support for v2.00+ is planned in a future update.

> **Gazebo deployment**  
> If you want to deploy your policy in Gazebo, please use:
> [Go2Arm_sim2sim](https://github.com/zzzJie-Robot/Go2Arm_sim2sim)

| IsaacLab Simulation | Gazebo Simulation |
|--------------------|-------------------|
| ![Gazebo](https://github.com/zzzJie-Robot/Go2Arm_Lab/raw/main/video/IsaacLab.gif) | ![Gazebo](https://github.com/zzzJie-Robot/Go2Arm_Lab/raw/main/video/Gazebo.gif) |

For **more videos**, please visit my [Bilibili homepage](https://space.bilibili.com/400627082?spm_id_from=333.1007.0.0).

## 📦 Installation

1. Install IsaacLab v1.4.1 following the [official guide](https://isaac-sim.github.io/IsaacLab/v1.4.1/source/setup/installation/index.html).
2. Clone this repository into your IsaacLab root (same level as `source/`):

```
cd /path/to/IsaacLab
git clone https://github.com/zzzJie-Robot/Go2Arm_Lab.git
```

### ⚙️ Training & Inference

#### Training

Run reinforcement learning training in headless mode to improve training efficiency:

```
# Activate IsaacLab environment
conda activate your_isaaclab_env

# Navigate to IsaacLab root
cd /path/to/IsaacLab

# Launch training (headless)
isaaclab.sh -p Go2Arm_main/train.py --num_envs 4096  --max_iterations 10000 --headless
```

#### Inference

Deploy a trained policy in a single environment:

```
# Activate IsaacLab environment  
conda activate your_isaaclab_env

# Navigate to IsaacLab root  
cd /path/to/IsaacLab

# Run inference
isaaclab.sh -p Go2Arm_main/play.py --num_envs 1
```

## 🙏 Acknowledgments  
The RL algorithm implementation in this project references the [Deep-Whole-Body-Control](https://github.com/MarkFzp/Deep-Whole-Body-Control) project, for which we extend our sincere gratitude.
