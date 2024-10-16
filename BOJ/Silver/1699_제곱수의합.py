# 20241016
# 1 / 1

n = int(input())
min_arr = [n] * (n + 1)
squares = []
i = 1
while i**2 <= n:
    squares.append(i**2)
    i += 1

for i in squares:
    min_arr[i] = 1

for i in range(2, n + 1):
    for j in squares:
        if i - j < 1:
            break
        min_arr[i] = min(min_arr[i], min_arr[i - j] + 1)
print(min_arr[-1])