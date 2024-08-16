# 20240816
# 09:56
# 1 / 1

# 10e8은 10**8이 아닌 10**9임.

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return (y < 0) or (n <= y) or (x < 0) or (n <= x)


def bfs():
    queue = deque()
    queue.append((0, 0))

    visited = [[10e5] * n for _ in range(n)]  # 불가능한 최대값으로 방문배열 초기화
    visited[0][0] = area[0][0]

    while queue:
        y, x = queue.popleft()

        if y == n - 1 and x == n - 1:  # 현재 좌표가 도착지점이라면 더 이상 갈 필요 없음.
            continue

        before = visited[y][x]  # 현재 좌표까지의 최소값

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] <= before + area[ny][nx]:  # 영역 밖 or 기존 방문 값이 작거나 같다면 continue
                continue
            queue.append((ny, nx))
            visited[ny][nx] = before + area[ny][nx]  # 다음 좌표에 대한 최소값 갱신

    return visited[-1][-1]  # 도착 좌표의 방문배열에 저장된 (최소)값을 반환


t = int(input())
for test in range(1, t + 1):
    n = int(input())
    area = [[int(i) for i in list(str(input()))] for _ in range(n)]

    print(f"#{test} {bfs()}")
