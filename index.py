f = open("Testfile.txt",'r')
print('nhập vào dòng muốn đọc: ')
n = int(input())
lines = f.readlines()
for i in range(n):
    y = int(input(f"Nhập vào số thứ tự dòng muốn đọc lần {i+1}: "))
    if 1 <= y <=len(lines):
       print(lines[y-1])
    else:
       print('file không có dòng này')
f.close()