import sys

added = ((1, 2, 2, 2, 2),
         (2, 1, 3, 4, 3),
         (2, 3, 1, 3, 4),
         (2, 4, 3, 1, 3),
         (2, 3, 4, 3, 1))

steps = list(map(int, sys.stdin.readline().split()))
steps.insert(0, steps.pop())

now = [0] + [1e6] * 4
for idx in range(1, len(steps)):

    bs, ns = steps[idx - 1], steps[idx]

    if bs == ns:
        now = [v + 1 for v in now]
        continue

    nex = [v + added[bs][ns] for v in now]
    for s, v in enumerate(now):
        if v + added[s][ns] < nex[bs]:
            nex[bs] = v + added[s][ns]
    now = nex

print(min(now))
