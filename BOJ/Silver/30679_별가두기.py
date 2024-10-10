# 20241010
# 07:32
# 1 / 1

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


def check(start_row):
    y, x, d = start_row, 0, 0

    visited = [[[0] * m for _ in range(n)] for _ in range(4)]

    while not oob(y, x):
        if visited[d][y][x]:
            return True
        visited[d][y][x] = 1
        dy, dx = direction[d]
        y, x = y + dy * area[y][x], x + dx * area[y][x]
        d = (d + 1) % 4

    return False


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

answer_rows = []
for row in range(n):
    if check(row):
        answer_rows.append(row + 1)

print(len(answer_rows))
if answer_rows:
    print(*answer_rows)
