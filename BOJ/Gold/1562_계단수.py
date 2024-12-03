# 20241203
# 26:55
# 1 / 1

from itertools import combinations

N = int(input())
M = 1_000_000_000

now = dict()
for i in range(1, 11):
    for comb in combinations([j for j in range(10)], i):
        for k in range(10):
            now[tuple(list(comb) + [k])] = 0
for i in range(1, 10):
    now[(i, i,)] = 1

for _ in range(N - 1):
    next = dict()
    for i in range(1, 11):
        for comb in combinations([j for j in range(10)], i):
            for k in range(10):
                next[tuple(list(comb) + [k])] = 0

    for comb, value in now.items():
        if not value:
            continue

        if comb[-1] == 0:
            key = tuple(sorted(list(set(comb) | {1}))) + (1,)
            next[key] = (next[key] + value) % M
        elif comb[-1] == 9:
            key = tuple(sorted(list(set(comb) | {8}))) + (8,)
            next[key] = (next[key] + value) % M
        else:
            key = tuple(sorted(list(set(comb) | {comb[-1] - 1}))) + (comb[-1] - 1,)
            next[key] = (next[key] + value) % M
            key = tuple(sorted(list(set(comb) | {comb[-1] + 1}))) + (comb[-1] + 1,)
            next[key] = (next[key] + value) % M

    now = next

answer = 0
for i in range(10):
    answer += now[(0, 1, 2, 3, 4, 5, 6, 7, 8, 9) + (i,)]
print(answer % M)
