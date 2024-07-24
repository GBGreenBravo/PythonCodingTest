# 20240724
# 36:25

n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
mx_lst = [0] * n
for i in range(n):
    tmp_mx = 0
    for j in range(i):
        if arr[j] > arr[i]:
            tmp_mx = max(tmp_mx, mx_lst[j])
    mx_lst[i] = arr[i] + tmp_mx
print(max(mx_lst))


# 뒤집을 필요 없이 앞에서부터 구해도 됨.
"""
N = int(input())
arr = list(map(int, input().split()))
DP = arr[:]

ans = 0

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            DP[i] = max(DP[j] + arr[i], DP[i])

print(max(DP))
"""