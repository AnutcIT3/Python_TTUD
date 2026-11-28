# Cho hai chuỗi $A$ và $B$. 
# Bạn muốn nối chuỗi $B$ vào ngay sau chuỗi $A$ 
# sao cho phần đuôi (hậu tố) của $A$ trùng khớp tối đa với phần đầu 
# (tiền tố) của $B$ để tiết kiệm ký tự. 
# Hãy in ra chuỗi kết quả ngắn nhất sau khi ghép $B$ vào sau $A$.

a = input().strip()
b = input().strip()

# Ghép B + '#' + A để tìm tiền tố dài nhất của B trùng với hậu tố của A
combined = b + "#" + a
n = len(combined)

lps = [0]*n
length = 0
i = 1
while i < n:
    if combined[i] == combined[length]:
        length += 1
        lps[i] = length
        i += 1
    elif length > 0 :
        length = lps[length - 1]
    else:
        lps[i] = 0
        i += 1
overlap = lps[-1]
print(a + b[overlap:])
