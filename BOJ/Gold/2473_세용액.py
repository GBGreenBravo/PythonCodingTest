# 20241205
# 1 / 1

N = int(input())
arr = sorted(map(int, input().split()))

minimum = abs(sum(arr[:3]))
answer = arr[:3]

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        now_value = arr[i] + arr[j]
        left, right = j + 1, N - 1
        if now_value + arr[left] > minimum:
            continue

        if abs(now_value + arr[left]) < minimum:
            minimum = abs(now_value + arr[left])
            answer = arr[i], arr[j], arr[left]
        if abs(now_value + arr[right]) < minimum:
            minimum = abs(now_value + arr[right])
            answer = arr[i], arr[j], arr[right]

        while left + 1 < right:
            mid = (left + right) // 2

            if now_value + arr[mid] < 0:
                left = mid
                if abs(now_value + arr[left]) < minimum:
                    minimum = abs(now_value + arr[left])
                    answer = arr[i], arr[j], arr[left]
            else:
                right = mid
                if abs(now_value + arr[right]) < minimum:
                    minimum = abs(now_value + arr[right])
                    answer = arr[i], arr[j], arr[right]

print(*answer)
