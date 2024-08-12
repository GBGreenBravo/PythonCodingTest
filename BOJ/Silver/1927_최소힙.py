# 20240812
# 12:24
# 1 / 1

# nums를 한번에 받지 않고, 반복문 안에서 매번 input()받아서 시간초과 났었음.

import heapq

n = int(input())
nums = [int(input()) for _ in range(n)]
arr = []
for num in nums:
    if num == 0:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, num)
