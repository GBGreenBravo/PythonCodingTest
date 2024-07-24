# 20240723
# 10:41

h, w = map(int, input().split())
area = []
for i in range(h):
    area.append(list(input()))

for i in range(h):
    for j in range(w):
        if area[i][j] == "c":
            area[i][j] = 0
        else:
            area[i][j] = -1

for i in range(h):
    for j in range(w):
        if area[i][j] == 0:
            move = 0
            while j < w - 1:
                j += 1
                move += 1
                if area[i][j] == 0:
                    j -= 1
                    break
                else:
                    area[i][j] = move

for i in area:
    print(*i, sep=" ", end="\n")
