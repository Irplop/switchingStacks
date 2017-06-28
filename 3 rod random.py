import random

numbiterations = 30 ###########


# for ii in range(10,100,10):
numb = 5 #ii

a = numb
b = numb
c = numb
flag = True
totSum = 0

count = 0


for i in range(numbiterations):

    while flag:
        #random split in 50
        aSplit = random.randint(0,a)
        # bSplit = random.randint(0,50) #b stays the same
        cSplit = random.randint(0,c)

        a = a - aSplit + cSplit
        c = c - cSplit + aSplit

        # print a + c
        #
        # print "a = ",a,"split at ",aSplit
        # print "c = ",c,"split at ",cSplit
        count += 1

        if  c == numb and a == numb:
            flag = False
    totSum += count
    # countArr.append(count)
    # print count
    count = 0
    flag = True
print numb,"\t",totSum,"\t",numbiterations


#
# countSum = 0
# for i in countArr:
#     countSum+= i
# print countSum
# print float(countSum / countArr.__len__())
# print totSum