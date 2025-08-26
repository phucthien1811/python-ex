a = int(input('nhaap vao a: '))
b= int (input('nhap vao b: '))
if a < 2:
    print('khong co so nguyen to')
if  a == 2:
    print('2 la so nguyen to')
for i in range(3,b+1):
    if i % 2 == 0:
        continue
    elif i > 2 :
        for j in range(3,i,2):
            if i % j == 0:
                break
        else:
            if i >= a:
                print(i,'la so nguyen to')
