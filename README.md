# Go2Arm_Lab

**A Reinforcement-Learning(RL) Training Framework for Legged Manipulation Robots**
  
<img src="https://img.shields.io/badge/IsaacSim-v4.5.0-blue" alt="IsaacSim-v4.5.0" /> <img src="https://img.shields.io/badge/IsaacLab-v2.1.0-blue" alt="IsaacLab v2.1.0" /> <img src="https://img.shields.io/badge/Python-3.10-blue" alt="Python 3.10" /> <img src="https://img.shields.io/badge/Platform-Linux--64-orange" alt="Linux-64" /> <img src="https://img.shields.io/badge/License-Apache2.0-yellow" alt="Apache2.0T License" />

[中文文档](https://github.com/zzzJie-Robot/Go2Arm_Lab/blob/main/README_CN.md "中文文档")

## 🚀 Overview

Go2Arm_Lab enables RL training for the **Go2Arm** robot:

- **Base platform**: Unitree Go2 quadruped
- **Manipulator**: Interbotix WidowX 250s robotic arm

> **Version compatibility**  
> This repository currently depends on **IsaacLab v2.1.0**.  
> The repository can also run on **IsaacLab v2.2.0**.
> For IsaacLab v1.4.1, please use the [v1.4.1](https://github.com/zzzJie-Robot/Go2Arm_Lab) version of this repository.

> **Gazebo deployment**  
> If you want to deploy your policy in Gazebo, please use:
> [Go2Arm_sim2sim](https://github.com/zzzJie-Robot/Go2Arm_sim2sim)

| IsaacLab Simulation (v2.1) | Gazebo Simulation |
|--------------------|-------------------|
| ![Gazebo](https://github.com/zzzJie-Robot/Go2Arm_Lab/raw/main/video/IsaacLab.gif) | ![Gazebo](https://github.com/zzzJie-Robot/Go2Arm_Lab/raw/main/video/Gazebo.gif) |

For **more videos**, please visit my [Bilibili homepage](https://space.bilibili.com/400627082?spm_id_from=333.1007.0.0).

## 📦 Installation

1. Follow the [official guide](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/index.html) to install IsaacLab v2.1.0.  
2. Clone this repository into the same directory as IsaacLab:
   ```
   git clone https://github.com/zzzJie-Robot/Go2Arm_Lab.git
   ```
3. Install the package using the Python interpreter that IsaacLab uses:
   ```
   python -m pip install -e source/Go2Arm_Lab
   ```

### ⚙️ Training & Inference

#### Training

Run reinforcement-learning training in headless mode for higher efficiency:

```
# Activate IsaacLab environment
conda activate your_isaaclab_env

# Go to Go2Arm_Lab
cd /path/to/Go2Arm_Lab

# Launch training (headless)
python scripts/rsl_rl/train.py --task Isaac-Go2Arm-Flat --headless
```

#### Inference

Deploy a trained policy in a single environment:

```
# Activate IsaacLab environment
conda activate your_isaaclab_env

# Go to IsaacLab root
cd /path/to/Go2Arm_Lab

# Run inference
python scripts/rsl_rl/play.py --task Isaac-Go2Arm-Flat-Play --num_envs 1
```

## 🙏 Acknowledgments  
The RL algorithm implementation in this project references the [Deep-Whole-Body-Control](https://github.com/MarkFzp/Deep-Whole-Body-Control) project, for which we extend our sincere gratitude.
