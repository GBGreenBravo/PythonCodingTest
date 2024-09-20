# 20240920
# 1:39:00
# 1 / 1

"""
풀이 시간: 1시간 39분 (09:00 - 10:39)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (09:00 - 09:11)
    문제를 다 읽고 단번에, 가능한 구상이 떠오르는 문제는 아니었습니다.
    공을 던지고 첫 공을 맞는 사람에 대한 처리는 구상이 가능했으나,
    팀의 이동에 대해서 단번에 떠오르는 명확한 구상이 없었습니다.

    조금 더 고민해본 결과,
    1부터 차례로 한칸씩 4로 옮기고 3에서 멈추면 되겠다는 생각이 들었고,
    구현 단계로 넘어갔습니다.


2. 1차 구현 (09:11 - 09:38)
    팀별 이동을 구현하던 와중에,
    1의 주변에는 4가 항상 있음을 가정하고 코드를 작성하는 부분에서,
    현재의 직관이 맞는지 의심이 들었습니다.

    문제에서 주어진 테케에서는, 1옆에 4가 항상 있었으나,
    (아래와 같이) 4없이 1/2/3만으로 채워진 이동선이 있을 수도 있겠다고 생각했습니다.
    1 3 2
    2 0 2
    2 2 2

    그렇다고 바로 이 케이스도 만족시키는 구현을 하지는 않았습니다.
    이 케이스를 만족시키는 별도의 분기처리만 해주면 되는 것으로 판단하고,
    메모에 해당 케이스를 표기하고, 기존 구현을 이어갔습니다.


3. 디버깅 (09:38 - 09:45)
    테케의 각 과정을 print하며 아래 2개의 실수를 잡아냈습니다.
    1) 이동선을 만나도 공이 멈추는 것으로 구현된 것
    2) turn을 k로 오타낸 것


4. 2차 구현 (09:45 - 10:00)
    1 3 2
    2 0 2
    2 2 2
    주어진 테케에서 다뤄지지 않은 위와 같은 경우(4없이 1/2/3만으로 채워진 이동선)도 만족시키는 구현을 했습니다.
    예상대로 분기처리를 통해 기존 구현에 큰 영향 없이, 구현할 수 있었습니다.


5. 검증 (10:00 - 10:39)
    O (1) 주어진 테스트케이스로 검증
    O (2) 메모 vs. 코드
    O (3) (머릿속 환기 후) 문제 재정독
    O (4) 커스텀 테스트케이스 검증
    O (5) 철저한 코드 검증
    O (6) 오답노트 활용
    X (7) 다양한 구상에 따른, 다른 구현
"""

from collections import deque

direction = ((0, 1), (-1, 0), (0, -1), (1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


# 현재 상태의 area에서 팀을 옮기는 함수
def move_people():
    one_visited = set()  # 옮겼던 팀 중복 이동 방지 set
    for sy in range(n):
        for sx in range(n):
            # 현재 좌표에 머리사람이 있고 and 이동되지 않은 팀이라면
            if area[sy][sx] == 1 and (sy, sx) not in one_visited:
                for sdy, sdx in direction:
                    """
                    1 3 2
                    2 0 2
                    2 2 2
                    """
                    # 위와 같이 4없이 123만으로 이동선 채워진 경우
                    if not oob(sy + sdy, sx + sdx) and area[sy + sdy][sx + sdx] == 3:
                        two = None
                        three = (sy + sdy, sx + sdx)
                        for dy, dx in direction:
                            if not oob(three[0] + dy, three[1] + dx) and area[three[0] + dy][three[1] + dx] == 2:
                                two = (three[0] + dy, three[1] + dx)
                                break

                        # 1 3 2 -> 2 1 3
                        area[sy][sx], area[three[0]][three[1]], area[two[0]][two[1]] = 2, 1, 3
                        # 팀의 중복이동 방지를 위해, 옮겨진 머리사람(1)좌표를 방문set에 추가
                        one_visited.add(three)
                        break

                # 이동선에 4 하나라도 존재하는 경우
                else:
                    y, x = sy, sx  # 머리사람(1) 좌표부터

                    while True:
                        something, four = None, None  # something: 안접한 2or3의 좌표 / four: 인접한 4의 좌표
                        for dy, dx in direction:
                            ny, nx = y + dy, x + dx
                            if oob(ny, nx):
                                continue
                            if area[ny][nx] == 4:
                                four = (ny, nx)
                            elif area[ny][nx]:  # elif area[ny][nx] in [2, 3]:
                                something = (ny, nx)

                        # 현재 좌표값과 4를 변경
                        area[y][x], area[four[0]][four[1]] = 4, area[y][x]

                        # 팀의 중복이동 방지를 위해, 옮겨진 머리사람(1)좌표를 방문set에 추가
                        if area[four[0]][four[1]] == 1:
                            one_visited.add(four)

                        # 다음에 옮겨줄 값이 3이면, 종료
                        if area[something[0]][something[1]] == 3:
                            area[y][x], area[something[0]][something[1]] = 3, 4
                            break
                        # 다음에 옮겨줄 값(2)의 좌표 갱신
                        y, x = something


# 입력 좌표 팀의 머리/꼬리를 바꾸고 & 입력 좌표가 팀에서 몇번째인지 반환하는 함수,
def find_order_and_change_direction(sy, sx):
    # BFS
    visited = [[0] * n for _ in range(n)]
    visited[sy][sx] = 1

    queue = deque()
    queue.append((sy, sx, 1))

    head, tail = None, None

    # 머리&꼬리 위치 찾을 때까지
    while queue and not (head and tail):
        y, x, o = queue.popleft()

        # 현재 좌표값이 머리사람(1)이면, 정보 저장 & 반환할 order 선언
        if area[y][x] == 1:
            head = (y, x)
            order = o
        # 현재 좌표값이 꼬리사람(3)이면, 정보 저장
        elif area[y][x] == 3:
            tail = (y, x)

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] or area[ny][nx] in [0, 4]:  # 영역 밖 / 이미 방문 / 사람X
                continue
            if area[y][x] == 3 and area[ny][nx] == 1:  # 4없이 123만으로 이동선 채워진 경우, 꼬리(3)->머리(1)로 못 가게 해야 정확한 순서 체크 가능
                continue
            visited[ny][nx] = 1
            queue.append((ny, nx, o + 1))

    # 머리 <-> 꼬리
    area[head[0]][head[1]], area[tail[0]][tail[1]] = 3, 1
    # 입력 좌표가 팀에서 몇번째인지 반환
    return order


# 공 던지고, 최초로 만나는 사람이 점수 얻는 함수
def throw_ball():
    global total_score

    # 4*N 만큼 반복하므로, 현재 turn에서 %연산 하면 됨
    by, bx, bd = ball_start_points[turn % (4 * n)]
    bdy, bdx = direction[bd]

    # 공이 좌표 밖으로 나갈 때까지
    while not oob(by, bx):
        # 사람 만나면, 점수 추가 & break
        if area[by][bx] in [1, 2, 3]:
            score = find_order_and_change_direction(by, bx) ** 2  # order ** 2
            total_score += score
            break
        # 사람 못 만나면, 공 한칸 이동
        by, bx = by + bdy, bx + bdx


n, m, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

# 4*N 개의 공 던지기의 초기 정보(시작 좌표, 던지는 방향)가 담길 배열
ball_start_points = []
for i in range(n):
    ball_start_points.append((i, 0, 0))
for i in range(n):
    ball_start_points.append((n - 1, i, 1))
for i in range(n - 1, -1, -1):
    ball_start_points.append((i, n - 1, 2))
for i in range(n - 1, -1, -1):
    ball_start_points.append((0, i, 3))

total_score = 0
for turn in range(k):  # k번 동안, 반복 수행
    move_people()
    throw_ball()
print(total_score)
