# Phần này thường áp dụng cho cây nhị phân (tree), cần tiền xử lý trước
# Đây là bản đơn giản dùng DFS + parent array

def lca_simple(tree, root, u, v):
    parent = {}
    depth = {}
    def dfs(node, par, d):
        parent[node] = par
        depth[node] = d
        for child in tree.get(node, []):
            if child != par:
                dfs(child, node, d+1)

    dfs(root, None, 0)

    while depth[u] > depth[v]:
        u = parent[u]
    while depth[v] > depth[u]:
        v = parent[v]
    while u != v:
        u = parent[u]
        v = parent[v]
    return u

tree = {1: [2, 3], 2: [4, 5], 3: [6, 7]}
print(lca_simple(tree, 1, 4, 5))  # Output: 2
print(lca_simple(tree, 4, 6))    # Output: 1
