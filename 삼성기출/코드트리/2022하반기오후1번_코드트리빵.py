# 20240923
# 1:25:00
# 1 / 1

"""
풀이 시간: 1시간 25분 (14:03 - 15:28)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:03 - 14:14)
    문제를 읽으며, 아래 부분에 대해서 모호함/엣지케이스가 있을 수 있다고 메모했지만, 모두 입력/출력 조건을 읽고 해소됐습니다.
    - ? 편의점의 수는 m 이상 주어짐이 보장되는지 ?
    - ? 다른 편의점으로 이동했는데, 그 턴에 그 편의점 못 지나감 처리되면 ?
    - ? 편의점 도달 못하는 경우는 ?


2. 1차 구현 (14:14 - 14:42)
    코드 수행순서는, move() -> depart()이나,
    0초에서는 move()를 수행하지 않기에, 체크포인트를 위해 depart() 함수 먼저 구현했습니다.


3. 1차 디버깅 (14:42 - 14:46)
    사람들을 이동시키는 move함수에서 BFS를 사용했는데,
    시작점을 (ey, ex)가 아닌 (sy, sx)로 하는 실수를 발견했습니다.
    깊이 생각하지 않고, 습관적으로 코드를 짰음을 회고하고, 해당 코드를 전부 삭제했습니다.


4. 2차 구현 (14:46 - 14:50)
    사람들을 이동시키는 move함수의 BFS를 (ey, ex)에서 시작하도록 재구현했습니다.


5. 2차 디버깅 (14:50 - 14:57)
    move 함수의 (sy, sx)가 restricted(못 지나감) 처리가 돼있었기에,
    도착지점에 도착하지 못하는 에러를 print디버깅으로 확인하고 수정했습니다.


6. 검증 (14:57 - 15:28)
    O (1) 주어진 테스트케이스로 검증
    O (2) 메모 vs. 코드
    O (3) (머릿속 환기 후) 문제 재정독
    O (4) 커스텀 테스트케이스 검증
    O (5) 철저한 코드 검증
    O (6) 오답노트 활용
    X (7) 다양한 구상에 따른, 다른 구현

    검증루틴 2단계의 "모호한 부분/엣지 케이스 반영됐는지 체크"를 통한 아래의 수정사항이 있었습니다.

    문제 지문의 '격자에 있는 사람들이 모두 이동한 뒤에 해당 칸을 지나갈 수 없어짐에 유의합니다.' 문장이 다소 헷갈렸습니다.
    기존 구현에서는, 베이스캠프에서 출발하는 사람을 놓고난 뒤, 도착된 편의점을 못 지나감 처리를 했습니다.
    그러나 구현 단계에서 해당 부분에 대한 모호함을 메모해놨기에,
    다시 문제를 살피며, 해당 부분에 대한 오해를 바로잡을 수 있었습니다.

    그리고 검증루틴 바로 다음 단계인 3단계의 문제 재정독에서,
    해당 지문을 꼼꼼히 살피고 근거를 찾아, 이해&확신 했습니다.
    근거: 출발 전 사람은 격자 밖 사람임 + 정확히 1->2->3 순서로 수행된다고 함
"""

from collections import deque

direction = ((-1, 0), (0, -1), (0, 1), (1, 0))  # 우선순위; 상좌우하


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


# m초 이하에 출발하는 사람의 출발지점 찾는 BFS 함수
def depart(ey, ex):
    # 도착지에 가장 가까운 베이스캠프 찾아야 하므로, (ey, ex)에서 시작
    visited = [[0] * n for _ in range(n)]
    visited[ey][ex] = 1

    queue = deque()
    queue.append((ey, ex))

    while queue:
        next_queue = deque()
        found_base_camps = []  # 현재 queue의 탐색에서, 가능한 베이스캠프 위치가 저장될 배열

        while queue:
            y, x = queue.popleft()
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or visited[ny][nx] or restricted[ny][nx]:
                    continue
                if base_camps[ny][nx]:  # 베이스캠프 있다면, found_base_camps에 추가
                    found_base_camps.append((ny, nx))
                    continue
                visited[ny][nx] = 1
                next_queue.append((ny, nx))

        # 현재 queue의 탐색에서, 가능한 베이스캠프 있다면
        if found_base_camps:
            by, bx = min(found_base_camps)   # 여러 개인 경우 -> 행 낮은 순, 열 낮은 순
            base_camps[by][bx] = 0           # 베이스캠프 사용 처리
            movers.append((by, bx, ey, ex))  # 출발 상태를, 이동하는 사람들 배열에 추가
            restricted[by][bx] = 1           # 사용된 베이스캠프 이제 더이상 못 지나감
            return
        # 현재 queue의 탐색에서, 가능한 베이스캠프 없다면
        queue = next_queue


# 최단거리로 (sy, sx) -> (ey, ex) 1칸을 이동시키는 함수
def move(sy, sx, ey, ex):
    # 도착지에 가장 가까운 이동경로 찾아야 하므로, (ey, ex)에서 시작
    visited = [[0] * n for _ in range(n)]
    visited[ey][ex] = 1

    queue = deque()
    queue.append((ey, ex))

    while queue:
        next_queue = deque()
        right_before = []  # 도착 바로 직전의 위치들이 저장될 배열

        while queue:
            y, x = queue.popleft()
            distance = visited[y][x]

            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or visited[ny][nx] or (restricted[ny][nx] and not (ny == sy and nx == sx)):  # 출발 지점은 제한됐지만, 이 BFS 탐색의 종료조건이기에 갈 수 있어야 함
                    continue
                visited[ny][nx] = distance + 1
                next_queue.append((ny, nx))
                if ny == sy and nx == sx:  # 출발 지점이라면
                    right_before.append((y, x))

        # 현재 queue의 탐색에서, 출발 지점에 도달했다면
        if right_before:
            break
        # 현재 queue의 탐색에서, 출발 지점에 도달하지 못했다면
        queue = next_queue

    # 1칸 이동 시 출발->도착이라면, 제한될 좌표 배열에 도착한 편의점 좌표 추가하고 return
    if visited[sy][sx] == 2:
        restricting.append((ey, ex))
        return

    for dsy, dsx in direction:  # 상좌우하 우선순위
        nsy, nsx = sy + dsy, sx + dsx
        if (nsy, nsx) in right_before:  # 최단거리로 이동하는 좌표에 해당된다면 -> 1칸 이동한 상태를 이동종료상태 배열에 추가 & return
            next_movers.append((nsy, nsx, ey, ex))
            return


n, m = map(int, input().split())
base_camps = [list(map(int, input().split())) for _ in range(n)]  # 출발 가능한 베이스캠프 배열
departures = [None] + [tuple(map(lambda dep: int(dep) - 1, input().split())) for _ in range(m)]

restricted = [[0] * n for _ in range(n)]  # 못 지나감 처리가 반영될 배열

time = 0
movers = []  # 이동하는 사람들
while not time or movers:  # 사람들 이동이 모두 종료될 때까지
    time += 1

    # 1분간의 영역 내 사람들의 이동이 끝나고, 못 지나감 처리될 편의점 위치 배열
    restricting = []

    # 이동 중인 사람들 모두, 이동 처리
    next_movers = []  # (아직 도착하지 못한) 이동 종료 상태가 저장될 배열; 편의점 도착한 사람들은 안 담김
    for my, mx, ey, ex in movers:
        move(my, mx, ey, ex)
    movers = next_movers

    # 편의점 도착한 사람들의 편의점 위치는 이제 못 지나감
    for ry, rx in restricting:
        restricted[ry][rx] = 1

    # m초 이하라면, 현재 시간의 사람 출발시키기
    if time <= m:
        depart(*departures[time])

print(time)
