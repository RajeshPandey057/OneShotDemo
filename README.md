# OneShotDemo
This is a forked project of siamese mask R-CNN for demonstration purpose.(https://github.com/bethgelab/siamese-mask-rcnn)
# One-Shot Instance Segmentation
One-shot instance segmentation can be summed up as: Given a query image and a reference image showing an object of a novel category, we seek to detect and segment all instances of the corresponding category (in the image above ‘person’ on the left, ‘car’ on the right). Note that no ground truth annotations of reference categories are used during training. This type of visual search task creates new challenges for computer vision algorithms, as methods from metric and few-shot learning have to be incorporated into the notoriously hard tasks ofobject identification and segmentation. Siamese Mask R-CNN extends Mask R-CNN - a state-of-the-art object detection and segmentation system - with a Siamese backbone and a matching procedure to perform this type of visual search.
# Installation
Open python notebook file and do as directed in notebook text cells
For best results, run in google colab.
You can also run py file directly in supported environment (Prone to erros hence Not recommended)
# Requirements
Linux, Python 3.4+, Tensorflow, Keras 2.1.6, cython, scikit_image 0.13.1, h5py, imgaug and opencv_python
