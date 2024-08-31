# 20240828
# 30:00
# 1 / 1

"""
풀이 시간: 30분 (15:00 ~ 15:30)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:00 - 15:10)
    어떤 문제를 먼저 풀지 선정할 때 테스트케이스를 보고,
    선호하는 문제(문제 설명이 한 단계씩 그림으로 표시돼 있는 지문)였기에, 먼저 풀기로 결정했습니다.

    문제를 읽으며, 다른 부분에 대한 구현은 바로 떠올랐으나,
    미세먼지의 동시 확산에 대한 부분을 어떻게 처리해줘야 할지 바로 떠오르지 않았습니다.
    일단은 문제 지문을 끝까지 정독하고 제 이해대로 세부사항들을 메모했습니다.

    지문의 3*3배열의 예시를 손코딩하며, 미세먼지 동시 확산에 대한 이해를 명확히 할 수 있었고,
    그에 따라, 미세먼지를 동시에 추가해줄 배열을 따로 두기로 구상할 수 있었습니다.


2. 구현 (15:10 - 15:26)
    미세먼지를 동시에 확산시키는 spread_dusts() 함수에서는,
    미세먼지 확산으로 인한 추가량을 저장할 배열을 따로 두고,
    마지막에 동시에 추가를 해줬습니다.

    공기청정기 바람 순환되는 circulate() 함수에서 사용할,
    공기청정기 바람이 지나는 좌표는 항상 고정되는 것이기에,
    그에 대한 배열을 함수 밖에서 먼저 구현했습니다.


3. 검증 (15:26 - 15:30)
    미세먼지 동시 확산 함수 spread_dusts()를 먼저 작성했고,
    위 함수 호출 1회에 따른 변화를 print 디버깅을 통해 확인했습니다.

    그리고 공기청정기 바람이 순환하는 좌표 배열인,
    top_reversed와 bottom_reversed에 대해, 각각 for문 4번을 통해 좌표를 저장해준 부분이 있습니다.
    이에 대해 한 좌표라도 틀리면 안됐기에 해당 코드를 구현하고,
    테스트케이스의 입력을 print()한 출력과 비교하며 검증해줬습니다.
"""

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or r <= y or x < 0 or c <= x


# 미세먼지가 동시에 확산되는 함수
def spread_dusts():
    added_dusts = [[0] * c for _ in range(r)]  # 미세먼지 확산으로 인한 추가량을 저장할 배열

    for y in range(r):
        for x in range(c):
            if area[y][x] and area[y][x] != -1:  # 미세먼지 좌표라면
                spread_cnt = 0  # 현재 좌표에서 확산되는 횟수
                dust_value = area[y][x] // 5  # 확산할 미세먼지 양
                if not dust_value:  # area[y][x] 가 4이하라서, 확산 양이 0이면, continue
                    continue

                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    if oob(ny, nx) or area[ny][nx] == -1:
                        continue
                    added_dusts[ny][nx] += dust_value  # 나중에 한번에 추가할 미세먼지로
                    spread_cnt += 1

                area[y][x] -= dust_value * spread_cnt  # 현재 미세먼지 좌표로부터 확산되는 양 만큼 빼주기

    for y in range(r):
        for x in range(c):
            area[y][x] += added_dusts[y][x]  # 미세먼지 확산으로 인한 추가량 동시에 반영


# 공기청정기 바람이 순환하는 함수
def circulate():
    for ii in range(len(top_reversed) - 1):  # 위쪽 공기청정기 바람방향 반대로
        y, x = top_reversed[ii]
        by, bx = top_reversed[ii + 1]
        area[y][x] = area[by][bx]  # 이전좌표의 미세먼지 그대로 가져오기
    area[top_reversed[-1][0]][top_reversed[-1][1]] = 0  # 공기청정기 바로 다음 좌표는, 미세먼지 정화되어 0으로

    # 아래쪽 공기청정기도, 위와 같이 순환
    for ii in range(len(bottom_reversed) - 1):
        y, x = bottom_reversed[ii]
        by, bx = bottom_reversed[ii + 1]
        area[y][x] = area[by][bx]
    area[bottom_reversed[-1][0]][bottom_reversed[-1][1]] = 0


r, c, t = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(r)]

for i in range(r):
    if area[i][0] == -1:
        top, bottom = i, i + 1  # 위/아래 공기청정기 행 index
        break

# 위쪽 공기청정기 바람이 방문하는 좌표들의 reversed
top_reversed = []
for i in range(top - 1, -1, -1):
    top_reversed.append((i, 0))
for i in range(1, c - 1):
    top_reversed.append((0, i))
for i in range(top + 1):
    top_reversed.append((i, c - 1))
for i in range(c - 2, 0, -1):
    top_reversed.append((top, i))

# 아래쪽 공기청정기 바람이 방문하는 좌표들의 reversed
bottom_reversed = []
for i in range(bottom + 1, r):
    bottom_reversed.append((i, 0))
for i in range(1, c - 1):
    bottom_reversed.append((r - 1, i))
for i in range(r - 1, bottom - 1, -1):
    bottom_reversed.append((i, c - 1))
for i in range(c - 2, 0, -1):
    bottom_reversed.append((bottom, i))

for _ in range(t):
    spread_dusts()  # 미세먼지 동시 확산
    circulate()  # 공기청정기 바람 순환

# area의 총합은, 미세먼지 총합 + 공기청정기(-1) 2개 이기에, + 2
print(sum(map(sum, area)) + 2)
