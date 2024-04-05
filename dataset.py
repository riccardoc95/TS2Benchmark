import numpy as np
from sklearn.datasets import fetch_openml
import os


def load_mnist():
    mnist = fetch_openml('mnist_784', version=1, cache=True, parser='auto')
    X = mnist.data
    y = mnist.target.astype(np.uint8)
    return X, y

def load_cifar10():
    cifar = fetch_openml('CIFAR_10', version=1, cache=True, parser='auto')
    X = cifar.data
    y = cifar.target.astype(np.uint8)
    return X, y


if not os.path.exists("data/MNIST"):
    os.makedirs("data/MNIST")
if not os.path.exists("data/CIFAR10"):
    os.makedirs("data/CIFAR10")


X, y = load_mnist()
for i, train_image in enumerate(X):
    np.save(f"data/MNIST/{i + 1}.npy", train_image)
    
X, y = load_cifar10()
for i, train_image in enumerate(X):
    np.save(f"data/CIFAR10/{i + 1}.npy", train_image)
