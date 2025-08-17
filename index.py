# Nhập dòng k cần lấy
k = int(input("Nhập số nguyên k (dòng cần lấy): "))

# Đọc toàn bộ file input
with open("TBCINP4.txt", "r") as f:
    lines = f.readlines()

# Kiểm tra k có hợp lệ không
if 1 <= k <= len(lines):
    # Lấy đúng dòng thứ k
    line = lines[k-1].strip()   # vì list tính từ 0
    numbers = list(map(int, line.split()))
    avg = sum(numbers) / len(numbers)

    # Ghi ra file output
    with open("TBCOUT4.txt", "w") as f:
        f.write(str(avg) + "\n")
    print("Đã ghi kết quả vào TBCOUT4.txt")
else:
    print("Dòng thứ", k, "không tồn tại trong file!")
