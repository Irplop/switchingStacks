from __future__ import print_function
import numpy as np


# This generates the ABSORBING markov matrix using the pattern realized from the Counting algorithm
# See Rod Markov - Counting to see how I realized the pattern

size = 10 #########

x = size * 2 + 1

### Numerators only
# for i in range(size+1):
#     for j in range(size+1):
#         if j == size:
#             print(0),
#         else:
#             if j < i:
#                 print((j+1)*2,"\t",end='')
#             else:
#                 print((i+1)*2,"\t",end='')
#
# print("\n")


### Denominator Only

# for i in range(size+1):
#     print(x)
#     # print (((size)*2)-i)
#     # print (size*2-2*i-1)
#
#     x += (size*2-2*i-1)


### Print Fractions

x = size * 2 + 1

for i in range(size+1):
    for j in range(size+1):
        if j == size:
            print(0),
        else:
            if j < i:
                print((j+1)*2,"/",x,"\t",sep='',end='')
            else:
                print((i+1)*2,"/",x,"\t",sep='',end='')

    x += (size*2-2*i-1)

# load matrix

matrixQ = np.zeros(shape=(size+1,size+1))
x = size * 2 + 1

for i in range(size+1):
    for j in range(size+1):
        if j < i:
            matrixQ[i,j] = float((j+1)*2) / float(x)
        else:
            matrixQ[i,j] = float((i+1)*2) / float(x)

    x += (size*2-2*i-1)




# print(matrixQ)

identity = np.asmatrix(np.identity(size + 1))

S = np.linalg.inv(identity - matrixQ)

one = np.mat([[1] for i in range(size + 1)])

finalStates = np.dot(S, one)

answer = finalStates.item(size)
print(size, "\t", answer)
