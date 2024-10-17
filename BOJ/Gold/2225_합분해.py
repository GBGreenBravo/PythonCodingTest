# 20241017
# 06:13
# 1 / 1

n, k = map(int, input().split())
arr = [1] * (n + 1)

for _ in range(k - 1):
    new_arr = [0] * (n + 1)
    for i in range(n + 1):
        value = 0
        for j in range(n + 1):
            if i - j < 0:
                break
            value += arr[i - j]
        new_arr[i] = value % 1_000_000_000
    arr = new_arr

print(arr[-1])
