# **Contributing to Brainswarm - Design & Simulation Working Group** 🚀

Welcome to the **Design & Simulation Working Group** at **Brainswarm**! We’re excited to have you contribute to our robotics simulation projects. This document outlines the contribution process, coding guidelines, and best practices for collaborating on this repository.

## **📌 How to Contribute**

### **1️⃣ Fork the Repository**

If you’re an intern or contributor, first fork this repository to your own GitHub account.

```bash
# Clone your fork
git clone https://github.com/munn33b/design-and-simulation-working-group.git
cd design-simulation-group
```

### **2️⃣ Set Up Your Local Environment**

Ensure you have the following installed:

1. ✅ **Ubuntu 22.04** (recommended)
2. ✅ **ROS 2 Humble**
3. ✅ **Gazebo** (Fortress or Classic, based on project needs)
4. ✅ **Git**

### **3️⃣ Create a New Branch**

Before making changes, create a new branch based on the task or feature you’re working on.

```bash
git checkout -b feature/my-new-feature
```

### **4️⃣ Make Your Changes**

- Follow the directory structure.
- Ensure URDF and Gazebo files are well-organized.
- Keep your commits clear and descriptive.

### **5️⃣ Test Your Work**

Before submitting, test your changes in ROS 2 and Gazebo. Example:

```bash
ros2 launch my_robot_simulation simulation.launch.py
```

### **6️⃣ Commit Your Changes**

Use meaningful commit messages:

```bash
git add .
git commit -m "Added URDF for simple robot"
```

### **7️⃣ Push to Your Fork & Create a Pull Request (PR)**

```bash
git push origin feature/my-new-feature
```

Then, go to the original repository on GitHub and create a **Pull Request (PR)**.

## **📌 Contribution Guidelines**

- ✅ **Follow the GitHub workflow** – Always work on a new branch, never commit directly to `main`.
- **✅ Write clean & modular code** – Keep URDFs well-structured, avoid redundant files.
- ✅ **Document your work** – Add comments in URDF/Xacro and Markdown explanations if needed.
- ✅ **Follow naming conventions** –
  - URDF files: `my_robot.urdf`
  - Xacro files: `my_robot.xacro`
  - Gazebo worlds: `indoor_lab.world`
- ✅ **Testing is required** – Ensure your simulation runs before submitting.

## **📌 Need Help?**

- 🚀 Post your questions in GitHub **Issues**.
- 📢 Discuss in **GitHub Discussions**.
- 🙌 Tag a mentor in your **Pull Request** if you need feedback.

Let’s build, simulate, and innovate together at **Brainswarm**! 🚀🤖