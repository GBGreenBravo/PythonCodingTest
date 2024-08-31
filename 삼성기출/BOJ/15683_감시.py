# 20240829
#
# 1 / 1

"""
풀이 시간: 28분 (15:45 ~ 16:13)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:45 - 15:51)
    5번을 제외한 1~4번 CCTV에 대해서 회전을 시켜주면 될 것이라고 생각하며 문제를 읽었고,
    마지막에 명시된 CCTV의 개수는 8개 이하라는 제한에서, DFS로 풀면 되겠다는 확신을 가졋습니다.
    시간복잡도에서도 넉넉한 구상이었기에 바로 구현으로 옮겼습니다.


2. 구현 (15:51 - 16:10)
    5번 CCTV를 만나면 바로 4방향에 대해 감시 처리를 해줬습니다.
    0부터 6까지는 모두 활용되는 수였기에, 7로 감시되는 빈땅을 변경했습니다.

    처음에는 5번 CCTV를 만나고 4방향에 대한 함수가 fix돼있었으나,
    다른 CCTV에서 감시 처리를 할 때, 해당 함수를 분리할 수 있겠다고 생각했기에,
    4방향을 다룬 함수에서 1방향으로의 감시 처리 함수로 변경했습니다.


3. 검증 (16:10 - 16:13)
    5번 CCTV를 만났을 때 4방향으로의 즉시 감시 처리,
    DFS함수의 종료조건에 도달할 때의 상태 확인
    을 print()를 통해 생각대로 작동됨을 확인하고 제출했습니다.
"""

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 동남서북
cctv_directions = (None, (0, ), (0, 2), (0, 1), (0, 1, 2))  # 1/2/3/4 -> -/ㅡ/ㄴ/ㅗ


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


# 현재 좌표에서 현재 방향으로, 가능할 때까지 7로 변경하고 area 리턴하는 함수 (now_area 최대 8*8이기 때문에 메모리 이슈X)
def make_7_for_this_direction(sy, sx, dy, dx, now_area):
    ny, nx = sy + dy, sx + dx

    while not oob(ny, nx) and now_area[ny][nx] != 6:
        if now_area[ny][nx] == 0:
            now_area[ny][nx] = 7  # 7은 CCTV 시야에 해당된다는, 내가 정한 표시
        ny, nx = ny + dy, nx + dx

    return now_area


def cal_invisible_area():
    tmp_area = [row[:] for row in area]  # origin area 복사

    for cctv_idx in range(len_rotatable_cctvs):
        cy, cx = rotatable_cctvs[cctv_idx]  # 현재 CCTV
        for plus_d in cctv_directions[area[cy][cx]]:  # 현재 CCTV의 번호가 감시할 수 있는 방향 추가값
            dy, dx = direction[(cctv_arr[cctv_idx] + plus_d) % 4]  # 현재 감시 방향
            tmp_area = make_7_for_this_direction(cy, cx, dy, dx, tmp_area)  # 현재 감시 방향에 대해, 감시 처리

    global min_answer
    # 7번으로 감시 처리됐으므로, 0번(사각지대)을 모두 세주고, 최소값 갱신
    min_answer = min(min_answer, sum(map(lambda x: x.count(0), tmp_area)))


# cctv_arr에 기준 방향을 하나씩 넣으며, 다 채워지면 위 함수 호출하는 함수
def rotate_cctvs(cnt, start_index):
    if cnt == len_rotatable_cctvs:  # 모든 회전가능 좌표에, 기준 방향 다 할당 됐다면
        cal_invisible_area()
        return

    for cctv_idx in range(start_index, len_rotatable_cctvs):
        for i in range(4):
            cctv_arr.append(i)
            rotate_cctvs(cnt + 1, cctv_idx + 1)
            cctv_arr.pop()


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

rotatable_cctvs = []  # 회전가능한 1/2/3/4번 CCTV의 좌표를 저장할 배열
for i in range(n):
    for j in range(m):
        if area[i][j] == 5:  # 모든 4방향 감시 가능한 5번 CCTV면 (회전할 필요 없음)
            for dy, dx in direction:
                area = make_7_for_this_direction(i, j, dy, dx, area)  # origin area에 CCTV 시야 적용
        elif 0 < area[i][j] < 5:  # 1/2/3/4번 CCTV는 회전가능 CCTV좌표 배열에 저장
            rotatable_cctvs.append((i, j))

len_rotatable_cctvs = len(rotatable_cctvs)
cctv_arr = []
min_answer = n * m
rotate_cctvs(0, 0)  # DFS 호출

print(min_answer)
