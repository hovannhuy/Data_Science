import math
n=int(input('Mời nhập giá trị n: '))
a=True
for i in range(1,n):
    if pow(i,2)==n:
        a=True
    else:
        a=False
if a==True:
    print(n,'là số chính phương')
else:
    print(n,'là số chính phương')