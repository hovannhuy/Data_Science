def find_square_number(n):
    #flag = 1 => số chính phương
    #flag = 0 => không phải số chính phương

    flag = 0;
    #Tìm số bất kỳ nhỏ hơn hoặc bằng n mà bình phương bằng n
    if any(i**2 == n for i in range(n+1)):
        flag = 1
    return flag


n = int(input(">> nhap mot so tu nhien: "))
check = find_square_number(n);
 
if check == 1:
    print(n,"la so chinh phuong")
else:
    print(n,"khong phai la so chinh phuong")