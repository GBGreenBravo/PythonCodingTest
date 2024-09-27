# 20240909
# 29:00
# 1 / 1

"""
풀이 시간: 29분 (14:45 ~ 15:14)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:45 - 14:51)
    각 원판의 지름은 다르나, m개로 구성됨은 같기에,
    2차원 배열로 원판들의 상태를 나타내면 되겠다고 생각했습니다.

    그리고 회전을 구상할 때, 이제까지 deque의 rotate함수를 써본 적이 없었지만,
    주말 스터디에서 그 활용을 코드리뷰를 통해 익힐 수 있었기에 활용해야겠다고 생각했습니다.

    그리고 숫자가 같아서 사라지는 경우에, 해당 값을 0으로 표시하기로 했기에,
    0이 평균을 구하거나 평균보다 작아 +1 해주는 과정에서 배제되도록 신경써야 했습니다.


2. 구현 (14:51 - 15:12)
    함수로 분리된 독립적인 수행들을 배제하고,
    함수들이 호출되는 메인 코드를 먼저 작성해줬습니다.
    위 작업을 통해, 큰 흐름의 구상을 코드로 먼저 정리하고, 별도의 독립수행을 함수화하여 각 수행에서의 구현에만 집중할 수 있었습니다.

    이 문제에서 점검해준 체크포인트들은 아래와 같습니다.
    1) deque의 rotate() 시계방향/반시계방향
    2) 각 원판의 회전 수행
    3) 인접한 같은 수 삭제 수행


3. 검증 (15:12 - 15:14)
    위의 구현 과정에서의 체크포인트 중 1,2번은 이상 없었고,
    3번에서 삭제 처리가 아예 수행되지 않는 이슈가 있었지만,
    코드 한줄을 까먹고 추가 안했음을 바로 확인하고 추가했습니다.

    그리고 문제 메모를 확인하고, 해당 요구사항들을 모두 만족했는지 코드와 대조해보며 확인했습니다.
"""

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0),)


def oob_row(y):
    return y < 0 or n <= y


# 들어온 1차원 배열에 대해, rotate_k만큼 시계/반시계 방향으로 회전시켜 반환하는 함수
def rotate(array, is_counterclockwise, rotate_k):
    queue = deque(array)
    if is_counterclockwise:  # 반시계방향이라면 rotate_k를 음수로
        rotate_k *= -1
    queue.rotate(rotate_k)  # 시계/반시계 방향으로 rotate_k만큼 회전
    return list(queue)


# 현재 원판에서 인접한 값이 같다면 BFS로 모두 0으로 만들고, 이러한 수행이 한번이라도 이뤄졌는지 True/False를 반환하는 함수
def check_same_near():
    same_near = False  # 반환할 Boolean Flag

    visited = [[0] * m for _ in range(n)]  # BFS 탐색을 위한 방문배열

    for r in range(n):
        for c in range(m):
            if not visited[r][c] and area[r][c]:  # 방문되지 않았고, 0이 아닌 숫자라면
                same_indexes = [(r, c)]  # 같은 값을 갖는 BFS인접 좌표를 넣을 배열

                queue = deque()
                queue.append((r, c))

                visited[r][c] = 1

                while queue:
                    y, x = queue.popleft()
                    for dy, dx in direction:
                        ny, nx = y + dy, (x + dx) % m  # nx는 같은 원판의 좌표를 의미하므로, oob가 없음
                        if oob_row(ny) or visited[ny][nx]:  # ny가 oob거나 이미 방문했다면 continue
                            continue
                        if area[y][x] == area[ny][nx]:  # 인접좌표가 같은 값이라면
                            queue.append((ny, nx))
                            visited[ny][nx] = 1
                            same_indexes.append((ny, nx))

                if len(same_indexes) > 1:  # 같은 값을 가진 인접좌표가 있다면
                    same_near = True  # Flag는 True로
                    for sy, sx in same_indexes:  # 같은 값 가진 인접 좌표들 모두 지우기 처리(0으로 변경)
                        area[sy][sx] = 0

    return same_near  # 인접한 같은 값 지우기 1번이라도 수행됐다면 True / 1번도 없었다면 False


# 평균보다 작은 값은 +1 / 평균보다 큰 값은 -1
def revise_numbers(average_num):
    for r in range(n):
        for c in range(m):
            if area[r][c]:
                area[r][c] += 1 if average_num > area[r][c] else (-1 if average_num < area[r][c] else 0)


n, m, t = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
for _ in range(t):
    mul, d, k = map(int, input().split())
    for row in range(mul - 1, n, mul):  # mul의 배수에 대해
        area[row] = rotate(area[row], d, k)  # 해당 원판 회전

    if not check_same_near():  # 같은 인접수 하나도 없다면,
        tmp_sum, tmp_cnt = 0, 0
        for i in range(n):
            for j in range(m):
                if area[i][j]:  # 0은 숫자 취급 X
                    tmp_cnt += 1
                    tmp_sum += area[i][j]
        if not tmp_cnt:  # 원판에 수가 하나도 없다면, break
            break
        average = tmp_sum / tmp_cnt  # 평균 구하고
        revise_numbers(average)  # 해당 평균으로, +1/-1 수행

print(sum(map(sum, area)))  # 원판에 적힌 수 총합 반환


# area에 list말고 deque로 넣어놔도 인덱싱 가능함
"""
from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0),)


def oob_row(y):
    return y < 0 or n <= y


# 들어온 1차원 배열에 대해, rotate_k만큼 시계/반시계 방향으로 회전시켜 반환하는 함수
def rotate(array, is_counterclockwise, rotate_k):
    if is_counterclockwise:  # 반시계방향이라면 rotate_k를 음수로
        rotate_k *= -1
    array.rotate(rotate_k)  # 시계/반시계 방향으로 rotate_k만큼 회전


# 현재 원판에서 인접한 값이 같다면 BFS로 모두 0으로 만들고, 이러한 수행이 한번이라도 이뤄졌는지 True/False를 반환하는 함수
def check_same_near():
    same_near = False  # 반환할 Boolean Flag

    visited = [[0] * m for _ in range(n)]  # BFS 탐색을 위한 방문배열

    for r in range(n):
        for c in range(m):
            if not visited[r][c] and area[r][c]:  # 방문되지 않았고, 0이 아닌 숫자라면
                same_indexes = [(r, c)]  # 같은 값을 갖는 BFS인접 좌표를 넣을 배열

                queue = deque()
                queue.append((r, c))

                visited[r][c] = 1

                while queue:
                    y, x = queue.popleft()
                    for dy, dx in direction:
                        ny, nx = y + dy, (x + dx) % m  # nx는 같은 원판의 좌표를 의미하므로, oob가 없음
                        if oob_row(ny) or visited[ny][nx]:  # ny가 oob거나 이미 방문했다면 continue
                            continue
                        if area[y][x] == area[ny][nx]:  # 인접좌표가 같은 값이라면
                            queue.append((ny, nx))
                            visited[ny][nx] = 1
                            same_indexes.append((ny, nx))

                if len(same_indexes) > 1:  # 같은 값을 가진 인접좌표가 있다면
                    same_near = True  # Flag는 True로
                    for sy, sx in same_indexes:  # 같은 값 가진 인접 좌표들 모두 지우기 처리(0으로 변경)
                        area[sy][sx] = 0

    return same_near  # 인접한 같은 값 지우기 1번이라도 수행됐다면 True / 1번도 없었다면 False


# 평균보다 작은 값은 +1 / 평균보다 큰 값은 -1
def revise_numbers(average_num):
    for r in range(n):
        for c in range(m):
            if area[r][c]:
                area[r][c] += 1 if average_num > area[r][c] else (-1 if average_num < area[r][c] else 0)


n, m, t = map(int, input().split())
area = [deque(map(int, input().split())) for _ in range(n)]
for _ in range(t):
    mul, d, k = map(int, input().split())
    for row in range(mul - 1, n, mul):  # mul의 배수에 대해
        rotate(area[row], d, k)  # 해당 원판 회전

    if not check_same_near():  # 같은 인접수 하나도 없다면,
        tmp_sum, tmp_cnt = 0, 0
        for i in range(n):
            for j in range(m):
                if area[i][j]:  # 0은 숫자 취급 X
                    tmp_cnt += 1
                    tmp_sum += area[i][j]
        if not tmp_cnt:  # 원판에 수가 하나도 없다면, break
            break
        average = tmp_sum / tmp_cnt  # 평균 구하고
        revise_numbers(average)  # 해당 평균으로, +1/-1 수행

print(sum(map(sum, area)))  # 원판에 적힌 수 총합 반환
"""