# 20240814
# 55:45
# 1 / 3


def find(child):
    if parents[child] == child:
        return child
    else:
        parents[child] = find(parents[child])
        return parents[child]


def union(parent, child):
    fp, fc = find(parent), find(child)
    if fp == fc:
        return
    if fp < fc:
        parents[fc] = fp
    else:
        parents[fp] = fc


v, e = map(int, input().split())
connections = [tuple(map(int, input().split())) for _ in range(e)]
connections.sort(key=lambda x: x[2])  # 비용 오름차순으로 정렬

connection_cnt = 0  # 이 카운트가 v - 1이 되면 v개의 모든 노드 연결되는 것.
total_cost = 0  # 정답이 될 총 비용

parents = [i for i in range(v + 1)]  # union-find를 활용하기 위한(연결된 그룹을 체크하기 위한) 부모노드 정보 배열

for a, b, c in connections:  # 비용이 적은 간선들부터
    if connection_cnt == v - 1:  # 모든 노드들이 연결 됐다면 종료
        break

    if find(a) != find(b):  # 부모 노드가 다르면(같은 그룹이 아니라면), 같은 그룹으로 묶어주기 => parents[] 비교가 아닌 find()!!!
        connection_cnt += 1
        total_cost += c  # 해당 간선을 채택
        union(a, b)

print(total_cost)
