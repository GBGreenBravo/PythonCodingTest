# 20241010
# 48:30
# 1 / 1

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))

t = int(input())
for test in range(1, t + 1):
    n, m, k = map(int, input().split())
    input_area = [list(map(int, input().split())) for _ in range(n)]

    area = dict()
    waiting = dict()
    for i in range(n):
        for j in range(m):
            if input_area[i][j]:
                area[(i, j)] = input_area[i][j]
                waiting[(i, j)] = input_area[i][j] + 1
    dying = dict()

    for _ in range(k):
        queue = []
        next_waiting = dict()
        for (i, j), time in waiting.items():
            if time == 1:
                queue.append((i, j))
                dying[(i, j)] = area[(i, j)]
            else:
                next_waiting[(i, j)] = time - 1
        waiting = next_waiting

        spreading = dict()
        for y, x in queue:
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if (ny, nx) in area:
                    continue
                spreading[(ny, nx)] = max(area[(y, x)], spreading.get((ny, nx), 0))
        for (y, x), life in spreading.items():
            area[(y, x)] = life
            waiting[(y, x)] = life + 1

        next_dying = dict()
        for (i, j), time in dying.items():
            if time == 1:
                pass
            else:
                next_dying[(i, j)] = time - 1
        dying = next_dying

    answer = 0
    for i, j in area.keys():
        if (i, j) in waiting.keys() or (i, j) in dying.keys():
            answer += 1
    print(f"#{test} {answer}")


# dictionay 사용 시, 위와 같이 튜플을 key로 쓰기보다,
# 아래 코드와 같이, 고유햔 int나 String으로 key를 설정하는 것이 효율적임.

"""
direction = ((0, 1), (0, -1), (1, 0), (-1, 0))

t = int(input())
for test in range(1, t + 1):
    n, m, k = map(int, input().split())
    input_area = [list(map(int, input().split())) for _ in range(n)]

    area = dict()
    waiting = dict()
    for i in range(n):
        for j in range(m):
            if input_area[i][j]:
                area[(i * 500 + j)] = input_area[i][j]
                waiting[(i * 500 + j)] = input_area[i][j] + 1
    dying = dict()

    for _ in range(k):
        queue = []
        next_waiting = dict()
        for dict_key, time in waiting.items():
            if time == 1:
                i, j = divmod(dict_key, 500)
                queue.append((i, j))
                dying[dict_key] = area[(i * 500 + j)]
            else:
                next_waiting[dict_key] = time - 1
        waiting = next_waiting

        spreading = dict()
        for y, x in queue:
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if ny * 500 + nx in area:
                    continue
                spreading[ny * 500 + nx] = max(area[(y * 500 + x)], spreading.get(ny * 500 + nx, 0))
        for dict_key, life in spreading.items():
            area[dict_key] = life
            waiting[dict_key] = life + 1

        next_dying = dict()
        for dict_key, time in dying.items():
            if time == 1:
                pass
            else:
                next_dying[dict_key] = time - 1
        dying = next_dying

    answer = 0
    for dict_key in area.keys():
        i, j = divmod(dict_key, 500)
        if i * 500 + j in waiting.keys() or i * 500 + j in dying.keys():
            answer += 1
    print(f"#{test} {answer}")
"""