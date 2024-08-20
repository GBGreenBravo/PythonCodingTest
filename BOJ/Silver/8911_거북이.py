# 20240820
# 20:00
# 1 / 1

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))  # (x, y) 기준으로 북동남서 순
l_dict = {0: 3, 1: 0, 2: 1, 3: 2}  # 왼쪽으로 회전할 때는 index -= 1 하고 %= 4
r_dict = {0: 1, 1: 2, 2: 3, 3: 0}  # 오른쪽으로 회전할 때는 index += 1 하고 %= 4

t = int(input())
for _ in range(t):
    commands = list(str(input()))

    x, y = 0, 0
    direction_idx = 0

    r_limit, l_limit, d_limit, u_limit = 0, 0, 0, 0  # 좌표평면상 xy의 최소/최대값 저장할 변수

    for command in commands:
        if command == "L":
            direction_idx = l_dict[direction_idx]  # 왼쪽으로 회전
        elif command == "R":
            direction_idx = r_dict[direction_idx]  # 오른쪽을 회전
        elif command == "F":
            dx, dy = direction[direction_idx]
            x, y = x + dx, y + dy  # 현재 방향에서 직진
            r_limit = max(r_limit, x)  # xy 최대/최소값 갱신
            l_limit = min(l_limit, x)
            d_limit = min(d_limit, y)
            u_limit = max(u_limit, y)
        elif command == "B":
            dx, dy = direction[direction_idx]
            x, y = x - dx, y - dy  # 현재 방향에서 후진
            r_limit = max(r_limit, x)
            l_limit = min(l_limit, x)
            d_limit = min(d_limit, y)
            u_limit = max(u_limit, y)

    print((r_limit - l_limit) * (u_limit - d_limit))  # 이동한 동선 모두 포함하는 직사각형 넓이 계산
