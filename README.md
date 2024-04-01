# How to Install TVM 
## Use pip for installing TVM (tested on Colab)
### CPU only
* <code>pip3 install apache-tvm</code>
### CUDA and CPU
* <code>pip3 install apache-tvm-cu102 -f https://tlcpack.ai/wheels</code>
* Check [TLCPack](https://tlcpack.ai/) for more TVM packages
- - -
## Install from source files (tested on Ubuntu 20.04 and above)
### Check enviroment 
* Find out installed graphics card by
  * <code>sudo lshw -C display</code> or
  * <code>lspci | grep -i --color 'vga\|3d\|2d'</code>
* CUDA toolkit version >= 8.0 is required
  * Use <code>nvidia-smi</code> to check your version
  * Use <code>sudo nvidia-settings</code> to configure NVIDIA graphics driver
### Install OpenCL
* Install OpenCL development files
  * <code>sudo apt install ocl-icd-opencl-dev</code>
* Install the package of querying OpenCL information
  * <code>sudo apt install clinfo</code>
* Deploy OpenCL runtime of Intel graphics
  * <code>sudo apt install intel-opencl-icd</code>
  * Check your Intel device with <code>clinfo</code>
### Install required libraries
- [ ] g++ 7.1 or higher
- [ ] CMake 3.18 or higher
- [ ] LLVM 4.0 or higher for CPU code generation
  * <code>sudo apt install -y llvm</code>
  * Use <code>llvm-config --version</code> to check your version
* <code>sudo apt update</code>
* <code>sudo apt install -y python3 python3-dev python3-setuptools gcc libtinfo-dev zlib1g-dev build-essential cmake vim git</code>
### Install Intel oneDNN
* <code>wget https://github.com/oneapi-src/oneDNN/archive/refs/tags/v2.6.tar.gz</code>
* <code>tar xf v2.6.tar.gz</code>
* <code>cd oneDNN-2.6/</code>
* <code>cmake . -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=lib</code>
* <code>make -j4</code>
* <code>sudo make install</code>
### Install ONNX packages
* <code>pip3 install onnx onnxoptimizer</code>
### Install ONNX Runtime
* For CPU: <code>pip3 install onnxruntime</code>
* For GPU: <code>pip3 install onnxruntime-gpu</code>
### Install necessary Python packages
* <code>sudo apt install -y python3-pip</code>
* <code>pip3 install numpy decorator attrs</code>
### Install optional Python packages
* <code>pip3 install --upgrade pip</code>
* <code>pip3 install pillow tflite opencv-python easydict typing-extensions psutil scipy tornado cloudpickle</code>
### List installed Python packages
* <code>pip3 list</code> or <code>pip3 freeze</code>
* Create requirements.txt
  * <code>pip3 freeze > requirements.txt</code>
* Install Python packages with requirements.txt
  * <code>pip3 install -r requirements.txt</code>
### Obtain source files
#### From release
* Download *.tar.gz (e.g. apache-tvm-src-v0.15.0.tar.gz) at [Release](https://github.com/apache/tvm/releases)
* <code>tar zxvf</code> the downloaded *.tar.gz
* Open a terminal and go to the directory containing decompressed files
#### From Github
* Open a terminal
* <code>cd ~</code>
* <code>git clone --recursive https://github.com/apache/tvm.git</code>
* <code>cd tvm</code>
* Switch branches (optional)
  * <code>git checkout</code> a commit
#### Build your own TVM
* <code>mkdir build</code>
* <code>cp cmake/config.cmake build</code>
* <code>cd build</code>
- [ ] Customize your compilation options
  * <code>vi config.cmake</code>
* <code>cmake ..</code>
* <code>make -j4</code>
#### Set environment variable
* <code>vi ~/.bashrc</code>
* Add the following two to ~/.bashrc
  * export TVM_HOME=/path_to_your_own_TVM
  * export PYTHONPATH=$TVM_HOME/python:${PYTHONPATH}
* <code>source ~/.bashrc</code>
- - -
## Install PAPI (Ver. 6 is required for TVM)
* git clone https://bitbucket.org/icl/papi.git
* cd papi/src/
* ./configure --prefix=$PWD/install
* sudo sh -c "echo 2 > /proc/sys/kernel/perf_event_paranoid"
  * Solve the problem: permission level does not permit operation
* make && make install
* cd install/bin
* ./papi_avail
  * To list available metrics
## Install TVM and enable PAPI support
* git clone --recursive https://github.com/apache/tvm.git
* cd tvm/
* mkdir build
* cd build/
* cp ../cmake/config.cmake .
* find [the directory where PAPI is cloned] -name papi.pc
* vi config.cmake to set: USE_LLVM ON
* vi config.cmake to set: USE_PAPI [the directory where papi.pc exists]
* cmake ..
* make -j4
* vi ~/.bashrc to set environment variable for TVM
* source ~/.bashrc
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
* Deploy OpenCL runtime of Intel graphics
  * <code>sudo apt install apt-file</code>
  * <code>sudo apt update</code>
  * <code>apt-file find libOpenCL.so</code>
  * <code>sudo add-apt-repository ppa:intel-opencl/intel-opencl</code>
  * <code>sudo apt update</code>
  * <code>sudo apt install intel-opencl-icd</code>
* Upgrade graphics driver using Software Updater of Ubuntu
  * Click on the 'Additional Drivers' tab
  * Choose the latest driver provided by Ubuntu  
## Notification
- [ ]  Some commands may need 'sudo'
- [ ]  Refer to https://docs.tvm.ai/install/from_source.html
## Reference
* https://note.nkmk.me/en/python-pip-list-freeze/
* https://note.nkmk.me/en/python-pip-install-requirements/
* https://tvm.apache.org/docs/install/from_source.html
* https://github.com/apache/tvm/blob/main/docker/install/ubuntu_install_dnnl.sh
* https://github.com/oneapi-src/oneDNN
