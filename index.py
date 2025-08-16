with open("testfile.txt", "r") as f:
    lines = f.readlines()

line1 = lines[0].strip()
print(line1)   # lấy dòng 1
print(type(line1))  # kiểm tra kiểu dữ liệu của dòng 1
numbers = line1.split()  
print(type(numbers))  # kiểm tra kiểu dữ liệu của numbers
print(numbers)  # ???  bước này sẽ ra gì
nums = list(map(int, numbers))
print(nums)
print(type(nums))  # ???  thử in ra xem
total = sum(nums)          # ???  cuối cùng ta có gì
print('tong cua minh la: ',total)
