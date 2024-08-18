# 20240818
# 19:29
# 1 / 1

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(map(sum, dp)))
        continue

    dp[0][-2] += dp[1][-1]
    dp[1][-2] += dp[0][-1]

    for i in range(n - 3, -1, -1):
        dp[0][i] += max(dp[1][i + 1], dp[1][i + 2])
        dp[1][i] += max(dp[0][i + 1], dp[0][i + 2])

    print(max(dp[0][0], dp[1][0]))
