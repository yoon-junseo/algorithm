import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# # 기본 단어 갯수도 못 가르치는 경우 (a, c, i, n, t)
if k < 5:
    print(0)
    exit(0)
elif k == 26:
    print(n)
    exit(0)

remainedNum = int(k - 5)
words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]
learn = [False] * 26
answer = int(0)

for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = 1

def dfs(idx, cnt):
    global answer
    if cnt == remainedNum:
        readCnt = 0
        for word in words:
            check = True
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                readCnt += 1
        answer = max(answer, readCnt)
        return
    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False
print(learn)
dfs(0, 0)
print(answer)