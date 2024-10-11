# 20241011
# 1:42:22
# 1 / 1

"""
풀이 시간: 1시간 42분 (13:30 - 15:12)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (13:30 - 13:44)
    이전 풀이에서는 N*N 배열의 santas_map을 두지 않고 구현했기에,
    시간복잡도를 계산하기 어려웠다는 단점이 있었습니다.
    따라서, 이번에는 santas_map을 두고, 구현했습니다.
    (정보를 중복적으로 관리해주는 코드를 짜야 하지만, for문을 돌지 않아도 해당 위치에 산타 있는지 유무를 판단할 수 있어,
    이 문제에 대해서는 코드가 더 간결해졌고 디버깅/검증도 용이했습니다.)


2. 구현 (13:44 - 14:16)


3. 디버깅 (14:16 - 14:31)
    산타가 이동해서 충돌했을 때, 이동 반대방향을 해줘야 할 것을,
    루돌프 이동 시 위와 같이 구현한 실수가 있었습니다.

    위 실수는 빠르게 디버깅할 수 있었고, 아래 실수는 디버그모드를 활용한 디버깅 체계로 찾아내고 수정했습니다.
    산타가 움직여서 충돌하기 전에, 산타 움직임 처리를 해주지 않은 것.


4. 검증 (14:31 - 15:12)
    디버깅 완료 후, 검증에서 찾은 실수는 없었습니다.
    루돌프/산타의 우선순위에 따른 이동, 충돌, 연쇄 상호작용 등이 잘 되는지,
    단위테스트를 할 수 있는 테케들을 만들어서 검증했습니다.

    O (1) 주어진 테스트케이스로 검증
    O (2) 메모 vs. 코드
    O (3) (머릿속 환기 후) 문제 재정독
    O (4) 커스텀 테스트케이스 검증
    O (5) 철저한 코드 검증
    O (6) 오답노트 활용
    X (7) 다양한 구상에 따른, 다른 구현
"""

direction_8 = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
direction_4 = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 상우하좌


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def cal_distance_with_rudolph(y, x):
    return (ry - y)**2 + (rx - x)**2


def cal_distance(y1, x1, y2, x2):
    return (y1 - y2)**2 + (x1 - x2)**2


def interact(moving_s_idx, origin_s_idx, dy, dx):
    y, x = santas_info[origin_s_idx]

    santas_map[y][x] = moving_s_idx
    santas_info[moving_s_idx] = (y, x)

    ny, nx = y + dy, x + dx
    if oob(ny, nx):
        santas_info[origin_s_idx] = None
    elif not santas_map[ny][nx]:
        santas_map[ny][nx] = origin_s_idx
        santas_info[origin_s_idx] = (ny, nx)
    elif santas_map[ny][nx]:
        interact(origin_s_idx, santas_map[ny][nx], dy, dx)


def crush(s_idx, distance, dy, dx):
    santas_score[s_idx] += distance
    stunned[s_idx] = 2

    y, x = santas_info[s_idx]
    santas_map[y][x] = 0

    ny, nx = y + dy * distance, x + dx * distance
    if oob(ny, nx):
        santas_info[s_idx] = None
    elif not santas_map[ny][nx]:
        santas_map[ny][nx] = s_idx
        santas_info[s_idx] = (ny, nx)
    elif santas_map[ny][nx]:
        interact(s_idx, santas_map[ny][nx], dy, dx)


def move_rudolph():
    global ry, rx

    candidates = []
    for s_idx in range(1, p + 1):
        if not santas_info[s_idx]:
            continue
        sy, sx = santas_info[s_idx]
        candidates.append((cal_distance_with_rudolph(sy, sx), -sy, -sx, sy, sx))

    target_y, target_x = min(candidates)[-2:]

    candidates = []
    for dy, dx in direction_8:
        ny, nx = ry + dy, rx + dx
        if oob(ny, nx):
            continue
        candidates.append((cal_distance(ny, nx, target_y, target_x), dy, dx))

    dry, drx = min(candidates)[-2:]
    ry, rx = ry + dry, rx + drx

    if santas_map[ry][rx]:
        crush(santas_map[ry][rx], c, dry, drx)


def move_santa(s_idx):
    candidates = []

    y, x = santas_info[s_idx]
    origin_distance = cal_distance_with_rudolph(y, x)

    for d_idx, (dy, dx) in enumerate(direction_4):
        ny, nx = y + dy, x + dx
        if oob(ny, nx) or santas_map[ny][nx] or cal_distance_with_rudolph(ny, nx) >= origin_distance:
            continue
        candidates.append((cal_distance_with_rudolph(ny, nx), d_idx, dy, dx))

    if not candidates:
        return

    dsy, dsx = min(candidates)[-2:]
    nsy, nsx = y + dsy, x + dsx

    santas_map[y][x] = 0
    santas_map[nsy][nsx] = s_idx
    santas_info[s_idx] = (nsy, nsx)

    if nsy == ry and nsx == rx:
        crush(s_idx, d, -dsy, -dsx)


n, m, p, c, d = map(int, input().split())
ry, rx = map(lambda inp: int(inp) - 1, input().split())
santas_map = [[0] * n for _ in range(n)]
santas_info = [None] * (p + 1)
santas_score = [None] + [0] * p
for _ in range(p):
    pp, aa, bb = map(int, input().split())
    santas_map[aa - 1][bb - 1] = pp
    santas_info[pp] = (aa - 1, bb - 1)
stunned = [0] * (p + 1)

for _ in range(m):
    move_rudolph()

    for i in range(1, p + 1):
        if santas_info[i] and not stunned[i]:
            move_santa(i)

    alive_santa_cnt = 0
    for i in range(1, p + 1):
        if not santas_info[i]:
            continue
        alive_santa_cnt += 1
        santas_score[i] += 1
    if not alive_santa_cnt:
        break

    for i in range(1, p + 1):
        if stunned[i]:
            stunned[i] -= 1

print(*santas_score[1:], sep=" ")
