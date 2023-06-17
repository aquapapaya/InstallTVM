# How to Install TVM
## Enviroment
- [ ] Linux (Ubuntu 18.04 LTS is tested)
  - [ ] Find out installed graphics card by 'sudo lshw -C display' or 'lspci | grep -i --color 'vga\|3d\|2d'
- [ ] Upgrade graphics driver using Software Updater of Ubuntu
  - [ ] Click on the 'Additional Drivers' tab
  - [ ] Choose the latest driver provided by Ubuntu
- [ ] CUDA toolkit version >= 8.0 is required
  - [ ] Use 'nvidia-smi' to check your version
  - [ ] Use 'sudo nvidia-settings' to configure NVIDIA graphics driver
- [ ] Deploy OpenCL runtime of Intel graphics
  * sudo apt install apt-file
  * sudo apt update
  * apt-file find libOpenCL.so
  * sudo add-apt-repository ppa:intel-opencl/intel-opencl
  * sudo apt update
  * sudo apt install intel-opencl-icd
- [ ] OpenCL
  - [ ] Use 'clinfo' to check OpenCL platform and devices available on your system
  * <code>sudo apt install clinfo</code>
  * sudo apt install ocl-icd-opencl-dev
## Notification
- [ ]  Some commands may need 'sudo'
- [ ]  Refer to https://docs.tvm.ai/install/from_source.html
## Install ITRI Certificate for Ubuntu (Optional)
- [ ] Download auto_ITRIRoot256_apped.tar
* tar xvf auto_ITRIRoot256_apped.tar
* cd ITRIRoot256/
* ./auto_ITRIRoot256
- [ ] Reboot
## Install Required Libraries
- [ ] g++ 4.8 or higher
- [ ] CMake 3.5 or higher
* apt update
* apt install -y python3 python3-dev python3-setuptools gcc libtinfo-dev zlib1g-dev build-essential cmake
* apt install -y python3-pip
* pip3 install numpy
* pip3 install decorator
* pip3 install scipy
* pip3 install attrs
* apt install -y vim
- [ ] LLVM 4.0 or higher is needed for build with LLVM
  * apt install -y llvm
  - [ ] Use 'llvm-config --version' to check your version
* apt install -y git
## Install Optional Libraries
* pip3 install --upgrade pip
* pip3 install Pillow
* pip3 install tflite
* pip3 install opencv-python
* pip3 install easydict
## Install TVM from Source
* cd ~
* git clone --recursive https://github.com/apache/incubator-tvm.git
* cd incubator-tvm
- [ ] Switch branches (optional)
  * git checkout &lt;commit>
* mkdir build
* cp cmake/config.cmake build
* cd build
- [ ] Customize your compilation options
  * vi config.cmake
* cmake ..
* make -j4
## Set Environment Variable
* cd ~
* vi .bashrc
- [ ] Add the following two to .bashrc
  * export TVM_HOME=/root/incubator-tvm
  * export PYTHONPATH=$TVM_HOME/python:$TVM_HOME/topi/python:$TVM_HOME/nnvm/python:${PYTHONPATH}
* source .bashrc
## Create Branch from Existing Commit
* git clone --recursive https://github.com/apache/incubator-tvm.git
* cd incubator-tvm
* git checkout &lt;commit>
* git checkout -b &lt;new_branch>
* git push --set-upstream origin &lt;new_branch>
## Create Your Own TVM
* git clone --recursive https://github.com/apache/incubator-tvm.git
* cd incubator-tvm
* git checkout &lt;commit>
* git checkout -b &lt;new_branch>
* git remote add &lt;remote_name> &lt;remote_URL>
* git remote -v
* git branch
* git config --global user.email &lt;email>
* git config --list
* git push --set-upstream &lt;remote_name> &lt;new_branch>
    * --set-upstream is equal to -u
    * --set-upstream is used in the first upload
    * git push &lt;remote_name> &lt;branch_name> for later upload
* git tag -l
* git push --set-upstream --tags &lt;remote_name>
## Push Existing Repository to Code Hosting Service
* cd [directory]
* git remote add [name for the hosting] [hosting's .git]
* git push -u [name for the hosting] --all
* git push -u [name for the hosting] --tags
## Push All New Repository to Code Hosting Service
* cd [directory]
* git init
* git remote add [name for the hosting] [hosting's .git]
* git add .
* git commit -m "Initial commit"
* git push -u [name for the hosting] master
## Misc.
* https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#runfile-nouveau
* find ./ -type f -size +20M (find large files, in this example, 20MB)
* git log --graph --oneline --all (visualize git log)
### Upgrade cmake on Ubuntu
* sudo apt remove cmake
* pip3 install cmake
* sudo ln /home/[account_name]/.local/bin/cmake /usr/bin/cmake
* cmake --version
