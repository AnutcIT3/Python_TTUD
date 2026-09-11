from collections import namedtuple
SinhVien = namedtuple("SinhVien", ["ten", "diem"])
ds = [SinhVien("An", 9.5), SinhVien("Binh", 9.0), SinhVien("Anh", 7.5)]
ds.sort(key=lambda sv: sv.diem, reverse=True)
for sv in ds:
    print(sv.ten, sv.diem)
