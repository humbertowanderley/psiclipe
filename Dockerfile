FROM ubuntu:14.04

RUN mkdir /code
ADD . /code/

# General dependencies, lots of them
RUN apt-get update
RUN apt-get install -qy libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev libatlas-dev libzmq3-dev libboost-all-dev libgflags-dev libgoogle-glog-dev liblmdb-dev protobuf-compiler bc libopenblas-dev supervisor
 
# Python + pip
RUN apt-get install -y python python-dev python-pip python-numpy python-scipy
RUN pip install numpy --upgrade && \
pip install flask && \
pip install python-musixmatch && \
pip install google-api-python-client && \
#pip install -U textblob && \
#python -m textblob.download_corpora && \
#pip install youtube-dl

# Caffe
WORKDIR /code/caffe
RUN cp Makefile.config.example Makefile.config
RUN easy_install --upgrade pip



# Enable CPU-only + openblas (faster than atlas)
RUN sed -i 's/# CPU_ONLY/CPU_ONLY/g' Makefile.config
RUN sed -i 's/BLAS := atlas/BLAS := open/g' Makefile.config

# Caffe's Python dependencies...
RUN pip install -r python/requirements.txt
RUN make all
RUN make pycaffe
ENV PYTHONPATH=/caffe/python

# Download model
RUN scripts/download_model_binary.py models/bvlc_googlenet

#supervisord conf

RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

WORKDIR /code


