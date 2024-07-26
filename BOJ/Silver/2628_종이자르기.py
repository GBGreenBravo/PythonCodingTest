# 20240726
# 18:15

m, n = map(int, input().split())
c = int(input())
cuts = [tuple(map(int, input().split())) for _ in range(c)]
paper_n = [1] + [0] * (n - 1) + [1]
paper_m = [1] + [0] * (m - 1) + [1]

for direction, index in cuts:
    if direction == 0:
        paper_n[index] = 1
    else:
        paper_m[index] = 1

mx = 0
length_n, length_m = 0, 0
for i in range(1, n + 1):
    length_n += 1
    for j in range(1, m + 1):
        length_m += 1
        if paper_n[i] == paper_m[j] == 1:
            mx = max(mx, length_n * length_m)
        if paper_m[j] == 1:
            length_m = 0
    if paper_n[i] == 1:
        length_n = 0

print(mx)
