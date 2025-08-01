import random

def simulate_once():
    # Khởi tạo danh sách gồm 'A'*80 và 'B'*20
    items = ['A'] * 80 + ['B'] * 20
    # Mất ngẫu nhiên 1 sản phẩm
    lost = random.choice(items)
    items.remove(lost)
    # Chọn tiếp 1 sản phẩm
    pick = random.choice(items)
    return pick == 'A'

def monte_carlo(trials=1_000_000):
    count_A = 0
    for _ in range(trials):
        if simulate_once():
            count_A += 1
    return count_A / trials

if __name__ == "__main__":
    p_est = monte_carlo(200_0000)  # ví dụ chạy 2 triệu lần
    print(f"Xác suất ước lượng: {p_est:.4f}")
