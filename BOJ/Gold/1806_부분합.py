# 20241204
# 1 / 1

N, S = map(int, input().split())
nums = list(map(int, input().split()))
answer = N + 1
l, r, now = 0, 0, nums[0]
while True:
    if now < S:
        r += 1
        if r == N:
            break
        now += nums[r]
    else:
        answer = min(answer, r - l + 1)
        if l == r:
            r += 1
            if r == N:
                break
            now += nums[r]
        else:
            if l == N:
                break
            now -= nums[l]
            l += 1
print(0 if answer == N + 1 else answer)
