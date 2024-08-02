# 20240802
# 2:17:18

from collections import deque


def solve():
    visited = [0] * 100_001
    visited[start] = 1
    queue = deque()
    queue.append(start)

    answer_cnt = 0

    while queue:
        now = queue.popleft()

        if visited[now] == visited[end]:
            break

        distance = visited[now] + 1

        multiply_2 = now * 2
        plus_1 = now + 1
        minus_1 = now - 1
        if multiply_2 == end:
            answer_cnt += 1
        if plus_1 == end:
            answer_cnt += 1
        if minus_1 == end:
            answer_cnt += 1

        if multiply_2 < 100_001 and now < end and not visited[multiply_2]:
            visited[multiply_2] = distance
            queue.append(multiply_2)

        if now < end and not visited[plus_1]:
            visited[plus_1] = distance
            queue.append(plus_1)

        if minus_1 >= 0 and not visited[minus_1]:
            visited[minus_1] = distance
            queue.append(minus_1)

    print(visited[end] - 1)
    if start < 2 and end > 2:
        print(answer_cnt * 2)
    else:
        print(answer_cnt)


start, end = map(int, input().split())
if end <= start:
    print(start - end)
    print(1)
else:
    solve()
