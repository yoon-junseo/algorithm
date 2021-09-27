# 피보나치 - 메모이제이션 (재귀)
d = [0] * 100

def fibo(x):
    print(x)
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]
print(fibo(4))