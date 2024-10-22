# 20241022
# 39:36
# 1 / 1

# 도형이 내려가는 도중에, 회전은 하지 않지만 좌우이동은 할 수 있기에
# (0, 0)에 가상의 도형 직사각형 좌상단을 놓고, BFS로 내려가기 처리. -> 이렇게 하면 위 조건의 모든 도착지점 탐색 가능.

# 한 행이 다 차서 사라진 후에, 위 블럭들이 개별로 떨어지면 더 어려웠겠지만,
# 행 모양을 유지하며 내려왔기에 구상에 어려움은 없었음.

from collections import deque

direction = ((0, 1), (0, -1), (1, 0))


def oob(y, x):
    return y < 0 or 20 <= y or x < 0 or 10 <= x


shapes = (((0, 0), (0, 1), (0, 2), (0, 3)),
          ((0, 0), (1, 0), (2, 0), (3, 0)),

          ((0, 0), (0, 1), (1, 0), (1, 1)),

          ((0, 0), (0, 1), (1, 0), (2, 0)),
          ((0, 0), (0, 1), (0, 2), (1, 2)),
          ((0, 1), (1, 1), (2, 0), (2, 1)),
          ((0, 0), (0, 1), (1, 1), (1, 2)),

          ((0, 0), (0, 1), (1, 1), (2, 1)),
          ((0, 2), (1, 0), (1, 1), (1, 2)),
          ((0, 0), (1, 0), (2, 0), (2, 1)),
          ((0, 0), (0, 1), (0, 2), (1, 0)),

          ((0, 0), (1, 0), (1, 1), (2, 0)),
          ((0, 0), (0, 1), (0, 2), (1, 1)),
          ((0, 1), (1, 0), (1, 1), (2, 1)),
          ((0, 1), (1, 0), (1, 1), (1, 2)),

          ((0, 0), (1, 0), (1, 1), (2, 1)),
          ((0, 1), (0, 2), (1, 1), (1, 0)),

          ((0, 1), (1, 0), (1, 1), (2, 0)),
          ((0, 0), (0, 1), (1, 1), (1, 2)))


def check_reached(y, x, shape_arr):
    for sy, sx in shape_arr:
        nsy, nsx = y + sy, x + sx
        if nsy + 1 == 20:
            return True
        elif area[nsy + 1][nsx]:
            return True

    return False


def simulate(y, x, shape_arr):
    global max_answer

    now_answer = 0
    copied_area = [row[:] for row in area]
    for sy, sx in shape_arr:
        copied_area[y + sy][x + sx] = 1

    row_idx = 19
    while row_idx >= 0:
        row_sum = sum(copied_area[row_idx])
        if row_sum == 10:
            del copied_area[row_idx]
            copied_area.insert(0, [0] * 10)
            now_answer += 1
        elif row_sum == 0:
            row_idx -= 1
        else:
            if row_idx == 19:
                row_idx -= 1
                continue

            fallable = True
            for col_idx in range(10):
                if copied_area[row_idx][col_idx] and copied_area[row_idx + 1][col_idx]:
                    fallable = False
                    break
            if fallable:
                for col_idx in range(10):
                    if copied_area[row_idx][col_idx]:
                        copied_area[row_idx][col_idx] = 0
                        copied_area[row_idx + 1][col_idx] = 1
                row_idx += 1
            else:
                row_idx -= 1

    max_answer = max(max_answer, now_answer)


def bfs(shape_arr):
    visited = [[0] * 10 for _ in range(20)]
    visited[0][0] = 1

    queue = deque()
    queue.append((0, 0))

    reached_points = []

    while queue:
        y, x = queue.popleft()

        if check_reached(y, x, shape_arr):
            reached_points.append((y, x))

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if not oob(ny, nx) and visited[ny][nx]:
                continue
            for sy, sx in shape_arr:
                nsy, nsx = ny + sy, nx + sx
                if oob(nsy, nsx) or area[nsy][nsx]:
                    break
            else:
                visited[ny][nx] = 1
                queue.append((ny, nx))

    for ry, rx in reached_points:
        simulate(ry, rx, shape_arr)


area = [[int(inp) for inp in str(input())] for _ in range(20)]

max_answer = 0
for shape in shapes:
    bfs(shape)
print(max_answer)
