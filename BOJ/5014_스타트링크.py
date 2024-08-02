# 20240802
# 09:50
# 1 / 1

from collections import deque

f, s, g, u, d = map(int, input().split())

visited = [0] * (f + 1)
visited[s] = 1

queue = deque()
queue.append(s)

while queue:
    now = queue.popleft()

    if now == g:
        break

    distance = visited[now] + 1
    up = now + u
    down = now - d

    if up <= f and not visited[up]:
        visited[up] = distance
        queue.append(up)
    if down > 0 and not visited[down]:
        visited[down] = distance
        queue.append(down)

print("use the stairs" if not visited[g] else visited[g] - 1)
