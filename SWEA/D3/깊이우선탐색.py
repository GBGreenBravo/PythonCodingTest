# 20240730
# 12:48

def dfs(start_node):
    visited = [0] * (v + 1)
    visited[start_node] = 1
    stk = []
    answer = [start_node]
    now = start_node

    while True:
        for n in lines[now]:
            if visited[n] == 0:
                visited[n] = 1
                answer.append(n)
                stk.append(now)
                now = n
                break
        else:
            if stk:
                now = stk.pop()
            else:
                break
    return answer


T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    lines = [[] for _ in range(v + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        lines[a].append(b)
        lines[b].append(a)

    for line in lines:
        line.sort()

    print(f"#{test_case}", *dfs(1))


# 위는 Stack을 활용한 루프로 푼 것.
# 아래는 재귀를 활용한 것.
"""
def dfs(node):
    visited[node] = 1
    answer.append(node)

    for n in lines[node]:
        if visited[n] == 0:
            dfs(n)


T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    lines = [[] for _ in range(v + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        lines[a].append(b)
        lines[b].append(a)

    for line in lines:
        line.sort()

    answer = []
    visited = [0] * (v + 1)
    dfs(1)

    print(f"#{test_case}", *answer)
"""