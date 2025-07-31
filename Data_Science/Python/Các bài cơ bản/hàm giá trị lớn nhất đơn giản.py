a=int(input('Nhập số a:'))
b=int(input("Nhập số b:"))
c=int(input('Nhập số c: '))
if a>b and a>c:
    print(a,'là số lớn nhất')
elif b>a and b>c:
    print(b,'là số lớn nhất')
else:
    print(c,'là số lớn nhất')