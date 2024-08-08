# 20240807
# 10:39
# 1 / 1


def dfs(level, sm, before):  # 사무실을 제외하고 지나온 구역 수, 비용 총합, 이전에 방문했던 곳
    global mn

    if sm > mn:  # 조기 종료 조건: 이미 총합이 최소값을 넘었을 때
        return

    if level == n - 1:
        sm += costs[before][0]  # 사무실은 방문처리가 이미 돼있기 때문에, 마지막 방에서 1로 가는 비용 추가해줘야 함.
        mn = min(mn, sm)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(level + 1, sm + costs[before][i], i)
            visited[i] = False


t = int(input())
for test in range(1, t + 1):
    n = int(input())
    costs = [list(map(int, input().split())) for _ in range(n)]

    visited = [False] * n
    visited[0] = True
    mn = 10_000
    dfs(0, 0, 0)

    print(f"#{test} {mn}")
