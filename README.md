# How ot Install TVM
## Enviroment
- [ ] Linux (Ubuntu is recommended)
- [ ] CUDA toolkit version >= 8.0 is required
  - [ ] Use 'nvidia-smi' to check your version
## Notification
- [ ]  Some commands may need 'sudo'
- [ ]  Refer to https://docs.tvm.ai/install/from_source.html
## Install ITRI certificate for Ubuntu
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
* apt install -y vim
- [ ] LLVM 4.0 or higher is needed for build with LLVM
  * apt install -y llvm
  - [ ] Use 'llvm-config --version' to check your version
* apt install -y git
## Install TVM from source
* cd ~
* git clone --recursive https://github.com/apache/incubator-tvm.git
* cd incubator-tvm
* mkdir build
* cp cmake/config.cmake build
* cd build
- [ ] Customize your compilation options
  * vi config.cmake
* cmake ..
* make -j4
## Set the environment variable
* cd ~
* vi .bashrc
- [ ] Add the following two to .bashrc
  * export TVM_HOME=/root/incubator-tvm
  * export PYTHONPATH=$TVM_HOME/python:$TVM_HOME/topi/python:$TVM_HOME/nnvm/python:${PYTHONPATH}
* source .bashrc
