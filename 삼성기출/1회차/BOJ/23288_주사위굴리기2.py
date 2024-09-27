# 20240910
# 27:00
# 1 / 1

"""
풀이 시간: 27분 (14:04 ~ 14:31)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:04 - 14:11)
    이전에 고전했던 '14499_주사위굴리기'문제와 비슷한 유형이라고 생각했습니다.
    해당 문제에서,
    보편적인 규칙을 찾으려고 고전했던 경험 &
    코드리뷰를 하며 매번 위/아래/상/하/좌/우 에 대한 값을 갱신해주면 쉽게 풀게 됨을 확인
    했었기에, 이번 문제에서는 해당 풀이를 잘 활용할 수 있겠다는 확신이 있었습니다.


2. 구현 (14:11 - 14:28)
    함수화 가능한 (즉, 독립적으로 수행되는) 부분들은 함수화하기로 하고,  => roll_dice(), cal_score()
    함수를 제외한 메인 코드를 먼저 구현했습니다.

    주사위의 6면(아래/위/동/서/남/북) 012345 index로 관리했습니다.
    따라서, roll_dice 함수에서 4방향에 대한 굴리기 처리를 할 때,
    해당 구현에서 오류가 나지 않도록, 각 변수가 1번씩 활용됐는지 등 여러번 점검해줬습니다.
    이 점검에서 오랜 시간이 소모됐지만, 그럴 만한 검증이었다고 생각합니다.

    cal_score()함수를 작성하고 최종적으로 점수를 반환하는 과정에서
    B와 C를 곱한 값을 반환해야 하는데, C만을 반환하는 실수가 있었지만,
    바로 탐지하고 수정해줬습니다.


3. 검증 (14:28 - 14:31)
    구현 전에, 구상의 시간복잡도를 계산해줬지만,
    혹시 모를 오류를 탐지하기 위해, 최대범위의 테스트케이스를 직접 만들어 시간 내에 답변을 출력하는지 확인해줬습니다.

    그리고 늘 하던, 메모/구현 비교검증 & 테스트케이스 검증을 했고, 제출했습니다.
"""

from collections import deque

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 동 남 서 북


def oob(yy, xx):
    return yy < 0 or n <= yy or xx < 0 or m <= xx


def roll_dice(now_dice, dice_direction_idx):
    down, up, east, west, south, north = now_dice
    if dice_direction_idx == 0:
        return east, west, up, down, south, north
    elif dice_direction_idx == 1:
        return south, north, east, west, up, down
    elif dice_direction_idx == 2:
        return west, east, down, up, south, north
    else:
        return north, south, east, west, down, up


def cal_score(sy, sx):
    criteria = area[sy][sx]

    visited = [[0] * m for _ in range(n)]
    visited[sy][sx] = 1

    queue = deque()
    queue.append((sy, sx))

    while queue:
        y, x = queue.popleft()
        for ddy, ddx in direction:
            nny, nnx = y + ddy, x + ddx
            if oob(nny, nnx) or visited[nny][nnx] or area[nny][nnx] != criteria:
                continue
            visited[nny][nnx] = 1
            queue.append((nny, nnx))

    return criteria * sum(map(sum, visited))


n, m, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

dice_y, dice_x = 0, 0
dice_d = 0
dice = (6, 1, 3, 4, 5, 2)  # 아래/위/동/서/남/북

total_score = 0

for _ in range(k):
    dy, dx = direction[dice_d]
    ny, nx = dice_y + dy, dice_x + dx
    if oob(ny, nx):
        ny, nx = dice_y - dy, dice_x - dx
        dice_d = (dice_d + 2) % 4

    dice_y, dice_x = ny, nx
    dice = roll_dice(dice, dice_d)

    B = area[dice_y][dice_x]
    total_score += cal_score(dice_y, dice_x)
    A = dice[0]
    if A > B:
        dice_d += 1
        dice_d %= 4
    elif A < B:
        dice_d -= 1
        dice_d %= 4

print(total_score)
