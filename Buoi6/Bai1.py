# 1. Hàm dựng Segment Tree
def build_tree(data, node, start, end, tree):
    if start == end:
        tree[node] = data[start]
        return
    mid = (start + end) // 2
    left_node = 2 * node + 1
    right_node = 2 * node + 2
    
    build_tree(data, left_node, start, mid, tree)
    build_tree(data, right_node, mid + 1, end, tree)
    
    tree[node] = min(tree[left_node], tree[right_node])

# 2. Hàm truy vấn giá trị nhỏ nhất [L, R]
def query_min(node, start, end, L, R, tree):
    if R < start or end < L:
        return float('inf')
    if L <= start and end <= R:
        return tree[node]
    
    mid = (start + end) // 2
    left_min = query_min(2 * node + 1, start, mid, L, R, tree)
    right_min = query_min(2 * node + 2, mid + 1, end, L, R, tree)
    
    return min(left_min, right_min)

# --- LUỒNG CHẠY TRỰC TIẾP (KHÔNG CẦN MAIN) ---

# Nhập n và q
first_line = input().split()
while not first_line:
    first_line = input().split()
n, q = int(first_line[0]), int(first_line[1])

# Nhập mảng A (nhập đủ n số)
a_line = input().split()
while len(a_line) < n:
    a_line.extend(input().split())

A = [int(x) for x in a_line[:n]]

# Tạo và dựng cây Segment Tree
tree = [float('inf')] * (4 * n)
if n > 0:
    build_tree(A, 0, 0, n - 1, tree)

# Nhập q truy vấn và in kết quả ngay
for _ in range(q):
    q_line = input().split()
    while not q_line:
        q_line = input().split()
    
    L, R = int(q_line[0]) - 1, int(q_line[1]) - 1
    print(query_min(0, 0, n - 1, L, R, tree))