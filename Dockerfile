FROM ubuntu:14.04

RUN mkdir /code
ADD . /code/



# General dependencies, lots of them
RUN apt-get update && apt-get install -y git
RUN apt-get update && apt-get install -y -f libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev libatlas-dev libzmq3-dev libboost-all-dev libgflags-dev libgoogle-glog-dev liblmdb-dev protobuf-compiler bc libopenblas-dev supervisor


# Python + pip
RUN apt-get install -y python python-dev python-pip python-numpy python-scipy
RUN pip install numpy --upgrade 


# Caffe
WORKDIR /code/caffe
RUN easy_install --upgrade pip


# Caffe's Python dependencies...
RUN pip install -r python/requirements.txt
RUN make all
RUN make pycaffe
ENV PYTHONPATH=/code/caffe/python:/caffe/python

# Download model
RUN chmod +x scripts/download_model_binary.py
RUN /code/caffe/scripts/download_model_binary.py /code/caffe/models/bvlc_googlenet

#supervisord conf

RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf



# We want the "add-apt-repository" command
RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:mc3man/trusty-media

RUN apt-get update && apt-get install -y ffmpeg


RUN pip install flask && \
pip install youtube-dl && \
pip install beautifulsoup4 && \
pip install google_images_download && \
pip install opencv-contrib-python-headless && \
pip install rake-nltk && \
pip install moviepy --ignore-installed  && \
pip install --upgrade youtube-dl  

WORKDIR /code


