f = open("Testfile.txt",'r')
print('nhập vào dòng muốn đọc: ')
x = int(input())


lines = f.readlines()

if 1 <= x <=len(lines):
    print(lines[x-1])
else:
    print('file không có dòng này')
f.close()