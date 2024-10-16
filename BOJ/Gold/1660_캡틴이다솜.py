# 20241016
# 1 / 1

tetrahedrons = [1]
bottom = 1
length = 1
while tetrahedrons[-1] < 300000:
    length += 1
    bottom += length
    tetrahedrons.append(tetrahedrons[-1] + bottom)

n = int(input())
min_arr = [300000] * (n + 1)
for i in tetrahedrons:
    if i > n:
        break
    min_arr[i] = 1
for i in range(2, n + 1):
    value = min_arr[i]
    if value == 1:
        continue
    for j in tetrahedrons:
        if i - j < 0:
            break
        value = min(value, min_arr[i - j] + 1)
    min_arr[i] = value
print(min_arr[n])
