import sys

def max_palindrome_length():
    # Đọc dữ liệu đầu vào
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    s = input_data[1] if len(input_data) > 1 else ""
    
    if n == 0 or not s:
        print(0)
        return

    # Tiền xử lý chuỗi: chèn ký tự '#' vào giữa các ký tự
    # Ví dụ: "abacd" -> "^#a#b#a#c#d#$"
    # Điều này giúp quy xâu về độ dài lẻ để xử lý chung cho cả Palindrome độ dài chẵn và lẻ.
    T = "^#" + "#".join(s) + "#$"
    
    m = len(T)
    P = [0] * m  # P[i] lưu bán kính của Palindrome tâm i
    C = 0        # Tâm của Palindrome có biên phải xa nhất
    R = 0        # Biên phải của Palindrome đó (R = C + P[C])

    max_len = 0

    for i in range(1, m - 1):
        # Đối xứng của i qua C
        i_mirror = 2 * C - i

        # Nếu i nằm trong vùng ảnh hưởng của C
        if R > i:
            P[i] = min(R - i, P[i_mirror])
        else:
            P[i] = 0

        # Mở rộng bán kính Palindrome tại tâm i
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        # Cập nhật C và R nếu Palindrome tại i vượt qua R hiện tại
        if i + P[i] > R:
            C = i
            R = i + P[i]

        max_len = max(max_len, P[i])

    print(max_len)

if __name__ == "__main__":
    max_palindrome_length()