# 20240724
# 07:31

# pypy 10억 연산이 약 1초인데, 해당 문제를 정렬 없이 비교한다면, t * 4 * 1억 번으로 시간 초과 남.
# 따라서 정렬을 활용하여 연산을 줄여줘야 한다.

t = int(input())
for _ in range(t):
    an, bn = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    len_b = len(b)

    a.sort(reverse=True)
    b.sort(reverse=True)

    cnt = 0
    pointer = 0
    for aa in a:
        while pointer < len_b:
            if b[pointer] < aa:
                cnt += len_b - pointer
                break
            else:
                pointer += 1

    print(cnt)


# b만 정렬하여 이분탐색으로 푸는 방법
"""
t = int(input())
for _ in range(t):
    an, bn = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()

    cnt = 0
    for aa in a:
        start, end = 0, len(b) - 1
        ans = -1
        while start <= end:
            mid = (start + end) // 2
            if aa <= b[mid]:
                end = mid - 1
            elif aa > b[mid]:
                ans = mid
                start = mid + 1
        cnt += ans + 1

    print(cnt)
"""