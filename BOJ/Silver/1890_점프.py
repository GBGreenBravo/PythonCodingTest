# 20241015
# 03:21
# 1 / 1

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
routes = [[0] * n for _ in range(n)]
routes[0][0] = 1

for i in range(n):
    for j in range(n):
        if not routes[i][j] or not area[i][j]:
            continue
        jump = area[i][j]
        if i + jump < n:
            routes[i + jump][j] += routes[i][j]
        if j + jump < n:
            routes[i][j + jump] += routes[i][j]
print(routes[i][j])