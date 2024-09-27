# 20240905
# 41:00
# 1 / 1

"""
풀이 시간: 41분 (15:42 ~ 16:23)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:42 - 15:51)
    문제를 읽으며, 풀이에 대한 구상이 바로 떠오르지는 않았지만,
    입력 지문의 가로/세로 범위와, 출력 지문의 -1 출력 조건을 보고,
    조합을 구성하는 문제임을 파악할 수 있었습니다.

    조합을 구성하는 문제였기에, 시간복잡도를 먼저 체크해줬습니다.
    comb(H * M, 3) * N 이었기에,
    comb(300, 3)을 출력해보니, 4,455,100 이었고,
    10(N)을 곱하면, 44,551,000이었기에 합리적인 구상이라고 생각했습니다.

    한가지 궁금했던 것은, 두 가로선이 연속하는 경우는 알겠는데,
    두 가로선이 접하는 경우가 어떤 것인지를 단번에 알지는 못했습니다.
    (이 경우는, 구현하며 깨우치기로 하여 구현 단계로 넘어갔습니다.)


2. 구현 (15:51 - 16:05)
    가로선가 있는 경우, connected에 왼쪽 좌표는 1을, 오른쪽 좌표는 -1로 표시해줬습니다.
    처음에는, 별 생각 없이 이렇게 구상했으나,
    나중에 사다리 내려오는 함수를 구현하면서, 운이 좋게 잘 설정했음을 확인했습니다.


3. 검증 (16:05 - 16:23)
    순열이 아닌 조합이고, 생각대로 조합을 구성했는지, print를 통해 확인했습니다.

    find_end 함수에서, 최종 열 index가 아닌 True/False를 반환하고 있었습니다.
    find_end 함수를 작성하고, 명확하게 체크해주지 않아 생긴 실수였습니다.

    기존 코드에서 가로선이 연속하는 경우를 반영해주지 않고 있었습니다.
    10분 동안의 print 디버깅을 통해, 발견했습니다.
    해당 코드를 수정해주는 것에는 오랜 시간이 걸리지 않았으나,
    구상 단계에서 고려를 해주지 않은 결과이이게 실수하면 안 됐는 부분이었습니다.

    메모에서 표시를 해줬으나, 메모를 보지 않고 테스트케이스만 보고서 디버깅하려 했기에 벌어진 일이었습니다.
    생각과는 다른 작동을 하고 있다면, 코드만 볼 것이 아니라,
    메모와 문제 지문도 살펴보면, 디버깅이 더 단축된다는 새로운 가이드라인을 얻을 수 있었습니다..
"""


# 현재의 사다리(connected)에서, start_col_idx로 시작해서, 끝 세로선 index를 반환하는 함수
def find_end(start_col_idx):
    # 초기 좌표 세팅
    col_idx = start_col_idx
    row_idx = 0

    # 사다리 내려오는 반복문
    while row_idx < h:  # 행 index가 h가 될 때까지
        col_idx += connected[row_idx][col_idx]  # 열 += 가로선 없다면 0 / 왼쪽으로 가로선 있다면 -1 / 오른쪽으로 가로선 있다면 1
        row_idx += 1  # 행 += 1

    return col_idx  # 도착 시점의 열 index 반환


# 모든 n개의 세로선에서 같은 세로선으로 끝나는 경우, possible(flag)를 True로 변경하는 함수
def cal_possible():
    global possible

    for ii in range(n):  # 모든 n개의 세로선에 대해
        if find_end(ii) != ii:  # 하나라도 다른 세로선으로 내려오면, break
            break
    else:  # 모든 세로선에서의 출발이 자신의 세로선으로 끝나면, possible = True
        possible = True


# 가로선 조합을 ladder_limit개 만큼 구성하고, 구성된 가로선들로 cal_possible()를 호출하는 함수
def get_ladders_combination(cnt, start_idx):
    if possible:  # 이미 특정 조합에서 만족했다면 return
        return

    if cnt == ladder_limit:  # 종료 조건: 가로선 조합 cal_possible개 완성 됐으면
        cal_possible()  # cal_possible() 호출
        return

    for li in range(start_idx, len_candidates):
        r, c = candidates[li]
        if connected[r][c] or connected[r][c + 1]:  # 가로선 연속하는 경우
            continue
        connected[r][c] = 1  # 가로선 왼쪽 좌표 1로 표시
        connected[r][c + 1] = -1  # 가로선 오른쪽 좌표 -1로 표시
        get_ladders_combination(cnt + 1, li + 1)  # 재귀 호출
        connected[r][c] = 0  # 가로선 왼쪽 좌표 복구
        connected[r][c + 1] = 0  # 가로선 오른쪽 좌표 복구


n, m, h = map(int, input().split())

# 가로선이 없으면: 0 / 가로선의 왼쪽 좌표: 1 / 가로선의 오른쪽 좌표: -1
connected = [[0 for _ in range(n)] for _ in range(h)]

for _ in range(m):
    a, b = map(int, input().split())
    connected[a - 1][b - 1] = 1  # 가로선의 왼쪽 좌표는 1로 표시
    connected[a - 1][b] = -1     # 가로선의 오른쪽 좌표는 -1로 표시

candidates = []  # 가로선이 없는 좌표들을 담을 배열
for i in range(h):
    for j in range(n - 1):
        if not connected[i][j]:
            candidates.append((i, j))
len_candidates = len(candidates)

for i in range(4):  # 놓을 사다리 수 (0, 1, 2, 3) 반복문
    possible = False
    ladder_limit = i  # 놓을 사다리 수 (0, 1, 2, 3)

    ladder_arr = []  # 사다리가 놓이는 좌표들의 배열
    get_ladders_combination(0, 0)  # 조합 함수 호출

    if possible:  # 특정 조합에서 문제 조건 만족하면,
        print(i)  # 해당 사다리 수 출력
        break
else:  # 0, 1, 2, 3개의 사다리로 안 되는 경우, -1 출력
    print(-1)
