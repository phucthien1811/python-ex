#Khoi lenh co the phat sinh loi
try:
    #Nhap gia tri tu ban phim
    #Ep kieu du lieu sang so nguyen
    n = int(input())
    
    #Su dung cau truc re nhanh xu ly truong hop n < 0
    if n < 0:
        print("Vui long nhap so tu nhien!")
    else:
        soDaoNguoc = 0
        #Su dung vong while de tach cac chu so
        while n > 0:
            chuSoCuoi = n % 10
            soDaoNguoc = soDaoNguoc * 10 + chuSoCuoi
            n = n // 10
        print(soDaoNguoc)
        
#Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")