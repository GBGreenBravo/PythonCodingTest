# 20240725
# 19:26

# bfs를 할때, queue에 넣기 전에 visited 처리를 해주자.
# 넣은 후에 꺼내고 한다면, 이전의 루프에서 이미 queue에 담겨있움에도 또 queue에 넣을 수 있기 때문.
# 위 솔루션 적용하기 전에는 시간 초과 났었음.

from collections import deque


def bfs(a, b):
    queue = deque()
    visited[a][b] = True
    queue.append((a, b))
    while queue:
        y, x = queue.popleft()
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx))


m, n = map(int, input().split())
visited = [list(not(bool(i)) for i in map(int, input().split())) for _ in range(m)]
cnt = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            cnt += 1
            bfs(i, j)
print(cnt)
