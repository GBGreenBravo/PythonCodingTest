# 20241002
# 18:49
# 1 / 1

# 17837_새로운게임2

"""
풀이 시간: 19분 (13:55 - 14:14)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (13:55 - 14:02)


2. 구현 (14:02 - 14:13)
    다소 중복되는 코드들은 있지만, 정확하게 구현했다는 점에 긍정적입니다.


3. 디버깅 (14:13 - 14:14)
"""

direction = (None, (0, 1), (0, -1), (-1, 0), (1, 0))
opposite = [None, 2, 1, 4, 3]


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def move_and_check_four():
    for p_idx in range(k):
        y, x, d = pieces[p_idx]

        dy, dx = direction[d]
        ny, nx = y + dy, x + dx

        if oob(ny, nx) or area[ny][nx] == 2:
            pieces[p_idx][-1] = opposite[d]

            dy, dx = direction[opposite[d]]
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or area[ny][nx] == 2:
                continue
            elif area[ny][nx] == 0:
                p_idx_idx = pieces_map[y][x].index(p_idx)
                moving = pieces_map[y][x][p_idx_idx:]
                pieces_map[y][x] = pieces_map[y][x][:p_idx_idx]
                pieces_map[ny][nx].extend(moving)
                for m_idx in moving:
                    pieces[m_idx][0], pieces[m_idx][1] = ny, nx
                if len(pieces_map[ny][nx]) >= 4:
                    return True
            elif area[ny][nx] == 1:
                p_idx_idx = pieces_map[y][x].index(p_idx)
                moving = pieces_map[y][x][p_idx_idx:][::-1]
                pieces_map[y][x] = pieces_map[y][x][:p_idx_idx]
                pieces_map[ny][nx].extend(moving)
                for m_idx in moving:
                    pieces[m_idx][0], pieces[m_idx][1] = ny, nx
                if len(pieces_map[ny][nx]) >= 4:
                    return True
            else:
                print("NOT HERE!")
        elif area[ny][nx] == 0:
            p_idx_idx = pieces_map[y][x].index(p_idx)
            moving = pieces_map[y][x][p_idx_idx:]
            pieces_map[y][x] = pieces_map[y][x][:p_idx_idx]
            pieces_map[ny][nx].extend(moving)
            for m_idx in moving:
                pieces[m_idx][0], pieces[m_idx][1] = ny, nx
            if len(pieces_map[ny][nx]) >= 4:
                return True
        elif area[ny][nx] == 1:
            p_idx_idx = pieces_map[y][x].index(p_idx)
            moving = pieces_map[y][x][p_idx_idx:][::-1]
            pieces_map[y][x] = pieces_map[y][x][:p_idx_idx]
            pieces_map[ny][nx].extend(moving)
            for m_idx in moving:
                pieces[m_idx][0], pieces[m_idx][1] = ny, nx
            if len(pieces_map[ny][nx]) >= 4:
                return True
        else:
            print("NOT HERE!")


n, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

pieces = []
pieces_map = [[[] for _ in range(n)] for _ in range(n)]
for idx in range(k):
    aa, bb, cc = map(int, input().split())
    pieces.append([aa - 1, bb - 1, cc])
    pieces_map[aa - 1][bb - 1].append(idx)

turn = 0
while turn != 1001:
    turn += 1
    if move_and_check_four():
        print(turn)
        break
else:
    print(-1)
