# 20241209
# 1 / 2

N = int(input())
arr = list(map(int, input().split()))

minimum = abs(arr[0] + arr[-1])
answer = arr[0], arr[-1]

for i in range(N - 1):
    now = arr[i]
    left, right = i + 1, N - 1

    if minimum > abs(now + arr[left]):
        minimum = abs(now + arr[left])
        answer = now, arr[left]

    if minimum > abs(now + arr[right]):
        minimum = abs(now + arr[right])
        answer = now, arr[right]

    while left + 1 < right:
        mid = (left + right) // 2
        mid_v = now + arr[mid]

        l_v, r_v = now + arr[left], now + arr[right]

        if mid_v >= 0:
            right = mid
            if minimum > abs(now + arr[right]):
                minimum = abs(now + arr[right])
                answer = now, arr[right]
        else:
            left = mid
            if minimum > abs(now + arr[left]):
                minimum = abs(now + arr[left])
                answer = now, arr[left]

print(*answer)
