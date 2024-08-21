# 20240821
# 11:00
# 1 / 1

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or r <= y or x < 0 or c <= x


def check_changing(y, x):
    near_sea_cnt = 0  # 상하좌우의 바다 세는 변수

    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if oob(ny, nx):  # 영역 밖은 바다
            near_sea_cnt += 1
            continue
        if area[ny][nx] == 'X':  # 섬이라면 그냥 continue
            continue
        near_sea_cnt += 1  # 섬도 아니고 영역 밖도 아니라면 바다

    return '.' if near_sea_cnt >= 3 else 'X'  # 3/4에 대해서는 가라 앉으므로 '.', 3 미만에서는 여전히 섬이므로 'X'


r, c = map(int, input().split())
area = [list(str(input())) for _ in range(r)]
fifty = [['.' for _ in range(c)] for _ in range(r)]  # 50년 후의 상태를 저장할 배열

for i in range(r):
    for j in range(c):
        if area[i][j] == 'X':  # 현재가 섬이라면
            fifty[i][j] = check_changing(i, j)  # 체크해서 섬 유지 or 바다로 변환하여 저장

uu, dd, ll, rr = 0, r - 1, c - 1, 0  # 배열 압축을 위한 상하좌우 초기값 (50년 후에 섬 하나 무조건 있으므로, 극단적 값으로 초기화해도 됨)

for i in range(r):
    for j in range(c):
        if fifty[i][j] == 'X':  # 50년 후에 섬 좌표에 대해, 상하좌우 값 갱신
            uu = max(uu, i)
            dd = min(dd, i)
            ll = min(ll, j)
            rr = max(rr, j)

fifty = [[fifty[i][j] for j in range(ll, rr + 1)] for i in range(dd, uu + 1)]  # 상하좌우 limit으로 압축
for row in fifty:
    print(*row, sep="")
