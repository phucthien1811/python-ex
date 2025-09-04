def liet_ke_so_hoan_thien(n):
    ket_qua = []
    for num in range(2, n+1):   # duyệt từ 2 đến n
        tong = 0
        for i in range(1, num):
            if num % i == 0:
                tong += i
        if tong == num:
            ket_qua.append(num)
    return ket_qua

# Ví dụ chạy
n = 10000
print(f"Các số hoàn thiện <= {n}: {liet_ke_so_hoan_thien(n)}")
