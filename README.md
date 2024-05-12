# Creating an Artificial Neural Network from Scratch, with an Application For Time Series Quantitative Trading

![alt text](images/image-1.png)  

YouTube Series: https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3

## Basic Steps of Neural Network:
### 1. Basic Structure
- Input Layer: Receives input data.
- Hidden Layers: Multiple layers that process the input through weighted connections.
- Output Layer: Produces the final prediction or classification.

![alt text](images/image-1.png)  

- called neural network because it looks like a network 
- data starts at input layer
- input --> hidden layer 1 --> hidden layer 2 --> output layer

- if we're classifying cat or dog, we will have two output neurons
- tuning the "weights and biases" is the process of training the neural network

- each connection == weight
- each neuron == bias

![alt text](images/image.png)

- as we can see the amount of parameters can grow to huge amounts

- inputs can be from the input layer, but they can also be outputs from other neurons

- weights have a multiplicative effect
- biases have an additive effect

- arrays need to be homologous, meaning at each dimension they need to have the same size

#### talking about shape
- common to get shape errors in deep learning problems

array: 1 = [1,5,6,2]
shape: (4,)
type: 1d array, vector

array: [[1,5,6,2],
        [3,2,1,3]] (list of lists)
shape: (2,4)
type: 2d array, matrix

- a tensor is an object *that can be represented as an array*

#### dot product
a = [1,2,3]
b = [2,3,4]

dot_product = (a[0] x b[0]) + (a[1] x b[1]) + (a[2] x b[2])
dot_product >> 20