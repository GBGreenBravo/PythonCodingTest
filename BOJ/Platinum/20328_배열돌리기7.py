# 20241206
# 1:23:46
# 1 / 1

N, R = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(2 ** N)]
commands = [tuple(map(int, input().split())) for _ in range(R)]

infos = [0] * (N + 1)
changes = ((3, 1, 4, 6),
           (2, 0, 7, 5),
           (1, 3, 6, 4),
           (0, 2, 5, 7),
           (7, 5, 2, 0),
           (6, 4, 1, 3),
           (5, 7, 0, 2),
           (4, 6, 3, 1))


for co_k, co_l in commands:
    if co_k <= 4:
        now = co_l
        while now:
            infos[now] = changes[infos[now]][co_k - 1]
            now -= 1
    else:
        now = N
        while now >= co_l + 1:
            infos[now] = changes[infos[now]][co_k - 5]
            now -= 1

for length in range(N, 0, -1):
    half = length - 1
    for i in range(0, 2**N, 2**length):
        for j in range(0, 2**N, 2**length):
            area1 = [[area[i + y][j + x] for x in range(2**half)] for y in range(2**half)]
            area2 = [[area[i + y][j + x + 2**half] for x in range(2**half)] for y in range(2**half)]
            area3 = [[area[i + y + 2**half][j + x] for x in range(2**half)] for y in range(2**half)]
            area4 = [[area[i + y + 2**half][j + x + 2**half] for x in range(2**half)] for y in range(2**half)]
            if infos[length] == 0:
                order = [area1, area2, area3, area4]
            elif infos[length] == 1:
                order = [area2, area1, area4, area3]
            elif infos[length] == 2:
                order = [area4, area3, area2, area1]
            elif infos[length] == 3:
                order = [area3, area4, area1, area2]
            elif infos[length] == 4:
                order = [area3, area1, area4, area2]
            elif infos[length] == 5:
                order = [area1, area3, area2, area4]
            elif infos[length] == 6:
                order = [area2, area4, area1, area3]
            elif infos[length] == 7:
                order = [area4, area2, area3, area1]

            for y in range(2**half):
                for x in range(2**half):
                    area[i + y][j + x] = order[0][y][x]
            for y in range(2**half):
                for x in range(2**half):
                    area[i + y][j + x + 2**half] = order[1][y][x]
            for y in range(2**half):
                for x in range(2**half):
                    area[i + y + 2**half][j + x] = order[2][y][x]
            for y in range(2**half):
                for x in range(2**half):
                    area[i + y + 2**half][j + x + 2**half] = order[3][y][x]
for row in area:
    print(*row)
