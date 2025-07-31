m=int(input('Nhập số m: '))
n=int(input('Nhập số n: '))
if m>n:
    Uocchunglonnhat=m%n
    if n%Uocchunglonnhat==0:
        print('Ước chung lớn nhất của',m,'và',n,'là:',Uocchunglonnhat)
else:
    Uocchunglonnhat=n%m
    if m%Uocchunglonnhat==0:
        print('Ước chung lớn nhất của',m,'và',n,'là:',Uocchunglonnhat)