FROM ubuntu:xenial

RUN mkdir /code
ADD . /code/

# General dependencies, lots of them
RUN apt-get update  && \
apt-get upgrade -y && \
apt-get install software-properties-common && \
add-apt-repository ppa:jonathonf/ffmpeg-4 -y
# Python + pip
RUN apt-get install -y python python-dev python-pip python-numpy python-scipy
RUN pip install numpy --upgrade 

RUN apt-get install -qy libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev libatlas-dev libzmq3-dev libboost-all-dev libgflags-dev libgoogle-glog-dev liblmdb-dev protobuf-compiler bc libopenblas-dev supervisor

 
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
RUN chmod +x scripts/download_model_binary.py
RUN /code/caffe/scripts/download_model_binary.py /code/caffe/models/bvlc_googlenet

#supervisord conf

RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN pip install flask && \
pip install youtube-dl && \
pip install textblob && \
python -m textblob.download_corpora
#pip install google-api-python-client
#pip install python-musixmatch

WORKDIR /code


