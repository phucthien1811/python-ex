f = open("Testfile.txt",'r')
print('nhập vào dòng muốn đọc: ')
x = int(input())
lines = f.readlines()
i =0 
while i < x:
    print('nhập vào số dòng muốn đọc:')
    y = int(input())
    i= i + 1 
    

    if 1 <= y <=len(lines):
       print(lines[y-1])
    else:
       print('file không có dòng này')
f.close()