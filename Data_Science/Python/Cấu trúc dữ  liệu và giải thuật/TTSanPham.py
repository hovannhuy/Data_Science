class SanPham:
    def __init__(self, tensp=None, loaisp=None, giaban=None):
        self.tensp = tensp
        self.loaisp = loaisp
        self.giaban = giaban
    def Nhaptt1sp(self):
        self.tensp = input("Nhap ten san pham: ")
        self.loaisp = input("Nhap loai san pham: ")
        self.giaban = int(input("Nhap gia ban: "))
    def xuattt1sp(self):
        print(f'Tên sản phẩm: {self.tensp}, Loại sản phẩm: {self.loaisp}, Giá bán: {self.giaban}')
def nhapn():
    while True:
        n = int(input("Nhap so luong san pham: "))
        if n >0:
            break
    return n
def nhapds(n,lst):
    for i in range(n):
        sp = SanPham()
        print(f'Nhap thong tin san pham thu {i+1}: ')
        sp.Nhaptt1sp()
        lst.append(sp)
    return lst
def xemds(lst):
    print('Danh sach san pham: ')
    for i in range(len(lst)):
        lst[i].xuattt1sp()
def giamdanteninsert(lst):
    for i in range(1,len(lst)):
        k=lst[i]
        pos=i-1 
        while pos>=0 and lst[pos].tensp<k.tensp:
            lst[pos+1]=lst[pos]
            pos-=1
        lst[pos+1]=k
def timnhiphan(lst,x):
    left=0 
    right=len(lst)-1
    while left<=right:
        mid=(left+right)//2
        if lst[mid].tensp==x:
            return mid
        elif lst[mid].tensp>x:
            right=mid-1
        else:
            left=mid+1
    return -1
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def InsertFirst(self,x):
        new_node=Node(x)
        new_node.next=self.head
        self.head=new_node
    def InputList(self):
        n=int(input("Nhap so luong san pham: "))
        for i in range(n):
            x=SanPham()
            x.Nhaptt1sp()
            self.InsertFirst(x)
    def giatrungbinh(self):
        p=self.head
        sum=0
        count=0
        while p is not None:
            sum+=p.data.giaban
            count+=1
            p=p.next
        if count==0:
            return 0
        return sum/count
    def showlist(self):
        p=self.head
        while p is not None:
            p.data.xuattt1sp()
            p=p.next
    def DelBeforX(lst,x):
        if self.head is None:
            print("Danh sach rong")
            return
        prev=None
        current=self.head
        nextnode = self.head.next
        while nextnode is not None:
            if nextnode.data.tensp==x:
                if prev is None:
                    self.head=current.next
                else:
                    prev.next=current.next
                print('Da xoa thanh cong')
                return
            prev=current
            current=nextnode
            nextnode=nextnode.next
        print('Khong tim thay')
def main():
    lst=[]
    l=LinkedList()
    n=nhapn()
    nhapds(n,lst)
    xemds(lst)
    giamdanteninsert(lst)
    xemds(lst)
    x=input("Nhap ten san pham can tim: ")
    result=timnhiphan(lst,x)
    if result==-1:
        print('Khong tim thay')
    else:
        print(f'Tim thay tai vi tri {result}')
    l.InputList()
    giatb=l.giatrungbinh()
    x=input("Nhap ten san pham can xoa: ")
    l.DelBeforX(x)
if __name__=='__main__':
    main()