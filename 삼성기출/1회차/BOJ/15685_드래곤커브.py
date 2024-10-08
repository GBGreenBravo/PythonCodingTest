# 20240829
#
# 1 / 2

"""
풀이 시간: 1시간 37분 (15:00 ~ 15:45) (16:13 ~ 17:05)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:00 - 15:06)
    문제에서, 네 변이 아닌 네 꼭짓점이 드래곤커브 일부이고, 겹치기가 가능하다고 했으므로
    101*101 배열에서 드래곤 커브가 지나는 좌표들을 기록하면 된다고 생각했습니다.

    그리고 한 좌표를 기준으로, 다른 좌표들을 90도 시계방향 회전시키는 건,
    좌표간 계산으로 가능하다고 판단했습니다.


2. 구현 (15:06 - 15:24)
    0세대 드래곤 커브부터 시작해서 g세대 드래곤 커브까지
    rotate_and_save() 함수를 통해 이전의 드래곤 커브 좌표들을 90도 돌려줬습니다.

    그리고 rotated_index() 함수를 구현하는 과정에서는
    종이에 좌표평면을 그리고 하나씩 체크하며, 해당 계산이 맞는지 검증했습니다.


3. 검증 및 재구상 (15:24 - 15:45)
    맞다고 생각했던 풀이가 틀렸기에,
    1) 회전 시 좌표로 접근하는 게 틀렸는지
    2) 이전 드래곤 커브 좌표를 회전하는 순서가 중요한지
    3) 0세대 드래곤 상태가 제대로 반영이 안 됐는지
    4) 끝점의 방문 체크가 안 되었는지
    위의 경우들에 대한 검증을 해봤지만 틀린 점이 보이지 않았습니다.

    print()를 통해 단계별 변화를 눈으로 봐도, 이상한 점이 보이지 않았기에,
    다른 문제를 풀고, 리프레쉬된 상태에서 다시 문제를 풀어보기로 했습니다.


4. 재시도 및 실수 발견 (16:13 - 17:05)
    틀렸던 코드를 다시 보기보다, 새롭게 시작하는 마음가짐으로 문제를 다시 읽었습니다.
    이전에 해줬던 검증을 다시 한번 해봤고, 문제를 멏번 더 반복하며 읽으며, 놓친 사항이 없는지 확인했습니다.
    기존 코드를 복사하여, 새로운 코드를 짜봤으나 기본 구상에는 차이가 없어서, 다른 구상을 떠올리려고도 노력했습니다.

    그렇게 코드를 보다가 사고의 전환을 위해 문제를 읽다가 하던 와중에,
    다행히도 실수를 발견해낼 수 있었습니다.
    실수는 (99, 99)까지 기준으로 하기 위해서는 range(100)을 썼어야 하는데, range(99)로 썼던 것입니다.

    이 실수를 통해, 최대값/최소값에 대한 테스트케이스 시간복잡도 체크뿐만 아니라,
    첫 행/열, 마지막 행/열에서의 동작도 체크해줘야 함을, 구현 문제 점검사항에 추가할 수 있었습니다.

    그리고 이렇게 막히는 경우에, 같은 풀이 방식이라고 하더라도 다시 처음부터 코드를 짜야겠다고 결심했습니다.
    머릿속에 있는 구상을 다시 새로운 코드로 한줄한줄 타이핑하는 과정에서
    사소한 변수/수치의 이유까지도 재고를 해볼 수 있지 않을까 생각합니다.
"""


# (cy, cx)를 기준으로 (y, x)를 90도 시계방향 회전시킨 좌표를 반환하는 함수
def rotated_index(y, x, cy, cx):
    return cy + (x - cx), cx - (y - cy)


# 인자의 좌표를 끝점으로 하여, 새로운 드래곤 커브를 기록하는 함수
def rotate_and_save(center_y, center_x):
    # 새롭게 추가되는 드래곤 커프 좌표들 (= 이전의 드래곤 커브에서 시계방향 90도 회전하는 좌표들)
    added_indexes = []

    # 기존 좌표들 하나하나씩, 회전시키고 1로 저장
    for iy, ix in indexes:
        ny, nx = rotated_index(iy, ix, center_y, center_x)
        area[ny][nx] = 1
        added_indexes.append((ny, nx))

    # 새로운 드래곤 커브 좌표 추가
    indexes.update(added_indexes)

    # 현재 연장된 드래곤 커브의 끝점이 되는, 시작좌표의 기준좌표로부터의 90도 회전 좌표
    return rotated_index(sy, sx, center_y, center_x)


direction = ((0, 1), (-1, 0), (0, -1), (1, 0))  # 우하좌상

area = [[0] * 101 for _ in range(101)]  # 좌표평면 (0, 0)부터 (100, 100)까지 있으므로.

n = int(input())
for i in range(n):
    sx, sy, d, g = map(int, input().split())

    ey, ex = sy + direction[d][0], sx + direction[d][1]  # 0세대 드래곤 커브의 끝점
    area[sy][sx], area[ey][ex] = 1, 1  # 0세대 드래곤 커브 저장

    indexes = set()  # 현재 드래곤 커브의 모든 좌표가 담길 set()
    indexes.add((sy, sx))
    indexes.add((ey, ex))

    for _ in range(g):  # g번 동안 드래곤 커브 연장
        ey, ex = rotate_and_save(ey, ex)

answer_cnt = 0
for i in range(100):  # (99, 99) 기준까지 점검해야 하므로, range(99)가 아닌 range(100)..
    for j in range(100):
        if area[i][j] and area[i + 1][j] and area[i][j + 1] and area[i + 1][j + 1]:
            answer_cnt += 1
print(answer_cnt)
