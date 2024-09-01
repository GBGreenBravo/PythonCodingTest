# 20240826
# 39:42
# 1 / 1

import sys
sys.setrecursionlimit(100_000)


def get_max_diameter(node):
    global mx_diameter
    # 현재 노드와 연결된 것들 중
    # 이미 visited 처리 된 하나는 부모노드로 취급하고, (루트노드 1은 자식노드만 가짐.)
    # visited 처리되지 않은 것은 자식노드로 취급한다.
    children_diameter = []  # 현재노드에서 각 자식노드들로 갈 때의 최대 지름

    for next_node, next_cost in connected[node]:
        if not visited[next_node]:  # 자식노드라면
            visited[next_node] = 1  # 방문처리
            children_diameter.append(get_max_diameter(next_node) + next_cost)  # (자식노드에서의 최대 지름 + 자식노드로 가는 비용)을 저장한다.

    if not children_diameter:  # 현재노드가 리프노드라면 return 0
        return 0
    else:
        children_diameter.sort(reverse=True)  # 내림차순 정렬
        if len(children_diameter) >= 2:  # 자식노드 2개 이상이라면
            mx_diameter = max(mx_diameter, children_diameter[0] + children_diameter[1])  # 현재가 루트노드가 되는 부분트리에서 최대지름 가질 수 있으므로, 최대값과 2번째로 큰 값을 더하여 갱신
        return children_diameter[0]  # 자식노드 지름들 중 최대값을 반환


v = int(input())
connected = [[] for _ in range(v + 1)]
for _ in range(v):
    a, *lst = map(int, input().split())
    lst = list(lst)[:-1]
    for i in range(0, len(lst), 2):
        connected[a].append((lst[i], lst[i + 1]))

visited = [0] * (v + 1)
visited[1] = 1

mx_diameter = 0
mx_in_case_of_root_has_one_child = get_max_diameter(1)  # 아무 번호에서 시작해도 상관 없지만, 1을 루트노드라고 가정하고 시작.
mx_diameter = max(mx_diameter, mx_in_case_of_root_has_one_child)  # 루트노드 1이 자식노드 1개만 가지는 경우도 있을 수 있으므로, 반환값으로 최대값 비교
print(mx_diameter)
