a=input("nhập chuỗi của bạn: ")
b=''
c=''
for i in a: 
    if i == "#":
        b+=" "
    else:
        b+=i
b=b.split()
print(b)5