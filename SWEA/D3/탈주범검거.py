# 20240820
# 20:06
# 1 / 1

from collections import deque

direction = ((-1, 0), (0, -1), (1, 0), (0, 1))  # 상좌하우

tunnel_dict = {1: (0, 1, 2, 3), 2: (0, 2), 3: (1, 3), 4: (0, 3), 5: (2, 3), 6: (2, 1), 7: (0, 1)}  # 터널 번호에 맞는 방향index


def oob(yy, xx):
    return yy < 0 or n <= yy or xx < 0 or m <= xx


t = int(input())
for test in range(1, t + 1):
    n, m, r, c, l = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]

    queue = deque()
    queue.append((r, c))

    visited = [[0] * m for _ in range(n)]
    visited[r][c] = 1

    while queue:
        y, x = queue.popleft()
        time = visited[y][x]  # 현재까지 도달하는 데 걸리는 시간

        if time == l:  # 시간제한과 현재시간이 같다면, 이전 시간까지의 BFS 탐색은 모두 종료됐으므로 종료
            break

        for d_idx in tunnel_dict[area[y][x]]:  # 현재 터널에 따라, 다음에 갈 수 있는 방향들
            dy, dx = direction[d_idx]
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or not area[ny][nx] or visited[ny][nx]:  # 영역 밖 / 터널 X / 이미 방문
                continue
            if (d_idx + 2) % 4 not in tunnel_dict[area[ny][nx]]:  # 다음 터널이 현재 터널과 연결되지 않는 경우 (상 <-> 하) (좌 <-> 우)
                continue
            visited[ny][nx] = time + 1  # 다음 좌표까지 걸리는 시간 저장
            queue.append((ny, nx))

    print(f"#{test} {n * m - sum(map(lambda x:x.count(0), visited))}")  # 전체(n * m)에서, visited에 0(방문 안했던 곳)을 센 것을 빼줌
