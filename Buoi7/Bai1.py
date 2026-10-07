# Cho hai chuỗi A và B gồm các chữ cái tiếng Anh in thường. 
# Hãy tìm độ dài lớn nhất của một dãy con chung liên tiếp sao cho không có hai ký tự liền kề nào giống nhau.
a = input().strip()
b = input().strip()

n,m = len(a), len(b)
dp = [[0]*(m-1) for _ in range(n+1)]
kq = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i-1] == b[j-1]:
            if i>1 and a[i-1] == a[i-2]:
                dp[i][j] = 1
            else: 
                dp[i][j] = dp[i-1][j-1]+1
            kq = max(kq, dp[i][j])
print(kq)