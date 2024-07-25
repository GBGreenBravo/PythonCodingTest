# 20240725
# 25:25

n, m = map(int, input().split())
puzzle = [list(str(input())) for _ in range(n)]


def check(y, x):
    if puzzle[y][x] == "#":
        return False

    width_start, height_start = False, False

    if x + 2 < m and puzzle[y][x + 1] == '.' and puzzle[y][x + 2] == '.':
        width_start = True
    if y + 2 < n and puzzle[y + 1][x] == '.' and puzzle[y + 2][x] == '.':
        height_start = True

    if x != 0 and puzzle[y][x - 1] == '.':
        width_start = False
    if y != 0 and puzzle[y - 1][x] == '.':
        height_start = False

    if width_start or height_start:
        return [y + 1, x + 1]


result = []
for i in range(n):
    for j in range(m):
        now = check(i, j)
        if now:
            result.append(now)

print(len(result))
print(*[" ".join(str(j) for j in i) for i in result], sep="\n")
