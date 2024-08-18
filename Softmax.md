## 2. Softmax

### Introduction
Softmax is an activation function that is typically used in the output layer of a classification neural network. It converts raw logits into probabilities, where the sum of all probabilities is 1.

### Definition
- **Softmax Function**:
  - The softmax function is defined as:
    \[
    \text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}
    \]
    where \(z_i\) are the logits (input values) and \(K\) is the number of classes.
  - It exponentiates each input value and then normalizes them by the sum of all the exponentiated values.

### Properties
- **Probability Distribution**:
  - The output of the softmax function is a vector of values between 0 and 1 that sum to 1. This makes it suitable for multi-class classification tasks, where each output can be interpreted as the probability of belonging to a particular class.

- **Differentiability**:
  - Softmax is differentiable, which allows for gradient-based optimization methods like backpropagation to be used during training.

### Use Cases
- **Multi-Class Classification**:
  - Softmax is often used in the final layer of a neural network to classify inputs into multiple categories. Each neuron in the output layer represents a different class, and softmax converts the logits into probabilities for these classes.
  - Common examples include image classification tasks like recognizing handwritten digits (MNIST) or objects in images (CIFAR-10).

### Example
- In a neural network trained to classify images of digits (0-9), the softmax output would consist of 10 values, each representing the probability that the input image belongs to one of the 10 classes.

### Limitations
- **Sensitivity to Large Logits**:
  - Softmax can be sensitive to the scale of the logits, potentially leading to very confident predictions even when the model is uncertain. This can be mitigated by techniques like temperature scaling.
- **Interpretation as Probability**:
  - While softmax outputs are often interpreted as probabilities, this interpretation assumes the model is well-calibrated, which might not always be the case.

