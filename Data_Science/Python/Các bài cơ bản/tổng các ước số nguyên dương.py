n=int(input('Mời nhập giá trị n: '))
S=0
for i in range(1,n):
    if n % i==0:
        S=S+i
print('Tổng các ước số nguyên dương của',n,'là:',S)