import statistics
# Đọc file input
with open("testfile.txt", "r") as f:
    lines = f.readlines()

# Dòng 1: N
N = int(lines[0].strip())

# Dòng 2: N số nguyên
numbers = list(map(int, lines[1].strip().split()))

# Lọc số chẵn
even_numbers = [num for num in numbers if num > 0]
avg = statistics.mean(even_numbers)

# Ghi file output
with open("output.txt", "w") as f:
     f.write(str(avg))
   
