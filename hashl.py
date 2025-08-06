def rolling_hash(s, base=257, mod=10**9+7):
    hash_val = 0
    power = 1
    for c in s:
        hash_val = (hash_val * base + ord(c)) % mod
        power = (power * base) % mod
    return hash_val

print(rolling_hash("hello"))
print(rolling_hash("hell") == rolling_hash("hell"))  # True


# Đây là pseudocode ngắn gọn, có thể dùng thư viện hoặc viết lại rõ hơn nếu cần

# pip install munkres
from munkres import Munkres
m = Munkres()
matrix = [[5, 9, 1], [10, 3, 2], [8, 7, 4]]
indexes = m.compute(matrix)
print("Chi phí nhỏ nhất:", sum(matrix[row][column] for row, column in indexes))
