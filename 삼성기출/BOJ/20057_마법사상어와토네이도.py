# 20240906
# 39:00
# 1 / 1

"""
풀이 시간: 39분 (14:05 ~ 14:44)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:05 - 14:10)
    이전에 시뮬레이션_연습1에서 풀었던, 백준 1913_달팽이" 문제가 생각났습니다.
    그 문제에서 가운데부터 좌표를 탐색하셨던 분들의 코드가, 바깥부터 탐색 코드보다 길었던 것이 기억났습니다.

    이 문제도 토네이도의 시작은 가운데부터 하지만,
    바깥부터 토네이도 이동경로의 역의 순서로 저장해놓고 활용하면 되겠다고 생각했습니다.

    그리고 흩어지는 먼지의 경우,
    토네이도 이동방향을 왼쪽으로 고정해놓고,
    (0, 0)으로부터의 dy, dx와, 흩어지는 percentage를 저장해놨습니다.
    그리고 토네이도 이동방향에 따라 dy, dx를 (0, 0) 기준으로 회전시킬 것으로 구상했습니다.


2. 구현 (14:10 - 14:32)
    팀의 문제풀이 템플릿을 열심히 반영해보는 팀원들을 보며,
    빠르게 풀기보다 꼼꼼히 팀 템플릿을 따르면서, 같은 경험에서 공유할 점이 더 많아진다고 생각했기에,
    그리고 템플릿을 따르는 풀이가 더 정확하고 온전한 풀이로 이끌기에,
    그리고 체크포인트에서 print를 찍어보지 않으면 디버깅의 늪에 빠질 것이 확실해 보였기에,
    체크포인트에서 print를 성실히 수행했습니다.
    (체크포인트: 입력받은 2차원 배열 / 토네이도 이동좌표 역순으로 roads에 저장됐는지 / 반시계 회전 잘 되는지 / 먼지 흩날리는지 유무)

    (0, 0) 기준 반시계방향 좌표 회전은, 종이에 좌표를 표시해보며 구현했습니다.


3. 검증 (14:32 - 14:44)
    체크포인트에서 print 확인을 해줬음에도,
    모든 동작에서의 print를 따져본 것은 아니었기에 몇몇 실수가 있었습니다.
    (d_percent * total) // 100 를 (d_percent * 100) // total 로 적은 실수와, total이 0이 돼서 // 연산이 불가능한 실수는,
    금세 수정할 수 있었습니다.

    그러나, += 를 + 로 적었던 실수는 바로 확인되지 않았기에,
    먼지 흩날림에 따른 area 변화를 print 디버깅과 손코딩을 통해 확인하여, 발견&수정 했습니다.
"""

direction = ((0, -1), (1, 0), (0, 1), (-1, 0))  # 좌하우상 (반시계방향)

# 토네이도 이동방향이 왼쪽임을 가정하고, (0, 0)를 기준으로 (dy, dx, percentage)를 저장해놓음. ((-2, 0)은 별도로 코드에서 처리)
separated_dust = ((-1, 0, 1), (1, 0, 1), (-1, -1, 7), (1, -1, 7), (-1, -2, 10), (1, -2, 10), (-2, -1, 2), (2, -1, 2), (0, -3, 5))


# 입력으로 주어진 좌표를, 반시계방향 90도 회전((0, 0) 기준)을 d회 수행하여 반환하는 함수
def turn_counterclockwise(yy, xx, d):
    for _ in range(d):
        yy, xx = -xx, yy
    return yy, xx


def oob(yy, xx):
    return yy < 0 or n <= yy or xx < 0 or n <= xx


# (sy, sx) -> (ey, ex) 토네이도 이동에 대한, 먼지 흩날림 처리를 하는 함수
def move_tornado(sy, sx, ey, ex):
    global oob_dust

    total = area[ey][ex]  # 토네이도가 이동할 다음 좌표의 모래 양 (= 흩어질 모래 양)
    if not total:  # 흩어질 모래가 없다면 return
        return

    subtracted = 0  # 흩어지는 모래 양 총합 (문제 그림의 a에, total-subtracted를 저장하기 위함)

    now_d = direction.index((ey - sy, ex - sx))  # 현재 토네이도의 이동방향 index

    # 특정 퍼센트로 흩날리는 모래들에 대한 코드
    for dy, dx, d_percent in separated_dust:           # (0, 0)에서 왼쪽을 가정한 (dy, dx)와 d_percent(흩어질 모래 퍼센트)
        dy, dx = turn_counterclockwise(dy, dx, now_d)  # dy, dx를 현재 토네이도 이동방향에 맞게 조정
        ndy, ndx = sy + dy, sx + dx                    # 모래가 흩날릴 좌표

        subtracted += (d_percent * total) // 100    # 흩날리는 양 기록
        if oob(ndy, ndx):                           # 영역 밖으로 흩날리면, oob_dust에 +=
            oob_dust += (d_percent * total) // 100
        else:                                       # 영역 내로 흩날리면, 해당 좌표에 +=
            area[ndy][ndx] += (d_percent * total) // 100

    # 흩어지고 남는 모래 양(total-subtracted)을, 문제 그림의 a 좌표로
    dy, dx = turn_counterclockwise(0, -2, now_d)
    ndy, ndx = sy + dy, sx + dx  # 그냥 ey + direction[now_d][0], ex + direction[now_d][1]로 해도 됨.
    if oob(ndy, ndx):
        oob_dust += total - subtracted
    else:
        area[ndy][ndx] += total - subtracted

    # 토네이도가 다음으로 이동하는 곳의 먼지 양은 0으로
    area[ey][ex] = 0


n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]  # 먼지 양이 저장되는 배열

road_visited = [[0] * n for _ in range(n)]  # 토네이도 이동 좌표를 구하는 과정에서 쓰이는 방문체크 배열
road_visited[0][0] = 1                      # 토네이도 최종 도착지점 방문처리
roads = [(0, 0)]                            # 토네이도 이동좌표가 역순으로 저장되는 배열
ry, rx = 0, 0                               # 현재의 이동좌표
rd = 2                                      # 다음 좌표 탐색할 이동방향 index (시작은 오른쪽)
while not(ry == n // 2 and rx == n // 2):                    # 토네이도 시작지점에 도달할 때까지
    nry, nrx = ry + direction[rd][0], rx + direction[rd][1]  # 현재 이동방향으로 한칸
    if oob(nry, nrx) or road_visited[nry][nrx]:              # 만약 영역밖이거나 이미 방문한 좌표라면 => 이동방향 반시계방향 90도 회전
        rd -= 1
        rd %= 4
    ry, rx = ry + direction[rd][0], rx + direction[rd][1]    # 이동좌표 갱신
    road_visited[ry][rx] = 1                                 # 이동좌표 방문처리
    roads.append((ry, rx))                                   # 이동좌표 저장

oob_dust = 0  # 출력할, 격자 밖으로 나간 모래의 양

y, x = roads.pop()  # 항상 (n // 2, n // 2)가 됨.
while roads:              # 토네이도 좌표 (y, x)가 (0, 0)이 될 때까지
    ny, nx = roads.pop()  # 토네이도가 다음으로 이동할 좌표 (roads에는 역순으로 저장돼 있기에, pop())
    move_tornado(y, x, ny, nx)
    y, x = ny, nx         # 토네이도 좌표 갱신

print(oob_dust)
