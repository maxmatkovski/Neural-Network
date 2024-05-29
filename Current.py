import math
softmax_output = [.7,.1,.2]

# one hot encoding just tells us what correct target variable is
target_output = [1,0,0]

loss = -(math.log(softmax_output[0]) * target_output[0] +
         math.log(softmax_output[1]) * target_output[1] +
         math.log(softmax_output[2]) * target_output[2])

print(loss)
print(-math.log(.7))