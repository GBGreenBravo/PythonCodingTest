# 20240824
# 13:53
# 1 / 1

direction_2 = ((0, 1), (1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def check_candies(y, x, dy, dx):  # 현재 좌표으로부터, 현재 방향에 있는 연속하는, 같은 캔디의 최대값 return
    criteria = area[y][x]  # 기준이 될, 현재 캔디

    # 현재 방향으로 1칸 이동
    y += dy
    x += dx

    candies = 0

    while not oob(y, x) and area[y][x] == criteria:  # 영역 안이면서, 같은 캔디 가질 동안
        candies += 1
        y += dy
        x += dx

    return candies


def swap_and_cal_candies(sy, sx):  # 현재 좌표의 오른쪽/아래 좌표와 캔디 바꾸며 캔디 계산
    global mx_candies

    for dy, dx in direction_2:  # 오른쪽과 아래에 대해서만
        ny, nx = sy + dy, sx + dx  # 캔디 교환할 좌표
        if oob(ny, nx):  # 캔디 교환할 좌표가 영역 밖이면 continue
            continue
        area[sy][sx], area[ny][nx] = area[ny][nx], area[sy][sx]  # 캔디 스왑
        # 스왑한 두 좌표에 대해 상하/좌우의 캔디 연속 개수 계산하여, 최대값 걩신
        mx_candies = max(mx_candies, check_candies(sy, sx, 1, 0) + check_candies(sy, sx, -1, 0) + 1)
        mx_candies = max(mx_candies, check_candies(sy, sx, 0, 1) + check_candies(sy, sx, 0, -1) + 1)
        mx_candies = max(mx_candies, check_candies(ny, nx, 1, 0) + check_candies(ny, nx, -1, 0) + 1)
        mx_candies = max(mx_candies, check_candies(ny, nx, 0, 1) + check_candies(ny, nx, 0, -1) + 1)
        area[sy][sx], area[ny][nx] = area[ny][nx], area[sy][sx]  # 캔디 스왑 복구


n = int(input())
area = [list(str(input())) for _ in range(n)]

mx_candies = 1  # 연속 최대 캔디 수를 저장할 변수
for i in range(n):
    for j in range(n):
        swap_and_cal_candies(i, j)  # 모든 좌표에 대해 오른쪽/아래와 스왑하며 캔디 계산

print(mx_candies)
