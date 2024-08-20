# 20240819
# 16:00
# 1 / 1


direction = ((0, 1), (-1, 0), (0, -1), (1, 0))  # 동남서북 (시계방향)


def oob(yy, xx):
    return yy < 0 or m + 1 <= yy or xx < 0 or m + 1 <= xx


m, n = map(int, input().split())
y, x = 0, 0
direction_idx = 0
commands = [tuple(map(str, input().split())) for _ in range(n)]
for MorT, d in commands:
    if MorT == "MOVE":
        d = int(d)
        dy, dx = direction[direction_idx]
        y, x = y + d * dy, x + d * dx
        if oob(y, x):  # 유효하지 않은 명령어 열이라면 print(-1)하고 exit()
            print(-1)
            exit()
    else:  # if MorT == "TURN":
        # direction이 동남서북 순으로 구성돼 있기 때문에, (+1)%4하면 오른쪽 90도 회전, (-1)%4하면 왼쪽 90도 회전
        direction_idx += 1 if int(d) else -1
        direction_idx %= 4
print(x, y)
