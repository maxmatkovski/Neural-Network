# coding neural net from scratch
inputs = [1.2, 5.1, 2.1] # input features
weights = [3.1,2.1,8.7] # multiplicative relationship with the input value
bias = 3

# simple pass forward calculation
output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias

print(output)
