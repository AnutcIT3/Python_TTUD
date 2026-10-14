# Bài 1: Những con đường quan trọng — Tìm cầu
# Một thành phố có N địa điểm và M con đường hai chiều. Ban đầu, từ một địa điểm bất kỳ có thể đi đến mọi địa điểm khác.
# Một con đường được gọi là quan trọng nếu khi đóng con đường đó, có ít nhất hai địa điểm không còn đi đến nhau được.
# Hãy tìm tất cả các con đường quan trọng.
# Dữ liệu vào
# •	Dòng đầu chứa hai số nguyên N, M.
# •	M dòng tiếp theo, mỗi dòng chứa hai số u, v, biểu diễn một con đường nối địa điểm u và v.
# •	Không có đường nối một địa điểm với chính nó và không có hai đường trùng nhau.
# Dữ liệu ra
# •	Dòng đầu ghi số con đường quan trọng.
# •	Các dòng tiếp theo ghi hai đầu mút của từng đường, với đầu nhỏ hơn đứng trước.
# •	In các đường theo thứ tự tăng dần của đầu mút thứ nhất, nếu bằng nhau thì theo đầu mút thứ hai.
# Giới hạn: 2 ≤ N ≤ 1.000, 1 ≤ M ≤ 5.000.
import sys
sys.setrecursionlimit(1000)
n,m = map(int, input().split())
ke = [[]for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    ke[u].append(v)
    ke[v].append(u)

tim = [0]*(n+1)
low = [0]*(n+1)
dem = 0
cau = []
def dfs(u,cha):
    global dem
    dem +=1
    tim[u] = low[u] = dem
    for v in ke[u]:
        if v == cha:
            continue
        if tim[v]:
            low[u] = min(low[u],tim[v])
        else:
            dfs(v,u)
            low[u] = min(low[u],low[v])
            if low[v]>tim[u]:
                cau.append((min(v,u),max(v,u)))

dfs(1,0)
cau.sort()
print(len(cau))
for a,b in cau:
    print(a,b)



