# 20240830
# 25:00
# 1 / 1

"""
풀이 시간: 25분 (14:07 ~ 14:32)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:07 - 14:15)
    지난 "마법사 상어와 비바라기"와 마찬가지로, 행열간 이동과 많은 지시사항을 상세히 구현하는 게 핵심이었습니다.
    그렇기에, 문제에서 요구하는 세부사항들을 상세히 적고, 정확히 이해하고 구현을 시작하기로 했습니다.

    새로운 질량/속도를 계산하는 지문에서  ⌊⌋가 쓰였는데,
    기억하기로는 소수점은 버리는 것으로 알고 있었지만, 확신이 없었습니다.


2. 구현 (14:15 - 14:29)
    반복적으로 파이어볼이 이동하고 합쳐지기에,
    함수로 구분하여 구상&구현했습니다.

    그리고 구현 과정에서 리스트 컴프리헨션이 자주 사용되었기에,
    해당 코드에서 사용된 변수명이 겹치지 않는지 체크하며 구현했습니다.


3. 검증 (14:29 - 14:32)
    입력 받을 때의 행/열 번호를 -1 해주지 않은 것을 발견하고, 수정해줬습니다.
    구현 과정에서부터 똑바로 잡았어야 하는 실수라고 생각합니다.
    분명 반영하라고 메모에도 항상 적는 건데,
    입력 받는 행/열 번호를 작성하는 코드에서는, 항상 메모된 사항을 보는 것을 루틴으로 가져야겠습니다.
"""

direction = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


# 현재 유효한 파이어볼을 모두 이동시키고, 겹치는 파이어볼을 병합/분할 해준 뒤의 area를 반환하는 함수
def move_fireballs():
    global area
    new_area = [[[] for _ in range(n)] for _ in range(n)]      # 1초 뒤의 파이어볼 상태들이 저장되는 배열
    for y in range(n):
        for x in range(n):
            for fm, fs, fd in area[y][x]:
                dy, dx = direction[fd]
                ny, nx = (y + dy * fs) % n, (x + dx * fs) % n  # 첫&마지막 행과 열이 연결되기에 % 연산자 활용
                new_area[ny][nx].append((fm, fs, fd))          # 이동된 좌표에 파이어볼 상태(질량/속도/방향) 저장

    for y in range(n):
        for x in range(n):
            if len(new_area[y][x]) > 1:  # 파이어볼 2개 이상 겹친다면 (병합/분할 필요)
                new_m = sum([i[0] for i in new_area[y][x]]) // 5                          # 새로운 질량 계산
                if not new_m:            # 질량이 0이 된다면, 파이어볼 소멸 처리
                    new_area[y][x] = []
                    continue
                new_s = sum([i[1] for i in new_area[y][x]]) // len(new_area[y][x])        # 새로운 속도 계산

                if sum([i[2] % 2 for i in new_area[y][x]]) in [0, len(new_area[y][x])]:   # 새로운 방향 계산
                    new_ds = [0, 2, 4, 6]  # 방향이 모두 홀수거나 모두 짝수라면, 0246
                else:
                    new_ds = [1, 3, 5, 7]

                new_area[y][x] = []
                for new_d in new_ds:  # 다음 4방향들에 대해
                    new_area[y][x].append((new_m, new_s, new_d))  # 현재 좌표에 (새로운 속도 / 새로운 방향 / 각 방향) 저장

    area = new_area  # 1초 뒤의 파이어볼 상태들로 갱신


n, m, k = map(int, input().split())
area = [[[] for _ in range(n)] for _ in range(n)]  # 현재 좌표에 위치한 파이어볼의 상태가 저장될 배열

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    area[r - 1][c - 1].append((m, s, d))  # area에 파이어볼 상태(질량/속도/방향) 그대로 넣어주기

for _ in range(k):
    move_fireballs()  # k번 동안 파이어볼 이동 & area 갱신

answer = 0
for i in range(n):
    for j in range(n):
        for fireball in area[i][j]:
            answer += fireball[0]   # 현재 파이어볼의 질량을 더해주기
print(answer)
