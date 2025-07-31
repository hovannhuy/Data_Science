import math
a=int(input('Nhập a: '))
b=int(input('Nhập b: '))
c=int(input('Nhập c: '))
denta=pow(b,2)-4*a*c
if denta<0:
    print('Phương trình vô nghiệm')
elif denta==0:
    x1=x2=-b/(2*a)
    print('Phương trình có nghiệm kép x1=x2= ',x1)
else:
    x1=((-b+math.sqrt(denta))/(2*a))  
    x2=((-b-math.sqrt(denta))/(2*a))
    print('Phương trình có 2 nghiệm phân biệt, x1= ',x1,'x2= ',x2)