# 20240813
# 05:03
# 1 / 1

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    maze[i][0] += maze[i - 1][0]  # 1열에 대해 누적합
for i in range(1, m):
    maze[0][i] += maze[0][i - 1]  # 1행에 대해 누적합
for i in range(1, n):
    for j in range(1, m):
        maze[i][j] += max(maze[i - 1][j - 1], maze[i][j - 1], maze[i - 1][j])  # (i,j)의 최대는 (i-1,j-1), (i,j-1), (i-1,j)의 누적합중 최대 + maze(i,j)이다.
print(maze[n - 1][m - 1])  # 도착점의 최대 누적합
