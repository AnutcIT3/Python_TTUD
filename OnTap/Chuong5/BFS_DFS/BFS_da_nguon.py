# Cho bản đồ thành phố kích thước $N \times M$. 
# Ô có giá trị 1 là trạm cứu hỏa, ô có giá trị 0 là khu dân cư. 
# Với mỗi ô trên bản đồ, hãy tính khoảng cách ngắn nhất (theo 4 hướng trên, dưới, trái, phải) 
# từ ô đó đến trạm cứu hỏa gần nhất.
from collections import depue

line1 = input().split()
while not line1:
    line1 = input().split()
n,m = int(line1[0]), int(line1[1])
grid = []
for _ in range(n):
    row = input().split()
    while not row:
        row = input().split()
    grid.append([int(x) for x in row])
dist = [[-1]*m for _ in range(n)]
q = depue()

# Đưa tất cả trạm cứu hỏa (nguồn) vào hàng đợi ngay từ đầu
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            dist[i][j] = 0
            q.append((i,j))
dr = [-1,1,0,0]
dc = [0,0,-1,1]

while q:
    r,c = q.popleft()
    for i in range(4):
        nr, nc =  r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))

for row in dist:
    print(*row)