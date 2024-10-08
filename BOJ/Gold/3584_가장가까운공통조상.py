# 20240805
# 07:46
# 1 / 1

def get_parents_of(start):  # 시작 노드부터 루트노드까지의 부모노드들을 리스트로 반환하는 함수
    parents = [start]  # 반환될 부모노드들의 리스트
    now = start

    while now:
        parents.append(connected[now])  # 부모노드 저장
        now = connected[now]  # 부모노드는 1개뿐이므로, 루트노드까지 반복

    return parents


t = int(input())
for _ in range(t):
    n = int(input())
    connected = [None] * (n + 1)  # 해당 index의 부모노드 정보를 저장. (부모노드는 1개만 가능하기에 []가 아닌 None으로)
    for _ in range(n - 1):
        parent, child = map(int, input().split())
        connected[child] = parent

    a, b = map(int, input().split())
    a_parents = get_parents_of(a)  # a와 b에 대해, 각각을 시작으로 루트노드까지의 부모노드들을, 리스트로 저장
    b_parents = get_parents_of(b)

    for a_parent in a_parents:  # a부터 시작하는 부모노드들을 거슬러 올라가면서
        if a_parent in b_parents:  # 이 부모노드가 b에도 있다면 이것이 가장 가까운 공통 조상
            print(a_parent)
            break
