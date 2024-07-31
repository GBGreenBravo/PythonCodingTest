# 20240731
# 11:58

# 리스트로 구현한 큐의 경우 pop(0)에 N의 연산이 들기 때문에, 10**9로 시간초과 남.
# 웬만하면 deque를 사용해서 풀자.

from collections import deque

m, n = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            queue.append((i, j))

while queue:
    y, x = queue.popleft()
    day = tomatoes[y][x] + 1

    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ny, nx = y + dy, x + dx
        if not(0 <= ny < n) or not(0 <= nx < m) or tomatoes[ny][nx] != 0:
            continue

        tomatoes[ny][nx] = day
        queue.append((ny, nx))

mx = max([max(row) for row in tomatoes])
mn = min([min([i * i for i in row]) for row in tomatoes])

print(-1 if mn == 0 else mx - 1)
