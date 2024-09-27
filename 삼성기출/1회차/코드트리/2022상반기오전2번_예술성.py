# 20240919
# 1:21:00
# 1 / 1

"""
풀이 시간: 1시간 21분 (09:00 ~ 10:21)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (09:00 - 09:06)
    그룹끼리 맞닿는 변의 수를 체크하는 것 말고는, 전부 구현해봤던 것들이기에
    해당 부분에 대한 구상만 따로 해줬습니다.
    그 결과, BFS에서 체크해주면 되는 것으로 확인하고 구현으로 넘어갔습니다.


2. 구현 (09:06 - 09:40)
    메인코드를 먼저 작성하고, 함수화된 부분을 구현했습니다.
    먼저, 배열 회전의 경우 중심 십자가 부분과 나머지는 달리 해줘야 했기에,
    따로 함수화하고, 문제 지문에서 주어진 예시 그림 대로 체크포인트를 찍어보고,
    별도의 커스텀 테케를 만들어서 해당 코드의 정상 동작을 확인했습니다.

    그룹 정보와 맞닿는 변 체크를 위한 BFS 함수를 2개로 분리했는데,
    앞의 함수를 작성하고 (문제는 없었지만) 체크포인트로 검증했어야 하는데, 그러지 못했음에 반성할 부분이 있습니다.


3. 디버깅 (09:40 - 09:45)
    맞닿는 변의 수를 세는 함수를 작성하고, 테스트케이스를 실행한 결과, 에러가 떴습니다.
    아래의 실수들에 따른 에러를 확인하고 수정했습니다.
    1) [i][j]의 인덱싱을 빠트림
    2) 2중리스트를 작성해야 하는 부분에, 실수로 []를 추가로 기입하여 3중리스트를 처음에 선언돼 있었음


4. 검증 (09:45 - 10:21)
    추석 연휴 동안 정리한, 최종 문제풀이 루틴을 점검해보기 위해
    + 한 번에 정확한 답안을 제출하기 위해
    검증 단계를 천천히 따랐습니다.
    (최종 문제풀이 루틴은 코드 맨 아래에 주석으로 첨부합니다!)
    아직 최종 루틴을 외우지는 못했기에, 해당 파일을 참고하며 검증 루틴을 한 단계씩 따랐습니다.

    (1) 주어진 테스트케이스로 검증
    (2) 메모 vs. 코드
    (3) (머릿속 환기 후) 문제 재정독
    (4) 철저한 코드 검증
    (5) 커스텀 테스트케이스 검증
    (6) 오답노트 활용
    (7) 다양한 구상에 따른, 다른 구현

    5번(커스텀 테케 검증)과 7번(다양한 구상에 따른 구현)을 제외하고는 모두 적용해봤습니다.

    1번에서는 2차원 배열, 각 그룹 정보, 그룹의 맞닿는 변, 시계/반시계 회전 등
    가시적으로 확인할 수 있는 정보들은 거의 다 print()를 통해 확인했습니다.

    2번의 검증에서 회고할 점은, 메모가 더 자세히 작성되면 좋았겠다는 점입니다.
    문제 지문이 길거나 복잡한 편은 아니었으나, 정독 시간이 6분 밖에 되지 않았기에,
    해당 시간을 더 늘려도 전혀 상관이 없기에, 더 꼼꼼히 문제를 읽고 메모도 자세히 해야겠습니다.

    3번에서는 처음에 바로 문제와 메모를 비교대조하려 했으나,
    그러면 기존 이해를 바탕으로 문제 지문을 읽게 될 것 같아,
    앞 단계에 완전히 머릿속을 비운 후 문제를 읽어보는 절차를 추가했습니다.
    (메모 재작성도 추가할지 생각 중입니다)

    4번에서는 실제 시험이었다면 코드를 재작성해봤겠지만,
    연습단계에서 코드 리뷰를 작성할 시간을 생각하면, 1시간 30분보다 적게 남았었기에,
    전체 코드를 재작성하지는 않았습니다.

    구현 단계의 체크포인트에서 7*7 배열 회전에 대해 확인한 바 있었고,
    1번에서 테스트케이스 정밀하게 확인했고,
    N * M 배열이 아니었기에,
    5번은 넘어갔습니다.

    6번의 오답노트 활용에서는, 기존 계획은 오답노트의 내용을 모두 암기하고
    코드의 단위 하나하나를 살펴보면서, 실수를 되풀이하지 않았는지 체크하려 했습니다.
    아직 오답노트 내용을 모두 암기하지 못했기에, 정리된 파일을 참고하며 코드를 살펴봤습니다.

    구상 단계에서 모호한 부분이 없었기에, 7번은 넘어갔습니다.
"""

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


# 십자가 부분(정중앙 제외)을 반시계 회전시키는 함수
def rotate_counterclockwise():
    for num in range(n):
        if num == n // 2:
            continue
        new_area[n // 2][num] = area[num][n // 2]
        new_area[n - 1 - num][n // 2] = area[n // 2][num]


# 시작좌표와 한계좌표를 받아, 해당 좌표의 영역을 시계방향 회전시키는 함수
def rotate_clockwise(sy, sx, ey, ex):
    tmp_area = []
    for row in range(sy, ey):
        tmp_area.append(area[row][sx:ex])
    tmp_area = [list(row)[::-1] for row in zip(*tmp_area)]  # 시계방향 90도 회전

    for y in range(n // 2):
        for x in range(n // 2):
            new_area[sy + y][sx + x] = tmp_area[y][x]


# 현재 좌표의 그룹을 표기하고, 그룹의 값과 칸 수를 반환하는 함수
def cal_group_info(sy, sx):
    group_visited[sy][sx] = group_flag

    queue = deque()
    queue.append((sy, sx))

    group_value = area[sy][sx]  # 그룹의 값
    group_cnt = 1               # 그룹의 칸 수

    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or group_visited[ny][nx] or area[ny][nx] != group_value:
                continue
            group_visited[ny][nx] = group_flag
            queue.append((ny, nx))
            group_cnt += 1

    return group_value, group_cnt


# 그룹별로 BFS를 실행하여, 맞닿는 변의 수를 세는 함수
def cal_group_nears():
    flag_visited = [[0] * n for _ in range(n)]

    for yy in range(n):
        for xx in range(n):
            # 그룹별로 BFS 실행
            if not flag_visited[yy][xx]:
                now_group_value = group_visited[yy][xx]  # 현재 그룹의 번호

                flag_visited[yy][xx] = 1

                queue = deque()
                queue.append((yy, xx))

                while queue:
                    y, x = queue.popleft()
                    for dy, dx in direction:
                        ny, nx = y + dy, x + dx
                        if oob(ny, nx):
                            continue
                        if group_visited[ny][nx] != now_group_value:  # 현재 그룹과 값이 다르다면
                            group_nears[now_group_value][group_visited[ny][nx]] += 1  # 현재 그룹에서 해당 그룹으로의 변 수 += 1
                            continue
                        if flag_visited[ny][nx]:  # BFS 재방문 방지
                            continue
                        flag_visited[ny][nx] = 1
                        queue.append((ny, nx))


n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

total_art_score = 0

for turn in range(4):
    if turn:  # 초기예술점수 계산 전에, 배열 회전하면 안됨
        new_area = [[0] * n for _ in range(n)]  # 배열회전된 값이 담길 배열
        new_area[n // 2][n // 2] = area[n // 2][n // 2]  # 정중앙

        # 십자가 부분 반시계방향 회전
        rotate_counterclockwise()

        # 나머지 4개의 사각형 부분 시계방향 회전
        rotate_clockwise(0, 0, n // 2, n // 2)
        rotate_clockwise(0, n // 2 + 1, n // 2, n)
        rotate_clockwise(n // 2 + 1, 0, n, n // 2)
        rotate_clockwise(n // 2 + 1, n // 2 + 1, n, n)
        area = new_area

    # 그룹의 (값, 칸 수) 계산
    group_visited = [[0] * n for _ in range(n)]
    group_infos = [None]  # 각 그룹의 (값, 칸 수)가 담길 배열
    group_flag = 0  # 그룹 index 번호
    for i in range(n):
        for j in range(n):
            if not group_visited[i][j]:
                group_flag += 1
                group_infos.append(cal_group_info(i, j))  # 그룹의 (값, 칸 수) 계산 & 추가

    # 그룹끼리 맞닿는 변 수 계산
    group_nears = [None] + [[0] * (group_flag + 1) for _ in range(group_flag)]  # 그룹끼리 맞닿는 변 수가 담길 2중 리스트
    cal_group_nears()

    # 예술점수 계산 & 반영
    now_art_score = 0
    for i in range(1, group_flag):
        for j in range(i + 1, group_flag + 1):
            # 맞닿는 변이 하나도 없다면 continue
            if not group_nears[i][j]:
                continue
            # (i그룹 칸 수 + j그룹 칸 수) * i그룹 값 * j그룹 값 * 맞닿는 변 수
            now_art_score += (group_infos[i][1] + group_infos[j][1]) * group_infos[i][0] * group_infos[j][0] * group_nears[i][j]
    total_art_score += now_art_score

print(total_art_score)
