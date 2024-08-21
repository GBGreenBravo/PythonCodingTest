# 20240821
# 14:00
# 1 / 1

direction = ((0, 1), (-1, 0), (1, 0), (0, -1))  # 0123 -> 우상하좌 (입력에서 상하좌우가 1234이므로, %4하면 우상하좌 순서가 됨)


def oob(yy, xx):
    return yy < 0 or r <= yy or xx < 0 or c <= xx


r, c = map(int, input().split())
area = [[0] * c for _ in range(r)]  # 0: 안 간 곳 / 1: 간 곳 / 2: 장애물  ->  간곳과 장애물은 같은 취급이기에, not area[][]로 갈 수 있는 곳 체크 가능

k = int(input())
for _ in range(k):
    ky, kx = map(int, input().split())
    area[ky][kx] = 2  # 장애물은 2로 표시

by, bx = map(int, input().split())
area[by][bx] = 1  # 시작(방문한 곳)은 1로 표시
y, x = by, bx  # 현재 로봇의 좌표

direction_order = [i % 4 for i in list(map(int, input().split()))]  # 상하좌우(1234) 입력을 우상하좌(0123)로 바꾸고, 그 순서를 저장.
order_idx = 0  # direction.index(현재 바라보는 방향)이 될 index 저장

while True:
    for i in range(4):  # 방향 4개에 대해
        next_order_idx = (order_idx + i) % 4  # 다음 방향의 index
        dy, dx = direction[direction_order[next_order_idx]]  # 방향 index로 dy, dx 가져오기
        ny, nx = y + dy, x + dx
        if oob(ny, nx) or area[ny][nx]:  # 다음 방향이 영역 밖이거나 or 1(방문한 곳)이나 2(장애물)라면, continue
            continue
        y, x = ny, nx
        area[y][x] = 1  # 방문 처리
        order_idx = next_order_idx  # 다음 방향이될 index 저장
        break

    if y == by and x == bx:  # 반복문 이전의 좌표와 계산된 다음 좌표가 같다면, 이동 못 했다는 뜻이므로, break  => by,bx 말고 for-else로 해도 됨.
        break
    else:
        by, bx = y, x  # 다음 반복문에서의 비교를 위해 현재의 좌표를 별도로 저장.

print(y, x)  # 로봇의 마지막 좌표를 출력
