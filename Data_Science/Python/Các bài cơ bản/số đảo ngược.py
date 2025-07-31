def daonguocsonguyen(n):
    sodaonguoc=0
    while n>0:
        digit=n%10
        sodaonguoc=sodaonguoc*10+digit
        n=n//10
    return sodaonguoc
n=int(input('Nhập số của bạn: '))
daonguoc= daonguocsonguyen(n)
print('Số đảo ngược của n là: ',daonguoc)