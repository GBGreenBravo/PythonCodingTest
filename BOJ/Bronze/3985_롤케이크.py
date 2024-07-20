# 20240719

l = int(input())
n = int(input())

cakes = [0] * l
max_anticipation = 0
max_anticipater = 0
for i in range(1, n + 1):
    start, end = map(int, input().split())

    if end - start > max_anticipation:
        max_anticipation = end - start
        max_anticipater = i

    for j in range(start - 1, end):
        if cakes[j] != 0:
            pass
        else:
            cakes[j] = i

max_count = 0
max_person = 0
for i in range(1, n + 1):
    now_count = cakes.count(i)
    if now_count > max_count:
        max_count = now_count
        max_person = i

print(max_anticipater)
print(max_person)
