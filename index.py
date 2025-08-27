def tinhgiaithua(n):
    if n==0 or n ==1:
        return 1
    return n * tinhgiaithua(n-1)
         
   


a = int(input('nhap vao n: '))

ketqua = tinhgiaithua(a)
print(ketqua)
 