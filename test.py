# --- BÀI TẬP ĐẦU TIÊN: CHƯƠNG TRÌNH CHÀO HỎI ---

# Dòng này in ra một câu giới thiệu (đây là OUTPUT)
print("--- chao mung ban! ---")

# Dòng này hỏi tên người dùng và chờ họ nhập vào.
# Dữ liệu người dùng nhập sẽ được lưu vào biến `ten` (đây là INPUT)
ten = input("ban ten la gi? ")

# Hỏi năm sinh của người dùng
nam_sinh_str = input("ban sinh nam bao nhieu ? ")

# Đổi kiểu dữ liệu của năm sinh từ chữ (string) thành số (integer) để tính toán
# Vì hàm input() luôn trả về kiểu chữ.
nam_sinh_so = int(nam_sinh_str)

# Lấy năm hiện tại để tính tuổi
nam_hien_tai = 2025
tuoi = nam_hien_tai - nam_sinh_so

# In ra câu chào cuối cùng, có sử dụng cả tên và tuổi đã tính được (đây là OUTPUT)
# f"" là một cách định dạng chuỗi rất hiện đại và dễ đọc
print(f"rat vui duoc gap ban nhe, {ten}!")
print(f"ban da {tuoi} tuoi. chuc ban hoc tap vui ve")