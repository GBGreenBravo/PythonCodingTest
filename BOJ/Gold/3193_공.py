# 20240925
# 41:06
# 1 / 1

# 4방향에 따른 행별, 벽 공간 미리 저장해 놓음
# 공 좌표만 중심좌표 기준으로 시계/반시계 회젼시키며, 중력처리 해줌
# 중력은 왼쪽으로 작용한다고 가정.


# area 배열을 시계방향 회전시키는 함수
def rotate_clockwise():
    global area
    area = [list(row)[::-1] for row in zip(*area)]


n, k = map(int, input().split())
area = [list(str(input())) for _ in range(n)]

# 공좌표 구하고, 공 있었던 곳 '.'으로 변경
by, bx = None, None
for i in range(n):
    for j in range(n):
        if area[i][j] == 'L':
            area[i][j] = '.'
            by, bx = i, j
            break
    else:
        continue
    break

# index 0/1/2/3 에 (입력배열 기준) 왼쪽/아래쪽/오른쪽/위쪽 중력작용 시, 걸리는 행별 벽의 열 좌표를 담아둠.
walls = []
for i in range(4):
    if i:
        rotate_clockwise()

    wall_indexes = []
    for y in range(n):
        row_wall_indexes = [-1]
        for x in range(n):
            if area[y][x] == 'X':
                row_wall_indexes.append(x)
        wall_indexes.append(row_wall_indexes)
    walls.append(wall_indexes)

# 이 코드 전체에서 N*N 사이즈는 안 변하므로, 항상 회전의 중심이 될 중심좌표 (cy, cx)
cy, cx = (n - 1) / 2, (n - 1) / 2

# (중력이 왼쪽으로 작용한다고 가정했기에) 공좌표 시계방향 회전으로 시작
dy, dx = by - cy, bx - cx
by, bx = int(cy + dx), int(cx - dy)

# 시작 시, 중력은 (입력배열 기준) 아래로 작용
gravity_idx = 1

# 시계방향으로 회전하는지 정보를 담은 배열
clockwise_arr = [str(input()) == 'D' for _ in range(k)]
for clockwise in clockwise_arr:
    # 배열 회전 위한, (dy, dx)
    dy, dx = by - cy, bx - cx

    # 시계방향 회전 시
    if clockwise:
        by, bx = int(cy + dx), int(cx - dy)  # 공 좌표 시계방향 회전
        gravity_idx = (gravity_idx + 1) % 4  # 중력방향도 시계방향 반영
    # 반시계방향 회전 시
    else:
        by, bx = int(cy - dx), int(cx + dy)  # 공 좌표 반시계방향 회전
        gravity_idx = (gravity_idx - 1) % 4  # 중력방향도 반시계방향 반영

    # 현재 중력으로 인해 떨어질 열 좌표 구하기
    # (왼쪽으로 중력이 작용하기에) 행 좌표는 그대로.
    next_bx = -1  # 무조건 갱신되는 최대값으로 선언
    for wall_x in walls[gravity_idx][by]:  # 현재 중력방향의 현재 행에 있는 벽 열 좌표들
        if wall_x > bx:  # 벽 열 좌표가 기존 열 좌표보다 크면, 계산할 필요 X
            break
        next_bx = max(next_bx, wall_x + 1)  # 벽보다 1칸 위의 좌표로 떨어질 열 좌표 갱신
    bx = next_bx  # 떨어진 열 좌표 갱신

# 중력작용 왼쪽 가정 때문에, 처음에 시계방향으로 회전시켰기 때문에
# 반시계방향 회전으로 올바른 공 좌표 복구
dy, dx = by - cy, bx - cx
by, bx = int(cy - dx), int(cx + dy)

# walls 구하는 과정에서 area 3회 시계방향 회전했으므로, 똑바로 돌려놓기
rotate_clockwise()
# k번 시계/반시계 회전 후, 현재 중력 방향에 맞게 회전
for _ in range((gravity_idx - 1) % 4):
    rotate_clockwise()

# 공 좌표 넣어서, 최종상태 출력
area[by][bx] = 'L'
for row in area:
    print(*row, sep="")
