# 20240816
# 38:26
# 1 / 5

import sys
sys.setrecursionlimit(500_000)


def find(child):
    if child == parents[child]:
        return child
    parents[child] = find(parents[child])
    return parents[child]


def union(parent, child):  # 서로소인 집합 원소들만 인자로 들어옴.
    fp, fc = find(parent), find(child)
    if fp < fc:  #
        parents[fc] = fp
    else:
        parents[fp] = fc


n, m = map(int, input().split())
turns = [tuple(map(int, input().split())) for _ in range(m)]

parents = [i for i in range(n)]

for i in range(m):
    a, b = turns[i]
    if find(a) == find(b):
        answer = i + 1
        break
    else:
        union(a, b)
else:
    answer = 0

print(answer)
