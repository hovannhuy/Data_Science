import math
list=[]
count=0
a=int(input('Nhập số lá bài: '))
for i in range(1,a+1):
    n=input()
    list.append(n)
for i in list:
    for a in list:
        c=abs(int(str(a)) -int(str(i)))
        if c<=1:
            count+=1
print(count)
           
           

           
