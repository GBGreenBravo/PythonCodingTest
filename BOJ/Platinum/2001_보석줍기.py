# 20241129
# 47:58
# 1 / 1

from collections import deque


def cal_max_weights(start_node):
    visited = [0] * N
    visited[start_node] = 100
    queue = deque([(start_node, 100)])

    while queue:
        now_node, max_weight = queue.popleft()
        for next_node, bridge_limit in connected[now_node]:
            if visited[next_node] < min(max_weight, bridge_limit):
                visited[next_node] = min(max_weight, bridge_limit)
                queue.append((next_node, min(max_weight, bridge_limit)))

    return_dict = dict()
    return_dict[0] = visited[0]
    for idx in jewels:
        return_dict[idx] = visited[idx]
    return return_dict


def bfs():
    answer = 0

    # 중복방문 줄이기 위한, 방문 배열
    visited = dict()
    for jew in jewels:
        visited[jew] = dict()

    queue = deque([[0, [0]]])

    while queue:
        now_node, route = queue.popleft()

        # 0으로 돌아가기가 불가능하면 continue
        if between_jewels[now_node][0] < len(route) - 1:
            continue

        # 최대값 갱신
        answer = max(answer, len(route) - 1)

        # 다음 보석 주우러 이동
        for next_node in jewels:
            # 같은 곳 or 이미 방문 했다면 continue
            if now_node == next_node or next_node in route:
                continue
            # 다음으로 갈 때 무게 제한 넘으면 continue
            if len(route) - 1 > between_jewels[now_node][next_node]:
                continue

            # 중복 방문 체크
            visited_value = visited[next_node].get(str(sorted(route)), 0)
            if visited_value:
                continue
            else:
                visited[next_node][str(sorted(route))] = len(route) - 1

            queue.append([next_node, route + [next_node]])

    return answer


N, M, K = map(int, input().split())

jewels = [int(input()) - 1 for _ in range(K)]
added_answer = 0
if 0 in jewels:
    jewels.remove(0)
    K -= 1
    added_answer = 1

connected = [[] for _ in range(N)]
for _ in range(M):
    aa, bb, cc = map(int, input().split())
    aa, bb = aa - 1, bb - 1
    connected[aa].append((bb, cc))
    connected[bb].append((aa, cc))

between_jewels = dict()
between_jewels[0] = cal_max_weights(0)
for i in jewels:
    between_jewels[i] = cal_max_weights(i)

print(bfs() + added_answer)
