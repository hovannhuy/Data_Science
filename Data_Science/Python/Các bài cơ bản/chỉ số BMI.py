import math
def kiemtra(a,b):
    BMI=a/pow(b,2)
    return BMI

chieu_cao=float(input("nhập chiều cao (m): "))
can_nang=float(input("nhập chiều cao (m): "))
BMI= kiemtra(chieu_cao,can_nang)
if BMI<=16:
    print('Gầy cấp độ 3')
elif BMI>=16 and BMI<= 17:
    print("Gầy cấp độ 2")
elif BMI>=17 and BMI <= 18.5:
    print("Gầy cấp độ 1")
elif BMI>=18.8 and BMI <= 25:
    print("Bình thường")
elif BMI >=25 and BMI <= 30:
    print("thừa cân")
elif BMI>= 30 and BMI<=35:
    print("Béo phì cấp độ 1")
elif BMI>=35 and BMI<=40:
    print("Béo phì cấp độ 2")
elif BMI>40:
    print("Béo phì cấp độ 3")