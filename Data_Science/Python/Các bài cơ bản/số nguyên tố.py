import math
n=int(input('nhập số nguyên: '))
def songuyento(n):
    if n<=1:
        print(n,'không phải là số nguyên tố')
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i ==0:
                return False
    return True
if songuyento(n):
    print(n,'là số nguyên tố')
else:
    print(n,'không phải là số nguyên tố')