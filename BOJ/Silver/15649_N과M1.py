# 20240806
# 07:35
# 1 / 1


def solve(num, next_arr):  # 현재 탐색중인 number, 다음으로 탐색할 number 리스트
    global now_arr

    if num == m:  # 선발한 수의 개수가 m개면 print
        print(*now_arr)
        return
    for i in next_arr:  # 다음으로 탐색할 리스트에서
        now_arr.append(i)
        solve(num + 1, [j for j in next_arr if j != i])  # i를 제외하고 재귀
        del now_arr[-1]


n, m = map(int, input().split())
now_arr = []  # 현재 탐색중인 배열을 저장할 리스트
solve(0, [i for i in range(1, n + 1)])
