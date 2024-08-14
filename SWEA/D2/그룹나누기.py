# 20240814
# 08:11
# 1 / 1


def dfs(node):
    visited[node] = True

    for next_node in connected[node]:
        if not visited[next_node]:
            dfs(next_node)


t = int(input())
for test in range(1, t + 1):
    n, m = map(int, input().split())
    applications = list(map(int, input().split()))

    connected = [[] for _ in range(n)]
    for i in range(len(applications) // 2):
        a, b = applications[2 * i] - 1, applications[2 * i + 1] - 1
        connected[a].append(b)
        connected[b].append(a)

    answer = 0

    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)

    print(f"#{test} {answer}")


# 위는 DFS, 아래는 union-find 활용
"""
def find(child):
    if parents[child] == child:
        return child
    elif parents[child] != child:
        parents[child] = find(parents[child])
        return parents[child]


def union(parent, child):
    parents[find(child)] = parents[find(parent)]


t = int(input())
for test in range(1, t + 1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    # [1] make_set
    parents = [n for n in range(n + 1)]

    # [2] union
    for i in range(0, len(lst), 2):
        union(lst[i], lst[i + 1])

    # [3] 그룹대표 개수 세기'
    answer = 0
    for i in range(1, n + 1):
        if i == parents[i]:
            answer += 1

    print(f"#{test} {answer}")
"""