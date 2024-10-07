# 20241007
# 1:06:33
# 1 / 1

"""
풀이 시간: 1시간 6분 (14:50 - 15:56)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:50 - 15:07)


2. 구현 (15:07 - 15:34)
    for cy, cx, cd in catcher_route:
        print_area = [[0] * n for _ in range(n)]
        print_area[cy][cx] = ['상', '우', '하', '좌'][cd]
        print(*print_area, sep="\n")
        print()
    술래의 이동을 확인하는 체크포인트에서, 위의 코드를 활용해 가시성 좋은 방식으로 중간검증 했습니다.
    확실히 이전에 숫자로만 print했던 방식보다 수월하게 체크할 수 있었습니다.


3. 디버깅 (-)


4. 검증 (15:34 - 15:56)
    O (1) 주어진 테스트케이스로 검증
    O (2) 메모 vs. 코드
        - catcher[1]로 적혀있어야 할 부분이, catcher[0]로 적혀있던 실수를 발견했습니다.
          (5)단계에서도 거를 수 있었겠지만, 코드를 읽는 과정에서 탐지했기에, 수정했습니다.
    O (3) (머릿속 환기 후) 문제 재정독
    O (4) 커스텀 테스트케이스 검증
    O (5) 철저한 코드 검증
    O (6) 오답노트 활용
    X (7) 다양한 구상에 따른, 다른 구현
"""

direction = ((-1, 0), (0, 1), (1, 0), (0, -1))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def move_all_runners():
    global runners_map

    new_runners_map = [[[] for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if abs(catcher[0] - y) + abs(catcher[1] - x) > 3:
                new_runners_map[y][x].extend(runners_map[y][x])
            else:
                for runner_d_idx in runners_map[y][x]:
                    dy, dx = direction[runner_d_idx]
                    ny, nx = y + dy, x + dx
                    if not oob(ny, nx):
                        if ny == catcher[0] and nx == catcher[1]:
                            new_runners_map[y][x].append(runner_d_idx)
                        else:
                            new_runners_map[ny][nx].append(runner_d_idx)
                    else:
                        runner_d_idx = (runner_d_idx + 2) % 4
                        dy, dx = direction[runner_d_idx]
                        ny, nx = y + dy, x + dx

                        if ny == catcher[0] and nx == catcher[1]:
                            new_runners_map[y][x].append(runner_d_idx)
                        else:
                            new_runners_map[ny][nx].append(runner_d_idx)
    runners_map = new_runners_map


n, m, h, k = map(int, input().split())
runners_map = [[[] for _ in range(n)] for _ in range(n)]
for runner_input_idx in range(m):
    aa, bb, cc = map(int, input().split())
    runners_map[aa - 1][bb - 1].append(cc)
trees = [[0] * n for _ in range(n)]
for _ in range(h):
    aa, bb = map(int, input().split())
    trees[aa - 1][bb - 1] = 1

spiral_visited = [[0] * n for _ in range(n)]
spiral_visited[0][0] = 1
sp_i, sp_j, sp_d = 0, 0, 2
catcher_route = [[0, 0, 2]]
temp_route = []
while not (sp_i == n // 2 and sp_j == n // 2):
    di, dj = direction[sp_d]
    sp_i, sp_j = sp_i + di, sp_j + dj
    spiral_visited[sp_i][sp_j] = 1
    temp_route.append([sp_i, sp_j, (sp_d + 2) % 4])

    ni, nj = sp_i + di, sp_j + dj
    if oob(ni, nj) or spiral_visited[ni][nj]:
        sp_d = (sp_d - 1) % 4

    catcher_route.append([sp_i, sp_j, sp_d])
temp_route.reverse()
catcher_route = temp_route + catcher_route[:-1]

catcher_idx = 0
catcher = catcher_route[0]

total_score = 0

for turn in range(1, k + 1):
    move_all_runners()

    now_caught_cnt = 0

    catcher_idx = (catcher_idx + 1) % len(catcher_route)
    catcher = catcher_route[catcher_idx]

    dci, dcj = direction[catcher[2]]
    for c_dist in range(3):
        nci, ncj = catcher[0] + dci * c_dist, catcher[1] + dcj * c_dist
        if oob(nci, ncj) or trees[nci][ncj]:
            continue
        now_caught_cnt += len(runners_map[nci][ncj])
        runners_map[nci][ncj] = []

    total_score += now_caught_cnt * turn

print(total_score)
