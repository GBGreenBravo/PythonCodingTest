# 20240930
# 20:15
# 1 / 1

# 14891_톱니바퀴

"""
풀이 시간: 20분 (14:32 - 14:52)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:32 - 14:36)


2. 구현 (14:36 - 14:42)
    이전 풀이에서는, list에 대해서 앞/뒤에 뒤/앞에서 뽑은 한 값을 추가해주는 식으로 rotate를 구현했으나,
    이 풀이에서는 deque의 rotate 함수를 활용하여 조금 더 간결하게 구현했습니다.


3. 디버깅 (14:42 - 14:52)
    왼쪽/오른쪽 의자의 6번/2번 인덱스 비교 시점이,
    의자 돌리기 전이 아니라, 의자 돌리고 난 후에 비교했던 코드를 구현했기에, 올바른 답변이 나오지 않았습니다.

    코드를 보며 디버깅다가, 구상한 그대로 작동함을 확인하고,
    문제를 다시 읽고 실수를 바로잡았습니다.
    앞으로도 이 부분을 더 확실히 인지한다면, 더욱 명료한 디버깅이 이뤄질 것으로 예상합니다.
"""

from collections import deque


def rotate_table(idx, rotate_d):
    if visited[idx]:
        return
    visited[idx] = 1

    if idx >= 1 and tables[idx - 1][2] != tables[idx][6]:
        rotate_table(idx - 1, -rotate_d)
    if idx <= 2 and tables[idx][2] != tables[idx + 1][6]:
        rotate_table(idx + 1, -rotate_d)

    tables[idx].rotate(rotate_d)


tables = [deque([int(inp) for inp in str(input())]) for _ in range(4)]
k = int(input())
for _ in range(k):
    n, d = map(int, input().split())
    visited = [0] * 4
    rotate_table(n - 1, d)

print(sum([tables[ii][0] * 2**ii for ii in range(4)]))
