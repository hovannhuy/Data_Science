n=int(input('Mời nhập giá trị n: '))
list=[]
for i in range(1,n):
    if n % i==0:
        list.append(i)
print('Các ước của',n,'là:',list)