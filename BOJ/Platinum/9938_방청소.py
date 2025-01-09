# 20250109
# 19:59
# 1 / 1


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a < b:
        parent[b] = a
        now_group_cnt[a] += now_group_cnt[b]
        max_group_cnt[a] += max_group_cnt[b]
    else:
        parent[a] = b
        now_group_cnt[b] += now_group_cnt[a]
        max_group_cnt[b] += max_group_cnt[a]


N, L = map(int, input().split())
inputs = [tuple(map(int, input().split())) for _ in range(N)]

parent = [i for i in range(L + 1)]
now_group_cnt = [0] * (L + 1)
max_group_cnt = [1] * (L + 1)


for first, second in inputs:
    first = find(first)
    second = find(second)

    if max_group_cnt[first] == 1 and not now_group_cnt[first]:
        now_group_cnt[first] += 1
        union(first, second)
        print("LADICA")
        continue

    if max_group_cnt[second] == 1 and not now_group_cnt[second]:
        now_group_cnt[second] += 1
        union(first, second)
        print("LADICA")
        continue

    if max_group_cnt[first] - now_group_cnt[first]:
        now_group_cnt[first] += 1
        union(first, second)
        print("LADICA")
        continue

    if max_group_cnt[second] - now_group_cnt[second]:
        now_group_cnt[second] += 1
        union(first, second)
        print("LADICA")
        continue

    print("SMECE")


# 아래는 if문이 더 간소화된 풀이
"""
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    if a == b:
        return
    if a < b:
        parent[b] = a
        now_group_cnt[a] += now_group_cnt[b]
        max_group_cnt[a] += max_group_cnt[b]
    else:
        parent[a] = b
        now_group_cnt[b] += now_group_cnt[a]
        max_group_cnt[b] += max_group_cnt[a]


N, L = map(int, input().split())

parent = [i for i in range(L + 1)]
now_group_cnt = [0] * (L + 1)
max_group_cnt = [1] * (L + 1)

for _ in range(N):
    first, second = map(int, input().split())
    first = find(first)
    second = find(second)

    if max_group_cnt[first] - now_group_cnt[first]:
        now_group_cnt[first] += 1
        union(first, second)
        print("LADICA")
        continue

    if max_group_cnt[second] - now_group_cnt[second]:
        now_group_cnt[second] += 1
        union(first, second)
        print("LADICA")
        continue

    print("SMECE")
"""
