def hoandoi(a,b):
    a=a+b
    b=a-b
    a=a-b    
    return a,b
a=float(input('Nhập số thứ nhất: '))
b=float(input("Nhập số thứ hai: "))
a,b=hoandoi(a,b)
print("số đầu tiên là: ",a,"\n số thứ hai là: ",b)