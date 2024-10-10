# 20241010
# 1:13:16
# 1 / 1

"""
풀이 시간: 1시간 13분 (15:08 - 16:21)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:08 - 15:18)
    이전 풀이 때는, 출구 좌표를 변수로 관리하여 좌표기준 회전으로 다뤘습니다.
    이번 풀이에서는 다른 풀이를 해보고자 했습니다.
    미로의 정보 배열(area)에 -1로 출구를 표시하여,
    미로를 회전시킬 때, 같이 회전시키는 것으로 구상했습니다.

    이전 코드와 비교해보니, 이전에는 1차원 배열에 좌표를 담았던 것과 달리,
    이번에는 참가자를 2차원 배열에 같은 칸에 있는 참가자는 같이 다뤘습니다.
    따라서, 이전에 활용했던 좌표기준 회전을 활용하지 않고, zip() 활용 회전만 사용해도 됐습니다.


2. 구현 (15:18 - 15:40)
    구현을 하며, 구상단계에서 생각하지 못했던 아래의 디테일들을 발견하고 바로 반영했습니다.
    - 참가자 없어서 k초 이전 게임 종료 체크는 미로 회전시키기 전에 해야함!
    - 참가자 정보를 갱신할 때는, = 가 아닌 +=


3. 디버깅 (15:40 - 15:43)
    아래의 실수들을 빠르게 확인하고 수정했습니다.
    - 미로 회전시 벽 내구도 깎지 않은 것.
    - 좌우가 상하보다 우선시 됐던 것.


4. 검증 (15:43 - 16:21)
    검증 루틴을 통해, 꽤나 주요한 실수들을 미리 발견할 수 있었습니다.
    - (15:55) n*n배열 전체를 회전시켜야 하는 경우를 포함하지 못한 것.
        (메모와 비교검증하다가 커스텀테케 만들어본 것에서 발견)
        이 실수의 경우, 이전에 술래잡기 문제에서도 초기구현에 했던 실수이기에,
        더 확실히 인지해뒀다가, 본시험에서 더 꼼꼼히 살펴볼 예정입니다.
    - (16:11) 참가자들 이동 시, 가장 가까워지는 곳으로 가야한다는 말 없었는데 그렇게 구현했던 것.
        (코드 정독 과정에서 문제에서 요구되지 않은 구현 발견)

    O (1) 주어진 테스트케이스로 검증
    O (2) 메모 vs. 코드
    O (3) (머릿속 환기 후) 문제 재정독
    O (4) 커스텀 테스트케이스 검증
    O (5) 철저한 코드 검증
    O (6) 오답노트 활용
    X (7) 다양한 구상에 따른, 다른 구현
"""

direction = ((1, 0), (-1, 0), (0, 1), (0, -1))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def cal_distance(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)


def find_maze_rotating_points_and_length():
    for leng in range(2, n + 1):
        for sy in range(n - leng + 1):
            for sx in range(n - leng + 1):
                if sum(map(lambda find: int(-1 in find), [area[row][sx:sx + leng] for row in range(sy, sy + leng)])) \
                        and sum(map(sum, [participants[row][sx:sx + leng] for row in range(sy, sy + leng)])):
                    return sy, sx, leng


n, m, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
participants = [[0] * n for _ in range(n)]
for _ in range(m):
    aa, bb = map(lambda inp: int(inp) - 1, input().split())
    participants[aa][bb] += 1
input_exit_y, input_exit_x = map(lambda inp: int(inp) - 1, input().split())
area[input_exit_y][input_exit_x] = -1

total_moved_distance = 0
for _ in range(k):
    exit_y, exit_x = None, None
    for i in range(n):
        for j in range(n):
            if area[i][j] == -1:
                exit_y, exit_x = i, j
                break
        else:
            continue
        break

    next_participants = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            people = participants[i][j]
            if not people:
                continue

            candidates = []
            for d_idx, (di, dj) in enumerate(direction):
                ni, nj = i + di, j + dj
                if oob(ni, nj):
                    continue
                if area[ni][nj] == -1:
                    total_moved_distance += people
                    break
                if area[ni][nj] or cal_distance(i, j, exit_y, exit_x) <= cal_distance(ni, nj, exit_y, exit_x):
                    continue
                candidates.append((d_idx, ni, nj))
            else:
                if not candidates:
                    next_participants[i][j] += people
                else:
                    npi, npj = min(candidates)[-2:]
                    next_participants[npi][npj] += people
                    total_moved_distance += people

    participants = next_participants

    if not sum(map(sum, participants)):
        break

    top, left, length = find_maze_rotating_points_and_length()
    rotating_area = [area[p_row][left:left + length] for p_row in range(top, top + length)]
    rotating_participants = [participants[p_row][left:left + length] for p_row in range(top, top + length)]
    rotating_area = [list(r_row)[::-1] for r_row in zip(*rotating_area)]
    rotating_participants = [list(r_row)[::-1] for r_row in zip(*rotating_participants)]
    for r_l in range(length):
        for c_l in range(length):
            area[top + r_l][left + c_l] = rotating_area[r_l][c_l] - 1 if rotating_area[r_l][c_l] > 0 else rotating_area[r_l][c_l]
            participants[top + r_l][left + c_l] = rotating_participants[r_l][c_l]

print(total_moved_distance)
for i in range(n):
    for j in range(n):
        if area[i][j] == -1:
            print(i + 1, j + 1)
            break
    else:
        continue
    break
