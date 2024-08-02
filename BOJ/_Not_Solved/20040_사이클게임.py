# 20240801
# 1:28:09

n, m = map(int, input().split())
connected = [[] for _ in range(n)]
kill_list = [[] for _ in range(n)]
lines = [tuple(map(int, input().split())) for _ in range(m)]


def connect(a, b):

    if connected[a]:
        for connec in connected[a]:
            if b in connected[connec] or b in kill_list[connec]:
                return True
            if connec in connected[b] or connec in kill_list[b]:
                return True
            kill_list[connec].append(b)
            kill_list[b].append(connec)
    connected[a].append(b)

    if connected[b]:
        for connec in connected[b]:
            if a in connected[connec] or a in kill_list[connec]:
                return True
            if connec in connected[a] or connec in kill_list[a]:
                return True
            kill_list[connec].append(a)
            kill_list[a].append(connec)
    connected[b].append(a)


answer = 0
for i in range(m):
    a, b = lines[i]
    if connect(a, b):
        answer = i + 1
        break

print(answer)
