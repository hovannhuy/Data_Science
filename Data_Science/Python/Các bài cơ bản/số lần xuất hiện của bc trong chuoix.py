s=input("nhập chuỗi của bạn: ")
a=''
for i in s:
    if i =="b":
        a+="b"
    elif i =="c":
        a+="c"
    else:
        a+=" "
c=a.split()
print("Số lần chuỗi bc xuất hiện là: ",c.count("bc"))