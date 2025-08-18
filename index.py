a, b, c = input('Nhập vào phép tính: ').split()

a = float(a)
c = float(c)

if b == '+':
    print(a + c)
elif b == '-':
    print(a - c)
elif b == '*':
    print(a * c)
elif b == '/':
    if c != 0:
        print(a / c)
    else:
        print("Lỗi: Không thể chia cho 0")
elif b == '**':
    print(a ** c)
elif b == '%':
    if c != 0:
        print(a % c)
    else:
        print("Lỗi: Không thể chia cho 0")
elif b == '//':
    if c != 0:
        print(a // c)
    else:
        print("Lỗi: Không thể chia cho 0")
else:
    print("Phép toán không hợp lệ")
