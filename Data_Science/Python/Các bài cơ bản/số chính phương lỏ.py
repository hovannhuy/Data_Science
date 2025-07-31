n=int(input('nhập số nguyên n:'))
for i in range (n+1):
    if pow(i,2)==n:
        print(n,'là số chính phương')
    else:
        print(n,'không là số chính phương')
    break