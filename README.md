## SelfDrivingRosPi4UbuntuServer


This has been tested on a Raspberry Pi 4 runing ubuntu 20.04. 

### Prerequisites

Here are a few things you will need before installation. You may be asked to type Y or N during installation.

  ```sh
  sudo apt-get update
  ```
  ```sh
  sudo apt upgrade
  ```
  ```sh
  cd catkin_ws/src
  ```
  ```sh
  git clone https://github.com/UbiquityRobotics/raspicam_node
  ```
  ```sh
  sudo apt install libraspberrypi-dev libraspberrypi0 libpigpiod-if-dev
  ```
  ```sh
  sudo apt install ros-noetic-compressed-image-transport ros-noetic-camera-info-manager ros-noetic-diagnostic-updater
  ```
  
  

### Installation
Update ~/.bashrc with ip address of pi and master and source it



1. Run this command once all pre-requisites are installed
   ```sh
   cd catkin_ws/src
   ```
2. Next you'll need this
   ```sh
   git clone https://github.com/Nick1770/SelfDrivingRosPi4UbuntuServer.git
   ```
3. Nagivate to...
   ```sh
   cd SelfDrivingRosPi4UbuntuServer
   ```
4. You'll need to move this to src
   ```sh
   mv turtlebot3_autorace/ ..
   mv Cmd2Serial/  ..
   ```
5. You'll need to remove the download folder from src
   ```sh
   cd ..
   ```
   ```sh
   sudo rm -r SelfDrivingRosPi4UbuntuServer/
   ```
   ```sh
   cd ..
   ```
   ```sh
   catkin_make
   ```
   ```sh
   cd catkin_ws/src/Cmd2Serial/src
   ```
   ```sh
   chmod +x main.py
   ```
   


### To Run
1. Run this on the raspberry pi
   ```sh
   roslaunch turtlebot3_autorace_camera turtlebot3_autorace_camera_pi.launchN
   ```
2. Run this on the master machine
   ```sh
   rqt_image_view
   ```
   ```sh
   rosrun keyboard_control main.py
   ```
  
3. Run this on the raspberry pi
   ```sh
   sudo chmod 777 /dev/ttyS0 
   ```
   ```sh
   rosrun Cmd2Serial main.py
   ```
4. Enjoy! If you need to end the script press "ctrl" + "c"
   
   
<p align="right">(<a href="#top">back to top</a>)</p>
