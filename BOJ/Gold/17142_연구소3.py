# 20240830
# 28:00
# 1 / 1

"""
풀이 시간: 28분 (09:05 ~ 09:33)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (09:05 - 09:11)
    이전에 연구소 문제를 풀어봤기에, 슬쩍 훑어봤을 때 어려워보이지 않아서 연구소3를 먼저 풀었습니다.
    모든 바이러스 위치에 대해서 m개의 바이러스 위치를 조합하여, 바이러스를 퍼뜨리는 구현을 하면 되겠다고 생각했습니다.

    이전의, '치킨배달' 문제에서 조합으로 구현해야 하는 걸, 순열로 구했던 경험이 있었기에,
    이번에는 신경 써서 조합으로 구현하고, 최대범위에 대해서도 테스트케이스를 만들고 검증하기로 했습니다.


2. 구현 (09:11 - 09:22)
    구현 과정에서 조합을 구성하는 get_combination()의 가지치기와 같은 경우,
    구현은 쉽게 할 수 있으나, 구상한 코드를 먼저 구현하고 싶어서
    해당 부분은 주석 & 북마크(F11) 처리하고 나중에 구현해주기로 했습니다.

    그리고 cal_spread_time() 함수에서 바이러스를 퍼뜨리는 구현을 할 때,
    visited 배열을 쓰지 않고, area(초기 입력된 배열)를 복사해서,
    0을 2로 바꾸며 퍼뜨리면 되겠다고 생각했습니다.


3. 검증 (: - 09:33)
    구현을 끝내고, 모든 테스트케이스를 돌려본 결과,
    이상 없이 답변을 출력해냈습니다.

    그래서 한번에 답변이 나온다는 것에 조금 더 의심을 하고,
    그래서 추가 검증을 위해, 우선 최대범위 테스트케이스를 만들고 시간 검증을 해줬습니다.
    그러다 4*4 최소범위 테스트케이스에서 값을 바꿔가는 과정에서, 큰 오류를 발견할 수 있었습니다.

    구상 단계에서, visited를 따로 쓰지 않고, area를 바꾸는 과정에서 0을 2로 바꾸고 2를 만나면 continue 시켰습니다.
    그러나 문제에서 '활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다'는 지문이 있었고,
    이 경우를 만족해주지 못한 것이었습니다.
    따라서, 해당 전파값을 2에서 1로 바꾸고, 전파시간 체크에 대한 코드도 리팩토링 했습니다.

    위 오류를 왜 구현 과정에서 생각해주지 못했을까 회고했을 때,
    문제를 꼼꼼히 읽지 않았다는 점이 주요했다고 생각합니다.
    문제를 읽을 때는 그 지문을 보고, '음 당연하지'하고 쉽게 넘어가고 메모하지 않았습니다.
    당연하다고 생각하는 것도, 복잡하고 반복적인 구현 과정에서 누락될 수 있으므로
    앞으로는 지문을 읽으며 당연하다고 생각하는 것도 모두, 메모로 적어야겠다는 플랜을 세울 수 있었습니다.
"""

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


# 현재의 m개 바이러스 전파 시작점에서, 전파 완료까지의 시간을 게산하고 최소값을 갱신하는 함수
def cal_spread_time():
    now_area = [row[:] for row in area]    # 기존 배열(origin area) 복사

    queue = deque()
    for vy, vx in start_virus_arr:         # 시작점 모두 queue에 담아주기
        queue.append((vy, vx, 0))          # 시작할 때의 시간은 0
        now_area[vy][vx] = 1               # 바이러스 전파된 곳 1로 표시

    mx_time = 0          # 전파 완료까지의 시간

    while queue:
        y, x, time = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or now_area[ny][nx] == 1:        # 영역 밖 or 1(벽 / 이미 바이러스 전파된 곳)이면 continue
                continue
            if not now_area[ny][nx]:                        # 빈 땅이면
                mx_time = max(mx_time, time + 1)            # 전파 시간 갱신
            now_area[ny][nx] = 1                            # 바이러스 전파된 곳 1로 표시
            queue.append((ny, nx, time + 1))

    if sum(map(lambda k: k.count(0), now_area)):            # 한 군데라도 바이러스 전파가 안 됐다면, 최소시간 갱신 없이 return
        return
    global answer
    answer = min(answer, mx_time)            # 바이러스 전파 최소시간 갱신


# 바이러스가 위치한 좌표들에서 m개를 조합하는 함수
def get_combination(cnt, start_idx):
    if cnt == m:             # 종료 조건
        cal_spread_time()    # 바이러스 전파 시뮬레이션
        return

    if len_viruses - start_idx < m - cnt:    # 조기 종료 조건: 앞으로 탐색할 수보다, 필요한 바이러스 수가 더 많으면
        return

    for i in range(start_idx, len_viruses):
        start_virus_arr.append(viruses[i])
        get_combination(cnt + 1, i + 1)
        start_virus_arr.pop()


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

viruses = []
for i in range(n):
    for j in range(n):
        if area[i][j] == 2:
            viruses.append((i, j))  # 바이러스 전파 시작점의 대상이 될 좌표 저장

answer = n**2                # 불가능한 최소시간으로 초기화
len_viruses = len(viruses)
start_virus_arr = []         # 조합되는 좌표를 넣을 배열
get_combination(0, 0)        # 조합 구성
print(answer if answer != n**2 else -1)
