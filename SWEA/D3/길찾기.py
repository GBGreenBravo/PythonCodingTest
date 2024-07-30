# 20240730
# 12:05

def dfs():
    visited = [0] * 100
    visited[0] = 1
    stk = []
    now = 0

    while True:
        for n in connected[now]:
            if visited[n] == 0:
                if n == 99:
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


for _ in range(10):
    test_case, e = map(int, input().split())
    connected = [[] for _ in range(100)]
    mixed_route = list(map(int, input().split()))
    for i in range(len(mixed_route) // 2):
        i *= 2
        connected[mixed_route[i]].append(mixed_route[i + 1])

    print(f"#{test_case} {1 if dfs() else 0}")


# 위는 스택 / 아래는 재귀
"""
def bfs(node):
    global find_99

    visited[node] = 1
    if find_99:
        return
    if node == 99:
        find_99 = True
        return
    for n in connected[node]:
        if visited[n] == 0:
            bfs(n)


for _ in range(10):
    test_case, e = map(int, input().split())
    connected = [[] for _ in range(e)]
    mixed_connected = list(map(int, input().split()))
    for i in range(0, len(mixed_connected), 2):
        connected[mixed_connected[i]].append(mixed_connected[i + 1])

    visited = [0] * 100
    find_99 = False
    bfs(0)

    print(f"#{test_case} {visited[99]}")
"""