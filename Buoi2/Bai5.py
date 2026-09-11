#Dùng itertools.combinations liệt kê tất cả tập con có tổng bằng S của một danh sách số nguyên cho trước.
from itertools import combinations
def find(a,s):
    kq = []
    for r in range(1,len(a)+1):
        for i in combinations(a,r):
            if sum(i) == s:
              kq.append(i)
    return kq

a = [2,3,4,8,0,6,4,-5]
s = 8
KQ = find(a,s)
print(list(KQ), end="\n")
