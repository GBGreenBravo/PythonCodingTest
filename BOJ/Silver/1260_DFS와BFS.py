# 20240801
# 08:10
# 1 / 1

def bfs(start):
    result = []

    queue = [start]
    visited = [0] * (n + 1)
    visited[start] = 1
    result.append(start)

    while queue:
        now = queue.pop(0)
        for nex in connected[now]:
            if not visited[nex]:
                visited[nex] = 1
                queue.append(nex)
                result.append(nex)

    print(*result)


def dfs(start):
    result = [start]
    visited = [0] * (n + 1)
    visited[start] = 1
    stk = []
    now = start

    while True:
        for nex in connected[now]:
            if not visited[nex]:
                visited[nex] = 1
                stk.append(now)
                now = nex
                result.append(nex)
                break
        else:
            if stk:
                now = stk.pop()
            else:
                break

    print(*result)


n, m, v = map(int, input().split())
connected = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)
for c in connected:
    c.sort()


dfs(v)
bfs(v)
