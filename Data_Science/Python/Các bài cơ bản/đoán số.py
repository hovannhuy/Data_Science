import random
a=int(input("Nhập số của bạn: "))
b=random.randint(1, 10)
if a==b:
    print("Chúc mừng! Bạn đã đoán trúng số")
else:
    print("Số đúng là số: ",b)