def flood_fill(image, sr, sc, new_color):
    old_color = image[sr][sc]
    if old_color == new_color: return image
    def dfs(r, c):
        if 0<=r<len(image) and 0<=c<len(image[0]) and image[r][c] == old_color:
            image[r][c] = new_color
            for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                dfs(r+dr, c+dc)
    dfs(sr, sc)
    return image

img = [[1,1,1],[1,1,0],[1,0,1]]
print(flood_fill(img, 1, 1, 2))
