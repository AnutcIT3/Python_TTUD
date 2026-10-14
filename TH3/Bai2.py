# Bài 2: Trạm liên lạc trọng yếu  
# Một mạng liên lạc gồm N trạm và M kết nối hai chiều. Ban đầu, tất cả các trạm đều có thể liên lạc với nhau, trực tiếp hoặc thông qua các trạm trung gian.
# Khi một trạm bị hỏng, trạm đó và tất cả kết nối gắn với nó bị loại bỏ.
# Một trạm được gọi là trọng yếu nếu khi nó bị hỏng, các trạm còn lại bị chia thành ít nhất hai nhóm không thể liên lạc với nhau.
# Hãy tìm tất cả các trạm trọng yếu.
# Dữ liệu vào
# •	Dòng đầu chứa hai số nguyên N, M.
# •	M dòng tiếp theo, mỗi dòng chứa hai số u, v, biểu diễn một kết nối giữa trạm u và trạm v.
# •	Không có kết nối từ một trạm đến chính nó và không có hai kết nối trùng nhau.
# Dữ liệu ra
# •	Dòng đầu ghi số trạm trọng yếu.
# •	Dòng thứ hai ghi số hiệu các trạm trọng yếu theo thứ tự tăng dần. Nếu không có, chỉ cần in 0 ở dòng đầu.
# Giới hạn: 2 ≤ N ≤ 1.000, 1 ≤ M ≤ 5.000.

import sys

# Tăng giới hạn đệ quy cho cây DFS
sys.setrecursionlimit(100000)

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit(0)

n = int(input_data[0])
m = int(input_data[1])

ke = [[] for _ in range(n + 1)]
pos = 2
for _ in range(m):
    u = int(input_data[pos])
    v = int(input_data[pos + 1])
    pos += 2
    ke[u].append(v)
    ke[v].append(u)

tim = [0] * (n + 1)
low = [0] * (n + 1)
dem = 0
khop = [False] * (n + 1)

def dfs(u, cha):
    global dem
    dem += 1
    tim[u] = low[u] = dem
    con = 0
    for v in ke[u]:
        if v == cha:
            continue
        if tim[v]:
            low[u] = min(low[u], tim[v])
        else:
            con += 1
            dfs(v, u)
            low[u] = min(low[u], low[v])
            # u không phải là gốc và có nhánh con không đi ngược lên trên u được
            if cha != 0 and low[v] >= tim[u]:
                khop[u] = True

    # u là gốc của cây DFS và có từ 2 con trở lên
    if cha == 0 and con > 1:
        khop[u] = True

# Duyệt qua các đỉnh để tìm khớp
for i in range(1, n + 1):
    if not tim[i]:
        dfs(i, 0)

ds_khop = [i for i in range(1, n + 1) if khop[i]]

print(len(ds_khop))
if len(ds_khop) > 0:
    print(*ds_khop)
