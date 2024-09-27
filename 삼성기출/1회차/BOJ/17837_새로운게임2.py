# 20240911
# 42:00
# 1 / 1

"""
풀이 시간: 42분 (14:51 ~ 15:34)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:51 - 15:01)
    '19237_어른상어'가 특정 우선순위와 같이 구현해줘야 할 로직이 더 많은 것으로 봤기에, 이 문제를 먼저 풀었습니다.
    문제 이해는 한 번만에 바로 했습니다.
    시간복잡도도 계산하여 구상에 이상 없음을 확인했습니다.


2. 구현 (15:01 - 15:24)
    문제를 구현하면서, 함수 1개만 쓰면 중복 코드가 상당할 것으로 생각했습니다.
    그러나 코드리뷰를 할 때마다 제우님의 코드를 보고 느낀 바가 있었습니다.
    구현 시험에서 중요한 것은, 중복 코드가 있는지가 아니라, 정확히 구현하는 것.
    따라서 이 문제에서는 중복 코드를 간단하게 구현하는 것보다, 중복 코드가 있더라도 정확하게 구현하는 것을 목표로 했습니다.


3. 검증 (15:24 - 15:34)
    4분 동안의 print디버깅을 통해,
    파란색/영역밖 만나고 반대편도 파란색/영역밖일 때, 방향 전환을 안 해줬음을 발견할 수 있었습니다.

    그리고 코드가 길었기에, 문제 요구조건/메모와 코드의 대조비교를 꼼꼼히 했습니다.

    한 함수에 구현하다보니, return하는 부분도 많았기에, 적절한 값을 return 해주고 있는지 일일이 체크했습니다.

    답안 코드를 복사붙여넣기 하는 과정에서, 따옴표를 잘못 입력해서 '컴파일 에러'가 떴습니다.
    바로 수정해서 제출했습니다..
"""

direction = (None, (0, 1), (0, -1), (-1, 0), (1, 0))
opposite_d_idx = [None, 2, 1, 4, 3]


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


# i_idx번째 체스 말을 옮기고, 옮긴 곳에 말이 4개 이상 쌓였는지를 True/False로 반환하는 함수
def move_individual(i_idx):
    y, x, d_idx = individuals[i_idx]
    dy, dx = direction[d_idx]

    # 현재 방향으로 갔을 때, 범위 밖으로 나간다면 => 파란색을 만난 경우와 동일하게
    if oob(y + dy, x + dx):
        d_idx = opposite_d_idx[d_idx]  # 반대 방향 idx
        dy, dx = direction[d_idx]

        backward = area[y + dy][x + dx]  # 반대 방향으로 갔을 때, 만나는 색 (oob인 경우 없음)
        # 반대 방향으로 갔을 때, 흰색을 만난 경우
        if backward == 0:
            moved_idx = stacked[y][x].index((i_idx, opposite_d_idx[d_idx]))
            stacked[y][x][moved_idx] = (i_idx, d_idx)
            moved_all = stacked[y][x][moved_idx:]
            stacked[y][x] = stacked[y][x][:moved_idx]

            for moved_idx, moved_d in moved_all:
                individuals[moved_idx] = (y + dy, x + dx, moved_d)

            stacked[y + dy][x + dx].extend(moved_all)

            return len(stacked[y + dy][x + dx]) >= 4  # 옮긴 곳에 4개 이상 쌓였는지 True/False 반환
        # 반대 방향으로 갔을 때, 빨간색을 만난 경우
        elif backward == 1:
            moved_idx = stacked[y][x].index((i_idx, opposite_d_idx[d_idx]))
            stacked[y][x][moved_idx] = (i_idx, d_idx)
            moved_all = stacked[y][x][moved_idx:][::-1]  # 흰색과 달리, 옮기는 원판을 뒤집어야 함
            stacked[y][x] = stacked[y][x][:moved_idx]

            for moved_idx, moved_d in moved_all:
                individuals[moved_idx] = (y + dy, x + dx, moved_d)

            stacked[y + dy][x + dx].extend(moved_all)

            return len(stacked[y + dy][x + dx]) >= 4  # 옮긴 곳에 4개 이상 쌓였는지 True/False 반환
        # 반대 방향으로 갔을 때, 파란색을 만난 경우
        elif backward == 2:
            # 방향만 돌려 저장
            stacked[y][x][stacked[y][x].index((i_idx, opposite_d_idx[d_idx]))] = (i_idx, d_idx)
            individuals[i_idx] = (y, x, d_idx)
            return

    # 현재 방향으로 갔을 때, 만나는 색
    forward = area[y + dy][x + dx]
    # 현재 방향으로 갔을 때, 흰색을 만난 경우
    if forward == 0:
        moved_idx = stacked[y][x].index((i_idx, d_idx))
        moved_all = stacked[y][x][moved_idx:]
        stacked[y][x] = stacked[y][x][:moved_idx]

        for moved_idx, moved_d in moved_all:
            individuals[moved_idx] = (y + dy, x + dx, moved_d)

        stacked[y + dy][x + dx].extend(moved_all)

        return len(stacked[y + dy][x + dx]) >= 4  # 옮긴 곳에 4개 이상 쌓였는지 True/False 반환

    # 현재 방향으로 갔을 때, 빨간색을 만난 경우
    elif forward == 1:
        moved_idx = stacked[y][x].index((i_idx, d_idx))
        moved_all = stacked[y][x][moved_idx:][::-1]  # 흰색과 달리, 옮기는 원판을 뒤집어야 함
        stacked[y][x] = stacked[y][x][:moved_idx]

        for moved_idx, moved_d in moved_all:
            individuals[moved_idx] = (y + dy, x + dx, moved_d)

        stacked[y + dy][x + dx].extend(moved_all)

        return len(stacked[y + dy][x + dx]) >= 4  # 옮긴 곳에 4개 이상 쌓였는지 True/False 반환

    # 현재 방향으로 갔을 때, 파란색을 만난 경우
    elif forward == 2:
        d_idx = opposite_d_idx[d_idx]
        dy, dx = direction[d_idx]
        # 반대 방향이 범위 밖인 경우
        if oob(y + dy, x + dx):
            # 방향만 돌려 저장
            stacked[y][x][stacked[y][x].index((i_idx, opposite_d_idx[d_idx]))] = (i_idx, d_idx)
            individuals[i_idx] = (y, x, d_idx)
            return
        backward = area[y + dy][x + dx]  # 반대 방향으로 갔을 때, 만나는 색 (oob인 경우 없음)
        # 반대 방향으로 갔을 때, 흰색을 만난 경우
        if backward == 0:
            moved_idx = stacked[y][x].index((i_idx, opposite_d_idx[d_idx]))
            stacked[y][x][moved_idx] = (i_idx, d_idx)
            moved_all = stacked[y][x][moved_idx:]
            stacked[y][x] = stacked[y][x][:moved_idx]

            for moved_idx, moved_d in moved_all:
                individuals[moved_idx] = (y + dy, x + dx, moved_d)

            stacked[y + dy][x + dx].extend(moved_all)

            return len(stacked[y + dy][x + dx]) >= 4  # 옮긴 곳에 4개 이상 쌓였는지 True/False 반환
        # 반대 방향으로 갔을 때, 빨간색을 만난 경우
        elif backward == 1:
            moved_idx = stacked[y][x].index((i_idx, opposite_d_idx[d_idx]))
            stacked[y][x][moved_idx] = (i_idx, d_idx)
            moved_all = stacked[y][x][moved_idx:][::-1]
            stacked[y][x] = stacked[y][x][:moved_idx]

            for moved_idx, moved_d in moved_all:
                individuals[moved_idx] = (y + dy, x + dx, moved_d)

            stacked[y + dy][x + dx].extend(moved_all)

            return len(stacked[y + dy][x + dx]) >= 4  # 옮긴 곳에 4개 이상 쌓였는지 True/False 반환
        # 반대 방향으로 갔을 때, 파란색을 만난 경우
        elif backward == 2:
            # 방향만 돌려 저장
            stacked[y][x][stacked[y][x].index((i_idx, opposite_d_idx[d_idx]))] = (i_idx, d_idx)
            individuals[i_idx] = (y, x, d_idx)
            return


n, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]  # 체스판 색 정보

stacked = [[[] for _ in range(n)] for _ in range(n)]  # 각 칸에 쌓이는 원판의 (index, 방향) 정보가 담길 배열
individuals = []  # 체스 말들의 (좌표 정보, 방향 정보)가 담길 배열
for idx in range(k):
    a, b, c = map(int, input().split())
    stacked[a - 1][b - 1].append((idx, c))
    individuals.append((a - 1, b - 1, c))

turn = 1
while turn <= 1000:
    # 모든 체스 말 차례대로 이동
    for idx in range(k):
        if move_individual(idx):  # 옮겨보고, 4개 이상 쌓였다면 break
            break
    else:
        turn += 1
        continue
    print(turn)
    break
else:
    print(-1)


# 아래는 중복 로직 제거
# + stacked에 (체스 말 idx, 방향정보) 말고, (체스 말 idx)만을 저장한 코드
"""
direction = (None, (0, 1), (0, -1), (-1, 0), (1, 0))
opposite_d_idx = [None, 2, 1, 4, 3]


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


# i_idx번째 체스 말을 옮기고, 옮긴 곳에 말이 4개 이상 쌓였는지를 True/False로 반환하는 함수
def move_individual(i_idx):
    y, x, d_idx = individuals[i_idx]
    dy, dx = direction[d_idx]

    # 현재 방향으로 갔을 때, 범위밖/파란색 이면
    if oob(y + dy, x + dx) or area[y + dy][x + dx] == 2:
        d_idx = opposite_d_idx[d_idx]  # 반대 방향 idx
        dy, dx = direction[d_idx]
        # 반대 방향으로 갔을 때, 범위밖/파란색 이면
        if oob(y + dy, x + dx) or area[y + dy][x + dx] == 2:
            # 방향만 돌려 저장
            individuals[i_idx] = (y, x, d_idx)
            return

    # 현재 방향으로 갔을 때, 만나는 색
    forward = area[y + dy][x + dx]

    moved_idx = stacked[y][x].index(i_idx)
    moved_all = stacked[y][x][moved_idx:]  # 옮겨지는 말들
    stacked[y][x] = stacked[y][x][:moved_idx]  # 기존 칸에서 빼기
    for moved_idx in moved_all:
        individuals[moved_idx] = (y + dy, x + dx, individuals[moved_idx][2])  # 옮겨지는 말들 위치정보 갱신
    individuals[i_idx] = (individuals[i_idx][0], individuals[i_idx][1], d_idx)

    # 현재 방향으로 갔을 때, 흰색을 만난 경우
    if forward == 0:
        stacked[y + dy][x + dx].extend(moved_all)
        return len(stacked[y + dy][x + dx]) >= 4  # 옮긴 곳에 4개 이상 쌓였는지 True/False 반환

    # 현재 방향으로 갔을 때, 빨간색을 만난 경우
    elif forward == 1:
        stacked[y + dy][x + dx].extend(moved_all[::-1])  # 흰색과 달리, 옮기는 원판을 뒤집어야 함
        return len(stacked[y + dy][x + dx]) >= 4  # 옮긴 곳에 4개 이상 쌓였는지 True/False 반환


n, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]  # 체스판 색 정보

stacked = [[[] for _ in range(n)] for _ in range(n)]  # 각 칸에 쌓이는 원판의 (index, 방향) 정보가 담길 배열
individuals = []  # 체스 말들의 (좌표 정보, 방향 정보)가 담길 배열
for idx in range(k):
    a, b, c = map(int, input().split())
    stacked[a - 1][b - 1].append(idx)
    individuals.append((a - 1, b - 1, c))

turn = 1
while turn <= 1000:
    # 모든 체스 말 차례대로 이동
    for idx in range(k):
        if move_individual(idx):  # 옮겨보고, 4개 이상 쌓였다면 break
            break
    else:
        turn += 1
        continue
    print(turn)
    break
else:
    print(-1)
"""