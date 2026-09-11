#Dùng mảng cộng dồn (accumulate) trả lời Q truy vấn "tổng đoạn [l, r]" trên một mảng n phần tử, 
#so sánh thời gian chạy với cách duyệt trực tiếp từng truy vấn.
from itertools import accumulate
import random
import time
N = 1000
Q = 100
arr = [random.randint(1, 20) for _ in range(N)]
queries = []

#1
start = time.time()
for _ in range(Q):
    l = random.randint(0, N - 1)
    r = random.randint(l, N - 1)
    queries.append((l, r))
pref = [0] + list(accumulate(arr))

res_prefix = []
for l, r in queries:
    res_prefix.append(pref[r + 1] - pref[l])
print(list(res_prefix))
time1 = time.time() - start

#2
start = time.time()
res_direct = []
for l, r in queries:
    res_direct.append(sum(arr[l:r+1]))
print(list(res_direct))
time2 = time.time() - start
print(f"{time1} - {time2}")