def tongchuso(x):
    if x < 10:
        return x
    return x%10+tongchuso(x//10)
n = int(input(""))
print(tongchuso(n))