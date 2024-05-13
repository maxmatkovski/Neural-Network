# Creating an Artificial Neural Network from Scratch, with an Application for Time Series Quantitative Trading

## YouTube Series
Explore this topic through our YouTube series: [Neural Networks for Quantitative Trading](https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3)

## Motivation For Project

Having studied deep learning in school, I've been captivated by the operational intricacies of neural networks. Although my coursework laid the foundational understanding, hands-on experience is unrivaled for grasping the true complexities and capabilities of these models. Eschewing high-level frameworks like Keras or TensorFlow, I've embarked on a journey to build a basic neural network from scratch. This project is designed to peel back the often opaque layers of machine learning libraries, exposing the core mechanisms that govern neural computations.

## What even is a Neural Network?

My academic background in Cognitive Science, Neuroscience, Computer Science, and Psychology converge in my fascination with neural networks, the technological nexus of these disciplines. A neural network is a computational model inspired by the brain's structure, designed to recognize patterns and make decisions from input data. Comprising layers of interconnected artificial neurons, these networks adjust their synaptic weights in response to data, akin to biological learning processes. This architecture aims to mimic human learning capabilities, enhancing machine performance across tasks like image recognition, language processing, and decision-making.

![Neural Network Concept](image.png)

**Eventual Goal:** Develop a neural network for trading foreign commodity option contracts.

## Basic Steps of a Neural Network:

### 1. Basic Structure
- **Input Layer**: Receives the input data.
- **Hidden Layers**: Consist of multiple layers that process the input through weighted connections.
- **Output Layer**: Produces the final prediction or classification, e.g., classifying between a cat or a dog using two neurons.

### Key Concepts and Terminology:
- **Neural Network Model**: Resembles a network where data flows from the input layer through multiple hidden layers to the output layer.
- **Training Process**: Involves tuning the "weights and biases" to refine the model's predictions.

![Neural Network Parameters](images/image.png)

- **Parameters**: Note that the number of parameters can grow significantly, influencing computational complexity.
- **Arrays and Shape**: Inputs and outputs must be homogenously shaped to ensure proper matrix operations.

### Common Array Structures:

**1D Array (Vector):**
- Example: [1, 5, 6, 2]
- Shape: (4,)

**2D Array (Matrix):**
- Example:
[[1, 5, 6, 2],
[3, 2, 1, 3]]

- Shape: (2, 4)

### Dot Product and Batching:
- **Dot Product**: Essential for calculating the weighted sum of inputs and weights; order matters due to matrix dimensions.
- **Batching**: Improves training efficiency by leveraging parallel computation capabilities of GPUs, which significantly outnumber those in CPUs. Optimal batch sizes (e.g., 32, 64, or 128) balance the risks of overfitting and underfitting.

### Activation Functions:
- **Step Function**: Binary output.
- **Sigmoid Function**: Continuous output between 0 and 1, providing granularity.
- **ReLU (Rectified Linear Unit)**: Offers computational efficiency and is preferred in many modern networks.

#### Further Exploration:
- **Softmax Function**: Used for multi-class categorization, applying exponentiation and normalization to convert logits to probabilities.


