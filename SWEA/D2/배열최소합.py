# 20240806
# 08:15
# 1 / 1


def dfs(index):  # 탐색할 행의 index
    if index == n:  # 마지막 행까지 탐색을 완료한 경우
        global mn
        mn = min(mn, sum(visited))  # 최소값 갱신
        return

    for i in range(n):
        if not visited[i]:  # 방문하지 않은 열에 대해 dfs()
            visited[i] = arr[index][i]
            dfs(index + 1)
            visited[i] = None


t = int(input())
for test in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    mn = 10 * n
    visited = [None] * n  # 열에 사용된 값을 저장하는 리스트
    dfs(0)

    print(f"#{test} {mn}")


# 백트래킹을 하지 않는다면, 시간이 많이 소모됨. 아래는 백트래킹 풀이.
"""
def dfs(index, sm):  # 탐색할 행의 index
    global mn

    if sm > mn:  # 조기 종료 조건: 이미 최소값보다 크다면
        return

    if index == n:  # 마지막 행까지 탐색을 완료한 경우
        mn = min(mn, sm)  # 최소값 갱신
        return

    for i in range(n):
        if not visited[i]:  # 방문하지 않은 열에 대해 dfs()
            visited[i] = 1
            dfs(index + 1, sm + arr[index][i])
            visited[i] = 0


t = int(input())
for test in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    mn = 10 * n
    visited = [0] * n  # 열에 사용된 값을 저장하는 리스트
    dfs(0, 0)

    print(f"#{test} {mn}")
"""