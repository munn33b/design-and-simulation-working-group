# BrainSwarm - Design & Simulation Working Group 🚀

Welcome to the **Design & Simulation Working Group** of **BrainSwarm**! This repository serves as a structured learning hub for interns to develop expertise in robot simulation, **URDF modeling**, and **ROS 2 integration**.

## 📌 About This Repository
This repository contains:

- [x] ✅ Learning Roadmap – A structured plan covering 3D modeling, URDF, ROS 2, and Gazebo.
- [x] ✅ Hands-on Tasks – Weekly tasks and assignments for interns to practice skills.
- [x] ✅ Simulation Projects – Real-world robotic simulations developed by the team.
- [x] ✅ Resources & Tutorials – Guides, references, and useful links for learning.

## 🎯 Objectives
1. Model robotic systems in SOLIDWORKS and export them to URDF.
2. Simulate robots in Gazebo and integrate with ROS 2.
3. Develop robotic environments for testing and experimentation.
4. Collaborate using GitHub to track progress and contribute to the team’s projects.

## 🚀 Getting Started

- Clone the repository:

  ```bash
  git clone https://github.com/munn33b/design-and-simulation-working-group.git
  cd design-and-simulation-working-group
  ```

- Follow the Guides in the Learning Path.

- Complete assigned tasks and submit pull requests.

- Stay updated on new challenges and projects!

## 👥 Team Collaboration
Each intern will work on specific tasks and projects, contribute through pull requests, and receive feedback. Regular updates and discussions will happen via GitHub Issues and Discussions.

## Directory Structure

├── assets                          # Images and media resources for documentation
│   ├── git_workflow.png
│   ├── joint_types_urdf.png
│   ├── mobile_robot_road_env_ignition.jpg
│   ├── pick_and_place_env_vrep.jpeg
│   ├── turtlebot3_burger.png
│   ├── urdf_structure.jpg
│   ├── urdf_structure.png
│   └── urdf_visual.jpg
├── CAD_Files                        # CAD models and components for robotic platforms
│   ├── Components                   # Individual component models
│   │   └── SIMBOT
│   │       └── SIMBOT_Cover_Original.SLDPRT
│   ├── README.md                     # CAD-related documentation
│   └── Robots                        # Complete robot models
│       ├── SIMBOT                    # SIMBOT CAD models
│       │   └── CAD Models
│       │       ├── PCBModelwithIRSensorsandSlideSwitchandTypeBConnectorandN20MotorsSIMBOTCover.SLDPRT
│       │       ├── simboid_wheel.SLDPRT
│       │       └── simbot_with_base_and_wheels.SLDASM
│       └── Turtlebot3 Burger         # CAD models for Turtlebot3 Burger
│           └── CAD Files
│               ├── FirstFloor
│               │   ├── ball_caster.zip
│               │   ├── connected plates.step
│               │   ├── FirstFloor Support Parts.zip
│               │   └── wheel.zip
│               ├── FourthFloor
│               │   ├── 4Plates.step
│               │   ├── 4RivetsBeneathLDS.step
│               │   ├── connected plates.step
│               │   └── LDS (1).step
│               ├── SecondFloor
│               │   ├── connected plates (1).step
│               │   ├── Floor2 Support Parts.zip
│               │   └── OPENCR (1).step
│               └── ThirdFloor
│                   ├── connected plates.step
│                   ├── RPi.step
│                   ├── SUPPORT_HEX_M3_0XL45_FF - SUPPORT_HEX_M3_0XL45_FF.step
│                   └── USBPart.step
├── Challenges                        # Hands-on simulation and coding challenges
│   ├── Navigate_through_Maze_Block_Coding
│   │   ├── brainswarm_ws             # ROS 2 workspace for navigation challenge
│   │   │   ├── src
│   │   │   │   └── turtlebot3
│   │   │   │       ├── CMakeLists.txt
│   │   │   │       ├── include
│   │   │   │       ├── launch
│   │   │   │       ├── maps
│   │   │   │       ├── models
│   │   │   │       ├── package.xml
│   │   │   │       ├── params
│   │   │   │       └── src
│   │   └── README.md                 # Description of the challenge
│   └── README.md
├── CONTRIBUTING.md                    # Contribution guidelines for this repository
├── docs                               # Learning materials and tutorials
│   ├── Gazebo_Simulation.md
│   ├── Git_Workflow.md
│   ├── ROS2_Basics.md
│   ├── SOLIDWORKS_Basics.md
│   └── URDF_Tutorials.md
├── README.md                          # Main repository documentation
├── RESOURCES.md                        # Additional learning resources
├── Simulation_Worlds_and_Models        # Gazebo simulation environments
│   └── GazeboWorlds
│       └── worlds
│           ├── ionic.sdf
│           └── tunnel.sdf
├── Week_1                              # Weekly tasks and submissions
│   ├── README.md
│   └── Submissions
│       ├── Task_1
│       │   └── README.md
│       ├── Task_2
│       │   └── README.md
│       └── Task_3
│           └── README.md
