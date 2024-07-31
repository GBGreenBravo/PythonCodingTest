# 20240731
# 04:20

T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    connected = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        connected[a].append(b)
        connected[b].append(a)
    for c in connected:
        c.sort()

    queue = [1]
    answer = []
    visited = [0] * (v + 1)
    visited[1] = 1
    while queue:
        now = queue.pop(0)
        answer.append(now)

        for n in connected[now]:
            if not visited[n]:
                visited[n] = 1
                queue.append(n)

    print(f"#{test_case}", *answer)
