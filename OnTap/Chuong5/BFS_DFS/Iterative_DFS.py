# Cho đồ thị vô hướng $N$ đỉnh ($1 \dots N$) 
# và $M$ cạnh (có thể $N$ lên tới $10^5$, 
# dễ tràn ngăn xếp đệ quy nếu đồ thị dạng đường thẳng dài). 
# Hãy sử dụng DFS lặp bằng Stack tường minh 
# để tìm số lượng đỉnh của thành phần liên thông lớn nhất
line1 = input().split()
while not line1:
    line1 = input().split()
n,m = int(line1[0]),int(line1[1])

adj = [[] for _ in range(n+1)]
for _ in range(m):
    e = input().split()
    while not e:
        e = input().split()
    u,v = int(e[0]),int(e[1])
    adj[u].append(v)
    adj[v].append(u)
visited = [False]*(n+1)
max_comp_size = 0
for i in range(1,n+1):
    if not visited[i]:
        # Khởi tạo DFS lặp với Stack
        stack = [i]
        visited[i] = True
        curr_size = 0
        
        while stack:
            u = stack.pop()
            curr_size += 1
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        if curr_size > max_comp_size:
            max_comp_size = curr_size
            
print(max_comp_size)