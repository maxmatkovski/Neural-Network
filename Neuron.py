# coding neural net from scratch
inputs = [1,2,3,2.5] # input features

 # multiplicative relationship with the input value
weights1 = [.2,.8,-.5,1.0]
weights2 = [.5,-.91,.26,-.5]
weights3 = [-.26, -.27,.17,.87]

bias1 = 2
bias2 = 3
bias3 = .5

# simple pass forward calculation function
def pass_forward(inputs,weights,bias):
    output = 0
    for i in range(len(inputs)):
        output += (inputs[i]*weights[i])
    output += bias
    return output

result1 = pass_forward(inputs,weights1,bias1)
result2 = pass_forward(inputs,weights2,bias2)
result3 = pass_forward(inputs,weights3,bias3)


final_result = [result1,result2,result3]
print(final_result)


