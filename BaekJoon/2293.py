n, k = map(int, input().split())
c = []
dp = [0 for i in range(k + 1)]
dp[0] = 1
for i in range(n):
    c.append(int(input()))
for i in c:
    for j in range(1, k + 1):
        if j - i >= 0:
            if i == 2 and j == 3:
                print(dp, dp[j] + dp[j - i])
            dp[j] += dp[j - i]
            if i == 2 and j == 3:
                print(dp)
print(dp[k])
print(dp)
