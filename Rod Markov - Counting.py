from __future__ import print_function
import numpy as np
from fractions import Fraction
from decimal import Decimal

for size in range(10, 11):

    # size = 10 ######################

    # print("For Rod Size",size,"\n\n")
    a = size
    b = size

    markov = [[0 for x in range(size+2)] for y in range(size+1)]
    #  from 0,4   [ 0,4     1,3     2,2     sum ]
    #  from 1,3   [ 0,4     1,3     2,2     sum ]
    #  from 2,2   [ 0,4     1,3     2,2     sum ]



    count = 0
    for i in range(0, a+1):  # i is amount to take from a
        # print("\nDoing for ",a,b)

        small = min(a,b)
        large = max(a,b)

        for j in range(small+1):
            for k in range(large+1):
                count +=1
                tempSmall = small-j+k
                tempLarge = large+j-k

                # print tempSmall,tempLarge,"\t from ",j,k

                markov[b][min(tempSmall,tempLarge)] +=1

        markov[b][size+1] = (small+1)*(large+1)

        a += 1
        b -= 1


    # print(markov)

    # print(count)

    # print("\n")

    # print matrix with fractions
    # for i in range(size+1):
    #     # print(markov[i][size+1], "\t", sep='', end='')                           # print only the denominator
    #     for j in range(size+1):
    #         print(markov[i][j],"\t", sep='', end='')                      # print only the numerator
    #         # print(markov[i][j],"/",markov[i][size+1],"\t", sep='', end='')  # print as a fraction
    #     print()



    matrixQ = [[0 for x in range(size+1)] for y in range(size+1)]

    for i in range(size+1):
        for j in range(size):
            # print(matrixQ[i][j],"/",markov[i][size+1]," ", sep='', end='')    ######## PRINTS MATRIX (NON-ABSORBING)
            matrixQ[i][j] = float(markov[i][j]) / float(markov[i][size+1])


    npMatrixQ = np.asmatrix(matrixQ)

    ############### Start Matrix Operations
    # Q is the state transitions excluding the absorbing state
    # identity is the identity matrix
    # one is a vertical Ones matrix (sums the last row of the matrix)
    # answer =   ( (I-Q)^-1 )One    and is the last entry in that vecor


    # Q = np.mat([[0.4, 0.4, 0],
    #               [0.25, 0.5, 0],
    #               [0.2222222, 0.4444444, 0]])

    identity = np.asmatrix(np.identity(size+1))
    # R = np.subtract(identity, npMatrixQ)
    R = identity - npMatrixQ

    # print("identity= ",identity)
    # print("npMatrix= ",npMatrixQ)
    #

    # print(Q)
    # print(R)

    S = np.linalg.inv(R)
    # print ("S = ", S)


    one = np.mat([[1] for i in range(size+1)])

    finalStates = np.dot(S,one)
    # print(finalStates)

    answer = finalStates.item(size)
    print(size,"\t",answer)

