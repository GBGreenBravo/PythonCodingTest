# 20240730
# 08:20

def dfs(start, end):
    visited = [0] * (v + 1)
    visited[start] = 1
    stk = []
    now = start

    while True:
        for n in connected[now]:
            if visited[n] == 0:
                if n == end:
                    return True
                visited[n] = 1
                stk.append(now)
                now = n
                break
        else:
            if stk:
                now = stk.pop()
            else:
                break

    return False


T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())

    connected = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        connected[a].append(b)

    start_node, end_node = map(int, input().split())

    print(f"#{test_case} {1 if dfs(start_node, end_node) else 0}")


# 위는 스택 활용, 아래는 재귀 활용
"""
def dfs(node):
    global find_end

    visited[node] = 1
    route.append(node)

    if find_end:
        return

    if node == end_node:
        find_end = True
        return

    for n in connected[node]:
        if visited[n] == 0:
            dfs(n)


T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())

    connected = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        connected[a].append(b)

    start_node, end_node = map(int, input().split())

    visited = [0] * (v + 1)
    visited[start_node] = 1
    route = [start_node]

    find_end = False
    dfs(start_node)

    print(f"#{test_case} {1 if end_node in route else 0}")
"""