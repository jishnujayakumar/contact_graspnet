#----------------------------------------------------------------------------------------------------
# Work done while being at the Intelligent Robotics and Vision Lab at the University of Texas, Dallas
# Please check the licenses of the respective works utilized here before using this script.
# 🖋️ Jishnu Jaykumar Padalunkal (2025).
# Date: "May 29 2025"
#----------------------------------------------------------------------------------------------------
# Ref: https://github.com/NVlabs/BundleSDF/blob/master/docker/dockerfile

FROM nvidia/cuda:11.3.1-cudnn8-devel-ubuntu20.04

ENV TZ=US/Pacific
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update --fix-missing && \
    apt-get install -y libgtk2.0-dev && \
    apt-get install -y wget bzip2 ca-certificates curl git vim tmux g++ gcc build-essential cmake checkinstall gfortran libjpeg8-dev libtiff5-dev pkg-config yasm libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev libxine2-dev libv4l-dev qt5-default libgtk2.0-dev libtbb-dev libatlas-base-dev libfaac-dev libmp3lame-dev libtheora-dev libvorbis-dev libxvidcore-dev libopencore-amrnb-dev libopencore-amrwb-dev x264 v4l-utils libprotobuf-dev protobuf-compiler libgoogle-glog-dev libgflags-dev libgphoto2-dev libhdf5-dev doxygen libflann-dev libboost-all-dev proj-data libproj-dev libyaml-cpp-dev cmake-curses-gui

RUN cd / &&\
    git clone https://github.com/opencv/opencv &&\
    cd opencv &&\
    git checkout 3.4.15 &&\
    cd / && git clone https://github.com/opencv/opencv_contrib.git &&\
    cd opencv_contrib &&\
    git checkout 3.4.15 &&\
    cd /opencv &&\
    mkdir build


RUN cd /opencv/build &&\
    cmake .. -DCMAKE_BUILD_TYPE=Release -DBUILD_CUDA_STUBS=OFF -DBUILD_DOCS=OFF -DWITH_MATLAB=OFF -Dopencv_dnn_BUILD_TORCH_IMPORTE=OFF -DCUDA_FAST_MATH=ON  -DMKL_WITH_OPENMP=ON -DOPENCV_ENABLE_NONFREE=ON -DWITH_OPENMP=ON -DWITH_QT=ON -WITH_OPENEXR=ON -DENABLE_PRECOMPILED_HEADERS=OFF -DBUILD_opencv_cudacodec=OFF -DINSTALL_PYTHON_EXAMPLES=OFF  -DWITH_TIFF=OFF -DWITH_WEBP=OFF -DOPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules -DCMAKE_CXX_FLAGS=-std=c++11 -DENABLE_CXX11=OFF  -DBUILD_opencv_xfeatures2d=ON -DOPENCV_DNN_OPENCL=OFF -DWITH_CUDA=ON -DWITH_OPENCL=OFF &&\
    make -j20 &&\
    make install &&\
    cd /opencv/build && make install


SHELL ["/bin/bash", "--login", "-c"]

RUN cd / && wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /miniconda.sh && \
    bash /miniconda.sh -b -p /opt/conda && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    rm /miniconda.sh && \
    /opt/conda/bin/conda clean -afy && \
    /opt/conda/bin/conda create -n jp_cgnet python=3.7 --yes


ENV PATH=$PATH:/opt/conda/envs/jp_cgnet/bin

RUN conda init bash &&\
    echo "conda activate jp_cgnet" >> ~/.bashrc &&\
    conda activate jp_cgnet &&\
    pip cache purge

ENV CUDA_HOME=/usr/local/cuda
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64
ENV OPENCV_IO_ENABLE_OPENEXR=1
ENV TF_CPP_MIN_LOG_LEVEL=2
