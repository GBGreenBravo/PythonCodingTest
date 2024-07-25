# 20240725
# 56:05

# 그림의 문 위치를 보고, 2->3 과 4->5가 안 겹친다고 생각했는데
# 겹치는 판정이었음.

import sys
sys.stdin = open("../input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    info = [list(map(int, input().split())) for _ in range(n)]
    cnt = [0] * 201
    for i in info:
        a, b = min(i[0], i[1]), max(i[0], i[1])
        a, b = (a+1)//2, (b+1)//2
        for j in range(a, b+1):
            cnt[j] += 1
    print(f"#{test_case} {max(cnt)}")

