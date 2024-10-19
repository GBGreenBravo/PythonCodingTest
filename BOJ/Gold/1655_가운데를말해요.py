# 20241019
# 15:52
# 1 / 1

from heapq import heappush, heappop
from collections import deque

n = int(input())
numbers = deque([int(input()) for _ in range(n)])

now = numbers.popleft()
before, after = [], []
len_before, len_after = 0, 0  # 늘 두 값이 같거나, after가 1 더 큼

print(now)
while numbers:
    next_num = numbers.popleft()
    if next_num == now:
        heappush(before, -next_num)
        len_before += 1
    elif next_num < now:
        heappush(before, -next_num)
        len_before += 1
    else:  # next_num > now:
        heappush(after, next_num)
        len_after += 1

    if len_before > len_after:
        tmp = now
        now = -heappop(before)
        heappush(after, tmp)
        len_before -= 1
        len_after += 1
    elif len_before + 1 < len_after:
        tmp = now
        now = heappop(after)
        heappush(before, -tmp)
        len_before += 1
        len_after -= 1
    print(now)
