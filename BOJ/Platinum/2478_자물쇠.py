# 20241129
# 1:13:59
# 1 / 4

"""
1 ~ N-1 번 오른쪽으로 민 배열을 test1()의 인자로 전달
test1()에서
    1을 기준으로, 1이 뒤집어야할 배열에 포함된 건지 먼저 판단해주고,
    그를 기준으로 뒤집을 범위(left, right)대로 뒤집고 test2()에 전달
test2()에서
    현재 배열에서 오른쪽밀기 1 ~ N-1 번 했을 때 오름차순 가능하면 정답 출력

아래는 실수했던 포인트들
- N을 10으로 오타냄
- test2()의 밀기에서 N번 밀기도 가능했기에, one_idx가 0이면 return시킴
"""

def test2(t1, s1, e1, arr2):
    one_idx = arr2.index(1)
    if not one_idx:
        return

    for v in range(1, N):
        if arr2[(one_idx + v) % N] != v + 1:
            return

    print(N - one_idx)
    print(s1 + 1, e1 + 1)
    print(t1)
    exit()


def test1(t1, arr1, one_idx):
    if (one_idx == 0 and arr1[1] != 2) or (one_idx == N - 1 and arr[-2] != N) or (one_idx not in (0, N - 1) and (arr1[one_idx - 1] != N or arr1[one_idx + 1] != 2)):
        # 1 포함 뒤집기
        if one_idx != N - 1 and arr1[one_idx + 1] == N:
            right = one_idx + 1
            while right < N - 1 and arr1[right + 1] == arr1[right] - 1:
                right += 1
        else:
            right = one_idx

        if right == one_idx:
            left = one_idx - 1
            while left > 0 and arr1[left - 1] == arr1[left] + 1:
                left -= 1
        elif one_idx == 0:
            left = 0
        elif arr1[one_idx - 1] + 1 == arr1[right]:
            left = one_idx
        else:
            left = one_idx - 1
            while left > 0 and arr1[left - 1] == arr1[left] + 1:
                left -= 1

        test2(t1, left, right, arr1[:left] + arr1[left:right + 1][::-1] + arr1[right + 1:])

    else:
        # 1 미포함 뒤집기
        # 왼쪽탐색
        left, right = None, None
        for idx in range(max(one_idx - 1, 0)):
            if not left and arr1[idx] > arr1[idx + 1]:
                left = idx
            if left and arr1[idx] > arr1[idx + 1]:
                right = idx + 1

        if right:
            test2(t1, left, right, arr1[:left] + arr1[left:right + 1][::-1] + arr1[right + 1:])

        # 오른쪽탐색
        left, right = None, None
        for idx in range(one_idx + 1, N - 1):
            if not left and arr1[idx] > arr1[idx + 1]:
                left = idx
            if left and arr1[idx] > arr1[idx + 1]:
                right = idx + 1
        if right:
            test2(t1, left, right, arr1[:left] + arr1[left:right + 1][::-1] + arr1[right + 1:])


N = int(input())
arr = list(map(int, input().split()))
found_one_idx = arr.index(1)
for i in range(1, N):
    test1(i, arr[N - i:] + arr[:N - i], (found_one_idx + i) % N)
