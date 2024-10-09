# 20241009
# 59:36
# 1 / 1

"""
풀이 시간: 1시간 (17:30 - 18:30)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (17:30 - 17:43)
    이번에도 문제 지문을 읽으며, 약간의 모호한 부분이 있었습니다.
    이전 풀이 때와 같은 의문이었는데, 해당 모호함을 해결하는 단서로 "출발 전 사람은 격자 밖"이라는 지문이 있음을 확인하고,
    역시 지문의 문장들은 의미 없이 적히는 게 없다고 생각했고 이번처럼 메모를 꼼꼼히 해두는 것의 중요성을 재확인했습니다.


2. 구현 (17:43 - 18:03)
    같은 BFS 최단거리였지만, 우선순위 비교가 달랐기에 비교에 따른 BFS를 달리 작성했습니다.
    base_camps를 입력배열 그대로 활용하면 됐지만,
    area에 -1로 못가는 곳을 그대로 표시해준다는 생각에, 새롭게 선언했습니다.


3. 디버깅 (18:03 - 18:08)
    기본 제공 테케에서 무한루프를 돌았습니다.
    도착지점과 거리가 1일 때, 바로 가지 못하고 돌아서 가는 코드로 작성돼 있었기에,
    해당 부분 확인하고 바로 수정했습니다.


4. 검증 (18:08 - 18:30)
    O (1) 주어진 테스트케이스로 검증
    O (2) 메모 vs. 코드
    O (3) (머릿속 환기 후) 문제 재정독
    O (4) 커스텀 테스트케이스 검증
    O (5) 철저한 코드 검증
    O (6) 오답노트 활용
    X (7) 다양한 구상에 따른, 다른 구현
"""

from collections import deque

direction = ((-1, 0), (0, -1), (0, 1), (1, 0))  # 상좌우하


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def move_person(person_num, sy, sx):
    visited = [[0] * n for _ in range(n)]
    visited[sy][sx] = 1

    queue = deque()
    for d_idx, (dsy, dsx) in enumerate(direction):
        nsy, nsx = sy + dsy, sx + dsx
        if oob(nsy, nsx) or area[nsy][nsx] < 0:
            continue
        visited[nsy][nsx] = 1
        queue.append((nsy, nsx, d_idx))

    while queue:
        y, x, started_d = queue.popleft()

        if area[y][x] == person_num:
            dsy, dsx = direction[started_d]
            ey, ex = sy + dsy, sx + dsx

            if area[ey][ex] == person_num:
                restricting.append((ey, ex))
            else:
                next_moving.append((person_num, ey, ex))
            return

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] or area[ny][nx] < 0:
                continue
            visited[ny][nx] = 1
            queue.append((ny, nx, started_d))


def find_closest_base_camp(person_num):
    for yy in range(n):
        for xx in range(n):
            if area[yy][xx] == person_num:
                sy, sx = yy, xx
                break
        else:
            continue
        break

    visited = [[0] * n for _ in range(n)]
    visited[sy][sx] = 1

    queue = deque()
    queue.append((sy, sx))

    while queue:
        next_queue = deque()
        targets = []

        while queue:
            y, x = queue.popleft()
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or visited[ny][nx] or area[ny][nx] < 0:
                    continue
                visited[ny][nx] = 1
                next_queue.append((ny, nx))

                if base_camps[ny][nx]:
                    targets.append((ny, nx))

        if targets:
            return min(targets)
        else:
            queue = next_queue


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
base_camps = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if area[i][j] == 1:
            area[i][j] = 0
            base_camps[i][j] = 1
for m_idx in range(1, m + 1):
    aa, bb = map(lambda inp: int(inp) - 1, input().split())
    area[aa][bb] = m_idx

time = 0
moving = []
while time <= m or moving:
    time += 1

    next_moving = []
    restricting = []
    for mover in moving:
        move_person(*mover)
    moving = next_moving

    for ri, rj in restricting:
        area[ri][rj] = -1

    if time <= m:
        bi, bj = find_closest_base_camp(time)
        base_camps[bi][bj] = 0
        moving.append((time, bi, bj))
        area[bi][bj] = -1

print(time)
