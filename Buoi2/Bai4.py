#Cho một chuỗi, tìm ký tự xuất hiện nhiều nhất và số lần xuất hiện của nó bằng Counter
from collections import Counter
def Dem_ki_tu(s):
    if not s:
        return None
    dem = Counter(s)
    ky_tu,so_lan = dem.most_common(1)[0]
    return ky_tu, so_lan
chuoi = input('nhap chuoi: ')
Dem_ki_tu(chuoi)
k,s = Dem_ki_tu(chuoi)
print(k,s)
