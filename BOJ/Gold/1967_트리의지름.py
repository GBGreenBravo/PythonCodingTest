# 20240818
# 14:32
# 1 / 2

import sys
sys.setrecursionlimit(10_000)


def get_mx(node):
    belows = []  # 자식노드별 최대값으로 가는 cost 저장할 배열
    for next_node, cost in connected[node]:
        belows.append(cost + get_mx(next_node))
    if not belows:  # 리프노드라면 return 0
        return 0

    belows.sort(reverse=True)  # 내림차순 정렬
    global mx
    if len(belows) == 1:  # 자식노드 하나라면, 현재에서 한 자식노드의 최대값으로 갱신 (루트노드가 1개의 자식노드만 갖는 경우 때문)
        mx = max(mx, belows[0])
    elif len(belows) > 1:  # 자식노드 여럿이면, 현재 노드가 루트노드인 부분트리의 최대 지름으로 갱신
        mx = max(mx, belows[0] + belows[1])
    return belows[0]  # 한 자식노드로 가는 최대값 반환


n = int(input())
connected = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    connected[a].append((b, c))

mx = 0
get_mx(1)

print(mx)
