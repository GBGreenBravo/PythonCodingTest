# 20250109
# 30:22
# 1 / 1

N = int(input())
lst = list(map(int, input().split()))
visited = set()
left, right = None, lst[0]
visited.add(lst[0])

for now in lst[1:]:
    visited.add(now)
    left, right = right, now
    while left != right:
        if left < right:
            right //= 2
            visited.add(right)
        else:
            left //= 2
            visited.add(left)
print(len(visited))
