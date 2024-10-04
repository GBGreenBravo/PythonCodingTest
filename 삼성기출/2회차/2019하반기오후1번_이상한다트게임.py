# 20241002
# 32:22
# 1 / 2

# 17822_원판돌리기

"""
풀이 시간: 32분 (14:16 - 14:48)
풀이 시도: 1 / 2


1. 문제 정독 & 풀이 구상 (14:16 - 14:23)


2. 구현 (14:23 - 14:35)
    이전 풀이와 거의 다 유사합니다.
    다만, 이번 풀이에서 같은 값을 지우는 과정에서 단순하게 구현하면 될 것을 초반에 복잡하게 구현했다고 생각합니다.
    따라서, 시간/메모리 복잡도 크게 생각하지 않고 단순하지만 정확한 구현에 더 집중하기로 했습니다.


3. 디버깅 (14:35 - 14:37)


4. 틀렸습니다 (14:38 - 14:48)
    중간에 같은 수를 지우는 과정에서 놓친 부분이 있었겠다고 예상하고, 그 부분 위주로 코드를 봤습니다.
    print를 통해 확인해도 이상이 없었기에 문제를 다시 봤지만, 오해한 부분도 없었습니다.
    코드 전체를 다시 보며, 각 모듈을 print로 과정을 확인하니,
    0(삭제처리)인 부분도 평균보다 작아서 1로 바뀌는 실수가 있었습니다.

    실수가 있을 것으로 예상하는 부분 보고,
    문제 다시 읽고,
    전체 코드 정독 & 각 과정별 print 디버깅,

    위 단계를 거치면, 간단한 실수들은 다 잡아낼 수 있을 것으로 생각합니다.
"""

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(yy):
    return yy < 0 or n <= yy


n, m, q = map(int, input().split())
area = [deque(map(int, input().split())) for _ in range(n)]

for _ in range(q):
    xx, dd, kk = map(int, input().split())
    clockwise = 1 if not dd else -1
    for xxx in range(xx, n + 1, xx):
        area[xxx - 1].rotate(clockwise * kk)

    erasing_happened = False
    for i in range(n):
        for j in range(m):
            if area[i][j]:
                queue = deque()
                queue.append((i, j))

                criteria = area[i][j]

                while queue:
                    y, x = queue.popleft()
                    for dy, dx in direction:
                        ny, nx = y + dy, (x + dx) % m
                        if oob(ny) or area[ny][nx] != criteria:
                            continue
                        area[ny][nx] = 0
                        queue.append((ny, nx))
                        erasing_happened = True

    if erasing_happened:
        continue

    value_cnt = 0
    value_sum = 0
    for i in range(n):
        for j in range(m):
            if area[i][j]:
                value_cnt += 1
                value_sum += area[i][j]

    if not value_cnt:
        break

    average = value_sum // value_cnt
    for i in range(n):
        for j in range(m):
            now_value = area[i][j]
            if not now_value:
                continue
            if now_value > average:
                area[i][j] = now_value - 1
            elif now_value < average:
                area[i][j] = now_value + 1

print(sum(map(sum, area)))
