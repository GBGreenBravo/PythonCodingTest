# 20241004
# 30:55
# 1 / 1

# 23291_어항정리

"""
풀이 시간: 31분 (16:58 - 17:29)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (16:58 - 17:06)
    이전에 구상했던 방식 그대로 구상&구현 했습니다.

    다 풀고, 다른 분들의 풀이가 기억이 나서,
    3회차에 이 문제를 푼다면 빈칸처리(0) 없이 구현해볼 생각입니다.


2. 구현 (17:06 - 17:29)
    리스트 컴프리헨션을 사용해서 코드가 더 짧아진 것 말고는, 기존 구현과 동일합니다.

    그리고 이전 풀이에서, while문의 조건에서 index()를 활용하다가
    실수할 뻔한 부분이 기억나서, index()함수를 쓸 때 주의하며 구현했습니다.

    그리고 지금 보니, 중복 로직의 함수화 과정에서,
    전역변수명만으로 쓰기로 한 i,j가 함수 내 변수명으로 쓰인 것이 보입니다.
    리팩토링 과정에서 사소한 변수명도 기존 컨벤션을 따라야, 실수가 없을 것으로 생각하여 이 부분 주의해야겠습니다.


3. 디버깅 (-)
"""

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def press():
    global area

    changed = [[0] * len(area[0]) for _ in range(len(area))]
    i_limit = len(area)
    j_limit = len(area[0])
    for i in range(i_limit):
        for j in range(j_limit):
            if not area[i][j]:
                continue

            for di, dj in direction:
                ni, nj = i + di, j + dj
                if ni < 0 or i_limit <= ni or nj < 0 or j_limit <= nj:
                    continue
                if not area[ni][nj] or area[i][j] <= area[ni][nj]:
                    continue

                value = (area[i][j] - area[ni][nj]) // 5
                changed[i][j] -= value
                changed[ni][nj] += value
    for i in range(i_limit):
        for j in range(j_limit):
            if changed[i][j]:
                area[i][j] += changed[i][j]

    new_area = []
    for col in range(j_limit):
        for row in range(i_limit - 1, -1, -1):
            if not area[row][col]:
                break
            new_area.append(area[row][col])
    area = new_area


n, k = map(int, input().split())
area = list(map(int, input().split()))

turn = 0
while max(area) - min(area) > k:
    turn += 1

    min_area = min(area)
    for i in range(len(area)):
        if area[i] == min_area:
            area[i] += 1

    area = [[area[0]] + [0] * (len(area) - 2), area[1:]]
    while 0 in area[0] and len(area) <= len(area[-1]) - area[0].index(0):
        rotating_height, rotating_width = len(area), area[0].index(0)
        below_length = len(area[-1]) - area[0].index(0)
        rotating = [area[row][:rotating_width] for row in range(rotating_height)]
        rotating = [list(row)[::-1] for row in zip(*rotating)]
        rotating = [row + [0] * (below_length - rotating_height) for row in rotating]
        area = rotating + [area[-1][rotating_width:]]

    press()

    area = [area[:n // 2][::-1]] + [area[n // 2:]]
    rotating = [area[row][:n // 4] for row in range(2)]
    rotating = [list(row)[::-1] for row in reversed(rotating)]
    area = rotating + [area[row][n // 4:] for row in range(2)]

    press()

print(turn)
