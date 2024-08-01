# 20240801
# 19:59
# 1 / 1

# arr의 첫 열과 첫 행에 0을 추가하고
# sum_arr에서는 (0,0)부터 현재좌표까지의 누적합을 구한다.
# command에 대해서 (y2,x2)누적합 - (y2,x1-1)누적합 - (y1-1,x2)누적합 + (y1-1,x1-1)누적합을 계산해주면 된다.

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.insert(0, [0] * (n + 1))
for i in range(1, n + 1):
    arr[i].insert(0, 0)
commands = [list(map(int, input().split())) for _ in range(m)]

sum_arr = [[0] * (n + 1) for _ in range(n + 1)]
sum_arr[1][1] = arr[1][1]
for i in range(2, n + 1):
    sum_arr[1][i] = arr[1][i] + sum_arr[1][i - 1]
    sum_arr[i][1] = arr[i][1] + sum_arr[i - 1][1]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum_arr[i][j] = arr[i][j] + sum_arr[i - 1][j] + sum_arr[i][j - 1] - sum_arr[i - 1][j - 1]

for command in commands:
    y1, x1, y2, x2 = command
    print(sum_arr[y2][x2] - sum_arr[y2][x1 - 1] - sum_arr[y1 - 1][x2] + sum_arr[y1 - 1][x1 - 1])
