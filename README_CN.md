# Go2Arm_Lab

**一个用于足式操作机器人的强化学习训练框架**
  
<img src="https://img.shields.io/badge/IsaacSim-v4.0.0-blue" alt="IsaacSim-v4.0.0" /> <img src="https://img.shields.io/badge/IsaacLab-v1.4.1-blue" alt="IsaacLab v1.4.1" /> <img src="https://img.shields.io/badge/Python-3.10-blue" alt="Python 3.10" /> <img src="https://img.shields.io/badge/Platform-Linux--64-orange" alt="Linux-64" /> <img src="https://img.shields.io/badge/License-Apache2.0-yellow" alt="Apache2.0T License" />

## 🚀 概述

Go2Arm_Lab 使足式操作机器人的强化学习训练成为可能:

- **基础平台**: Unitree Go2 四足机器人
- **操作臂**: Interbotix WidowX 250s 机械臂

> **版本兼容性**
> 当前版本仅针对 IsaacLab v1.4.1。对 v2.00+ 的支持将在未来的更新中提供。

> **Gazebo 部署**
> 如果您想在 Gazebo 中部署您的策略，请使用：
> [Go2Arm_sim2sim](https://github.com/zzzJie-Robot/Go2Arm_Lab)

| IsaacLab 仿真                                                        | Gazebo 仿真 Simulation                                                      |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| ![IsaacLab](https://via.placeholder.com/300x150/0a84ff/ffffff?text=IsaacLab) | ![Gazebo](https://via.placeholder.com/300x150/ff6b6b/ffffff?text=Gazebo) |

## 📦 安装

1. 按照[官方指南](https://isaac-sim.github.io/IsaacLab/v1.4.1/source/setup/installation/index.html)安装 IsaacLab v1.4.1。
2. 将此仓库克隆到您的 IsaacLab 根目录（与 `source/` 同级）:
```
cd /path/to/IsaacLab
git clone https://github.com/zzzJie-Robot/Go2Arm_Lab.git
```

### ⚙️ 训练与推理

#### 训练

在无头模式下运行强化学习训练，以提高训练效率:

```
# Activate IsaacLab environment
conda activate your_isaaclab_env

# Navigate to IsaacLab root
cd /path/to/IsaacLab

# Launch training (headless)
isaaclab.sh -p Go2Arm_main/train.py --num_envs 4096  --max_iterations 10000 --headless
```

#### 推理

在单个环境中部署训练好的策略：

```
# Activate IsaacLab environment  
conda activate your_isaaclab_env

# Navigate to IsaacLab root  
cd /path/to/IsaacLab

# Run inference
isaaclab.sh -p Go2Arm_main/play.py --num_envs 1
```
