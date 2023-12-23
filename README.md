# Mobile Manipulator Lab Notebooks

[![Binder](https://mybinder.org/badge_logo.svg)](<https://mybinder.org/v2/gh/Foundations-of-Robotics/mobile_manip_notebooks/HEAD>)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](<https://colab.research.google.com/github/AIResearchLab/mobile_manip_notebooks>)
[![vscode.dev](https://img.shields.io/badge/vscode-dev-blue)](<https://vscode.dev>)

These Python Jupyter notebooks are designed for academic teaching laboratories in robotics, using Gazebo for simulation up to physical deployment on robotic platforms. The students are not expected to install or deploy the required ROS workspace on their personal computer, but rather use a server infrastructure at the university. The laboratories were designed at École de technologie supérieure, in Montréal, Canada, where we host the physical infrastructure to which these tools are tailored. We have 8 robotic platforms for the students to test their algorithms and several shared desktop stations. The stations are accessible remotely.

## Prerequisites

The notebooks are designed to be used with a ROS workspace that contains the following packages:

- [mobile manipulator workspace](<https://github.com/Foundations-of-Robotics/mobile_manip_ws>)

## Projects

- [**Project 0**](<./Project0/>) - Primers on Python, the terminal, and ROS
- [**Project 1**](<./Project1/>) - Mobile Base Kinematics
- [**Project 2**](<./Project2/>) - Localization and Kalman Filters
- [**Project 3**](<./Project3/>) - Kinematics for a 3-DoF Manipulator
- [**Project 4**](<./Project4/>) - Mobile Robotics & Manipulator Control
- [**Project 5**](<./Project5/>) - Perception and Navigation

## Installation

### Virtual Environment

Setting up a python virtual environment for can be useful in some development situations. Run the following command in a terminal at the top level of this git repository.

```python
python3 -m venv .venv

# windows
# may not work on windows
.venv\Scripts\activate.bat

pip install -r requirements.txt


# linux
source .venv/bin/activate

pip install -r requirements.txt
```

### Running the code

In a terminal at the top level of this git repository, run the following.

```bash
source .venv/bin/activate

# start a jupyter notebook server
python3 -m jupyter lab --ip=0.0.0.0 --port=8888

# or run a voila server for the UI only version
voila notebooks --port=8866
```

## Experimental Software Disclaimer

The contents of this source is provided in an experimental state and does not guarantee safe or correct operation.

The contents of this source is subject to change, without prior notice. Any available APIs are to be considered unstable and are not guaranteed to be complete and / or functional.
