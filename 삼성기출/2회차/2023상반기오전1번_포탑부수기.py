# 20241010
# 50:14
# 1 / 1

"""
풀이 시간: 50분 (14:02 - 14:52)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:02 - 14:15)


2. 구현 (14:15 - 14:29)
    이전 풀이에서는 공격자 찾는 반복문 따로, 공격대상 찾는 반복문 따로 했었는데,
    코드리뷰 때 혜민님이 반복문 한번에 찾았던 게 기억이 나서, 반복문을 분리하지 않고 min()/max()를 이용해서 공격자/공격대상을 찾았습니다.


3. 디버깅 (-)


4. 검증 (14:29 - 14:52)
    메모와 코드를 비교검증하는 과정에서,
    부서지지 않은 포탑이 1개가 되면 바로 종료하는 부분이 빠진 걸 발견하고 추가했습니다.

    그리고 코드를 정독하는 과정에서, 포탑 공격력이 음수면 0으로 바꾼다는 로직에서
    조건이 area[ey][ex] < 0 이 돼야 할 부분이, not area[ey][ex]로 작성돼 있는 걸 발견하고 수정했습니다.

    O (1) 주어진 테스트케이스로 검증
    O (2) 메모 vs. 코드
    O (3) (머릿속 환기 후) 문제 재정독
    O (4) 커스텀 테스트케이스 검증
    O (5) 철저한 코드 검증
    O (6) 오답노트 활용
    X (7) 다양한 구상에 따른, 다른 구현
"""

from collections import deque

direction_4 = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 우하좌상
direction_8 = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))


def attack(sy, sx, ey, ex):
    full_power = area[sy][sx]
    half_power = full_power // 2

    visited = [[0] * m for _ in range(n)]
    visited[sy][sx] = 1

    queue = deque()
    queue.append((sy, sx, []))

    while queue:
        y, x, route = queue.popleft()
        for dy, dx in direction_4:
            ny, nx = (y + dy) % n, (x + dx) % m
            if not area[ny][nx] or visited[ny][nx]:
                continue
            visited[ny][nx] = 1
            queue.append((ny, nx, [rr[:] for rr in route] + [(ny, nx)]))

            if ny == ey and nx == ex:
                for ry, rx in route:
                    relevant[ry][rx] = 1
                    area[ry][rx] -= half_power
                    if area[ry][rx] < 0:
                        area[ry][rx] = 0
                area[ey][ex] -= full_power
                if area[ey][ex] < 0:
                    area[ey][ex] = 0
                return

    area[ey][ex] -= full_power
    if area[ey][ex] < 0:
        area[ey][ex] = 0

    for dy, dx in direction_8:
        ny, nx = (ey + dy) % n, (ex + dx) % m
        if not area[ny][nx] or (ny == sy and nx == sx):
            continue
        relevant[ny][nx] = 1
        area[ny][nx] -= half_power
        if area[ny][nx] < 0:
            area[ny][nx] = 0


n, m, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

recent_attacked = [[0] * m for _ in range(n)]

for time in range(1, k + 1):
    if n * m - sum(map(lambda row: row.count(0), area)) == 1:
        break

    candidates = []
    for i in range(n):
        for j in range(m):
            if area[i][j]:
                candidates.append((area[i][j], -recent_attacked[i][j], -(i + j), -j, i, j))

    si, sj = min(candidates)[-2:]
    ei, ej = max(candidates)[-2:]

    relevant = [[0] * m for _ in range(n)]
    relevant[si][sj] = 1
    relevant[ei][ej] = 1

    area[si][sj] += n + m
    recent_attacked[si][sj] = time
    attack(si, sj, ei, ej)

    for i in range(n):
        for j in range(m):
            if area[i][j] and not relevant[i][j]:
                area[i][j] += 1

print(max(map(max, area)))
