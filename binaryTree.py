

class BIT:
    def __init__(self, n):
        self.tree = [0]*(n+1)

    def update(self, i, delta):
        i += 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

bit = BIT(10)
bit.update(2, 5)
bit.update(4, 3)
print(bit.query(4))  # Output: 8
