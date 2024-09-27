# 20240920
# 1:17:00
# 1 / 1

"""
풀이 시간: 1시간 17분 (15:00 - 16:17)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:00 - 15:14)
    백준 기출에서 상어 냄새를 남겼던 문제와 마찬가지로,
    특정 좌표에 대한 제한이 특정 기간동안 남아있는 유형의 문제임을 알았습니다.

    문제를 읽으며 궁금했던 건,
    벽이 있는 칸에 제초제를 뿌리는 것이 가능한지였습니다.
    (고민 후, '벽 있는 칸'도 '나무 없는 칸'에 포함되는 개념이므로 가능하다고 판단했습니다.)


2. 구현 (15:14 - 15:36)
    문제의 그림 설명들에 대해,
    독립적인 모듈을 함수로 완성한 뒤, 매번 print 체크포인트를 뒀습니다.


3. 디버깅 (15:36 - 15:38)
    짧은 시간 동안 응급처치 print를 통해, 아래의 두 실수를 잡아낼 수 있었습니다.
    - max_cnt를 갱신해주지 않은 것
    - 살충제 전파 시, 전파 시작 좌표의 나무 죽이지 않은 것


4. 검증 (15:38 - 16:17)
    검증 단계에서도 2개의 실수를 잡아낼 수 있었습니다.
    - (1)단계 -> c를 m으로 잘못 쓴 것 (15:42)
    - (2)단계 -> kill_trees함수에서, 나무 없는 칸에서도 전파가 발생했던 것 (15:50)

    O (1) 주어진 테스트케이스로 검증
    O (2) 메모 vs. 코드
    O (3) (머릿속 환기 후) 문제 재정독
    O (4) 커스텀 테스트케이스 검증
    O (5) 철저한 코드 검증
    O (6) 오답노트 활용
    X (7) 다양한 구상에 따른, 다른 구현
"""

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))
diagonal_direction = ((-1, -1), (-1, 1), (1, 1), (1, -1))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


# 나무들 동시 성장하는 함수
def trees_grow():
    # (나무 존재 유무만 파악하므로) 동시성 보장을 위한 배열 필요 X

    for y in range(n):
        for x in range(n):
            # 나무 있으면
            if area[y][x] > 0:
                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    # 인접칸에 나무 있으면 +=1
                    if not oob(ny, nx) and area[ny][nx] > 0:
                        area[y][x] += 1


# 나무들 동시 번식하는 함수
def trees_spread():
    # (동시성 보장을 위해) 칸별 추가되는 나무 배열
    added_trees = [[0] * n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            # 나무 있으면
            if area[y][x] > 0:
                possibles = []  # (벽X/나무X/제초제X)의 인접칸이 담길 배열

                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    # 영역내 and 벽X&나무X and 제초제X
                    if not oob(ny, nx) and not area[ny][nx] and not pesticides[ny][nx]:
                        possibles.append((ny, nx))

                # ZeroDivisionError 방지
                if not possibles:
                    continue

                # 추가되는 값 계산 & 추가
                added_value = area[y][x] // len(possibles)
                for py, px in possibles:
                    added_trees[py][px] += added_value

    # 추가되는 나무 동시 반영
    for y in range(n):
        for x in range(n):
            if added_trees[y][x]:
                area[y][x] += added_trees[y][x]


# 현재 좌표에 제초제 전파시킬 때, 예상되는 죽는 나무 수 반환하는 함수
def cal_dead_trees(sy, sx):
    # 초기값 (나무 없는 경우는 입력으로 안 들어옴)
    cnt = area[sy][sx]

    for dy, dx in diagonal_direction:  # 대각선 4방향에 대해
        y, x = sy + dy, sx + dx
        for _ in range(k):  # k범위 만큼
            if oob(y, x):  # 영역 밖 -> break
                break

            if area[y][x] > 0:  # 나무 있으면 -> cnt+=나무수 & 현재방향으로 1칸 더
                cnt += area[y][x]
                y, x = y + dy, x + dx
            else:               # 나무 없으면(벽O or 나무X) -> break
                break

    return cnt  # 예상되는 죽는 나무 수 반환


# 입력 위치에 살충제 뿌리며, 나무 죽이는 함수
def kill_trees(sy, sx):
    # 입력 위치에 살충제 뿌리기
    pesticides[sy][sx] = c + 1

    # 입력 위치에 나무 없으면(벽O or 나무X) -> return(전파 X)
    if area[sy][sx] <= 0:
        return

    # 전파 시작위치의 나무 제거
    area[sy][sx] = 0

    for dy, dx in diagonal_direction:  # 대각선 4방향에 대해
        y, x = sy + dy, sx + dx
        for _ in range(k):  # k범위 만큼
            if oob(y, x):  # 영역 밖 -> break
                break

            pesticides[y][x] = c + 1  # 나무 없는(벽O or 나무X) 칸에도, 살충제 전파는 이뤄짐

            if area[y][x] > 0:  # 나무 있으면 -> 나무 제거 & 1칸 더
                area[y][x] = 0
                y, x = y + dy, x + dx
            else:               # 나무 없으면(벽O or 나무X) -> break (전파 종료)
                break


# (가장 많이 나무 죽이는 위치 찾고) & (제초제 뿌리며 나무 죽이고) & (+= 죽인 나무 수) 하는 함수
def spread_pesticide():
    # 가장 많이 나무 죽이는 위치 찾기
    max_cnt = -1
    pesticide_index = (n, n)

    for y in range(n):
        for x in range(n):
            if area[y][x] <= 0:  # 나무 없으면 -> 죽이는 나무도 없음
                now_cnt = 0
            else:                # 나무 있으면 -> 전파 시 죽이는 나무 수 계산
                now_cnt = cal_dead_trees(y, x)

            # 나무 더 많이 죽이면, 최대값&위치 갱신
            if now_cnt > max_cnt:
                max_cnt = now_cnt
                pesticide_index = (y, x)

    # 제초제 뿌리며 나무 죽이기
    kill_trees(*pesticide_index)

    # 정답 += 죽인 나무 수
    global answer
    answer += max_cnt


# 제초제 유효시간 줄이는 함수
def decrease_pesticide():
    for y in range(n):
        for x in range(n):
            if pesticides[y][x]:  # 1 이상이면 -=1
                pesticides[y][x] -= 1


n, m, k, c = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]  # 나무/벽 정보 배열 (-1: 벽 / 0: 빈칸 / 자연수: 나무 그루 수)

pesticides = [[0] * n for _ in range(n)]  # 칸별 제초제의 남은 유효시간

answer = 0
for _ in range(m):        # ( m년 동안 반복 수행 )
    trees_grow()          # 1. 나무들 동시 성장
    trees_spread()        # 2. 나무들 동시 번식
    spread_pesticide()    # 3. 제초제 살포
    decrease_pesticide()  # + 제초제 유효시간 줄이기
print(answer)
