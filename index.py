def sohoanthien(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong+=i
    if tong == n:
        return "{} là số hoàn thiện ".format(n)
    else :
        return "{} không phải là số hoàn thiện".format(n)


n = int(input('Nhập vào số N: '))

ketqua = sohoanthien(n)
print(ketqua)
