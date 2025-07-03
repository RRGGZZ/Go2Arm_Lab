# Go2Arm_Lab
## 概述
Go2Arm_Lab是一个基于IsaacLab平台的足式操控机器人强化学习训练框架  
  
Go2Arm由Unitree Go2机器狗 + Interbotix WidowX 250s机械臂组成  
  
>版本  
>本框架适用于IsaacLab的v1.4.1版本，v2.00及以上的版本将在后续更新
  
>推荐  
>如果您想在Gazebo中部署策略，请使用[Go2Arm_sim2sim](https://github.com/zzzJie-Robot/Go2Arm_Lab "Go2Arm_sim2sim")
    
| IsaacLab  | Gazebo|
| ---------- | -----------|
| 图片   | 图片   |  
  
## 安装
按照安装指南安装IsaacLab v1.4.1：[IsaacLab v1.4.1](https://isaac-sim.github.io/IsaacLab/v1.4.1/source/setup/installation/index.html "IsaacLab")  

安装Go2Arm_Lab环境  
* 将此代码库克隆或复制到 Isaac Lab 安装目录之内，即与source文件夹的同一路径  
    git clone xxx  

## 训练和推理
* 您可以使用如下命令进行Go2Arm的训练  

    conda activate your_isaaclab_env  
    cd /your_path/IsaacLab  
    isaaclab.sh -p /Go2Arm_main/train.py --num_envs 4096 --max_iterations 10000 --headless  
    
其中，headless代表无头模式，这将关闭isaacsim窗口，这可以大大提高训练效率  

* 您可以使用如下命令，让训练好的智能体进行推理  

    conda activate your_isaaclab_env  
    cd /your_path/IsaacLab  
    isaaclab.sh -p /Go2Arm_main/play.py --num_envs 1  
