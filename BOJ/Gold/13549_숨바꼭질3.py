# 20240930
# 17:10
# 1 / 2

# *2 먼저 안 뽑는 일반적인 deque기반 BFS 써서 한번 틀렸음.


from heapq import heappop, heappush


def oob(node):
    return node < 0 or 150_000 <= node


n, k = map(int, input().split())
if n >= k:
    print(n - k)
else:
    visited = [0] * 150_000
    visited[n] = 1

    queue = []
    heappush(queue, (1, n))

    while queue and not visited[k]:
        distance, now = heappop(queue)

        next_ = now * 2
        while not oob(next_) and not visited[next_]:
            visited[next_] = distance
            heappush(queue, (distance, next_))
            next_ *= 2

        if not oob(now + 1) and not visited[now + 1]:
            visited[now + 1] = distance + 1
            heappush(queue, (distance + 1, now + 1))
        if not oob(now - 1) and not visited[now - 1]:
            visited[now - 1] = distance + 1
            heappush(queue, (distance + 1, now - 1))

    print(visited[k] - 1)


# 20240813
# 34:13
# 1 / 3

from collections import deque


def bfs():
    visited = [False] * 100_001  # 중복방문을 피하기 위한 배열
    visited[n] = True

    queue = deque()
    queue.append((0, n))  # 초기값
    while True:
        next_queue = deque()  # 이 다음에 +1/-1 계산해줄 것들
        while queue:
            time, now = queue.popleft()
            next_queue.append((time, now))  # 현재 time에 대한 +1/-1 계산 목록에 추가
            if now == k:
                return time

            if now * 2 <= 100_000 and not visited[now * 2]:  # 현재 time에서 0초만에 *2를 갈 수 있고, 미방문이라면
                visited[now * 2] = True
                queue.append((time, now * 2))  # 이 queue에 추가

        queue = deque()
        while next_queue:  # 현재 시간에 대해 위의 *2 연산이 모두 끝났다면, 이제 +1/-1 차례
            time, now = next_queue.popleft()
            if now == k:
                return time

            if now + 1 <= 100_000 and not visited[now + 1]:
                visited[now + 1] = True
                queue.append((time + 1, now + 1))

            if now - 1 >= 0 and not visited[now - 1]:
                visited[now - 1] = True
                queue.append((time + 1, now - 1))


n, k = map(int, input().split())
if k <= n:  # 두 좌표가 같거나, -1만 할 수 있는 상황이면
    print(n - k)
else:  # n < k 이라면
    print(bfs())
