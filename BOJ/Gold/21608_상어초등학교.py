# 20240830
# 28:00
# 1 / 1

"""
풀이 시간: 28분 (09:34 ~ 10:02)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (09:34 - 09:43)
    문제를 읽으며, 이 문제는 N의 범위가 어떻게 주어지느냐에 따라,
    구현이 갈릴 것이라고 생각했습니다.

    N이 20보다 더 크게도 가능했다면,
    좋아하는 친구의 수는 4명으로 고정이므로, 그 주변 좌표들을 먼저 살펴보고, 다 불가능하다면 N*N 모두 탐색하려 했습니다.
    그러나 시간복잡도를 계산해본 결과, 넉넉하다는 결론이 나왔고,
    복잡하게 생각할 것 없이, 완전탐색으로 구현해주면 되겠다는 결론이 나왔습니다.

    그리고 문제에서 주어진 자리의 우선순위 배정방식을 다시 읽어보며,
    구상에 대한 확신을 갖고 구현을 시작했습니다.


2. 구현 & 중간 검증 (09:43 - 10:02)
    자리 배정의 우선순위에 대한 명확한 이해를 갖고 구현했기에,
    구현 시 큰 어려움은 없었습니다.

    1) 입력된 좋아하는 친구들이 잘 저장됐는지,
    2) answer를 계산하기 전에 배열에 우선순위의 순서대로 잘 배치가 됐는지,
    에 대한 중간 검증으로 구현 중 실수를 바로 발견해낼 수 있었습니다.
    변수를 잘못 할당하거나, for문 밖에 변수를 선언해야 할 것을 안에서 선언하는 자잘한 실수들이 있었지만,
    각 파트에 대한 구현 후, print()를 통해 눈으로 확인했기에 바로 수정할 수 있었습니다.
"""

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


# student_num의 번호를 가진 학생의 자리를 배정해주는 함수
def seat_student(student_num):
    near_favorites = 0      # 인접하고 좋아하는 학생의 최대 수
    candidates = []         # 위의 near_favorites를 만족하는 좌표들이 담길 배열
    for y in range(n):
        for x in range(n):
            if not area[y][x]:       # 배정 안된 자리만
                tmp_favorites = 0    # 현재 좌표의 인접&좋아하는 학생 수
                tmp_empties = 0      # 현재 좌표의 인접 빈 자리

                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    if oob(ny, nx):                               # 영역 밖이면 continue
                        continue
                    if not area[ny][nx]:                          # 빈 자리 +=1
                        tmp_empties += 1
                    elif area[ny][nx] in favorites[student_num]:  # 인접&좋아하는 학생 +=1
                        tmp_favorites += 1

                if near_favorites < tmp_favorites:                # 현재 인접&좋아하는 학생 수가 더 크다면, 이전 좌표들 모두 제거
                    near_favorites = tmp_favorites
                    candidates = [(-tmp_empties, y, x)]           # 후보로 담을 때는, 인접 빈 자리 수에 - 붙여서.
                elif near_favorites == tmp_favorites:             # 현재 인접&좋아하는 학생 수 동일하다면, 후보 좌표로 추가
                    candidates.append((-tmp_empties, y, x))

    candidates.sort()               # 각 요소는 (-인접빈자리수, 행, 열)로 돼있기에, sort()하면 문제에서 요구하는 우선순위대로 정렬된다.
    sy, sx = candidates[0][1:]      # 최우선순위의 좌표로 선정
    area[sy][sx] = student_num      # 자리 배정


n = int(input())
area = [[0] * n for _ in range(n)]

favorites = [set() for _ in range(n**2 + 1)]  # index번의 친구가 좋아하는 친구들의 번호를 set으로 담아둠
orders = []                                   # 자리 배정 순서
for _ in range(n**2):
    s, *fs = map(int, input().split())
    favorites[s].update(fs)
    orders.append(s)

# 순서대로 자리 배정
for now_student in orders:
    seat_student(now_student)

# 아래는 배정 종료된 배치도에 대해 만족도를 계산하는 코드
answer = 0
for i in range(n):
    for j in range(n):
        student_ij = area[i][j]

        favorite_cnt = 0
        for di, dj in direction:
            ni, nj = i + di, j + dj
            if oob(ni, nj):
                continue
            if area[ni][nj] in favorites[student_ij]:
                favorite_cnt += 1

        answer += 10 ** (favorite_cnt - 1) if favorite_cnt else 0

print(answer)
