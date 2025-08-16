# Đọc file input
with open("testfile.txt", "r") as f:
    lines = f.readlines()

# Dòng 1: N
N = int(lines[0].strip())

# Dòng 2: N số nguyên
numbers = list(map(int, lines[1].strip().split()))

# Lọc số chẵn
even_numbers = [str(num) for num in numbers if num % 2 == 0]
print(even_numbers)
print(type(even_numbers))

# Ghi file output
with open("output.txt", "w") as f:
    f.write(" ".join(even_numbers))
