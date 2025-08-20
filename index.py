def is_prime(num):
    if num <= 1:
        return False
    if num == 2:     # 2 là số nguyên tố duy nhất chẵn
        return True
    if num % 2 == 0: # loại bỏ các số chẵn > 2
        return False
    for i in range(3, int(num**0.5) + 1, 2):  # duyệt số lẻ
        if num % i == 0:
            return False
    return True

# Nhập từ bàn phím
n = int(input("Nhập vào n: "))

# Kiểm tra và in kết quả
if is_prime(n):
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không phải là số nguyên tố")
