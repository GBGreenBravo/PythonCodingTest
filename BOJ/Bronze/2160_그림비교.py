# 20240726
# 11:19

# 초기값 제대로 설정해야 함.
# mn을 (35, None, None)으로 설정하면, 서로 다 다른 그림이 2개 들어올 경우 None이 그대로 남아있게 됨.

n = int(input())
pictures = [[list(str(input())) for _ in range(5)] for _ in range(n)]

mn = (36, None, None)
for i in range(n - 1):
    for j in range(i + 1, n):
        picture1, picture2 = pictures[i], pictures[j]
        diff = 35
        for y in range(5):
            for x in range(7):
                if picture1[y][x] == picture2[y][x]:
                    diff -= 1
        if diff < mn[0]:
            mn = diff, i, j
print(mn[1] + 1, mn[2] + 1)
