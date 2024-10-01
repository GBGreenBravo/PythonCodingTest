# 20241001
# 35:39
# 1 / 1


# people_arr(현재 사람들이 이용하는 계단(0 or 1) 정보 배열)을 바탕으로,
# 계단 내려가기 시뮬레이션 하는 함수
def check(people_arr):
    global min_answer

    stairs0_coming, stairs1_coming = [], []  # 계단으로 오고 있는 사람들
    stairs0_waiting, stairs1_waiting = 0, 0  # 계단 입구에서 기다리는 사람들
    stairs0_using, stairs1_using = [], []    # 계단 내려가고 있는 사람들

    # 계단별 오고 있는 사람들의 시간 계산 & 오름차순 정렬
    for idx, stair_num in enumerate(people_arr):
        if stair_num:
            stairs1_coming.append(moving_time[1][idx])
        else:
            stairs0_coming.append(moving_time[0][idx])
    stairs0_coming.sort()
    stairs1_coming.sort()

    # 시간
    time = 0
    # 계단 모두 내려갈 때까지
    while stairs0_coming or stairs1_coming or stairs0_waiting or stairs1_waiting or stairs0_using or stairs1_using:
        time += 1
        if time >= min_answer:  # 이미 시간이 최소시간 이상이면, return
            return

        # 계단 도착한 사람들, 대기시키기
        while stairs0_coming and stairs0_coming[0] == time:
            stairs0_waiting += 1
            del stairs0_coming[0]
        while stairs1_coming and stairs1_coming[0] == time:
            stairs1_waiting += 1
            del stairs1_coming[0]

        # 계단 다 내려간 사람들 제거
        stairs0_using = [u for u in stairs0_using if u]
        stairs1_using = [u for u in stairs1_using if u]

        # 계단 내려갈 사람들 내리기
        while stairs0_waiting and len(stairs0_using) < 3:
            stairs0_waiting -= 1
            stairs0_using.append(stairs0_using_time)
        while stairs1_waiting and len(stairs1_using) < 3:
            stairs1_waiting -= 1
            stairs1_using.append(stairs1_using_time)

        # 계단 내려가기 처리
        stairs0_using = [u - 1 for u in stairs0_using]
        stairs1_using = [u - 1 for u in stairs1_using]

    # 최소값 갱신
    min_answer = time


# 2**사람수 의 순열을 구성하는 DFS 함수
def dfs(cnt, dfs_arr):
    if cnt == len_people:
        check(dfs_arr)
        return

    dfs(cnt + 1, dfs_arr + [0])
    dfs(cnt + 1, dfs_arr + [1])


t = int(input())
for test in range(1, t + 1):
    n = int(input())
    area = [list(map(int, input().split())) for _ in range(n)]

    # 사람/계단 위치 찾기
    people = []
    stairs0, stairs1 = None, None
    for i in range(n):
        for j in range(n):
            if area[i][j] == 1:
                people.append((i, j))
            elif area[i][j]:
                if not stairs0:
                    stairs0 = (i, j)
                    stairs0_using_time = area[i][j]
                else:
                    stairs1 = (i, j)
                    stairs1_using_time = area[i][j]
    len_people = len(people)
    s0y, s0x = stairs0
    s1y, s1x = stairs1

    # 사람별 두 계단까지 걸리는 시간 + 1(계단 1번 내려가는 시간) 구하기
    moving_time = [[] for _ in range(2)]
    for pi, pj in people:
        moving_time[0].append(abs(s0y - pi) + abs(s0x - pj) + 1)
        moving_time[1].append(abs(s1y - pi) + abs(s1x - pj) + 1)

    # 2**사람수 의 순열 구성하며, 최소값 찾기
    min_answer = 10 * n**2 * n**2
    dfs(0, [])
    print(f"#{test} {min_answer}")
