# 20241210
# 07:43
# 1 / 1

from collections import deque

N, K = map(int, input().split())
products = deque(map(int, input().split()))
using = []
answer = 0
while products:
    p = products.popleft()
    if p in using:
        continue
    if len(using) == N:
        candidates = []
        copied = list(products) + using[:]
        for u in using:
            candidates.append((copied.index(u), u))
        _, u = max(candidates)
        using.remove(u)
        answer += 1
    using.append(p)
print(answer)
