# 피보나치 - 재귀함수 -> 반복 호출이 생겨서 성능에 문제가 생길 수 있다.
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)
print(fibo(4))