# 20240812
# 06:19
# 1 / 1

from heapq import heappush, heappop

n = int(input())
nums = [int(input()) for _ in range(n)]
arr = []
for num in nums:
    if num == 0:
        if not arr:
            print(0)
        else:
            print(-1 * heappop(arr))
    else:
        heappush(arr, -1 * num)
