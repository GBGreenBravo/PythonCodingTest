# 20240829
# 32:10
# 1 / 1

from collections import deque

n = int(input())
populations = list(map(int, input().split()))
connected = [[] for _ in range(n)]

# 간선 연결
for now_node in range(n):
    _, *next_nodes = map(int, input().split())
    for next_node in next_nodes:
        connected[now_node].append(next_node - 1)

answer = sum(populations)  # 불가능한 최대값으로 초기화

# 아래는 이진수 활용
# 0번 인덱스는 1로 고정
# n이 10일 때, 1000000000 부터 1111111110 까지 (모두 1팀/0팀인 경우는 없음)
for i in range(2**(n-1), 2**n - 1):
    # 비트연산자 활용; 이진수->팀 (ex. 100110 -> [1, 0, 0, 1, 1, 0]
    teams = [(i >> (n-1-j)) & 1 for j in range(n)]

    population_diff = abs(sum(populations) - 2 * sum([populations[j] for j in range(n) if teams[j]]))
    # (내혁님 코드에서 본) 가지치기; 지금 조합 인구차이가 최소값 이상이라면 continue
    if population_diff >= answer:
        continue

    visited = [0] * n

    # 0번 인덱스는 1선거구(1team)로 고정
    # => 1선거구 BFS
    queue = deque()
    queue.append(0)
    visited[0] = 1

    while queue:
        now = queue.popleft()

        for next_ in connected[now]:
            if not visited[next_] and teams[next_]:
                visited[next_] = 1
                queue.append(next_)

    # 방문 안한 1선거구(1team) 있으면 continue
    if sum([not visited[j] and teams[j] for j in range(n)]):
        continue

    # 0선거구(0team) 찾아서
    # => 0선거구 BFS
    queue = deque()
    queue.append(visited.index(0))
    visited[visited.index(0)] = 1

    while queue:
        now = queue.popleft()

        for next_ in connected[now]:
            if not visited[next_] and not teams[next_]:
                visited[next_] = 1
                queue.append(next_)

    # 방문 안된 노드 있으면 (= 하나라도 고립됐다면) continue
    if sum(visited) != n:
        continue

    # 인구수 차이 최소값 갱신
    answer = min(answer, population_diff)

print(answer if answer != sum(populations) else -1)  # 초기값 갱신 안 됐으면 -1 출력
