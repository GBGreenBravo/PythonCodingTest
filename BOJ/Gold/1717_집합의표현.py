# 20240814
# 07:55
# 1 / 1


def find(child):
    if parents[child] == child:
        return child
    else:
        parents[child] = find(parents[child])
        return parents[child]


def union(parent, child):
    parents[find(child)] = find(parent)


n, m = map(int, input().split())
orders = [tuple(map(int, input().split())) for _ in range(m)]

parents = [i for i in range(n + 1)]

for order, a, b in orders:
    if order == 0:
        union(a, b)
    else:
        print('yes' if find(a) == find(b) else 'no')  # union()과정에서 연산에 포함되지 않은 자식들이 존재할 수 있으므로, parents[a] == parents[b]가 아닌 find(a) == find(b)가 되어야 한다.


# 시간 조금 더 단축할 수 있는 def union() 풀이
"""
import sys
sys.setrecursionlimit(100000)


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


n, m = map(int, input().split())
orders = [tuple(map(int, input().split())) for _ in range(m)]

parents = [i for i in range(n + 1)]

for order, a, b in orders:
    if order == 0:
        union(a, b)
    else:
        print('yes' if find(a) == find(b) else 'no')
"""