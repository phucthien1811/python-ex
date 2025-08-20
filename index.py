n = int(input('nhập vào n: '))
tong = 0
for i  in range(1, n):
    if n % i == 0:
        tong += i

if tong == n:
    print(f'{n} là số hoàn hảo')
else:
    print(f'{n} không phải là số hoàn hảo')  
