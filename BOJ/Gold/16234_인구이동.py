# 20240828
# 23:00
# 1 / 1

"""
풀이 시간: 23분 (15:30 ~ 15:53)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:30 - 15:35)
    어떤 문제를 먼저 풀지 선정할 때 테스트케이스를 보고,
    선호하는 문제(문제 설명이 한 단계씩 그림으로 표시돼 있는 지문)가 아니었기에, '미세먼지안녕' 문제를 먼저 풀고 '인구이동'을 풀기로 결정했습니다.

    문제를 읽으며 생각보다 체계적인 절차로 단계가 명시돼 있어, 구현에 큰 어려움은 없어 보였습니다.
    그러나, 구상하는 풀이로 시간복잡도를 생각해봤으나, 이에 대한 확신이 없었습니다.
    구현함에 따라, 시간복잡도가 더 늘 수 있으므로,
    일단 정상적인 답변을 반환하도록 구현한 후, 재확인/리팩토링을 하기로 했습니다.


2. 구현 (15:35 - 15:45)
    국경선을 모두 여는 것과, 열린 국경선에 대한 이동 처리는
    독립적으로 수행되는 것이라고 생각했기에, 두 수행에 따른 함수를 요구사항대로 구현했습니다.


3. 검증 (15:45 - 15:53)
    국경선을 여는 함수를 작성한 후에는, print디버깅을 통해
    함수호출 1회에 따른 변화를 정상적으로 확인했습니다.

    열린 국경에 대해 이동하는 함수를 작성한 후에는, 모든 구현이 끝나는 단계였기에,
    테스트케이스를 돌리려 했습니다.
    그러나 + 연산은 int 끼리 가능하다는 에러가 떴고,
    opened_directions[y][x]를 인덱싱 없이 opened_directions와 같이 적었음을 확인하고 수정했습니다.

    그러나 인구이동 종료 체크가 정상적으로 되지 않아, 무한루프를 도는 것을 발견하고,
    설정해준 flag에 대한 변경이 이뤄지지 않았음을 깨닫고,
    인구이동이 한번도 실행되지 않은 경우에 종료하도록 구현했습니다.

    위 2번의 변경 후 돌린 테스트케이스는 정상적으로 작동했습니다.

    시간복잡도에 대한 계산을 다시 했고, 구현된 코드에서는 이상이 없음을 확인했습니다.

    그리고 코드를 다시 읽어보는 과정에서,
    열린 국경선이 없는 나라에 대해 불필요하게 4방향 탐색을 함을 깨닫고,
    조건 추가를 통해 해당 연산을 줄여줬습니다.
"""

from collections import deque

# 모든 좌표에 대해 열 수 있는 국경인지를 파악하기 때문에, 오른쪽과 아래만 해줘도 됨.
direction_2 = ((0, 1), (1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def open_borders():
    for x in range(n):
        for y in range(n):
            for dy, dx in direction_2:
                ny, nx = y + dy, x + dx
                if oob(ny, nx):
                    continue
                # 현재 좌표와 인접한 좌표 사이에, 국경을 열 수 있다면
                if l <= abs(area[y][x] - area[ny][nx]) <= r:
                    opened_directions[y][x].append((dy, dx))  # 현재좌표 -> 인접좌표
                    opened_directions[ny][nx].append((-dy, -dx))  # 인접좌표 -> 현재좌표

                    global all_borders_closed
                    all_borders_closed = False


def move_people():
    visited = [[0] * n for _ in range(n)]  # 연합 내 중복방문 방지를 위한 배열

    for sy in range(n):
        for sx in range(n):
            if not visited[sy][sx] and opened_directions[sy][sx]:  # 중복방문X and 국경 하나라도 열려있다면
                visited[sy][sx] = 1  # 시작 좌표 방문처리

                union_sum = area[sy][sx]  # 연합의 총 인구수
                union_indexes = [(sy, sx)]  # 연합의 좌표들

                queue = deque()
                queue.append((sy, sx))

                while queue:
                    y, x = queue.popleft()
                    for dy, dx in opened_directions[y][x]:
                        ny, nx = y + dy, x + dx
                        # 이동 가능한 좌표내 영역으로의 방향만 opened_directions로 저장했기에, oob() 불필요
                        if visited[ny][nx]:
                            continue
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
                        union_sum += area[ny][nx]  # 연합 총 인구수에 +=
                        union_indexes.append((ny, nx))  # 연합 좌표에 저장

                union_value = union_sum // len(union_indexes)  # 연합에 분배되는 인구수
                for uy, ux in union_indexes:
                    area[uy][ux] = union_value


n, l, r = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

days = 0
all_borders_closed = False
while not all_borders_closed:
    all_borders_closed = True

    # 현재 좌표에서, 열린 국경의 방향을 담는 배열
    opened_directions = [[list() for _ in range(n)] for _ in range(n)]
    open_borders()  # 열 수 있는 국경 모두 열기
    move_people()  # 열린 국경에 대한 인구이동

    # 모든 국경이 닫혔다면, 인구이동이 없다는 뜻이므로 종료
    # (한 국경이라도 열려 있으면 인구이동 무조건 수행됨; 그 차이로 인해 인구 분배가 발생하므로)
    if all_borders_closed:
        print(days)
        break

    days += 1
