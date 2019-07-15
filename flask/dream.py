#!/usr/bin/env python
# coding: utf-8

# # Deep Dreams (with Caffe)
# 
# This notebook demonstrates how to use the [Caffe](http://caffe.berkeleyvision.org/) neural network framework to produce "dream" visuals shown in the [Google Research blog post](http://googleresearch.blogspot.ch/2015/06/inceptionism-going-deeper-into-neural.html).
# 
# It'll be interesting to see what imagery people are able to generate using the described technique. If you post images to Google+, Facebook, or Twitter, be sure to tag them with **#deepdream** so other researchers can check them out too.
# 
# ##Dependencies
# This notebook is designed to have as few dependencies as possible:
# * Standard Python scientific stack: [NumPy](http://www.numpy.org/), [SciPy](http://www.scipy.org/), [PIL](http://www.pythonware.com/products/pil/), [IPython](http://ipython.org/). Those libraries can also be installed as a part of one of the scientific packages for Python, such as [Anaconda](http://continuum.io/downloads) or [Canopy](https://store.enthought.com/).
# * [Caffe](http://caffe.berkeleyvision.org/) deep learning framework ([installation instructions](http://caffe.berkeleyvision.org/installation.html)).
# * Google [protobuf](https://developers.google.com/protocol-buffers/) library that is used for Caffe model manipulation.

# In[2]:


# imports and basic notebook setup
from io import BytesIO as StringIO
import numpy as np
import scipy.ndimage as nd
import PIL.Image
from IPython.display import clear_output, Image, display
from google.protobuf import text_format
import random

import caffe

# If your GPU supports CUDA and Caffe was built with CUDA support,
# uncomment the following to run Caffe operations on the GPU.
# caffe.set_mode_gpu()
# caffe.set_device(0) # select GPU device if multiple devices exist

def showarray(a, fmt='jpeg'):
    a = np.uint8(np.clip(a, 0, 255))
    f = StringIO()
    PIL.Image.fromarray(a).save(f, fmt)
    display(Image(data=f.getvalue()))


# ## Loading DNN model
# In this notebook we are going to use a [GoogLeNet](https://github.com/BVLC/caffe/tree/master/models/bvlc_googlenet) model trained on [ImageNet](http://www.image-net.org/) dataset.
# Feel free to experiment with other models from Caffe [Model Zoo](https://github.com/BVLC/caffe/wiki/Model-Zoo). One particularly interesting [model](http://places.csail.mit.edu/downloadCNN.html) was trained in [MIT Places](http://places.csail.mit.edu/) dataset. It produced many visuals from the [original blog post](http://googleresearch.blogspot.ch/2015/06/inceptionism-going-deeper-into-neural.html).

# In[3]:


model_path = '/code/caffe/models/bvlc_googlenet/' # substitute your path here
net_fn   = model_path + 'deploy.prototxt'
param_fn = model_path + 'bvlc_googlenet.caffemodel'

# Patching model to be able to compute gradients.
# Note that you can also manually add "force_backward: true" line to "deploy.prototxt".
model = caffe.io.caffe_pb2.NetParameter()
text_format.Merge(open(net_fn).read(), model)
model.force_backward = True
open('tmp.prototxt', 'w').write(str(model))

net = caffe.Classifier('tmp.prototxt', param_fn,
                       mean = np.float32([104.0, 116.0, 122.0]), # ImageNet mean, training set dependent
                       channel_swap = (2,1,0)) # the reference model has channels in BGR order instead of RGB

# a couple of utility functions for converting to and from Caffe's input image layout
def preprocess(net, img):
    return np.float32(np.rollaxis(img, 2)[::-1]) - net.transformer.mean['data']
def deprocess(net, img):
    return np.dstack((img + net.transformer.mean['data'])[::-1])


# ##  Producing dreams

# Making the "dream" images is very simple. Essentially it is just a gradient ascent process that tries to maximize the L2 norm of activations of a particular DNN layer. Here are a few simple tricks that we found useful for getting good images:
# * offset image by a random jitter
# * normalize the magnitude of gradient ascent steps
# * apply ascent across multiple scales (octaves)
# 
# First we implement a basic gradient ascent step function, applying the first two tricks:

# In[17]:


def objective_L2(dst):
    dst.diff[:] = dst.data 

def make_step(net, step_size=1.5, end='inception_4c/output', 
              jitter=32, clip=True, objective=objective_L2):
    '''Basic gradient ascent step.'''

    src = net.blobs['data'] # input image is stored in Net's 'data' blob
    dst = net.blobs[end]

    ox, oy = np.random.randint(-jitter, jitter+1, 2)
    src.data[0] = np.roll(np.roll(src.data[0], ox, -1), oy, -2) # apply jitter shift
            
    net.forward(end=end)
    objective(dst)  # specify the optimization objective
    net.backward(start=end)
    g = src.diff[0]
    # apply normalized ascent step to the input image
    src.data[:] += step_size/np.abs(g).mean() * g

    src.data[0] = np.roll(np.roll(src.data[0], -ox, -1), -oy, -2) # unshift image
            
    if clip:
        bias = net.transformer.mean['data']
        src.data[:] = np.clip(src.data, -bias, 255-bias)    


# Next we implement an ascent through different scales. We call these scales "octaves".

# In[5]:


def deepdream(net, base_img, iter_n=10, octave_n=4, octave_scale=1.4, 
              end='inception_4c/output', clip=True, **step_params):
    # prepare base images for all octaves
    octaves = [preprocess(net, base_img)]
    for i in xrange(octave_n-1):
        octaves.append(nd.zoom(octaves[-1], (1, 1.0/octave_scale,1.0/octave_scale), order=1))
    
    src = net.blobs['data']
    detail = np.zeros_like(octaves[-1]) # allocate image for network-produced details
    for octave, octave_base in enumerate(octaves[::-1]):
        h, w = octave_base.shape[-2:]
        if octave > 0:
            # upscale details from the previous octave
            h1, w1 = detail.shape[-2:]
            detail = nd.zoom(detail, (1, 1.0*h/h1,1.0*w/w1), order=1)

        src.reshape(1,3,h,w) # resize the network's input image size
        src.data[0] = octave_base+detail
        for i in xrange(iter_n):
            make_step(net, end=end, clip=clip, **step_params)
            
            # visualization
            vis = deprocess(net, src.data[0])
            if not clip: # adjust image contrast if clipping is disabled
                vis = vis*(255.0/np.percentile(vis, 99.98))
            showarray(vis)
            print(octave);print(i)
            print(end)
            print(vis.shape)
            clear_output(wait=True)
            
        # extract details produced on the current octave
        detail = src.data[0]-octave_base
    # returning the resulting image
    return deprocess(net, src.data[0])


# img = np.float32(PIL.Image.open('sky1024px.jpg'))
# guide = np.float32(PIL.Image.open('flowers.jpg'))
# end = 'inception_3b/output'
# h, w = guide.shape[:2]
# src, dst = net.blobs['data'], net.blobs[end]
# src.reshape(1,3,h,w)
# src.data[0] = preprocess(net, guide)
# net.forward(end=end)
# guide_features = dst.data[0].copy()


def objective_guide(dst):
    x = dst.data[0].copy()
    y = guide_features
    ch = x.shape[0]
    x = x.reshape(ch,-1)
    y = y.reshape(ch,-1)
    A = x.T.dot(y) # compute the matrix of dot-products with guide features
    dst.diff[0].reshape(ch,-1)[:] = y[:,A.argmax(1)] # select ones that match best



def mydream(img_in,guide_in,end_in, img_name):
    global guide_features
    global net
    global end
    global guide
    global src
    global dest
    global h
    global w

    img = img_in
    guide = guide_in
	
	
    end = end_in
    h, w = guide.shape[:2]
    src, dst = net.blobs['data'], net.blobs[end]
    src.reshape(1,3,h,w)
    src.data[0] = preprocess(net, guide)
    net.forward(end=end)
    guide_features = dst.data[0].copy()
    myoutput = deepdream(net, img, end=end, objective=objective_guide)
	
    h1,w1 = myoutput.shape[:2]
	# h1, w1 = myoutput.shape[:2]
    s1 = 0.1
	# s1 = 0.1 # scale coefficient
    myoutput = nd.affine_transform(myoutput, [1-s1,1-s1,1], [h1*s1/2,w1*s1/2,0], order=1)
	# myoutput = nd.affine_transform(frame, [1-s,1-s,1], [h1*s1/2,w1*s1/2,0], order=1)
    
	
    PIL.Image.fromarray(np.uint8(myoutput)).save("/code/flask/dream_frames/" + img_name)
    return myoutput
	# PIL.Image.fromarray(np.uint8(myoutput)).save("/code/flask/dream_frames/" + img_name)
    # return myoutput



# Instead of maximizing the L2-norm of current image activations, we try to maximize the dot-products between activations of current image, and their best matching correspondences from the guide image.

# In[53]:

# img = np.float32(PIL.Image.open('sky1024px.jpg'))
# guide = np.float32(PIL.Image.open('flowers.jpg'))
# end = 'inception_3a/5x5_reduce'
# myoutput = mydream(img, guide, end)



# This way we can affect the style of generated images without using a different training set.


# def aux_dream(image_timestamp):

#     dream_image_timestamp = []


#     i = 0

   

#     for line in image_timestamp:
#         img_guide = None
#         img_in = np.float32(PIL.Image.open(line[0]))

#         if i < (len(image_timestamp) - 1):
#             img_guide = np.float32(PIL.Image.open(image_timestamp[i + 1][0]))

#         img_name = line[0].split('/code/flask/imagens/')[1]
#         if(img_guide is not None):
            
#             mydream(img_in, img_guide, 'inception_3b/output',img_name)

#         else:
#             deepdream(net,base_img=img_in,end='inception_3b/5x5_reduce')
        
#         dream_image_timestamp.append(['/code/flask/dream_frames/'+img_name, line[1], line[2]])
#         i = i + 1

    
#     return dream_image_timestamp
# def dreamVideoVelho(image_timestamp):
    
# 	dream_image_timestamp = []

	
# 	i = 0

	
# 	last_frame = None
# 	img_in = None
# 	imageGuide = None

#     rangeVolum = 10
#     #temporario
#     foiPrimeira = True

# 	for line in image_timestamp:
# 		timeBetween = (line[2]-line[1])/rangeVolum

#         if foiPrimeira:    
#             for y in range(rangeVolum):
#                 if(last_frame is None):
#                     img_in = np.float32(PIL.Image.open(line[0]))
#                 else:
#                     img_in = last_frame
                
                
#                 if i < (len(image_timestamp) - 1):
#                     img_guide = np.float32(PIL.Image.open(image_timestamp[i + 1][0]))

#                 img_name = line[0].split('/code/flask/imagens/')[1]
#                 if(img_guide is not None):
#                     last_frame = mydream(img_in, img_guide, 'inception_3b/output',img_name+str(y)+'.jpg')

#                 else:
#                     last_frame = deepdream(net,base_img=img_in,end='inception_3b/5x5_reduce')
                
#                 dream_image_timestamp.append(['/code/flask/dream_frames/'+img_name+str(y), (line[1]+timeBetween*y), (line[1]+timeBetween*(y+1)) ])
#             foiPrimeira=False
#         else:
#             dream_image_timestamp.append(line)
	
# 		i = i + 1
	
# 	return dream_image_timestamp

def dreamImage(json_subtitle):
    endChoices = []
    endChoices.append("conv2/3x3_reduce")
    endChoices.append("inception_3b/pool_proj")
    endChoices.append("inception_3b/output")
    count = 0
    while count < len(json_subtitle):
        img_in = np.float32(PIL.Image.open(json_subtitle[count]['Image']))
        
        if count < (len(json_subtitle)-1):
            img_guide = np.float32(PIL.Image.open(json_subtitle[count+1]['Image']))

        if(img_guide is not None):
            last_frame = mydream(img_in, img_guide, random.choice(endChoices),str(count)+'.jpg')
        else:
            last_frame = deepdream(net,base_img=img_in,end='inception_3b/5x5_reduce')
        
        json_subtitle[count]['ImageDeepDream'] = '/code/flask/dream_frames/'+str(count)+".jpg"
        print json_subtitle[count]['ImageDeepDream']
        count += 1

    return json_subtitle

def dreamImage_5(json_subtitle):
    endChoices = []
    endChoices.append("conv2/3x3_reduce")
    endChoices.append("inception_3b/pool_proj")
    endChoices.append("inception_3b/output")
    count = 0
    while count < len(json_subtitle):
        timeBetween = ( (json_subtitle[count]['End']-json_subtitle[count]['Begin'])/5 )
        last_frame = None
        frame_name = ''
        json_subtitle[count]['ImageDeepDream']=[]
        for y in range(5):
            if y == 0:
                img_in = np.float32(PIL.Image.open(json_subtitle[count]['Image']))
            else:
                img_in = np.float32(PIL.Image.open('/code/flask/dream_frames/'+frame_name))
            
            frame_name = str(count) + '_'+ str(y)+'.jpg'
            
            if count < (len(json_subtitle)-1):
                img_guide = np.float32(PIL.Image.open(json_subtitle[count+1]['Image']))
            if(img_guide is not None):
                last_frame = mydream(img_in, img_guide, random.choice(endChoices),frame_name)
            else:
                last_frame = deepdream(net,base_img=img_in,end='inception_3b/5x5_reduce')
            deep_image = {
                "Image": '/code/flask/dream_frames/'+frame_name,
                "Begin": (json_subtitle[count]['Begin']+(timeBetween*y)),
                "End": (json_subtitle[count]['Begin']+(timeBetween*(y+1)))
            }
            json_subtitle[count]['ImageDeepDream'].append(deep_image)
        print json_subtitle[count]['ImageDeepDream']
        count += 1

    return json_subtitle


# def dreamVideo(image_timestamp):
    
#     dream_image_timestamp = []

	
#     i = 0

	
# 	# last_frame = None
#     last_frame = None
# 	# img_in = None
#     img_in = None
# 	# imageGuide = None
#     imageGuide = None
    
#     numero = 0

#     for line in image_timestamp:
#         timeB = (line[2] - line[1])/5

#         endChoices = []
# 		# endChoices = []
#         endChoices.append("conv2/3x3_reduce")
# 		# endChoices.append("conv2/3x3_reduce")
#         endChoices.append("inception_3b/pool_proj")
# 		# endChoices.append("inception_3b/pool_proj")
#         endChoices.append("inception_3b/output")
# 		# endChoices.append("inception_3b/output")
		
#         # timeBetween = ( line[2]-line[1] )

#         if numero > 1 and numero < 4 :
#             for y in range(5):
#                 if(last_frame is None):
#                     img_in = np.float32(PIL.Image.open(line[0]))
                    
#                 else:
#                     img_in = last_frame
                
                
#                 if i < (len(image_timestamp) - 1):
#                     img_guide = np.float32(PIL.Image.open(image_timestamp[i + 1][0]))

#                 img_name = line[0].split('/code/flask/imagens/')[1]
#                 if(img_guide is not None):
                
#                     last_frame = mydream(img_in, img_guide, random.choice(endChoices),img_name+str(y)+".jpg")

#                 else:
#                     last_frame = deepdream(net,base_img=img_in,end='inception_3b/5x5_reduce')
                
#                 dream_image_timestamp.append(['/code/flask/dream_frames/'+img_name+str(y)+".jpg", (line[1]+timeB*y), (line[1]+timeB*(y+1)) ])
#             # numero = numero + 1
#         else:
#             dream_image_timestamp.append(line)
#         i = i + 1
#         numero = numero + 1
# 		# i = i + 1
		
		
#     return dream_image_timestamp

# print 'comecando...'

# image_timestamp = [['/code/flask/imagens/0 1.lefthand.jpg', 167.9, 169.8],['/code/flask/imagens/1 1.writing-number-words-1.jpg', 169.9, 174.1]]
# print 'fotos separadas...'
# dream_image_timestamp = aux_dream(image_timestamp)
# print 'feito o deep dream das fotos:\n'
# print dream_image_timestamp