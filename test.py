# Số lượng ban đầu
total = 100
A = 80
B = 20

# Trường hợp mất sản phẩm loại A
P_mất_A = A / total
P_chọn_A_sau_khi_mất_A = (A - 1) / (total - 1)

# Trường hợp mất sản phẩm loại B
P_mất_B = B / total
P_chọn_A_sau_khi_mất_B = A / (total - 1)

# Tổng xác suất
P_chọn_A = P_mất_A * P_chọn_A_sau_khi_mất_A + P_mất_B * P_chọn_A_sau_khi_mất_B

print(f"Xác suất lấy được sản phẩm loại A là: {P_chọn_A:.4f}")
