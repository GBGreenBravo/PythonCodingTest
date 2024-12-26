# 20241226
# 15:41
# 1 / 1

N = int(input())
M = int(input())
total_len = len(bin(N)) - 2
visited = [total_len] * (N + 1)
starts = list(map(int, input().split()))
for start in starts:
    visited[start] = 0
queue = starts
while queue:
    next_queue = []
    for now in queue:
        distance = visited[now]
        for i in range(total_len):
            nex = now - (1 << i) if now & (1 << i) else now + (1 << i)
            if nex > N:
                continue
            if distance + 1 < visited[nex]:
                visited[nex] = distance + 1
                next_queue.append(nex)
    queue = next_queue

print(max(visited))
