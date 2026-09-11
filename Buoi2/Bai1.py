#Viết generator sinh ra n số Fibonacci đầu tiên (không dùng vòng lặp vô hạn).
def fibonacci_vo_han():
    a, b = 0, 1
    while True:            
        yield a
        a, b = b, a + b
n = int(input('nhap n: '))
gen = fibonacci_vo_han()
for _ in range(n):
    print(next(gen), end=" ")
