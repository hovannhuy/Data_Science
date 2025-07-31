a=int(input('Nhập a: '))
b=int(input('Nhập b: '))
if a==0:
    if b!=0:
        print('Phương trình vô nghiệm')
    else:
        print('Phương trình có vô số nghiệm')
else:
    x=-b/a
print(x,'là nghiệm của phương trình')