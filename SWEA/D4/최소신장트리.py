# 20240814


def prim(start):
    mst = set()
    mst.add(start)
    sm = 0

    for _ in range(n):
        mn, mn_i = 11, 0
        for c in mst:
            for next_node, cost in connected[c]:
                if next_node not in mst and mn > cost:
                    mn = cost
                    mn_i = next_node
        mst.add(mn_i)
        sm += mn

    return sm


t = int(input())
for test in range(1, t + 1):
    n, v = map(int, input().split())
    connected = [[] for _ in range(n + 1)]
    for _ in range(v):
        a, b, c = map(int, input().split())
        connected[a].append((b, c))
        connected[b].append((a, c))

    print(f"#{test} {prim(0)}")
