# 20240812
# 03:04
# 1 / 1

from heapq import heappop, heappush

n = int(input())
arr = []
nums = [int(input()) for _ in range(n)]

for num in nums:
    if num == 0:
        if not arr:
            print(0)
        else:
            print(heappop(arr)[1])
    else:
        heappush(arr, (abs(num), num))
