def tinh_tong(n):
   if n:
       return n + tinh_tong(n - 1)
   return 0
try:
    n = int(input("nhập số nguyên dương n:"))
    if n < 0:
        print("vui lòng nhập số nguyên dương")
    else:
        print(f"Tổng các số từ 1 đến {n} là: {tinh_tong(n)}")
except ValueError:
    print("vui lòng nhập số nguyên hợp lệ")
        
