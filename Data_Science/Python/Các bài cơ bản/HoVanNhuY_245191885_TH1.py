#bài 7
def demkitu(D,S):
    D={}
    for char in S:
        D[char]=D.get(char,0)+1
    return D
#bài 8
def tinhtong(D):
    return sum(D)
#bài 9
import math
def tinhtich(S):
    return math.prod(S)
#bài 10
def giatrilonnhat(S):
    return max(S)
#bài 11
def lasole(S):
    A=[]
    for i in S:
        if i%2!=0:
            A.append(i)
    print(f'Các số lẻ trong danh sách là: {x for x in A}')
#bài 12
def lasochan(S):
    A=[]
    for i in S:
        if i%2==0:
            A.append(i)
    print(f'Các số chẵn trong danh sách là: {x for x in A}')
#bài 13
ds_con_vat = {"chó": 4, "mèo": 4, "gà": 2, "vịt": 2, "bò": 4, "cá": 0, "rắn": 0, "ngựa": 4}
ds_con_vat_4_chan=[ten for ten,chan in ds_con_vat.items() if chan==4]
print(f'Các con vật có 4 chân là: {ds_con_vat_4_chan}')
#bài 14
def hieu100(lst):
    hieu=[100 - so for so in lst]
    return hieu
#bài 15
def chiahetcho2(lst):
    chiahetcho2=[so for so in lst if so%2==0]
    return chiahetcho2