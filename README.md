# Install ROS


## Steps

### 1. First open PowerShell and install wsl and Ubuntu-22.04

1-Copy this prompt " wsl --install -d Ubuntu-22.04 " and put it in Powerhell.
2-Then after finisid installing successfully, create a default Unix user account (it must start with a lowercase letter or underscore) and put your own password.
3-When you see yor user account in the end, you are doing well.

<img width="966" height="363" alt="Screenshot 2026-08-03 213937" src="https://github.com/user-attachments/assets/7e0a69f4-9be5-466f-bfcc-d3bcbc156520" />

### 2. Second open Ubuntu to install ROS (Ubuntu works with me without Restrat my device)

Copy these prompts line by line.

sudo apt update && sudo apt upgrade
sudo apt install software-properties-common curl
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu jammy main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update
sudo apt install ros-humble-desktop


1-  sudo apt update && sudo apt upgrade

ensure to put the prompt without any addition like (~).

<img width="710" height="901" alt="Screenshot 2026-08-03 214100" src="https://github.com/user-attachments/assets/4e1e7568-5119-47dd-bc82-36b52c4381ce" />

2- sudo apt install software-properties-common curl

<img width="672" height="125" alt="Screenshot 2026-08-03 214236" src="https://github.com/user-attachments/assets/20196dab-94ad-44d2-9a7f-884c06a29fbf" />

3- sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

and "  echo "deb [arch=amd64 signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu jammy main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null  "

<img width="1826" height="70" alt="Screenshot 2026-08-03 214607" src="https://github.com/user-attachments/assets/288a4f0d-4d8a-43da-b38e-0d4abcd4339a" />

4- sudo apt update

<img width="701" height="263" alt="Screenshot 2026-08-03 215143" src="https://github.com/user-attachments/assets/a3b24916-c809-4171-b023-305cb3e2a734" />

5- sudo apt install ros-humble-desktop

<img width="708" height="402" alt="Screenshot 2026-08-03 215310" src="https://github.com/user-attachments/assets/21397925-22c6-4abb-8e0d-7c7014a5e034" />

Enter Y

 
### 3. Run ROS

After installed ROS, copy these prompts line by line to run ROS.

echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
ros2 –version
echo $ROS_DISTRO

In the end, of you see the word "humble", you ran it perfectly without problems.
<img width="1896" height="271" alt="Screenshot 2026-08-03 221757" src="https://github.com/user-attachments/assets/0fe873ec-162a-4fd0-9b9a-162c24000eb9" />




 
