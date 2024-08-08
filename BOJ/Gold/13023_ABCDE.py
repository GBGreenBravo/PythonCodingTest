# 20240808
# 53:08
# 1 / 1


def dfs(now, distance):  # 현재 노드, DFS 시작지점으로부터의 거리
    if distance >= 4:  # ABCDE관계, 즉 4개의 connection을 거쳤다면 종료
        global five_in_a_row
        five_in_a_row = True
        return

    for nex in connected[now]:
        if not visited[nex]:
            visited[now] = True
            dfs(nex, distance + 1)
            visited[nex] = False


n, m = map(int, input().split())
connected = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)

visited = [False] * n  # DFS로 방문할 때, 중복 방문하지 않기 위한 배열
for node in range(n):
    five_in_a_row = False  # ABCDE관계가 있는지 체크하는 flag
    visited[node] = True
    dfs(node, 0)
    visited[node] = False
    if five_in_a_row:  # ABCDE관계 있으면 반복문 종료
        break
print(1 if five_in_a_row else 0)
