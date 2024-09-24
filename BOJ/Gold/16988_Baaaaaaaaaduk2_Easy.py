# 20240924
# 21:23
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


# 두 좌표에 내 돌을 놓고, 최대값을 갱신하는 코드
def check(y1, x1, y2, x2):
    # 이 함수의 board에서 죽는 상대 돌 수 총합
    death_sum = 0

    # deepcopy해서, 입력의 두 좌표에 내 돌(1) 놓기
    board = [row[:] for row in area]
    board[y1][x1], board[y2][x2] = 1, 1

    # BFS 중복 방지 위한 방문배열
    visited = [[0] * m for _ in range(n)]

    for sy in range(n):
        for sx in range(m):
            # 상대 돌이고, 방문 안 했다면
            if board[sy][sx] == 2 and not visited[sy][sx]:
                death_cnt = 1   # 죽게 된다면, 죽는 돌 수
                all_die = True  # 현재 상대 돌 그룹 다 죽는다고 가정하고 시작

                visited[sy][sx] = 1

                queue = deque()
                queue.append((sy, sx))

                while queue:
                    y, x = queue.popleft()
                    for dy, dx in direction:
                        ny, nx = y + dy, x + dx
                        if oob(ny, nx) or visited[ny][nx]:
                            continue

                        if board[ny][nx] == 2:
                            visited[ny][nx] = 1
                            queue.append((ny, nx))
                            death_cnt += 1
                        elif board[ny][nx] == 0:  # 인접한 곳에 빈칸 있다면, 이 그룹은 안 죽음
                            all_die = False

                # 위의 BFS에서 탐색한 그룹이 다 죽는 그룹이라면
                if all_die:
                    death_sum += death_cnt  # 죽는 상대 돌 수 총합에 추가

    # 최대값 갱신
    global max_deaths
    max_deaths = max(max_deaths, death_sum)


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

max_deaths = 0

for i in range(n * m - 1):  # 첫 번째 돌 놓을 곳
    iy, ix = divmod(i, m)
    if area[iy][ix]:  # 이미 돌 놓여있다면 -> continue
        continue

    for j in range(i + 1, n * m):  # 두 번째 돌 놓을 곳
        jy, jx = divmod(j, m)
        if area[jy][jx]:  # 이미 돌 놓여있다면 -> continue
            continue

        # 돌 놓을 수 있는 두 좌표에 돌 놓고, 최대값 갱신 시도
        check(iy, ix, jy, jx)

print(max_deaths)
