# 20240924
# 1:31:00
# 1 / 1

"""
풀이 시간: 1시간 31분 (14:03 - 15:34)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:03 - 14:14)
    문제에서 말하는 최단거리는 택시거리로, BFS식 최단거리가 아님을 체크했습니다.

    그리고 한 가지 궁금했던 건,
    "K초 이전에 모든 참가자가 탈출했을 때, 미로회전하고 break인지 그냥 break인지" 였습니다.
    (추후 검증 단계에서, 미로회전을 하기 위해서는 참가자가 최소 1명 남아있어야 했기에 전자가 맞음을 확인했습니다.)


2. 1차 구현 (14:14 - 14:42)
    참가자가 최대 10명이었기에, 참가자 좌표 리스트 하나만 두고 구현하기로 했습니다. (참가자 존재 N*N배열 활용 X)
    출구좌표도 walls에 -1과 같이 표현할 수도 있겠지만, 익숙한 방식인 '변수로 따로 관리'를 택했습니다.


3. 디버깅 (14:42 - 14:52)
    빠른 print 디버깅을 통해 아래의 실수 3개를 확인하고 수정했습니다.
    - 회전용 배열을 슬라이싱할 때, 한번 더 리스트로 감싼 것
    - cy, cx 변수 할당 시, 하나만 해준 것
    - 정사각형 영역 내 참가자들 좌표 회전시키기 까먹은 것

    테스트케이스와 답이 다른 것을 확인했기에, 테케의 절차를 볼 수 있도록 print 디버깅했고, 다음 실수를 확인했습니다.
    - 회전할 정사각형 영역 찾을 때, 출구 기준 대각선방향으로만 확장하면 안됨. (출구가 꼭짓점에 존재하지 않는 정사각형도 있기 때문)
    해당 실수는 재구현을 해줘야하는 부분이었기에, 2차 구현으로 넘어갔습니다.


4. 2차 구현 (14:52 - 14:57)
    기존에 출구 기준 대각선 방향으로 정사각형을 확장하며 정사각형 영역을 찾았던 코드를,
    정사각형 사이즈를 1씩 늘리며 2중 for문으로 탐색하는 코드로, 변경했습니다.


4. 검증 (14:57 - 15:34)
    O (1) 주어진 테스트케이스로 검증
    O (2) 메모 vs. 코드
        - 정독 단계에서 모호하다고 했던 부분을, 확실히 이해하고 넘어갔습니다.
        - 2차 구현으로 인해, 초기 구상과 달라졌기에, 코드를 바탕으로 시간복잡도를 다시 계산했습니다.
    O (3) (머릿속 환기 후) 문제 재정독
    O (4) 커스텀 테스트케이스 검증
        - 모든 참가자가 탈출하면, K초 이전에 break 하는지
        - 미로 회전이 최대 사이즈에서도 잘 되는지
        - 입력 조건 최대치 테케에서 실행시간 이슈 없는지
        - 다양한 상황에서의, 좌표기준 시계방향 90도 회전 검증
        - zip 활용 시계방향 90도 회전 검증
    O (5) 철저한 코드 검증
    O (6) 오답노트 활용
    X (7) 다양한 구상에 따른, 다른 구현
"""

direction = ((1, 0), (-1, 0), (0, 1), (0, -1))  # 하상우좌


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


# (y, x)에 있는 참가자를 이동시키는 함수
def move_participant(y, x):
    global total_distance

    origin_shortest = abs(ey - y) + abs(ex - x)  # 기존 위치에서 출구까지의 최단거리
    for dy, dx in direction:  # '하/상'이 '우/좌'보다 우선순위 높음
        ny, nx = y + dy, x + dx
        # 영역 밖 / 벽 O / 기존 최단거리보다 작지 않음 -> continue
        if oob(ny, nx) or walls[ny][nx] or abs(ey - ny) + abs(ex - nx) >= origin_shortest:
            continue

        # 이동거리 1 추가
        total_distance += 1

        # 이동하는 곳이 출구라면 -> 탈출 (next_participants에 추가하지 않고 바로 return)
        if ny == ey and nx == ex:
            return

        # 이동하는 곳이 출구가 아니라면 -> next_participants에 추가 & return
        next_participants.append([ny, nx])
        return

    # 움직일 수 없는 상황 -> 움직이지 않은 상태를 next_participants에 추가
    next_participants.append([y, x])


# 특정 정사각형 영역을 회전시키는 함수
def rotate_maze():
    global ey, ex

    # upper_left: 좌상단 좌표가 담길 변수 / rotated_size = 정사각형 변 길이-1
    upper_left = None
    rotated_size = 0

    # 가장 작은 정사각형 영역 찾는 코드
    while not upper_left:  # 정사각형 영역 찾을 때까지
        rotated_size += 1  # 탐색 길이 += 1
        for y in range(n - rotated_size):
            for x in range(n - rotated_size):
                # 현재 영역: (y ~ y+rotated_size) ~ (x ~ x+rotated_size)
                if not (y <= ey <= y + rotated_size) or not (x <= ex <= x + rotated_size):  # 출구가 해당 영역에 없다면 -> continue
                    continue
                for py, px in participants:
                    if (y <= py <= y + rotated_size) and (x <= px <= x + rotated_size):     # 특정 참가자가 해당 영역에 있다면 -> break
                        upper_left = (y, x)
                        break
                else:
                    continue
                break
            else:
                continue
            break

    # (zip활용 회전) 정사각형 영역의 벽 회전시키며 내구도 감소시키는 함수
    rotating = [walls[row][upper_left[1]:upper_left[1] + rotated_size + 1] for row in range(upper_left[0], upper_left[0] + rotated_size + 1)]
    rotating = [list(row)[::-1] for row in zip(*rotating)]  # 시계방향 90도 회전
    for y in range(rotated_size + 1):
        for x in range(rotated_size + 1):
            walls[upper_left[0] + y][upper_left[1] + x] = rotating[y][x] - 1 if rotating[y][x] else rotating[y][x]  # 벽 있다면 내구도 -1

    # (좌표기준 회전)
    cy, cx = upper_left[0] + rotated_size / 2, upper_left[1] + rotated_size / 2  # 정사각형 영역의 중심 좌표

    # 출구좌표 회전
    edy, edx = ey - cy, ex - cx
    ey, ex = int(cy + edx), int(cx - edy)

    # 정사각형 영역 내 참가자들 좌표 회전
    for pi in range(len(participants)):
        py, px = participants[pi]
        if (upper_left[0] <= py <= upper_left[0] + rotated_size) and (upper_left[1] <= px <= upper_left[1] + rotated_size):  # 영역 내라면
            epy, epx = py - cy, px - cx
            participants[pi] = [int(cy + epx), int(cx - epy)]


n, m, k = map(int, input().split())
walls = [list(map(int, input().split())) for _ in range(n)]                          # 벽의 내구도 배열
participants = [list(map(lambda p: int(p) - 1, input().split())) for _ in range(m)]  # 참가자들 위치 리스트
ey, ex = map(lambda e: int(e) - 1, input().split())                                  # 출구 좌표

total_distance = 0  # 참가자들 총 이동 거리
for _ in range(k):
    # 탈출 못한 참가자들 동시 이동
    next_participants = []  # 이동 후의 참가자들 위치가 담길 리스트 (탈출한 참가자는 안 담김)
    for par_y, par_x in participants:
        move_participant(par_y, par_x)
    participants = next_participants

    # 모든 참가자가 탈출했다면 -> break
    if not participants:
        break

    # 미로 회전
    rotate_maze()

# 참가자들 총 이동 거리 & 출구 좌표 출력
print(total_distance)
print(ey + 1, ex + 1)
