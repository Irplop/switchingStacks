import random

numbiterations = 1000000 ###########


# for ii in range(10,100,10):
numb = 10 #ii

a = numb
b = numb
c = numb
flag = True
totSum = 0

count = 0

while flag:
    aSplit = random.randint(0,a)
    cSplit = random.randint(0,c)

    print "====Step ", count,"===="
    print "a = ",a,"split at ",aSplit
    print "c = ",c,"split at ",cSplit
    print
    a = a - aSplit + cSplit
    c = c - cSplit + aSplit

    # print a + c
    #

    count += 1

    if  c == numb and a == numb:
        flag = False
totSum += count
# countArr.append(count)
# print count
count = 0
flag = True


#
# countSum = 0
# for i in countArr:
#     countSum+= i
# print countSum
# print float(countSum / countArr.__len__())
# print totSum