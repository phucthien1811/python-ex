from collections import deque

def bfs_shortest_path(grid):
    n, m = len(grid), len(grid[0])
    q = deque([(0, 0, 0)])  # (x, y, steps)
    visited = set((0, 0))

    while q:
        x, y, d = q.popleft()
        if x == n-1 and y == m-1:
            return d
        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny, d+1))
    return -1

grid = [
    [0,0,0],
    [1,1,0],
    [0,0,0]
]
print(bfs_shortest_path(grid))  # Output: 4
