# 20240926
# 1:19:00
# 1 / 1

"""
풀이 시간: 1시간 19분 (09:02 - 10:21)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (09:02 - 09:15)
    BFS 템플릿을 큰 변형 없이 그대로 적용하면 되는 문제로 확인했습니다.

    시간복잡도를 계산하고 여유 있음을 확인하고 넘어갔습니다.


2. 구현 (09:15 - 09:30 / 09:38 - 09:49)
    문제에서는 3*3영역 회전을 설명할 때, 중심 좌표로 설명했습니다.
    좌표기준 회전을 활용한다면, range(1, 4)로 하면 되지만,
    저는 좌상단 좌표를 기준으로 zip()활용 회전을 했기에, range(0, 3)으로 모든 3*3영역 회전을 다뤄줬습니다.


3. 디버깅 (09:49 - 09:50)
    최종 답안 출력에서, 구분자가 '\n'이 아닌 ' '가 되도록 수정했습니다.


4. 검증 (09:50 - 10:21)
    O (1) 주어진 테스트케이스로 검증
    O (2) 메모 vs. 코드
        - 문제 메모를 다시 읽으며, (틀린 코드는 아니었지만) 오해했던 부분을 바로잡았습니다.
          벽면의 숫자들이 다 쓰이면, 다시 index 0부터 쓰는 걸로 구현했지만,
          문제를 다시 읽어보니, 사용된 벽면의 수는 재사용 불가능하고 & 조각이 부족한 경우는 없다고 명시돼 있었습니다.
          따라서, 기존의 코드였던 "add_idx = (add_idx + 1) % m"을 "add_idx += 1"로 수정했습니다.
    O (3) (머릿속 환기 후) 문제 재정독
    O (4) 커스텀 테스트케이스 검증
    O (5) 철저한 코드 검증
    O (6) 오답노트 활용
    X (7) 다양한 구상에 따른, 다른 구현
"""

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or 5 <= y or x < 0 or 5 <= x


# 입력의 arr 배열의 좌상단 좌표(top, left)를 기준으로 3*3 영역을 rotating_cnt만큼 시계방향 회전해서 반환하는 함수
def rotate_clockwise(arr, top, left, rotating_cnt):
    return_arr = [row[:] for row in arr]  # deepcopy

    # 회전시킬 영역
    rotating = [return_arr[row][left:left + 3] for row in range(top, top + 3)]
    # rotating_cnt만큼 시계방향 회전
    for _ in range(rotating_cnt):
        rotating = [list(row)[::-1] for row in zip(*rotating)]
    # 회전된 결과 반영
    for y in range(3):
        for x in range(3):
            return_arr[top + y][left + x] = rotating[y][x]
    return return_arr


# (BFS) 현재 arr의 유물 가치를 계산하는 함수
def cal_first_value(arr):
    value = 0  # 유물 가치
    visited = [[0] * 5 for _ in range(5)]

    for sy in range(5):
        for sx in range(5):
            # 미방문이라면 BFS 시작
            if not visited[sy][sx]:
                group_cnt = 1                 # 연결되는 같은 유물들 수
                group_criteria = arr[sy][sx]  # 유물 종류

                visited[sy][sx] = 1

                queue = deque()
                queue.append((sy, sx))

                while queue:
                    y, x = queue.popleft()
                    for dy, dx in direction:
                        ny, nx = y + dy, x + dx
                        if oob(ny, nx) or visited[ny][nx] or arr[ny][nx] != group_criteria:
                            continue
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
                        group_cnt += 1

                # 3 이상이면 유물 구성 O
                if group_cnt >= 3:
                    value += group_cnt

    return value


# 5*5배열의 모든 3*3영역에 대해 90/180/270 시계방향 회전시켜보고,
# 문제 조건의 최우선순위에 해당하는 회전 정보를 반환하는 함수
def find_max_method():
    candidates = []

    # 5*5배열의 가능한 모든 3*3영역은 9개
    for top in range(3):
        for left in range(3):
            # 90/180/270 시계방향 회전 후, 회전 정보 저장
            for rotating_cnt in range(1, 4):
                now_area = rotate_clockwise(area, top, left, rotating_cnt)
                candidates.append((top, left, rotating_cnt, cal_first_value(now_area)))

    candidates.sort(key=lambda candi: (-candi[3], candi[2], candi[1], candi[0]))  # 1차획득가치 내림차순 / 회전각도 오름차순 / 열 오름차순 / 행 오름차순
    return candidates[0]


# (BFS) 현재 area의 유물을 0으로 바꾸고, 유물 가치를 반환하는 함수
def get_value():
    value = 0  # 유물 가치
    visited = [[0] * 5 for _ in range(5)]

    for sy in range(5):
        for sx in range(5):
            # 미방문이라면 BFS 시작
            if not visited[sy][sx]:
                group_indexes = [(sy, sx)]     # 연결되는 같은 유물들의 좌표가 저장될 배열
                group_criteria = area[sy][sx]  # 유물 종류

                visited[sy][sx] = 1

                queue = deque()
                queue.append((sy, sx))

                while queue:
                    y, x = queue.popleft()
                    for dy, dx in direction:
                        ny, nx = y + dy, x + dx
                        if oob(ny, nx) or visited[ny][nx] or area[ny][nx] != group_criteria:
                            continue
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
                        group_indexes.append((ny, nx))

                # 3 미만이면 유물 구성 X
                if len(group_indexes) < 3:
                    continue

                value += len(group_indexes)   # 유물 가치 +=
                for gy, gx in group_indexes:  # 유물 좌표 0으로 변환
                    area[gy][gx] = 0

    return value


# 열 번호 작은 순, 행 번호 큰 순으로 탐색하며, 빈 곳에 조각 채우는 함수
def fill():
    global add_idx

    for col in range(5):
        for row in range(4, -1, -1):
            if not area[row][col]:
                area[row][col] = additions[add_idx]
                add_idx += 1  # 조각 재사용 X and 조각 부족하지 않다고 했기에, 'add_idx %= m' 안 해줘도 됨


k, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(5)]

# 조각 채우기 위한 벽면의 수 정보 / index
additions = list(map(int, input().split()))
add_idx = 0

answers = []
for _ in range(k):
    top_y, left_x, rotate_cnt, start_value = find_max_method()  # 현재 턴에서 회전 시킬 좌상단 좌표, 회전 횟수, 1차 획득 가치
    area = rotate_clockwise(area, top_y, left_x, rotate_cnt)    # 위 정보 대로 배열 회전

    if not start_value:  # 현재 턴에 얻을 수 있는 가치 없으면, 즉시 종료(break)
        break

    tmp_value = get_value()  # start_value와 같은 값이지만, 유물 0으로 바꾸는 작업을 위해 호출
    fill()                   # 조각 채우기
    turn_value = tmp_value   # 현재 턴에 얻는 유물 총 가치

    while tmp_value:             # 유물 안 생길 때까지
        tmp_value = get_value()  # 유물 0으로 바꾸고, 유물 가치 계산
        fill()                   # 조각 채우기
        turn_value += tmp_value  # 현재 턴 유물 총 가치 += 유물 가치

    answers.append(turn_value)  # 현재 턴 유물 총 가치 추가
print(*answers, sep=" ")
