# Installation guide for Ubuntu 18.04 LTS
### Notice
- This instruction provides guideline to install prerequisites in Ubuntu 18.04 LTS
- This instruction is also for Windows WSL users
- This instruction is not guaranteed for other Linux distributions
	- It is expected that Debian-based distribution might be work somehow
- All commands must be ran one line at a time and follow the exact order

<hr>

### 0. Change your current directory to the project folder

<hr>

### 1. Update Python version to 3.8.x
- Only if Python version 3.8.x >= is not installed yet
- Running install_ubuntu.sh also runs these commands
- Ref: https://phoenixnap.com/kb/how-to-install-python-3-ubuntu
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8 python3.8-dev
```

<hr>

### 2. Install packages in virtualenv
- Running install_ubuntu.sh also runs these commands
- Ref: https://codechacha.com/ko/virtual-env-setup/
```
sudo apt update
sudo apt install virtualenv
virtualenv -p python3.8 venv
source venv/bin/activate
pip install cmake
pip install dlib pyqt5
pip install imutils jupyter scipy pandas opencv-python face-recognition sklearn numpy progressbar
```

<hr>

### 3. Install VcXsrv
- For Windows
- Ref: https://psychoria.tistory.com/739
##### 3.1. Install [VcXsrv](https://sourceforge.net/projects/vcxsrv/) for Windows
##### 3.2. If you cannot see "Display Settings" window after the installation, run XLaunch
- Search XLaunch in Start
##### 3.3. If you see "Display Settings" window, click "Next" until "Extra settings"
##### 3.4. For "Extra settings", check "Disable access control" checkbox and click "Next"
##### 3.5. In "Finish configuration" window, click "Save configuration" button, save it, and click "Finish"
- A location of the configuration file does not matter
##### 3.6. If you see "Windows Security Alert", you should click "Allow access"

<hr>

### 4. WSL VcXsrv settings
- For Windows WSL
- Ref: https://psychoria.tistory.com/739
##### 4.1. Go to your shell and open your shell's configuration file
- For bash, it is ~/.bashrc file. If you are not using bash, you must open the right shell configuration file
##### 4.2. Add these commands to your shell's configuration file
- Add this command for first time
  ```
  export DISPLAY=$(whoami):0.0
  ```
- If the above command does not work, fix it as this command
  ```
  export DISPLAY="`grep nameserver /etc/resolv.conf | sed 's/nameserver //'`:0"
  ```
- You do not have to fix this command, just enter it
  ```
  export LIBGL_ALWAYS_INDIRECT=1
  ```

<hr>

### 5. Ubuntu remote server settings for X11
- For Ubuntu remote server & Windows
- Ref: http://bahndal.egloos.com/534415
##### 5.1. Access to your remote server with SSH client
##### 5.2. Run these commands
```
sudo apt update
sudo apt install xauth
```
##### 5.3. Open /etc/ssh/sshd_config as root privilege
- For Vim user, you should enter "sudo vim /etc/ssh/sshd_config"
##### 5.4. Find "X11Forwarding" configuration and set it as "yes"
```
X11Forwarding yes
```
##### 5.5. Backup your default .Xauthority file & create a new one with these commands
```
mv ~/.Xauthority ~/.Xauthority.bak
touch .Xauthority
```
##### 5.6. Open /etc/ssh/ssh_config as root privilege
##### 5.7. Set "ForwardX11" to "yes"
```
ForwardX11 yes
```
##### 3.8. Close SSH connection and access to the server again with -X option in ssh command
- Example
  ```
  e.g. ssh -X USER@REMOTE_ADDRESS
  ```


