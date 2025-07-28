class LazySegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0]*(4*self.n)
        self.lazy = [0]*(4*self.n)
        self.build(arr, 0, 0, self.n-1)

    def build(self, arr, node, l, r):
        if l == r:
            self.tree[node] = arr[l]
        else:
            mid = (l+r)//2
            self.build(arr, 2*node+1, l, mid)
            self.build(arr, 2*node+2, mid+1, r)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def update_range(self, node, l, r, ql, qr, val):
        if self.lazy[node] != 0:
            self.tree[node] += (r-l+1) * self.lazy[node]
            if l != r:
                self.lazy[2*node+1] += self.lazy[node]
                self.lazy[2*node+2] += self.lazy[node]
            self.lazy[node] = 0

        if ql > r or qr < l:
            return

        if ql <= l and r <= qr:
            self.tree[node] += (r-l+1) * val
            if l != r:
                self.lazy[2*node+1] += val
                self.lazy[2*node+2] += val
            return

        mid = (l+r)//2
        self.update_range(2*node+1, l, mid, ql, qr, val)
        self.update_range(2*node+2, mid+1, r, ql, qr, val)
        self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def query(self, node, l, r, ql, qr):
        if self.lazy[node] != 0:
            self.tree[node] += (r-l+1) * self.lazy[node]
            if l != r:
                self.lazy[2*node+1] += self.lazy[node]
                self.lazy[2*node+2] += self.lazy[node]
            self.lazy[node] = 0

        if ql > r or qr < l:
            return 0

        if ql <= l and r <= qr:
            return self.tree[node]

        mid = (l+r)//2
        return self.query(2*node+1, l, mid, ql, qr) + self.query(2*node+2, mid+1, r, ql, qr)
