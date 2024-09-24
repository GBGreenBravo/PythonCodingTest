# 20240924
# 1:25:00
# 1 / 1

"""
풀이 시간: 1시간 25분 (09:03 - 10:28)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (09:03 - 09:20)
    문제 길이가 있는 편이었기에, 천천히 정독&메모 했습니다.
    최근 공격시점을 위한 N*M배열과, 공격과 유관한지를 체크하는 N*M배열을 두고, 무너진 포탑은 모두 0으로만 처리하면
    구현에 다른 어려움은 없을 것으로 생각했습니다.


2. 구현 (09:20 - 09:44)
    구현이 간단해보이는 3.포탑무너짐 과 4.포탑정비 에 대한 함수 구현을 먼저 했습니다.
    (체크포인트를 고려하지 않은 구현 절차 => 실수 미리 탐지하기 어려움)


3. 디버깅 (09:44 - 09:46)
    print 디버깅을 통해 아래의 실수를 잡아냈습니다.
    - repair(포탑정비) 함수에서, 무너진 포탑에 대해서도 +1을 해주고 있었음.

    구현 과정에서 체크포인트를 고려하지 않고, 3.포탑무너짐 과 4.포탑정비 에 대한 함수 구현을 먼저 했습니다.
    그렇기에 체크포인트를 활용하지 않았고, 이 단계에서의 실수를 미리 탐지하지 못해, 디버깅 단계에서 찾아내게 됐습니다.
    앞으로는, 구현 단계에서 쉬워보이는 것을 먼저 구현하기 보다, 체크포인트를 고려한 구현 절차를 따라야겠습니다.


4. 검증 (09:46 - 10:28)
    - 메모를 보며 코드와 대조하는 과정에서 직관적으로 쓰인 수치를 검증해줬습니다.
        - select_attacked_object 함수에서 최대값을 -1로 선언한 것은 합당했으나,
        - select_attacker 함수의 최소값을 5001로 선언하는 것에 대한 정확한 검증은 어려웠습니다.
            - N*M이 최대 100이었기에, 최대값+1로 선언하는 것으로 수정했습니다.


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
direction_8 = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1))


# (1. 공격자 선정) 수행하는 함수
def select_attacker():
    # 불가능한 최소값 설정
    min_attack = max(map(max, area)) + 1
    candidates = []

    for y in range(n):
        for x in range(m):
            if not area[y][x]:  # 부서진 포탑 -> continue
                continue
            if area[y][x] < min_attack:     # 최소값보다 작다면 -> 최소값 갱신 & 후보 초기화
                min_attack = area[y][x]
                candidates = [(-recent[y][x], -(y + x), -x, y, x)]
            elif area[y][x] == min_attack:  # 최소값과 같다면 -> 후보에 추가
                candidates.append((-recent[y][x], -(y + x), -x, y, x))

    # 우선순위대로 넣어놨기에 그대로 sort & index 0의 (y,x)좌표 가져오기
    candidates.sort()
    weakest_y, weakest_x = candidates[0][-2:]

    area[weakest_y][weakest_x] += n + m             # 공격력 N+M 증가
    relevant_with_attack[weakest_y][weakest_x] = 1  # 현재 턴의 공격과 유관함 처리
    recent[weakest_y][weakest_x] = turn             # 최근 공격시점 갱신

    return weakest_y, weakest_x


# (2-0. 공격대상 선정) 수행하는 함수
def select_attacked_object():
    # 불가능한 최대값 설정
    max_attack = -1
    candidates = []

    for y in range(n):
        for x in range(m):
            if not area[y][x] or (y == ay and x == ax):  # 부서진 포탑 or 공격자 좌표 -> continue
                continue
            if area[y][x] > max_attack:     # 최대값보다 크다면 -> 최대값 갱신 & 후보 초기화
                max_attack = area[y][x]
                candidates = [(recent[y][x], y + x, x, y, x)]
            elif area[y][x] == max_attack:  # 최대값과 같다면 -> 후보에 추가
                candidates.append((recent[y][x], y + x, x, y, x))

    # 우선순위대로 넣어놨기에 그대로 sort & index 0의 (y,x)좌표 가져오기
    candidates.sort()
    strongest_y, strongest_x = candidates[0][-2:]

    area[strongest_y][strongest_x] -= area[ay][ax]      # 공격 피해량 반영
    relevant_with_attack[strongest_y][strongest_x] = 1  # 현재 턴의 공격과 유관함 처리

    return strongest_y, strongest_x


# (2. 레이저/포탄 공격 수행) 수행하는 함수
def attack(sy, sx, ey, ex):
    # 레이저 공격 시도 (BFS)
    visited = [[0] * m for _ in range(n)]
    visited[sy][sx] = 1

    queue = deque()
    queue.append((sy, sx, []))

    while queue:
        y, x, routes = queue.popleft()  # routes: 경유지 좌표 리스트
        for dy, dx in direction_4:                   # 우하좌상순
            ny, nx = (y + dy) % n, (x + dx) % m      # oob -> %
            if visited[ny][nx] or not area[ny][nx]:  # 이미 방문 or 부서진 포탑 -> continue
                continue

            # 공격대상 좌표에 도달 가능하다면 -> 레이저공격 수행 & return
            if ny == ey and nx == ex:
                attack_power = area[sy][sx] // 2
                # 경유지들에 대한, 공격 피해량 반영 & 현재 턴의 공격과 유관함 처리
                for ry, rx in routes:
                    area[ry][rx] -= attack_power
                    relevant_with_attack[ry][rx] = 1
                return

            visited[ny][nx] = 1
            queue.append((ny, nx, routes + [(ny, nx)]))

    # 위의 레이저 공격이 수행되지 않았다면, 포탄 공격 수행
    attack_power = area[sy][sx] // 2
    for dy, dx in direction_8:
        ny, nx = (ey + dy) % n, (ex + dx) % m  # oob -> %
        if area[ny][nx] and not (ny == sy and nx == sx):  # 부서지지 않은 포탑 & 공격자 좌표X
            # 공격 피해량 반영 & 현재 턴의 공격과 유관함 처리
            area[ny][nx] -= attack_power
            relevant_with_attack[ny][nx] = 1


# (3. 포탑 부서짐) 수행하는 함수
def collapse():
    for y in range(n):
        for x in range(m):
            if area[y][x] < 0:  # 포탑 공격력이 음수라면 -> 0(부서진 포탑)으로 처리
                area[y][x] = 0


# (4. 포탑 정비) 수행하는 함수
def repair():
    for y in range(n):
        for x in range(m):
            if area[y][x] and not relevant_with_attack[y][x]:  # 포탑 부서지지 않았고 & 공격과 무관하다면
                area[y][x] += 1


n, m, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]  # 포탑 공격력 N*M배열

# 최근 공격시점 저장할 N*M배열
recent = [[0] * m for _ in range(n)]

for turn in range(1, k + 1):
    if sum(map(lambda ar: ar.count(0), area)) == n * m - 1:
        break

    # 현재 턴의 공격과 유관한지 체크할 N*M배열
    relevant_with_attack = [[0] * m for _ in range(n)]

    ay, ax = select_attacker()         # 1. 공격자 선정
    oy, ox = select_attacked_object()  # 2-0. 공격대상 선정
    attack(ay, ax, oy, ox)             # 2. 레이저/포탄 공격 수행

    collapse()                         # 3. 포탑 부서짐
    repair()                           # 4. 포탑 정비

# 가장 강한 포탑 공격력 출력
print(max(map(max, area)))
