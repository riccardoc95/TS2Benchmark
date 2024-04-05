import numpy as np
import numpy_dataset
import os

if not os.path.exists("data/temp"):
    os.makedirs("data/temp")
if not os.path.exists("data/MNIST"):
    os.makedirs("data/MNIST")
if not os.path.exists("data/CIFAR10"):
    os.makedirs("data/CIFAR10")

train_images, train_labels, valid_images, valid_labels, \
test_images, test_labels  = numpy_datasets.images.mnist.load(path="data/temp")

for i, train_image in enumerate(train_images):
    np.save("")

train_images, train_labels, test_images, test_labels \
= numpy_datasets.images.cifar10.load(path="data/temp")





