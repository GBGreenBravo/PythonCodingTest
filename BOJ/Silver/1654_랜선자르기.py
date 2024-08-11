# 20240811
# 36:24
# 1 / 6

# right의 제한을 min(lans)로 잡아서, 계속 틀렸던 문제.. max(lans)가 됐어야 함.

def cut(length):
    cnt = 0
    for lan in lans:
        cnt += lan // length
    return cnt


k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]

left, right = 1, max(lans)
while left < right:
    middle = (left + right) // 2 + 1
    cut_middle = cut(middle)
    if cut_middle > n:
        left = middle
    elif cut_middle == n:
        left = middle
    elif cut_middle < n:
        right = middle - 1

print(right)
