# 20241007
# 17:39
# 1 / 1


def check(sy, sx, length1, length2):
    global max_answer

    route = set()
    route.add(area[sy][sx])
    route.add(area[sy + length1 + length2][sx - length1 + length2])

    ly, lx = sy, sx
    for _ in range(length1):
        ly += 1
        lx -= 1
        route.add(area[ly][lx])
    for _ in range(length2 - 1):
        ly += 1
        lx += 1
        route.add(area[ly][lx])

    ry, rx = sy, sx
    for _ in range(length2):
        ry += 1
        rx += 1
        route.add(area[ry][rx])
    for _ in range(length1 - 1):
        ry += 1
        rx -= 1
        route.add(area[ry][rx])

    if len(route) == (length1 + length2) * 2:
        max_answer = max(max_answer, (length1 + length2) * 2)


t = int(input())
for test in range(1, t + 1):
    n = int(input())
    area = [list(map(int, input().split())) for _ in range(n)]

    max_answer = -1

    for i in range(0, n - 2):
        for j in range(1, n - 1):

            for l1 in range(1, j + 1):
                for l2 in range(1, min(n - 1 - (i + l1), n - 1 - j) + 1):
                    check(i, j, l1, l2)

    print(f"#{test} {max_answer}")
