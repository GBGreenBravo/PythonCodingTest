# 20240805
# 51:06
# 1 / 5

n = int(input())
connected = [[] for _ in range(n + 1)]  # 어디가 부모/자식 노드인지 모르므로, 양방향 간선으로 저장.
for _ in range(n - 1):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)

indexes = [1]  # 1이 부모노드임은 확실하므로 1부터 시작
while indexes:
    tmp_indexes = []
    for index in indexes:
        for i in connected[index]:  # 부모노드에 저장된 자식노드에 대해 역의 관계는 끊어주는 for문
            connected[i].remove(index)
            tmp_indexes.append(i)  # 자식노드의 자식노드와의 역의 관계도 끊어야 하기에, tmp_indexes에 저장
    indexes = tmp_indexes  # 다음 while문에서 끊을 부모노드들이 저장된 리스트

parent_nodes = [0] * (n + 1)  # 해당 인덱스의 부모노드 표시할 리스트
for parent in range(1, len(connected)):
    for child in connected[parent]:
        parent_nodes[child] = parent

print(*parent_nodes[2:], sep="\n")


# 아래는 BFS 풀이
"""
from collections import deque


def bfs():
    visited = [0] * (n + 1)
    visited[1] = 1
    queue = deque()
    queue.append(1)

    while queue:
        now = queue.popleft()
        for nex in connected[now]:
            if not visited[nex]:
                visited[nex] = now
                queue.append(nex)

    return visited


n = int(input())
connected = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)

print(*bfs()[2:], sep="\n")
"""


# 아래는 DFS 풀이
"""
def dfs():
    visited = [0] * (n + 1)
    visited[1] = 1
    stk = []
    now = 1

    while True:
        for nex in connected[now]:
            if not visited[nex]:
                visited[nex] = now
                stk.append(now)
                now = nex
                break
        else:
            if stk:
                now = stk.pop()
            else:
                break

    return visited


n = int(input())
connected = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)

print(*dfs()[2:], sep="\n")
"""