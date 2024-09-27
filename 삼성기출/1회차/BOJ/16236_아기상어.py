# 20240905
# 41:00
# 1 / 1

"""
풀이 시간: 41분 (15:00 ~ 15:41)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:00 - 15:08)
    평소보다 문제가 잘 안 읽히는 듯한 느낌이 들었습니다.
    그냥 문장을 흘려 읽는 것 같은 느낌이 들었지만,
    메모를 상세히 한다는 루틴 덕에, 차근히 문제를 이해할 수 있었습니다.

    문제를 읽고 한 가지 모호하다고 생각했던 점은,
    아기상어가 성장할 때, 이제까지 먹은 물고기수 초기화의 유무였습니다.
    성장할 때 초기화 안 하면 2개 이후로 먹을 때마다 항상 커지기에,
    초기화 하는 것이 합리적이라고 생각했지만, 추후 판단을 위해서 별도의 물음표로 표시해줬습니다.
    (테스트케이스를 눈으로만 보면서 궁금증을 해결할 수 없기도 하고,
    초기화해주는 코드 하나만 작성해주면 되는 사항이었기에,
    구현 후에 명확하게 확인하기로 했습니다.)


2. 구현 (15:08 - 15:26)
    구현을 하며, 처음에는 먹을 수 있는 물고기의 좌표를
    possibles라는 배열에 다 담고, sort()를 통해서 가장 가까운 거리의 물고기를 찾으려 했습니다.

    그러나, 구현하다 보니 더 효율적인 방식이 없을까? 생각하고,
    dy, dx를 가져오는 direction을 상좌우하 순으로 설정하고 BFS를 돌면 => 먹을 수 있는 물고기를 찾는 즉시 반환
    하면 되겠다고 생각하고 이 구상대로 구현했습니다. (추후 검증에서 틀린 구상으로 판명)
    (메모에 "거리/행/열 우선순위"가 아닌 "거리, 상좌우하"와 같이 적었기에, 이 구상에 대한 큰 의심이 없었습니다.)


3. 검증 (15:26 - 15:41)
    첫 실행에서 무한루프를 돌았습니다.
    간단한 프린트 디버깅을 통해, 0일 때도 아기상어가 물고기로 인식하고 먹음처리를 해서 그랬음을 확인하고 수정해줬습니다.

    그리고 구현단계에서 착각했던, 가장 가까운 물고기 찾는 방식에 대해
    오답이 나왔고, 해당 오류를 눈으로 확인하기 위해,
    아기상어가 물고기를 먹을 때마다, area를 출력했습니다.
    위의 디버깅을 통해, 우선순위 설정이 잘못 돼있음을 확인하고,
    기존 코드의 반례를 고려하며 초기 구상대로 코드를 수정해줬습니다.

    문제를 읽으며 표시했던 "아기상어 성장 시, 그간 먹은 물고기 수 리셋"에 대한 의문은
    테스트케이스에서의 코드1줄(ate_cnt = 0)의 비교를 통해,
    리셋하는 것이 옳음을 확인했습니다.

    구현 단계에서 맞는 구상에서 (더 효율적이라고 생각했던) 틀린 구상으로 수정했던 근거 중에 하나는,
    메모에 적힌 상좌우하 표시때문이었습니다.
    이제까지는 모든 요구사항을 메모한다면, 어떤 표현이든 상관 없다고 생각했습니다.
    그러나 이번 경우를 통해, 문제 조건 표시는 최대한 그대로 하되,
    구상을 위한 별도의 메모를 하는 것이 더 나을 수 있겠다는 고민을 하게 됐습니다.
"""

from collections import deque

direction = ((-1, 0), (0, -1), (1, 0), (0, 1))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


# 현재 아기상어의 위치에서 먹을 수 있는 물고기를 먹으러 이동하는 함수. (못 먹는다면 return False)
def find_fish():
    global baby, baby_size, ate_cnt, time

    sy, sx = baby[0], baby[1]  # 현재의 아기상어 위치

    visited = [[0] * n for _ in range(n)]  # BFS 중복방문 방지를 위한 방문 배열
    visited[sy][sx] = 1

    queue = deque()
    queue.append((sy, sx))

    possibles = []  # 아기상어가 먹을 수 있는 물고기들의 위치를 담을 배열

    while queue:
        y, x = queue.popleft()

        distance = visited[y][x]

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] or area[ny][nx] > baby_size:  # 영역 밖 / 이미 방문 / 못 지나가는 물고기 => continue
                continue
            # '지나갈 수 있음'에 따른 처리
            queue.append((ny, nx))
            visited[ny][nx] = distance + 1
            if area[ny][nx] and area[ny][nx] < baby_size:  # 0이 아니고 아기상어보다 작다면, 먹을 수 있음
                possibles.append((distance, ny, nx))

    # 먹을 수 있는 물고기가 하나라도 있으면, 그 물고기 먹으러 이동 처리 and return True
    if possibles:
        # 요소가 (거리, 행, 열)로 구성돼 있으므로, 거리 오름차순 -> 행 번호 오름차순 -> 열 번호 오름차순
        possibles.sort()
        shortest, ey, ex = possibles[0][0], possibles[0][1], possibles[0][2]

        area[ey][ex] = 0  # 가장 가까운 물고기 먹혀서, 빈칸 됨.
        baby = (ey, ex)   # 그 칸으로 아기상어 이동 처리
        ate_cnt += 1      # 먹은 물고기수 += 1
        if ate_cnt == baby_size:  # 먹은 물고기 수가 아기상어 사이즈와 같으면,
            baby_size += 1  # 아기상어 사이즈 += 1
            ate_cnt = 0   # 먹은 물고기 수 리셋
        time += shortest  # 이동한 거리만큼 이동시간 추가
        return True

    # 먹을 수 있는 물고기 없으면 return False
    return False


n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

baby = (None, None)  # 아기상어의 현재 위치
baby_size = 2        # 아기상어의 현재 사이즈
ate_cnt = 0          # 아기상어가 현재까지 먹은 물고기 수

# 아기상어 초기 위치 찾는 코드
for i in range(n):
    for j in range(n):
        if area[i][j] == 9:
            area[i][j] = 0
            baby = (i, j)
            break
    else:
        continue
    break

time = 0  # 물고기 먹으러 가는 이동 시간

# 반복할 때마다, 아기상어는 물고기를 찾고 먹음.
while True:
    if not find_fish():  # 더 이상 먹을 수 있는 물고기가 없다면, 답변 출력하고 반복문 종료
        print(time)
        break
