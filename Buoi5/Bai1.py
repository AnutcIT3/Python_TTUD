#Dùng KMP tìm tất cả vị trí xuất hiện của một từ trong một đoạn văn bản dài cho trước.
def xay_dung_lps(mau):
    m = len(mau)
    lps = [0] * m
    do_dai = 0            # do dai tien to=hau to hien tai
    i = 1
    while i < m:
        if mau[i] == mau[do_dai]:
            do_dai += 1
            lps[i] = do_dai
            i += 1
        elif do_dai > 0:
            do_dai = lps[do_dai - 1]
        else:
            lps[i] = 0
            i += 1
    return lps

def kmp_tim_kiem(van_ban, mau):
    n, m = len(van_ban), len(mau)
    lps = xay_dung_lps(mau)
    ket_qua = []
    i = j = 0                    # i: van ban, j: mau
    while i < n:
        if van_ban[i] == mau[j]:
            i += 1; j += 1
            if j == m:
                ket_qua.append(i - j)   # tim thay 1 vi tri khop
                j = lps[j - 1]
        elif j > 0:
            j = lps[j - 1]        # lui mau theo bang LPS
        else:
            i += 1
    return ket_qua

print(xay_dung_lps("ababcabab"))
# [0, 0, 1, 2, 0, 1, 2, 3, 4]

print(kmp_tim_kiem("ban than la mot thang ngu, no hay cho toi vay tien, ban than con hay trom do cua toi", "ban"))   # [0, 5, 7]