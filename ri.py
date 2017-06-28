
### PRINTS OUT THE SUCCESSES

# sum = 0
# success = ''
#
# for bigN in range(1, 1000):
#     print '--- '+str(bigN)+' ---'
#
#     for i in range(1, bigN):
#         while sum < bigN:
#             success = success + str(i) +  ', '
#             sum += i
#             i += 1
#
#             if sum == bigN:
#                 print success
#                 success = ''
#         success = ''
#         # print ' = ', sum
#         # print '-----'
#         sum = 0
#





### PRINTS OUT THE NUMBER OF SUCCESSES

sum = 0
success = ''
numbSuccess = 0
succList = list(1000)

for bigN in range(1, 1000):

    for i in range(1, bigN):
        while sum < bigN:
            success = success + str(i) +  ', '
            sum += i
            i += 1 ######
            if sum == bigN:
                numbSuccess += 1
        sum = 0

    succList.append(numbSuccess)
    print str(bigN), ',' , str(numbSuccess)
    numbSuccess = 0

succList.sort()

