# Áp dụng BFS đa nguồn giải bài toán "khoảng cách đến trạm cứu hỏa gần nhất" cho mọi ô trên một bản đồ lưới.
# Áp dụng BFS đa nguồn: khoảng cách đến trạm cứu hỏa gần nhất cho mọi ô
from collections import deque


def khoang_cach_tram_cuu_hoa(luoi):
    if not luoi or not luoi[0]:
        return []

    m, n = len(luoi), len(luoi[0])
    kc = [[-1] * n for _ in range(m)]
    hang_doi = deque()

    for i in range(m):
        for j in range(n):
            if luoi[i][j] == 'F':
                kc[i][j] = 0
                hang_doi.append((i, j))

    huong = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while hang_doi:
        i, j = hang_doi.popleft()
        for di, dj in huong:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and luoi[x][y] != '#' and kc[x][y] == -1:
                kc[x][y] = kc[i][j] + 1
                hang_doi.append((x, y))

    return kc


# Ví dụ
ban_do = [
    "F..#",
    "...#",
    "#..F",
    "....",
]
for dong in khoang_cach_tram_cuu_hoa(ban_do):
    print(dong)