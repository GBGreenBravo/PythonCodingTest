# 20240801
# 11:22
# 1 / 2

def dfs(node, cnt):
    if node == b:
        answers.append(cnt)

    cnt += 1

    next1 = node * 2
    if next1 <= b:
        dfs(next1, cnt)

    next2 = int(str(node) + "1")
    if next2 <= b:
        dfs(next2, cnt)


a, b = map(int, input().split())

answers = []
dfs(a, 1)

print(-1 if not answers else min(answers))


# 아래는 BFS 풀이
"""
from collections import deque


def bfs():
    visited = dict()
    visited[a] = 1

    queue = deque()
    queue.append((a, 1))

    while queue:
        now, cnt = queue.popleft()
        if now == b:
            return cnt

        cnt += 1

        next1 = now * 2
        if next1 <= b and visited.get(next1) != 1:
            visited[next1] = 1
            queue.append((next1, cnt))

        next2 = int(str(now) + "1")
        if next2 <= b and visited.get(next2) != 1:
            visited[next2] = 1
            queue.append((next2, cnt))

    return -1


a, b = map(int, input().split())

answers = []
print(bfs())
"""