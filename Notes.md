# CREATING NEURAL NET FROM SCRATCH

import numpy as np

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        
    # - initiliaze weights and biases
    # - weights have a multiplicative effect (*)
    # - biases have an additive effect (+)

    # - generates matrix of random values sampled from a standard normal 
    # - distribution (mean 0, variance 1)
    # - dimensions of the matrix are n_inputs x n_neurons 

    # - neuron has a unique weight that begins with a random small value 
    #     - here we are also multiplying by 0.1 to scale down the weights to a smaller range 
    #     and avoid values that might range quite broadly as a result of random.randn output
    #         - having smaller weights ensures that the network starts with smaller values and
    #         prevents any one neuron from dominating early on
    #         - if the outputs are too large to begin with, the outputs could saturate the actiavtion function (especially non-linear activations like sigmoid or ReLu) --> leading to issues such as vanishing / exploding gradient
        
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
  
- this portion initliazes the biases for each neuron to zero
- unlike weights, biases are typically initialized to zero 
    
    
        self.biases = np.zeros((1,n_neurons))
        


