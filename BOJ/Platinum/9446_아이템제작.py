# 20250110
# 15:08
# 1 / 1

from heapq import heappush, heappop

N, M = map(int, input().split())
prices = [None] + list(map(int, input().split()))
recipes = [None] + [[] for _ in range(N)]
queue = []
for _ in range(M):
    aa, xx, yy = map(int, input().split())
    recipes[xx].append((yy, aa))
    recipes[yy].append((xx, aa))
    if prices[xx] + prices[yy] < prices[aa]:
        heappush(queue, (prices[xx] + prices[yy], xx, yy, aa))

while queue:
    new_price, first, second, third = heappop(queue)

    if prices[third] <= new_price:
        continue

    prices[third] = new_price
    for next_second, next_third in recipes[third]:
        if new_price + prices[next_second] < prices[next_third]:
            heappush(queue, (new_price + prices[next_second], third, next_second, next_third))

print(prices[1])
