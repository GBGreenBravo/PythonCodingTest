# 20241205
# 1 / 1

N = int(input())
sizes = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
for length in range(2, N + 1):
    for i in range(N - length + 1):
        s = i
        e = i + length - 1
        min_value = 2**32

        for j in range(s, e):
            start = dp[s][j]
            end = dp[j + 1][e]
            min_value = min(min_value, start + end + sizes[s][0] * sizes[j][1] * sizes[e][1])

        dp[s][e] = min_value

print(dp[0][N - 1])
