n=int(input('Mời nhập giá trị n: '))
S=0
for i in range(1,n):
    if n % i==0:
        S=S+i
if S==n:
    print(n,'là số hoàn thiện')
else:
    print(n,'không phải số hoàn thiện') 