# BFS đa nguồn: thay vì bắt đầu từ 1 đỉnh, ta đưa TẤT CẢ các đỉnh 
# xuất phát vào hàng đợi ngay từ đầu — lan truyền đồng thời từ nhiều nguồn, vẫn đúng thứ tự "theo từng lớp" như BFS thường.

from collections import deque
 
def thoi_gian_cam_thoi(luoi):
    n, m = len(luoi), len(luoi[0])
    hang_doi = deque()
    tuoi = 0
    for i in range(n):
        for j in range(m):
            if luoi[i][j] == 2: hang_doi.append((i, j, 0))  # cam thoi
            elif luoi[i][j] == 1: tuoi += 1
    thoi_gian = 0
    while hang_doi:
        i, j, t = hang_doi.popleft()
        thoi_gian = max(thoi_gian, t)
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<m and luoi[ni][nj]==1:
                luoi[ni][nj] = 2; tuoi -= 1
                hang_doi.append((ni, nj, t+1))
    return thoi_gian if tuoi == 0 else -1
