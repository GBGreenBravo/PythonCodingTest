# 20241008
# 1:07:08
# 1 / 1

"""
풀이 시간: 1시간 7분 (14:12 - 15:19)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:12 - 14:23)
    문제에 대해 궁금한 부분은 아니었지만,
    코드에서 꼭 처리해줘야 하는 포인트로 아래 2개의 사항을 메모했습니다.
    - 살충제 있는 칸(벽X)에는 항상 나무가 0이어야 함!
    - 벽에도 제초제 뿌릴 수 있다!


2. 구현 (14:23 - 14:45)
    이전 풀이와 같은 구상을 했기에,
    구현에서도, 나무 가장 많이 죽이는 위치를 찾는 부분(현재 구현에서는 min() 사용)을 제외하고는 모두 같았습니다.

    함수별 체크포인트를 통해,
    죽일 수 있는 나무 계산 시, 벽이 있는 칸에서도 제초제가 전파됐던 부분을 미리 탐지할 수 있었습니다.


3. 디버깅 (14:45 - 14:47)
    제초제 살포 시, 나무 죽임 처리를 안 해줬기에,
    적절한 부분에 area[y][x] = 0 코드를 추가했습니다.


4. 검증 (14:47 - 15:19)
    print_.py에는 프린트용 코드를 작성해서,
    칸별 죽일 수 있는 나무수도 가시성 있게 확인할 수 있었습니다.

    커스텀한 최대 사이즈의 테케를 만들어 돌려봤습니다.

    Ctrl+F7으로 입력받은 값들, 대각선4방향, 십자4방향이 적절한 곳에 쓰였는지 확인했습니다.
    index()함수가 쓰인 곳은 없었기에, [가 쓰인 곳들만 다 살펴보며, IndexError를 반환할 부분은 없는지 체크했습니다.
    커서를 하나씩 다 올려보며, i/j, y/x, ny/nx, dy/dx, sy/sx 를 바꿔쓴 부분은 없는지 체크했습니다.

    모든 좌표에서 최대로 죽일 수 있는 나무 수가 0인 경우, 바로 break를 할 수도 있지만,
    해당 코드는 효율을 생각한 풀이기에, 따로 구현&검증을 하지는 않았습니다.

    미리 따로 빼놨던 test.py의 코드와 temp.py의 코드를 비교하고 다른 부분이 없음을 확인한 뒤, 최종 제출했습니다.

    O (1) 주어진 테스트케이스로 검증
    O (2) 메모 vs. 코드
    O (3) (머릿속 환기 후) 문제 재정독
    O (4) 커스텀 테스트케이스 검증
    O (5) 철저한 코드 검증
    O (6) 오답노트 활용
    X (7) 다양한 구상에 따른, 다른 구현
"""

direction_4 = ((0, 1), (0, -1), (1, 0), (-1, 0))
diagonal_direction = ((1, 1), (1, -1), (-1, 1), (-1, -1))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def trees_grow():
    for y in range(n):
        for x in range(n):
            if area[y][x] <= 0:
                continue
            for dy, dx in direction_4:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or area[ny][nx] <= 0:
                    continue
                area[y][x] += 1


def trees_duplicate():
    duplicated = [[0] * n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if area[y][x] <= 0:
                continue

            possibles = []
            for dy, dx in direction_4:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or area[ny][nx] or pesticides[ny][nx]:
                    continue
                possibles.append((ny, nx))

            if not possibles:
                continue
            duplicated_value = area[y][x] // len(possibles)
            for py, px in possibles:
                duplicated[py][px] += duplicated_value

    for y in range(n):
        for x in range(n):
            if duplicated[y][x]:
                area[y][x] += duplicated[y][x]


def cal_max_killing_index():
    candidates = []
    for sy in range(n):
        for sx in range(n):
            if area[sy][sx] <= 0:
                candidates.append((0, sy, sx))
                continue

            now_cnt = area[sy][sx]
            for dy, dx in diagonal_direction:
                y, x = sy + dy, sx + dx
                for _ in range(k):
                    if oob(y, x) or area[y][x] <= 0:
                        break
                    now_cnt += area[y][x]
                    y, x = y + dy, x + dx
            candidates.append((-now_cnt, sy, sx))

    killing_cnt, killing_y, killing_x = min(candidates)
    return -killing_cnt, killing_y, killing_x


def spread_pesticide(sy, sx):
    pesticides[sy][sx] = c + 1
    if area[sy][sx] <= 0:
        return
    area[sy][sx] = 0

    for dy, dx in diagonal_direction:
        y, x = sy + dy, sx + dx
        for _ in range(k):
            if oob(y, x):
                break
            pesticides[y][x] = c + 1
            if area[y][x] <= 0:
                break
            area[y][x] = 0
            y, x = y + dy, x + dx


def decrease_pesticide():
    for y in range(n):
        for x in range(n):
            if pesticides[y][x]:
                pesticides[y][x] -= 1


n, m, k, c = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

pesticides = [[0] * n for _ in range(n)]

total_dead_trees = 0
for _ in range(m):
    trees_grow()
    trees_duplicate()
    killed_trees_cnt, ky, kx = cal_max_killing_index()
    total_dead_trees += killed_trees_cnt
    spread_pesticide(ky, kx)
    decrease_pesticide()
print(total_dead_trees)
