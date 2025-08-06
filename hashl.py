def rolling_hash(s, base=257, mod=10**9+7):
    hash_val = 0
    power = 1
    for c in s:
        hash_val = (hash_val * base + ord(c)) % mod
        power = (power * base) % mod
    return hash_val

print(rolling_hash("hello"))
print(rolling_hash("hell") == rolling_hash("hell"))  # True
