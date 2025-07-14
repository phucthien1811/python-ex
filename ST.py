class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0]*(4*self.n)
        self.build(arr, 0, 0, self.n-1)

    def build(self, arr, node, l, r):
        if l == r:
            self.tree[node] = arr[l]
        else:
            mid = (l + r)//2
            self.build(arr, 2*node+1, l, mid)
            self.build(arr, 2*node+2, mid+1, r)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r)//2
        return self.query(2*node+1, l, mid, ql, qr) + self.query(2*node+2, mid+1, r, ql, qr)

arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)
print(st.query(0, 0, len(arr)-1, 1, 3))  # Output: 15 (3+5+7)
