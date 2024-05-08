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