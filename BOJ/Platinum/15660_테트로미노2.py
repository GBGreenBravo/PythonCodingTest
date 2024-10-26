# 20241026
# 2:45:32
# 1 / 5

# 주요 로직:
# 19개의 가능한 도형들의 모든 가능한 경우들을 results에 (해당 도형이 차지하는 수 합, 좌상단 좌표, 도형index)의 형식으로 담는다.
# 우선순위 큐에서 (도형이 차지하는 수 합) 내림차순으로 꺼내고,
# 가능한 경우(두 도형이 맞닿는 부분 없는 경우)에 대해 최대값 계산&갱신

"""
놓이는 2개의 테트로미노가 서로 한 변이라도 닿아야 하는 것으로 이해해서,
앞 2시간 소모하고 1번 시간초과 제출 했음.

93번째 줄의 break 작성 안 해서 1번 틀렸고,

5 5
8 8 8 8 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
2 2 2 2 1
위 케이스를 고려하지 못한 코드를 짜서,
while문 종료 조건을 변경 (while results and not max_answer: -> while results:)

그런데 95-96번째 줄 작성 안해서 시간초과 떴음.
"""

from heapq import heapify, heappop


def oob(y, x):
    return y < 0 or N <= y or x < 0 or M <= x


shapes = (((0, 0), (0, 1), (0, 2), (0, 3)),
          ((0, 0), (1, 0), (2, 0), (3, 0)),

          ((0, 0), (0, 1), (1, 0), (1, 1)),

          ((0, 0), (1, 0), (2, 0), (2, 1)),
          ((0, 0), (0, 1), (0, 2), (1, 0)),
          ((0, 0), (0, 1), (1, 1), (2, 1)),
          ((0, 2), (1, 0), (1, 1), (1, 2)),
          ((0, 1), (1, 1), (2, 0), (2, 1)),
          ((0, 0), (1, 0), (1, 1), (1, 2)),
          ((0, 0), (0, 1), (1, 0), (2, 0)),
          ((0, 0), (0, 1), (0, 2), (1, 2)),

          ((0, 0), (1, 0), (1, 1), (2, 1)),
          ((0, 1), (0, 2), (1, 0), (1, 1)),
          ((0, 1), (1, 0), (1, 1), (2, 0)),
          ((0, 0), (0, 1), (1, 1), (1, 2)),

          ((0, 0), (0, 1), (0, 2), (1, 1)),
          ((0, 1), (1, 0), (1, 1), (2, 1)),
          ((0, 1), (1, 0), (1, 1), (1, 2)),
          ((0, 0), (1, 0), (1, 1), (2, 0)))

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]

results = []  # 값, sy, sx, shape_index

for i in range(N):
    for j in range(M):
        for s_idx, shape in enumerate(shapes):
            now_value = 0

            for si, sj in shape:
                if oob(i + si, j + sj):
                    break
                now_value += area[i + si][j + sj]
            else:
                results.append((-now_value, i, j, s_idx))

heapify(results)

candidates = [heappop(results)]
max_answer = 0
while results:
    candidates.append(heappop(results))
    set1 = set()
    s_value, si, sj, s_type = candidates[-1]
    for di, dj in shapes[s_type]:
        set1.add((si + di, sj + dj))

    for j in range(len(candidates) - 1):
        # 현재 반복문 j의 수치와 합해도 최대값 이하면 => break
        if - s_value - candidates[j][0] <= max_answer:
            break

        set2 = set()
        sii, sjj = candidates[j][1], candidates[j][2]
        for dii, djj in shapes[candidates[j][-1]]:
            set2.add((sii + dii, sjj + djj))

        # 겹치는 좌표가 하나도 없다면 => 최대값 갱신
        if len(set1 | set2) == 8:
            max_answer = -candidates[-1][0] + -candidates[j][0]
            break

    # 최근에 추가한 값이 단일 최대값과 합해도, 현재 최대값보다 작으면 => break
    if -candidates[0][0] + -candidates[-1][0] <= max_answer:
        break

print(max_answer)
