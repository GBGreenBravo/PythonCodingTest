# 20240807
# 04:37
# 1 / 1


def dfs(index, sm):  # costs 행(제품)의 index, 이전까지의 총비용
    global answer

    if sm > answer:  # 조기 종료조건: 이미 총합이 answer을 넘어선 경우
        return

    if index == n:  # 모든 제품에 대해 공장비용을 다 선정한 경우
        answer = min(answer, sm)  # 최소값 갱신
        return

    for i in range(n):
        if not visited[i]:  # 이전에 채택하지 않은 공장에 대해 DFS
            visited[i] = True
            dfs(index + 1, sm + costs[index][i])
            visited[i] = False


t = int(input())
for test in range(1, t + 1):
    n = int(input())
    costs = [list(map(int, input().split())) for _ in range(n)]

    answer = 100 * 15
    visited = [False] * n  # 공장 중복 선정을 피하기 위한 방문 배열
    dfs(0, 0)

    print(f"#{test} {answer}")
