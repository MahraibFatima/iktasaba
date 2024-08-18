# Flattening and Softmax in Deep Learning

## 1. Flattening

### Introduction
Flattening is a process in deep learning where multi-dimensional input data is transformed into a one-dimensional vector. It is typically used in the transition between convolutional layers and fully connected layers in a neural network.

### Definition
- **Flattening**:
  - Flattening involves taking a multi-dimensional tensor, such as a 2D matrix or a 3D tensor, and converting it into a single-dimensional vector.
  - For example, if the output of a convolutional layer is a 3D tensor with dimensions (height, width, depth), flattening will convert this tensor into a vector of length `height * width * depth`.

### Purpose
- **Transition from Convolutional to Fully Connected Layers**:
  - In Convolutional Neural Networks (CNNs), after the convolution and pooling layers, the data is typically flattened before being fed into fully connected layers.
  - Flattening allows the network to process the multi-dimensional output of convolutional layers as input to the dense layers that follow.

### Example
- If the output of a pooling layer is a tensor of shape `(7, 7, 64)`, flattening this would result in a vector of length `7 * 7 * 64 = 3136`.

### Applications
- Flattening is commonly used in CNN architectures like LeNet, AlexNet, and VGG, where the feature maps are flattened before passing through fully connected layers leading to the output.
