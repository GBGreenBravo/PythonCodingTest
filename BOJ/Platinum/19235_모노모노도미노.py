# 20241023
# 55:46
# 1 / 1


def oob(y, x):
    return y < 0 or 6 <= y or x < 0 or 4 <= x


def fall_green(block_type, sy, sx):
    global total_score, green

    if block_type == 1:
        green[sy][sx] = flag
        falling = [[[sy, sx]]]
    elif block_type == 2:
        green[sy][sx] = flag
        green[sy][sx + 1] = flag
        falling = [[(sy, sx), (sy, sx + 1)]]
    elif block_type == 3:
        green[sy][sx] = flag
        green[sy + 1][sx] = flag
        falling = [[(sy, sx), (sy + 1, sx)]]

    # 떨어지는 그룹이 존재하는 동안 반복
    while falling:
        # 현재 떨어지는 그룹들, 떨어질 수 있는 만큼 떨어짐 처리
        for falling_group in falling:
            reached = False
            while not reached:
                for fy, fx in falling_group:
                    if fy == 5 or green[fy + 1][fx] not in (0, green[fy][fx]):
                        reached = True
                        break
                else:
                    value = green[falling_group[0][0]][falling_group[0][1]]
                    for fy, fx in falling_group:
                        green[fy][fx] = 0
                    next_falling_group = []
                    for fy, fx in falling_group:
                        green[fy + 1][fx] = value
                        next_falling_group.append((fy + 1, fx))
                    falling_group = next_falling_group

        # 행 다 차있는지 체크 & 반영
        removed_cnt = 0
        for row in range(5, 1, -1):
            if not green[row].count(0):
                del green[row]
                removed_cnt += 1
        total_score += removed_cnt
        green = [[0] * 4 for _ in range(removed_cnt)] + green

        # 새로 떨어질 수 있는 블럭 있는지 체크
        next_falling = []
        visited = [[0] * 4 for _ in range(6)]
        for r in range(5, -1, -1):
            for c in range(4):
                if not visited[r][c] and green[r][c]:
                    visited[r][c] = 1
                    now_group = [(r, c)]

                    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        nr, nc = r + dr, c + dc
                        if not oob(nr, nc) and green[nr][nc] == green[r][c]:
                            visited[nr][nc] = 1
                            now_group.append((nr, nc))
                            break

                    fallable = False
                    for gy, gx in now_group:
                        if gy == 5 or green[gy + 1][gx] not in (0, green[gy][gx]):
                            fallable = False
                            break
                        elif green[gy + 1][gx] == 0:
                            fallable = True
                    if fallable:
                        next_falling.append(now_group)
        falling = next_falling

    if sum(green[0]):
        green = [[0] * 4 for _ in range(2)] + green[:4]
    elif sum(green[1]):
        green = [[0] * 4] + green[:5]


def fall_blue(block_type, sy, sx):
    global total_score, blue

    if block_type == 1:
        blue[sy][sx] = flag
        falling = [[[sy, sx]]]
    elif block_type == 2:
        blue[sy][sx] = flag
        blue[sy + 1][sx] = flag
        falling = [[(sy, sx), (sy + 1, sx)]]
    elif block_type == 3:
        blue[sy][sx] = flag
        blue[sy][sx - 1] = flag
        falling = [[(sy, sx), (sy, sx - 1)]]

    while falling:
        for falling_group in falling:
            reached = False
            while not reached:
                for fy, fx in falling_group:
                    if fy == 5 or blue[fy + 1][fx] not in (0, blue[fy][fx]):
                        reached = True
                        break
                else:
                    value = blue[falling_group[0][0]][falling_group[0][1]]
                    for fy, fx in falling_group:
                        blue[fy][fx] = 0
                    next_falling_group = []
                    for fy, fx in falling_group:
                        blue[fy + 1][fx] = value
                        next_falling_group.append((fy + 1, fx))
                    falling_group = next_falling_group

        removed_cnt = 0
        for row in range(5, 1, -1):
            if not blue[row].count(0):
                del blue[row]
                removed_cnt += 1
        total_score += removed_cnt
        blue = [[0] * 4 for _ in range(removed_cnt)] + blue

        next_falling = []
        visited = [[0] * 4 for _ in range(6)]
        for r in range(5, -1, -1):
            for c in range(4):
                if not visited[r][c] and blue[r][c]:
                    visited[r][c] = 1
                    now_group = [(r, c)]

                    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        nr, nc = r + dr, c + dc
                        if not oob(nr, nc) and blue[nr][nc] == blue[r][c]:
                            visited[nr][nc] = 1
                            now_group.append((nr, nc))
                            break

                    fallable = False
                    for gy, gx in now_group:
                        if gy == 5 or blue[gy + 1][gx] not in (0, blue[gy][gx]):
                            fallable = False
                            break
                        elif blue[gy + 1][gx] == 0:
                            fallable = True
                    if fallable:
                        next_falling.append(now_group)
        falling = next_falling

    if sum(blue[0]):
        blue = [[0] * 4 for _ in range(2)] + blue[:4]
    elif sum(blue[1]):
        blue = [[0] * 4] + blue[:5]


green = [[0] * 4 for _ in range(6)]
blue = [[0] * 4 for _ in range(6)]
flag = 0

n = int(input())
blocks = [tuple(map(int, input().split())) for _ in range(n)]

total_score = 0

for b_type, i, j in blocks:
    flag += 1
    fall_green(b_type, 0, j)
    fall_blue(b_type, 0, 3 - i)  # blue도 green과 같은 사이즈로 배열 선언했기에, 떨어지는 초기 블럭 모양만 수정해주면 됨.

print(total_score)
print(48 - sum(map(lambda row: row.count(0), green)) - sum(map(lambda row: row.count(0), blue)))
