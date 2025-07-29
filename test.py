# Ghi vào file
with open('kkk.py', 'w') as file:
    file.write('phuc thien dep trai')

# Đọc lại file vừa ghi
with open('kkk.py', 'r') as file:
    data = file.read()

print(data)  # In ra nội dung đã ghi
