# Có n đoạn đóng trên trục số. 
# Mỗi đoạn được biểu diễn bởi hai đầu mút [lᵢ, rᵢ]. Sau đó có q truy vấn; mỗi truy vấn đưa ra một đoạn [a, b].
# Với mỗi truy vấn, hãy xem trong đoạn từ [a, b], điểm có số lượng đoạn phủ lên nhiều nhất là bao nhiêu đoạn.
n, q = map(int, input().split())
N = 10**5 + 2
diff = [0] * (N+1)

for _ in range(n):
    l,r = map(int,input().split())
    diff[l] += 1
    diff[r+1] -= 1
cnt = [0]*N
cur = 0
for x in range(N):
    cur += diff[x]
    cnt[x] = cur

table = [cnt]
k=1
while (1<<k) <=N:
    prev = table[-1]
    half = 1 <<(k-1)
    table.append([max(prev[i],prev[i + half])
                  for i in range(N-(1<<k)+1)])
    k += 1

for _ in range(q):
    a,b = map(int, input().split())
    k = (b-a+1).bit_length() - 1
    print(max(table[k][a], table[k][b - (1<<k) + 1]))
    
                  