
# Actor Recognition In Movie Clips and Images
![ex1](https://user-images.githubusercontent.com/31413064/51027993-43f7f480-15b8-11e9-809a-f711c59aac8a.gif)


![ex1_540](https://user-images.githubusercontent.com/31413064/51028169-c5e81d80-15b8-11e9-9c15-d12ce4905027.png)


![ex2_540](https://user-images.githubusercontent.com/31413064/51028202-d7312a00-15b8-11e9-9c6e-948bc385967d.png)

Recognizing actors in a movie clip or image, using DeepLearning and Python.
Can use either CNN or HOG for face detection and then compare the face with our dataset of faces.

Here I've used **Spiderman 2** (2004), as an example. It can work with any piece of media, given the right dataset.

Tons of help from ageitgey's [face_recognition](https://github.com/ageitgey/face_recognition) library.

Inspired by [this](https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/) wonderful article.

## Process
- ### Dataset
    The dataset has the following structure, containing actor images collected using the Bing Image API (getData.py).


    ![screenshot from 2019-01-11 19-19-13](https://user-images.githubusercontent.com/31413064/51037313-dc50a200-15d5-11e9-94d1-45e94290ee52.png)


    As I'm using Spiderman 2, I've collected several pictures of the actors in the movie. Per actor I have ~15 images. More will do better, but this number seems to work fine.

- ### Training
  For every image in the dataset, we first get a square enclosing the face in the image, then generate a 128d vector for that face, which is dumped to the 'encodings.pickle' file.

  We can either use CNN(slower, more accurate) or HOG(faster, less accurate) for the face detection process. Here I've used the face_recognition library, which gives me both the options.

- ### Face Recognition
  Consider an image, be it a still from the movie, or a frame of a video clip.
  First, we identify the faces in the image using the same method as above (CNN or HOG), generate an encoding for it(128d vector), and then compare it with our collected encodings. The actors with the most matched encodings is the actor in the image.

## Usage

Read the first few lines of the Python file involved to understand the parameters used in each case

- ### Making encodings
    ```
    python faceEncode.py --dataset dataset/actors --encodings encodings.pickle -d hog
    ```

- ### Face Recognition in Image
  ```
  python faceRecImage.py -e encodings.pickle -i examples/ex6.png -d hog
  ```

- ### Face Recognition in Video File
  ```
  python faceRecVideoFile.py -e encodings.pickle -i input_vids/ex2.mp4 -o output_vids/ex2.mp4 -y 0 -d hog
  ```
  Outputs a video with the faces marked.

- ### Face Recognition in Video Stream from Webcam
  ```
  python faceRecVideo.py -e encodings.pickle -o output_vids/ex1.avi -y 0 -d hog
  ```
- ### Getting Image Data
  ```
  python getData.py --query "tobey macguire" --output dataset/tobey_macquire
  ```
  Will fetch images from Bing Image Search and save in the mentioned directory (Max 50).
  Make sure to get your own Bing search API key from [here](https://azure.microsoft.com/en-us/try/cognitive-services/?api=bing-image-search-api) and fill it up in the code.

#### Feel free to fork the repository and use it on your own movies, maybe expand the dataset and make it a general software for any given movie :)



<hr>
<hr>

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


