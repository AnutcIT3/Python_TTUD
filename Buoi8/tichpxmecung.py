from collections import deque

# 1. Nhập n và m
line1 = input().split()
while not line1:
    line1 = input().split()
n, m = int(line1[0]), int(line1[1])

# 2. Nhập ma trận n x m
grid = []
for _ in range(n):
    line = input().split()
    while not line:
        line = input().split()
    grid.append([int(x) for x in line])

# 3. Nhập tọa độ Mèo (r1, c1) và Chuột (r2, c2)
line_pos = input().split()
while not line_pos:
    line_pos = input().split()

# Quy đổi từ 1-indexed về 0-indexed (trừ 1)
r1, c1 = int(line_pos[0]) - 1, int(line_pos[1]) - 1
r2, c2 = int(line_pos[2]) - 1, int(line_pos[3]) - 1

# 4. Thuật toán BFS tìm đường đi ngắn nhất
if grid[r1][c1] == 1 or grid[r2][c2] == 1:
    print(-1)
else:
    # Mảng lưu khoảng cách, khởi tạo -1 (chưa thăm)
    dist = [[-1] * m for _ in range(n)]
    dist[r1][c1] = 0

    # Hàng đợi BFS
    queue = deque([(r1, c1)])

    # 4 hướng di chuyển: Trái, Phải, Trên, Dưới
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    while queue:
        r, c = queue.popleft()

        # Nếu đã đến vị trí chuột thì dừng
        if r == r2 and c == c2:
            break

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # Kiểm tra trong phạm vi ma trận, là ô 0 và chưa thăm
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

    # In ra khoảng cách tới vị trí chuột
    print(dist[r2][c2])