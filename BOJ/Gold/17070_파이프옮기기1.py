# 20240818
# 31:00
# 1 / 2


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
dp1 = [[0] * n for _ in range(n)]  # 가로
dp2 = [[0] * n for _ in range(n)]  # 세로
dp3 = [[0] * n for _ in range(n)]  # 대각선
dp1[0][1] = 1

for i in range(2, n):
    if area[0][i] != 1:
        dp1[0][i] = dp1[0][i - 1]

for i in range(1, n):
    for j in range(2, n):
        if oob(i, j) or area[i][j] == 1:
            continue
        dp1[i][j] = dp1[i][j - 1] + dp3[i][j - 1]
        dp2[i][j] = dp2[i - 1][j] + dp3[i - 1][j]
        if area[i - 1][j] == 0 and area[i][j - 1] == 0:
            dp3[i][j] += dp1[i - 1][j - 1] + dp2[i - 1][j - 1] + dp3[i - 1][j - 1]

print(dp1[-1][-1] + dp2[-1][-1] + dp3[-1][-1])
