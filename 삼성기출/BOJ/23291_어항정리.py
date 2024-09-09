# 20240909
# 43:00
# 1 / 1

"""
풀이 시간: 43분 (15:15 ~ 15:58)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:15 - 15:27)
    문제 지문이 길고 요구사항이 많았기에, 해당 작업들을 명료하게 메모하는 것이 중요했습니다.
    다행히 그림을 통한 상세한 설명이 있었기에, 문제 이해에는 어려움이 없었습니다.

    어항의 공중부양/쌓기 수행에 대해서는,
    그 결과를 2차원 배열로 저장하면 되겠다고 생각했습니다.
    그리고 어항의 물고기 수가 0이 될 가능성이 없었기에, 2차원배열의 빈 공간은 0으로 채우기로 생각했습니다.


2. 구현 (15:27 - 15:52)
    메모해둔, 1번의 어항 정리에 대한 수행 순서들에 대해 차례로 구현해줬습니다.
    (수행 1) 물고기 최소값을 가진 어항들 += 1
    (수행 2-1) 맨 왼쪽의 어항을, 위로 쌓기
    (수행 2-2) 바닥면 충분할 때까지, 공중부양 & 90도 시계방향 회전 & 쌓기
    (수행 3) 어항 물고기 수 차이 조절
    (수행 4) 바닥에 어항 일렬로 놓기
    (수행 5) 다시 공중부양 & 180도 회전 & 쌓기 => 2회 수행
    (수행 6-1) 어항 물고기 수 차이 조절
    (수행 6-2) 바닥에 어항 일렬로 놓기

    위의 각 수행을 구현 완료할 때마다를 체크포인트로 설정하여 중간 점검을 했습니다.


3. 검증 (15:52 - 15:58)
    체크포인트들에서의 중간 점검을 통해, 이상이 없음을 확인했으나, 테스트케이스 검증에서 한가지 오류가 있음을 확인했습니다.
    (수행 2-2)의 '바닥면 충분할 때까지'에서 while문의 종료조건으로
    while len(area) <= len(area[-1]) - area[0].index(0):
    을 활용했는데,
    어항의 맨 윗줄(area[0])에 0이 없을 수도 있음을 간과했습니다. (print 디버깅을 통해 찾아냈습니다.)
    따라서 종료조건에 0 in area[0]을 추가해줬고, 정상 수행을 확인했습니다.

    테스트케이스에 해당 경우가 있었기에, 그저 운으로 해당 에러를 발견했습니다.
    다음에는 테스트케이스 검증 전에 이러한 이슈를 발견할 수 있도록,
    .index()를 쓰는 경우, 해당 값이 없으면 error를 발생시키는 것을 확실히 인지하고,
    index 함수와 같이 에러를 반환하는 함수를 활용할 때는,
    에러를 반환하는 경우가 있는지를 구현/검증 단계에서 분명하게 확인해야 함을 성찰할 수 있었습니다.
"""

direction = ((0, 1), (0, -1), (1, 0), (-1, 0),)

n, k = map(int, input().split())
area = list(map(int, input().split()))  # 어항의 상태를 표현하는 배열

time = 0  # 출력할 정리 횟수
while True:
    min_fish = min(area)
    max_fish = max(area)
    if max_fish - min_fish <= k:  # 최대/최소 차이가 k이하라면 종료
        break
    time += 1  # 정리 횟수 += 1

    # (수행 1) 물고기 최소값을 가진 어항들 += 1
    for i in range(n):
        if area[i] == min_fish:
            area[i] += 1

    # (수행 2-1) 맨 왼쪽의 어항을, 위로 쌓기
    area = [[area[0]] + [0] * (n - 2), area[1:]]

    # (수행 2-2) 바닥면 충분할 때까지, 공중부양 & 90도 시계방향 회전 & 쌓기
    while 0 in area[0] and len(area) <= len(area[-1]) - area[0].index(0):
        upper_width = area[0].index(0)
        upper = [area[row][:upper_width] for row in range(len(area))]
        lower = area[-1][upper_width:]
        upper = [list(row[::-1]) for row in zip(*upper)]

        area = []
        for u in range(len(upper)):
            area.append(upper[u] + [0] * (len(lower) - len(upper[0])))
        area.append(lower)

    # (수행 3) 어항 물고기 수 차이 조절
    h = len(area)
    w = len(area[0])
    moved_fishes = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if area[i][j]:
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    if ni < 0 or h <= ni or nj < 0 or w <= nj:
                        continue
                    if not area[ni][nj] or area[i][j] <= area[ni][nj]:
                        continue
                    diff = (area[i][j] - area[ni][nj]) // 5
                    if diff:
                        moved_fishes[i][j] -= diff
                        moved_fishes[ni][nj] += diff
    for i in range(h):
        for j in range(w):
            area[i][j] += moved_fishes[i][j]

    # (수행 4) 바닥에 어항 일렬로 놓기
    new_area = []
    for j in range(w):
        for i in range(h - 1, -1, -1):
            if not area[i][j]:
                break
            new_area.append(area[i][j])

    # (수행 5) 다시 공중부양 & 180도 회전 & 쌓기 => 2회 수행
    area = [new_area[:n // 2][::-1], new_area[n // 2:]]

    upper = [area[row][:n // 4] for row in range(2)]
    upper = [list(row[::-1]) for row in reversed(upper)]
    lower = [area[row][n // 4:] for row in range(2)]
    area = upper + lower

    # (수행 6-1) 어항 물고기 수 차이 조절
    h = len(area)
    w = len(area[0])
    moved_fishes = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if area[i][j]:
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    if ni < 0 or h <= ni or nj < 0 or w <= nj:
                        continue
                    if not area[ni][nj] or area[i][j] <= area[ni][nj]:
                        continue
                    diff = (area[i][j] - area[ni][nj]) // 5
                    if diff:
                        moved_fishes[i][j] -= diff
                        moved_fishes[ni][nj] += diff
    for i in range(h):
        for j in range(w):
            area[i][j] += moved_fishes[i][j]

    # (수행 6-2) 바닥에 어항 일렬로 놓기
    new_area = []
    for j in range(w):
        for i in range(h - 1, -1, -1):
            if not area[i][j]:
                break
            new_area.append(area[i][j])
    area = new_area

print(time)


# 중복되는 코드 (어항 물고기 수 차이 조절 & 바닥에 어항 일렬로 놓기)
# 함수화한 버전
"""
direction = ((0, 1), (0, -1), (1, 0), (-1, 0),)


# 어항 물고기 수 차이 조절 & 바닥에 어항 일렬로 놓기
def adjust_fish_diff_and_arrange_in_a_line():
    global area

    # 어항 물고기 수 차이 조절
    h = len(area)
    w = len(area[0])
    moved_fishes = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if area[i][j]:
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    if ni < 0 or h <= ni or nj < 0 or w <= nj:
                        continue
                    if not area[ni][nj] or area[i][j] <= area[ni][nj]:
                        continue
                    diff = (area[i][j] - area[ni][nj]) // 5
                    if diff:
                        moved_fishes[i][j] -= diff
                        moved_fishes[ni][nj] += diff
    for i in range(h):
        for j in range(w):
            area[i][j] += moved_fishes[i][j]

    # 바닥에 어항 일렬로 놓기
    new_area = []
    for j in range(w):
        for i in range(h - 1, -1, -1):
            if not area[i][j]:
                break
            new_area.append(area[i][j])
    area = new_area


n, k = map(int, input().split())
area = list(map(int, input().split()))  # 어항의 상태를 표현하는 배열

time = 0  # 출력할 정리 횟수
while True:
    min_fish = min(area)
    max_fish = max(area)
    if max_fish - min_fish <= k:  # 최대/최소 차이가 k이하라면 종료
        break
    time += 1  # 정리 횟수 += 1

    # (수행 1) 물고기 최소값을 가진 어항들 += 1
    for i in range(n):
        if area[i] == min_fish:
            area[i] += 1

    # (수행 2-1) 맨 왼쪽의 어항을, 위로 쌓기
    area = [[area[0]] + [0] * (n - 2), area[1:]]

    # (수행 2-2) 바닥면 충분할 때까지, 공중부양 & 90도 시계방향 회전 & 쌓기
    while 0 in area[0] and len(area) <= len(area[-1]) - area[0].index(0):
        upper_width = area[0].index(0)
        upper = [area[row][:upper_width] for row in range(len(area))]
        lower = area[-1][upper_width:]
        upper = [list(row[::-1]) for row in zip(*upper)]

        area = []
        for u in range(len(upper)):
            area.append(upper[u] + [0] * (len(lower) - len(upper[0])))
        area.append(lower)

    # (수행 3) 어항 물고기 수 차이 조절
    # (수행 4) 바닥에 어항 일렬로 놓기
    adjust_fish_diff_and_arrange_in_a_line()


    # (수행 5) 다시 공중부양 & 180도 회전 & 쌓기 => 2회 수행
    area = [area[:n // 2][::-1], area[n // 2:]]

    upper = [area[row][:n // 4] for row in range(2)]
    upper = [list(row[::-1]) for row in reversed(upper)]
    lower = [area[row][n // 4:] for row in range(2)]
    area = upper + lower

    # (수행 6-1) 어항 물고기 수 차이 조절
    # (수행 6-2) 바닥에 어항 일렬로 놓기
    adjust_fish_diff_and_arrange_in_a_line()

print(time)
"""