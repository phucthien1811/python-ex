def get_line(filename, line_number):
    with open(filename, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):  # enumerate đếm từ 1
            if i == line_number:
                return line.strip()   # trả về đúng dòng
    return None  # nếu không có dòng này

# Nhập số lần cần đọc
n = int(input("Nhập vào số dòng muốn đọc: "))

for i in range(n):
    y = int(input(f"Nhập vào số thứ tự dòng muốn đọc lần {i+1}: "))
    line = get_line("DanhSachHS.txt", y)
    if line is not None:
        print(f"Nội dung dòng {y}: {line}")
    else:
        print("File không có dòng này")
