# 20240926
# 1:19:00
# 1 / 1

"""
풀이 시간: 1시간 19분 (14:06 - 15:25)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:06 - 14:21)
    패딩처리,하드코딩,임의로지정한flag가 활용된 문제였기에,
    문제 메모 뿐만 아니라, (아래의) 구상의 기초 세팅들도 적고 시작했습니다.
    -----------------------------------------------------------
    < 기초 세팅 >

    패딩으로 왼쪽/아래쪽/오른쪽에 벽을 넣고,
    (진입하는 골렘 넣기 위해) 윗부분에 가상의 3행을 추가하여,
    아래와 같이 area배열을 구성했습니다.

          0   1   .   .   .   c   c+1

    0    -1   0   0   0   0   0   -1    가상의 행
    1    -1   0   0   0   0   0   -1    가상의 행
    2    -1   0   0   0   0   0   -1    가상의 행
    3    -1   0   0   0   0   0   -1    실제 1행
    .    -1   0   0   0   0   0   -1       .
    .    -1   0   0   0   0   0   -1       .
    .    -1   0   0   0   0   0   -1       .
    .    -1   0   0   0   0   0   -1       .
    r+2  -1   0   0   0   0   0   -1    실제 r행
    r+3  -1  -1  -1  -1  -1  -1   -1    패딩 (벽)

    -1 : 벽
    0  : 빈칸
    1  : 골렘의 가운데
    2  : 골렘의 출구
    3  : 십자부분 중 출구가 아닌 나머지

    그리고 아래의 골렘의 정보를 area 내에 표시하기 위해, 1/2/3을 활용했습니다. (정령 번호는 표시할 필요 X)
      3
    2 1 3  => 서쪽이 출구인 골렘
      3

2. 구현 (14:21 - 15:05)
    체크포인트를 활용하여 아래의 실수를 미리 탐지하고 수정했습니다.
    - 골렘이 내려갈 때, 원래 있던 좌표 0 처리 안 해준 것


3. 디버깅 (15:05 - 15:08)
    골렘이 다른 골렘의 3(출구가 아닌 십자 부분)에 갔을 때,
    별도의 수행을 하지 않던 부분을 발견하고 추가로 구현했습니다.


4. 검증 (15:08 - 15:25)
    하드코딩을 활용한 풀이였기에, 하드코딩된 부분을 위주로 검증했습니다.

    O (1) 주어진 테스트케이스로 검증
    O (2) 메모 vs. 코드
    O (3) (머릿속 환기 후) 문제 재정독
    O (4) 커스텀 테스트케이스 검증
    O (5) 철저한 코드 검증
    O (6) 오답노트 활용
    X (7) 다양한 구상에 따른, 다른 구현
"""

from collections import deque

direction = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 북동남서

# 현재 골렘의 중심 좌표(y, x)를 기준으로
# 각각 '아래 / 왼쪽&아래 / 오른쪽&아래'로 갈 때,
# 비어있어야 하는 (dy, dx)를 하드코딩했습니다.
south = ((1, -1), (2, 0), (1, 1))
west_south = ((-1, -1), (0, -2), (1, -1), (1, -2), (2, -1))
east_south = ((-1, 1), (0, 2), (1, 1), (1, 2), (2, 1))


# 현재 골렘의 중심 좌표(y, x)를 기준으로,
# 아래쪽으로 갈수 있는지 판단하는 함수
def can_move_south(y, x):
    for dy, dx in south:
        if area[y + dy][x + dx]:
            return False
    return True


# 현재 골렘의 중심 좌표(y, x)를 기준으로,
# 왼쪽&아래쪽으로 갈수 있는지 판단하는 함수
def can_move_west_south(y, x):
    for dy, dx in west_south:
        if area[y + dy][x + dx]:
            return False
    return True


# 현재 골렘의 중심 좌표(y, x)를 기준으로,
# 오른쪽&아래쪽으로 갈수 있는지 판단하는 함수
def can_move_east_south(y, x):
    for dy, dx in east_south:
        if area[y + dy][x + dx]:
            return False
    return True


# 시작 시, 골렘을 (1행, sx)을 중심으로 한 십자부분까지 area에 두고,
# 가능할 때까지 아래로 내리는 함수 (최종 골렘 중심좌표를 반환)
def move_golem(sx, e_idx):
    # 골렘의 중심 좌표
    y, x = 1, sx

    # 중심 좌표는 1로 표시
    area[1][sx] = 1

    # 십자 부분은 3으로 표시
    area[0][sx] = 3
    area[2][sx] = 3
    area[1][sx - 1] = 3
    area[1][sx + 1] = 3

    # 출구 부분은 2로 표시
    dy, dx = direction[e_idx]
    area[y + dy][x + dx] = 2

    # 가능할 때까지 아래로 내리기
    while True:
        # (우선순위 1) 아래로 이동 가능한 경우
        if can_move_south(y, x):
            # 골렘의 다음 좌표를 알맞게 표시
            area[y + 1][x], area[y][x], area[y + 1][x + 1], area[y + 2][x], area[y + 1][x - 1] = area[y][x], area[y - 1][x], area[y][x + 1], area[y + 1][x], area[y][x - 1]
            # 이동한 뒤 비워지는 좌표들 0으로 표시
            area[y][x - 1], area[y - 1][x], area[y][x + 1] = 0, 0, 0
            y, x = y + 1, x

        # (우선순위 2) 왼쪽&아래로 이동 가능한 경우
        elif can_move_west_south(y, x):
            area[y + 1][x - 1], area[y + 1][x - 2], area[y][x - 1], area[y + 1][x], area[y + 2][x - 1] = area[y][x], area[y - 1][x], area[y][x + 1], area[y + 1][x], area[y][x - 1]
            area[y][x], area[y - 1][x], area[y][x + 1] = 0, 0, 0
            y, x = y + 1, x - 1

        # (우선순위 3) 오른쪽&아래로 이동 가능한 경우
        elif can_move_east_south(y, x):
            area[y + 1][x + 1], area[y + 1][x + 2], area[y + 2][x + 1], area[y + 1][x], area[y][x + 1] = area[y][x], area[y - 1][x], area[y][x + 1], area[y + 1][x], area[y][x - 1]
            area[y][x], area[y - 1][x], area[y][x - 1] = 0, 0, 0
            y, x = y + 1, x + 1

        # (우선순위 3까지 불가능하다면) 내려올 수 있는 만큼 내려온 것이므로, break
        else:
            break

    # 골렘의 최종 중심좌표를 반환
    return y, x


# (BFS) (sy, sx)부터 시작해서, 정령이 이동할 수 있는 가장 큰 행을 반환하는 함수
def move_fairy(sy, sx):
    # 입력의 (sy, sx)는 항상 골렘의 중심좌표기에, sy + 1로 선언
    max_row = sy + 1

    visited = [[0] * (c + 2) for _ in range(r + 4)]
    visited[sy][sx] = 1

    queue = deque()
    queue.append((sy, sx))

    while queue:
        y, x = queue.popleft()

        # 최대 행 갱신
        max_row = max(max_row, y)

        # (y, x)가 골렘 중심좌표인 경우 -> 4방향 다 갈 수 있음
        if area[y][x] == 1:
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if visited[ny][nx]:
                    continue
                visited[ny][nx] = 1
                queue.append((ny, nx))

        # (y, x)가 골렘 출구인 경우 -> 빈칸(0)과 벽(-1) 빼고 다 갈 수 있음
        elif area[y][x] == 2:
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if visited[ny][nx] or area[ny][nx] in [0, -1]:
                    continue
                visited[ny][nx] = 1
                queue.append((ny, nx))

        # (y, x)가 출구가 아닌 골렘의 십자 부분인 경우 -> 골렘 중심(1)으로만 갈 수 있음
        elif area[y][x] == 3:
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if area[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    queue.append((ny, nx))
        else:  # 이 경우는 코드가 거치지 않음 (디버깅용)
            pass

    #  정령이 이동할 수 있는 가장 큰 행을 반환
    return max_row


r, c, k = map(int, input().split())
golem_start_information = [tuple(map(int, input().split())) for _ in range(k)]

# 왼쪽/아래쪽/오른쪽 벽 패딩처리 & 위쪽의 가상의 행 3개
# 를 반영한 area 선언
area = [[-1] + [0] * c + [-1] for _ in range(r + 3)] + [[-1] * (c + 2)]

answer = 0
for start_column, exit_idx in golem_start_information:
    # (start_column에서 exit_idx의 출구 방향을 갖는)
    # 골렘을 출발시키고, 도착지점의 좌표 가져오기
    center_y, center_x = move_golem(start_column, exit_idx)

    # 도착한 행index가 3이하면, (몸 일부가 숲 밖에 있으므로)
    # area 초기화 & continue
    if center_y <= 3:
        area = [[-1] + [0] * c + [-1] for _ in range(r + 3)] + [[-1] * (c + 2)]
        continue

    # 도착한 골렘의 중심지점부터 시작해서, 정령이 이동할 수 있는 가장 큰 번호의 행 불러오기
    moved_y = move_fairy(center_y, center_x)
    # 행 번호를 누적 (-2; 가상의 행 3개와 0 index부터 시작을 반영한 수치)
    answer += moved_y - 2
print(answer)
