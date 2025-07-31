import string
def kiemtra(matkhau):
    chu_thuong=chu_hoa=so=ki_tu=do_manh= 0
    matkhau=list(matkhau)
    for i in matkhau:
        if i in string.ascii_letters:
            ki_tu+=1
        if i in string.ascii_lowercase:
            chu_thuong+=1
        if i in string.ascii_uppercase:
            chu_hoa+=1
        if i in string.digits:
            so+=1
    if so>=1:
        do_manh+=1
    if ki_tu>=8:
        do_manh+=1
    if chu_hoa>=1:
        do_manh+=1
    if chu_thuong>=1:
        do_manh+=1
    return do_manh

a=input("Nhập mật khẩu của bạn: ")
s= kiemtra(a)
print("Độ mạnh của mật khẩu là: ", s,"/4")