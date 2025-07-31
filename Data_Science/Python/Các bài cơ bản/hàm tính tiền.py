def tinhtong(list1):
    a=0
    for i in list1:
        a+= int(i)
    return a
def hienthi(a):
    if a > 100:
        print("Miễn phí ship")
    else:
        print("Phí ship là 15000đ")
    pass
s=input("Nhập tiền từng đơn hàng; ").split(",")
c=tinhtong(s)
print("Tổng tiền là: ", c)
print(hienthi(c))