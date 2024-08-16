# 20240816
# 08:53
# 1 / 1

from heapq import heappop, heappush

t = int(input())
for test in range(1, t + 1):
    n, e = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(e)]
    connected = [[] for _ in range(n)]
    for a, b, c in edges:
        connected[a].append((b, c))

    visited = [1e4] * n  # 불가능한 최대값으로 방문배열 초기화
    visited[0] = 0

    heap_queue = []
    heappush(heap_queue, (0, 0))  # cost, node (heapq에서 cost 낮은 순으로 꺼내기 위해)

    while heap_queue:
        cost, node = heappop(heap_queue)

        if node == n - 1:  # 도착 노드 만나면 종료
            answer = cost
            break

        if cost > visited[node]:  # 이미 더 낮은 비용으로 갱신된 큐가 지나갔기에, 불필요한 계산이므로 continue
            continue

        for next_node, next_cost in connected[node]:  # 현재 노드에서 갈 수 있는 곳 중에
            if visited[next_node] > cost + next_cost:  # 현재 노드에서 가는 게, 기존보다 더 적은 비용이라면
                heappush(heap_queue, (cost + next_cost, next_node))
                visited[next_node] = cost + next_cost

    print(f"#{test} {answer}")
