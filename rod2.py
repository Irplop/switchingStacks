from decimal import Decimal


a = 10
b = 10


for i in range(a):
    print a*b, "\t",min(b,a), Decimal(min(a,b) / (a*b))
    a+=1
    b-=1

