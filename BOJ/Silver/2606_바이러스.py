# 20240730
# 03:52

def dfs(node):
    visited[node] = 1
    for i in connected[node]:
        if visited[i] == 0:
            dfs(i)


n = int(input())
e = int(input())
connected = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)

visited = [0] * (n + 1)
dfs(1)

print(sum(visited) - 1)


# 위는 재귀 활용, 아래는 스택 활용
"""
def dfs(start_node):
    visited = [0] * (n + 1)
    visited[start_node] = 1
    stk = []
    now = start_node

    while True:
        for i in connected[now]:
            if visited[i] == 0:
                visited[i] = 1
                stk.append(now)
                now = i
                break
        else:
            if stk:
                now = stk.pop()
            else:
                break

    return sum(visited) - 1


n = int(input())
e = int(input())
connected = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)

print(dfs(1))
"""