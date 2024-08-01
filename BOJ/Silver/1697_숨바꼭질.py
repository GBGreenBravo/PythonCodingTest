# 20240801
# 31:36
# 1 / 7

# 최대값 설정을 안해줘서 오래 걸렸던 문제
# now < k 조건은 now - 1에서만 없애주면 됨. now * 2 와 now + 1 에서도 없애버려서 메모리초과 났었음.

from collections import deque


def bfs():
    visited = dict()
    visited[n] = 1

    queue = deque()
    queue.append((n, 0))

    while queue:
        now, sec = queue.popleft()

        if now == k:
            return sec
        if now < k and visited.get(now * 2) != 1 and k - now > now * 2 - k:
            visited[now * 2] = 1
            queue.append((now * 2, sec + 1))
        if now < k and visited.get(now + 1) != 1:
            visited[now + 1] = 1
            queue.append((now + 1, sec + 1))
        if visited.get(now - 1) != 1:
            visited[now - 1] = 1
            queue.append((now - 1, sec + 1))


n, k = map(int, input().split())
print(bfs())
