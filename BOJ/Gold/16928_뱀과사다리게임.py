# 20240915
# 08:54
# 1 / 2

# BFS 활용할 때, visited 필요 여부 항상 체크하자..!

from collections import deque


def bfs():
    queue = deque()
    queue.append((1, 0))

    while queue:
        now, cnt = queue.popleft()
        for i in range(6, 0, -1):
            nex = now + i
            if nex > 100 or visited[nex]:
                continue
            if nex == 100:
                print(cnt + 1)
                return
            if ladders[nex]:
                nex = ladders[nex]
            elif snakes[nex]:
                nex = snakes[nex]
            queue.append((nex, cnt + 1))
            visited[nex] = 1


n, m = map(int, input().split())
ladders = [0] * 101
snakes = [0] * 101
for _ in range(n):
    a, b = map(int, input().split())
    ladders[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    snakes[a] = b
visited = [0] * 101
visited[1] = 1
bfs()


# 20240818
# 10:54
# 1 / 1
"""
from heapq import heappop, heappush

n, m = map(int, input().split())
ladder = dict()
for _ in range(n + m):  # 사다리, 뱀 상관없이 key, value가 출발지점, 도착지점이 되는 dictionary에 다 담기
    a, b = map(int, input().split())
    ladder[a] = b

visited = [10e2] * 101
visited[1] = 0  # 0이 아닌 1부터 시작

queue = [(0, 1)]

while queue:
    time, now = heappop(queue)  # 최소시간으로 움직이는 것부터

    if now == 100:  # 100번 칸에 도착하면 출력하고 break
        print(time)
        break

    for i in range(1, 7):
        next = now + i
        if ladder.get(next):  # 사다리나 뱀 타면, 해당 값 반영
            next = ladder[next]

        if next <= 100 and visited[next] > time + 1:  # 100칸 이내에 있고, 기존보다 더 적은 시간으로 도달 가능하다면
            visited[next] = time + 1
            heappush(queue, (time + 1, next))
"""