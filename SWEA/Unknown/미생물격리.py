# 20240923
# 17:22
# 1 / 1

direction = (None, (-1, 0), (1, 0), (0, -1), (0, 1))
opposite = [None, 2, 1, 4, 3]


# 테두리 부분인지 판단하는 함수
def edge(y, x):
    return y == 0 or y == n - 1 or x == 0 or x == n - 1


# 모든 미생물 군집 이동시키는 함수
def move():
    for y in range(n):
        for x in range(n):
            if area[y][x]:
                cnt, d = area[y][x][0]
                dy, dx = direction[d]
                ny, nx = y + dy, x + dx

                # 테두리라면 -> 방향 전환 & 개수 반감
                if edge(ny, nx):
                    d = opposite[d]
                    cnt //= 2

                # 이동 상태 반영
                new_area[ny][nx].append((cnt, d))


# 두 군집 이상 모인 곳에 대해 병합시키는 함수
def merge():
    for y in range(n):
        for x in range(n):
            if len(new_area[y][x]) > 1:  # 2 이상이라면
                new_area[y][x].sort(reverse=True)  # 개수 내림차순 정렬
                new_area[y][x] = [(sum([ar[0] for ar in new_area[y][x]]), new_area[y][x][0][1])]  # [(개수 합, 개수 가장 많은 군집의 방향)]


t = int(input())
for test in range(1, t + 1):
    n, m, k = map(int, input().split())

    # 군집 정보 저장
    area = [[[] for _ in range(n)] for _ in range(n)]
    for _ in range(k):
        a, b, c, d = map(int, input().split())
        area[a][b].append((c, d))

    # m 시간 동안 반복 수행
    for _ in range(m):
        new_area = [[[] for _ in range(n)] for _ in range(n)]  # 이동된 군집 저장할 배열
        move()   # 군집 이동
        merge()  # 군집 병합
        area = new_area

    print(f"#{test} {sum([sum([area[row][col][0][0] for row in range(n) if area[row][col]]) for col in range(n)])}")


# 군집 정보 2차원배열 말고 1차원배열로 관리하여, 시간효율 개선
# (병합을 위한 2차원배열은 그대로)
"""
direction = (None, (-1, 0), (1, 0), (0, -1), (0, 1))
opposite = [None, 2, 1, 4, 3]


# 테두리 부분인지 판단하는 함수
def edge(y, x):
    return y == 0 or y == n - 1 or x == 0 or x == n - 1


# 모든 미생물 군집 이동시키는 함수
def move():
    for y, x, cnt, d in groups:
        dy, dx = direction[d]
        ny, nx = y + dy, x + dx

        # 테두리라면 -> 방향 전환 & 개수 반감
        if edge(ny, nx):
            d = opposite[d]
            cnt //= 2

        # 이동 상태 반영
        new_area[ny][nx].append((cnt, d))


# 두 군집 이상 모인 곳에 대해 병합시키는 함수
def merge():
    for y in range(n):
        for x in range(n):
            if new_area[y][x]:
                if len(new_area[y][x]) > 1:  # 2 이상이라면
                    new_area[y][x].sort(reverse=True)  # 개수 내림차순 정렬
                    new_area[y][x] = [(sum([ar[0] for ar in new_area[y][x]]), new_area[y][x][0][1])]  # [(개수 합, 개수 가장 많은 군집의 방향)]
                new_groups.append((y, x, new_area[y][x][0][0], new_area[y][x][0][1]))


t = int(input())
for test in range(1, t + 1):
    n, m, k = map(int, input().split())

    # 군집 정보 저장
    groups = []
    for _ in range(k):
        a, b, c, d = map(int, input().split())
        groups.append((a, b, c, d))

    # m 시간 동안 반복 수행
    for _ in range(m):
        new_area = [[[] for _ in range(n)] for _ in range(n)]  # 이동된 군집 저장할 N*N 배열
        move()   # 군집 이동

        new_groups = []  # 새로운 군집정보가 저장될 배열
        merge()  # 군집 병합
        groups = new_groups  # 군집정보 갱신

    print(f"#{test} {sum([group[2] for group in groups])}")
"""