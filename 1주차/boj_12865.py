n, k = map(int, input().split())
item = []
dp = [[0] * (k + 1) for i in range(n)]

for i in range(n):
    w, v = map(int, input().split())
    item.append((w, v))

item.sort()

for i in range(n):
    for w in range(1, k + 1):
        if item[i][0] > w:
            if i == 0:
                dp[i][0] = 0
                continue
            dp[i][w] = dp[i - 1][w]
        else:
            dp[i][w] = max(dp[i - 1][w], 
                dp[i - 1][w - item[i][0]] + item[i][1])

print(dp[n - 1][k])