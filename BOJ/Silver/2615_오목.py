# 20240725
# 27:18

board = [list(map(int, input().split())) for _ in range(19)]


def check(y, x):
    criteria = board[y][x]
    if criteria == 0:  # 현재 위치에 돌 없다면 return False
        return False
    for dy, dx in ((1, 0), (1, 1), (0, 1), (-1, 1)):  # (하, 우하, 우, 우상) 방향에 대해
        by, bx = y + (-1 * dy), x + (-1 * dx)
        if 0 <= by < 19 and 0 <= bx < 19 and board[by][bx] == criteria:  # 현재방향 이전의 값과 같으면 continue
            continue
        for i in range(1, 5):
            ny, nx = y + dy * i, x + dx * i
            if ny < 0 or 19 <= ny or nx < 0 or 19 <= nx or board[ny][nx] != criteria:  # 다음 4개의 돌 이어지지 않으면 break
                break
        else:
            ny, nx = y + dy * 5, x + dx * 5
            if 0 <= ny < 19 and 0 <= nx < 19 and board[ny][nx] == criteria:  # 6개 이상 이어져 있다면 continue
                continue
            return criteria  # 오목 완성이라면 해당 돌 반환
    return False  # 오목 안되어 있으면 return False


for i in range(19):
    for j in range(19):
        result = check(i, j)
        if result:  # 오목 완성이면 print() & break
            print(result)
            print(i + 1, j + 1)
            break
    else:
        continue
    break

else:  # 완성된 오목 없으면(= 위 반복문 break 없이 다 돌면) print(0)
    print(0)
