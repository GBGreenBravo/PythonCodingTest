# 20240913
# 1:00:00
# 1 / 1

"""
풀이 시간: 1시간 (09:00 ~ 10:00)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (09:00 - 09:13)
    문제를 읽는 도중에 구상이 떠오르는 편이었는데,
    이번 문제는 출력조건을 읽기 전까지는 구상이 떠오르지 않았습니다.
    그래도 정독&메모를 통해 온전히 이해했기에, DFS로 풀어야겠다는 구상을 할 수 있었습니다.

    DFS 구상의 시간복잡도의 경우, 계산해도 3**15 (print결과: 14_348_907) 였기에, 합당한 풀이라고 생각했습니다.


2. 구현 (09:13 - 09:46)
    아래는 이 문제에서 중간검증한 체크포인트들입니다.
    1) 입력이 생각대로 저장되는지
    2) move_fish() 함수 먼저 구현했기에, 문제의 설명 그림처럼 물고기 이동하는지
        2-1) 단계별 살펴보기
        2-2) 그림5와 출력결과 비교
    3) move_shark() 함수
        처음으로 호출된 함수에서 무한루프를 돌았고,
        nsy, nsx를 ny, nx로 적은 실수를 발견하고 수정했습니다.


3. 검증 (09:46 - 10:00)
    루틴 대로 검증을 수행했습니다.
    1) 문제 다시 읽으며, 모호한 부분 없는지 & 메모에 다 적혔는지 체크
    2) 메모 다시 읽으며, 모두 코드에 반영됐는지 체크
    3) 메모에 작성해둔, 모호한 부분/엣지 케이스 반영됐는지 체크
    4) 과거에 했던 실수들 되풀이하지 않았는지 체크 (DFS 초기 상태 확인 및 습관적 visited 처리 등)

    그리고 코드를 다시 보는 과정에서, 불필요한 중복 코드를 발견하여 리팩토링했습니다.
        move_fish 함수에서, 제 구상 대로면 빈칸이든 다른 물고기가 있든, 두 값을 바꿔주기만 하면 됐기에,
        같은 동작을 함을 발견하고 중복코드를 제거했습니다.
"""

direction = ((-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1))


def oob(y, x):
    return y < 0 or 4 <= y or x < 0 or 4 <= x


# 물고기 이동시키고, 4*4배열과 물고기방향배열 반환하는 함수
def move_fish(before_area, before_fish_info, sy, sx):
    # deepcopy
    now_area = [a[:] for a in before_area]
    now_fish_info = [f for f in before_fish_info]

    # 물고기 순서대로 이동처리
    for fish_num in range(1, 17):
        # 물고기가 이미 먹혔다면, continue
        if now_fish_info[fish_num] == -1:
            continue

        # 현재번호의 물고기 좌표 찾기
        for ii in range(4):
            for jj in range(4):
                if now_area[ii][jj] == fish_num:
                    fy, fx = ii, jj
                    break
            else:
                continue
            break

        # 현재 물고기 이동가능한 방향으로 이동시키기
        for dd in range(8):
            fd = (now_fish_info[fish_num] + dd) % 8  # 반시계 45도 회전
            fdy, fdx = direction[fd]

            nfy, nfx = fy + fdy, fx + fdx
            if oob(nfy, nfx) or (nfy == sy and nfx == sx):  # 영역 밖 or 상어좌표 -> continue
                continue

            # 다음좌표(nfy, nfx)에 물고기 있든 없든 아래 코드로 같이 처리해도 됨.
            now_area[fy][fx], now_area[nfy][nfx] = now_area[nfy][nfx], now_area[fy][fx]  # 4*4배열에서의 물고기 자리 교환
            now_fish_info[fish_num] = fd  # 현재 물고기 방향만 갱신
            break

    return now_area, now_fish_info


def move_shark(before_area, before_fish_info, sy, sx, sd, s_ate):
    global mx_answer

    can_go_indexes = []       # 상어가 현재 방향으로 이동가능한 좌표들
    sdy, sdx = direction[sd]  # 상어의 현재 방향

    # 이동가능한 좌표 탐색
    nsy, nsx = sy + sdy, sx + sdx
    while not oob(nsy, nsx):
        if before_area[nsy][nsx]:  # 물고기 있어야 이동가능
            can_go_indexes.append((nsy, nsx))
        nsy, nsx = nsy + sdy, nsx + sdx

    # 이동가능한 좌표 없다면, 상어 집 보내야 함.
    if not can_go_indexes:
        mx_answer = max(mx_answer, s_ate)  # 먹은 물고기번호합 최대값 갱신
        return

    # 이동가능한 좌표 있다면, DFS 재귀 호출
    for ny, nx in can_go_indexes:
        # deepcopy
        next_area = [a[:] for a in before_area]
        next_fish_info = [f for f in before_fish_info]

        # 먹히는 물고기 번호
        eaten_fish_num = next_area[ny][nx]

        # 상어 방향 & 먹은 물고기 번호 합 갱신
        next_sd = next_fish_info[eaten_fish_num]
        next_s_ate = s_ate + eaten_fish_num

        # 물고기 먹힘 처리
        next_fish_info[eaten_fish_num] = -1
        next_area[ny][nx] = 0

        # 물고기 이동 처리
        next_area, next_fish_info = move_fish(next_area, next_fish_info, ny, nx)

        # DFS 재귀 호출
        move_shark(next_area, next_fish_info, ny, nx, next_sd, next_s_ate)


area = [[0] * 4 for _ in range(4)]  # 4*4배열에 있는 물고기 번호
fish_dir_infos = [0] * 17  # 각 물고기 번호에 따른 방향 배열 (번호를 그대로 index로 활용하기 위해 앞에 0index 추가)

# 입력값 저장
for i in range(4):
    lst = list(map(int, input().split()))
    for j in range(0, 8, 2):
        fish_dir_infos[lst[j]] = (lst[j + 1]) % 8
        area[i][j//2] = lst[j]

# 상어 (0, 0)으로 이동 및 먹기 처리
shark_ate = area[0][0]                                        # 먹은 물고기 번호
shark_y, shark_x, shark_d = 0, 0, fish_dir_infos[area[0][0]]  # 상어 좌표, 상어 방향
# (0, 0)에 있던 물고기 먹힘 처리
fish_dir_infos[area[0][0]] = -1  # 방향들(0~8)과 구분하기 위해 -1로 표시
area[0][0] = 0                   # 4*4배열에서 (0, 0)에 있던 물고기 번호 제거

# (상어 이동 후) 물고기 이동
area, fish_dir_infos = move_fish(area, fish_dir_infos, shark_y, shark_x)

mx_answer = 0  # 상어가 먹는 물고기번호합 최대값
move_shark([a[:] for a in area], [f for f in fish_dir_infos], shark_y, shark_x, shark_d, shark_ate)  # DFS 호출
print(mx_answer)
