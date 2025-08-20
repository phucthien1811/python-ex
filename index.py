#Khoi lenh co the phat sinh loi
try:
    #Nhap gia tri tu ban phim
    #Ep kieu du lieu sang so nguyen
    n = int(input())
    
    #Su dung cau truc re nhanh xu ly truong hop n < 0
    if n < 0:
        print("Vui long nhap so tu nhien!")
    else:
        tongChuSoChan = 0
        tongChuSoLe = 0
        #Su dung vong while de tach cac chu so
        while n > 0:
            #Kiem tra chu so cuoi la chan hay le
            if n % 2 == 0:
                tongChuSoChan += n % 10
            else:
                tongChuSoLe += n % 10
            n = n // 10

        ketQua = tongChuSoChan * tongChuSoLe
        print(ketQua)
        
#Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")