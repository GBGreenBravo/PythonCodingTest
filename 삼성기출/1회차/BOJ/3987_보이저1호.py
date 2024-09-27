# 20240822
# 27:00
# 1 / 1

"""
풀이 시간: 27분 (15:11 ~ 15:38)
풀이 시도: 1 / 1


1. 문제 정독 (15:11 - 15:15)
    (아래는 문제를 읽는 당시, 메모한 사항을 모두 옮겨적은 것입니다.)
    - 현재는 태양권덮개
    - 항성계 만날 때마다 -> 라디오 signal msg recording
    - 행/열 : M/N
    - 구분
        행성: '/', '\'
        블랙홀: 'C'
        빈칸: '.'
    - 시그널 상하좌우 전파
    - 시그널이 (블랙홀 만나거나) (항성계 벗어날 때까지) 전파
    - 1초당 1칸
    - 시그널 4방향 중 stay시간 최대값
    - 1 <= N,M <= 5 * 10**2
    - 무한??


2. 풀이 구상 (15:11 - 15:20)
    핵심은 아래의 2가지라고 생각했습니다.
    1) / 이나 \ 를 만났을 때, 방향을 어떻게 바꿔줄 것인지
    2) 무한으로 도는 보이저를 어떻게 체크할 것인지

    1)의 경우는, /를 만난 경우와 \를 만난 경우의, 다음 방향값을 지정해주면 된다고 생각했습니다.

    2)의 경우는,
    처음에는 time을 체크하다가 이 time이 n*m과 같은 특정 최대값을 넘어선다면,
    무한으로 체크하면 된다고 생각했습니다.
    그러나 위 경우도 가능하나, 명확하다고 판단되지 않아, 다른 방법을 생각하는 시간을 가졌습니다.

    visited = [북쪽으로 퍼뜨린 전파의 visited n*m 배열, 동쪽으로 퍼뜨린 ~, 남쪽으로 퍼뜨린 ~, 서쪽으로 퍼뜨린 ~]
    그 결과, 위와 같은 배열에, 초기에 전파를 시작하는 방향 4개에 대해 각각의 visited 처리를 해주면,
    같은 좌표에 또 다시 오게 되면 이는 무한이라고 판단했습니다.


3. 구현 (15:18 - 15:32)


4. 검증 (15:32 - 15:38)
    문제를 읽으며 메모했던 사항들을 하나씩 다시 읽음과 동시에,
    생각했던 점을 만족시킨 코드를 하나씩 찾으며 점검했습니다.

    위 점검에서는 모든 부분을 만족시켰다고 생각했으나,
    테스트케이스2번을 통해서 초기 구상의 허점을 발견할 수 있었습니다.

    '/'와 같은 경우에는, 동서남북에서 오는 접근이 모두 다른 걸로 취급돼야 함을,
    테스트케이스2번을 눈으로 따라가며 알아챘습니다.

    따라서, visited 배열의 최하위를 0으로 선언했던 것을 [0, 0, 0, 0]으로 선언하여,
    그 좌표에 오는 방향별 방문체크를 따로 해주는 것으로 변경했습니다.
    변수명이 길기는 하나, 개인적인 문제 이해를 바탕으로 명명한 것이었기에, 리팩토링에서 어려움을 겪지는 않았습니다.
"""

from collections import deque


def oob(yy, xx):
    return yy < 0 or n <= yy or xx < 0 or m <= xx


# "북,동,남,서 -> 0,1,2,3 index로 취급하기"를, 전역적인 규칙으로 설정했습니다.
direction = ((-1, 0), (0, 1), (1, 0), (0, -1))

# '/'를 만났을때 북동남서 -> 동북서남
meet_right_up = [1, 0, 3, 2]
# '\'를 만났을때 북동남서 -> 서남동북
meet_left_up = [3, 2, 1, 0]


n, m = map(int, input().split())
area = [list(str(input())) for _ in range(n)]
sy, sx = map(int, input().split())
sy -= 1
sx -= 1

# 북동남서
max_per_directions = [0, 0, 0, 0]

queue = deque()
# 초기 좌표로부터 4방향으로의 전파 시작
queue.append((sy, sx, 0, 0, 0))  # 현재 좌표 y, x, 현재 바라보는 방향index, 현재 좌표까지의 시간, 전파가 시작한 초기 방향
queue.append((sy, sx, 1, 0, 1))
queue.append((sy, sx, 2, 0, 2))
queue.append((sy, sx, 3, 0, 3))

visited = [[[[0] * 4 for _ in range(m)] for _ in range(n)] for _ in range(4)]
# 무한히 순환하는지 여부를 체크하는 flag
is_voyager = False

while queue:
    # 현재 좌표 y, x, 현재 바라보는 방향index, 현재 좌표까지의 시간, 전파가 시작한 초기 방향
    y, x, direction_idx, time, start_direction = queue.popleft()

    # 현재까지의 시간이 최대값보다 크다면 갱신
    # (영역 밖이거나 블랙홀 도달까지의 시간으로 계산하기에, queue에서 뺀 후에 체크해줬습니다.)
    if max_per_directions[start_direction] < time:
        max_per_directions[start_direction] = time

    # 현재 좌표가 '영역 밖'이거나 '블랙홀'이라면, 전파 소멸.
    if oob(y, x) or area[y][x] == 'C':
        continue

    # 현재 좌표에 현재 방향으로 도달한 적이 없다면,
    if not visited[start_direction][y][x][direction_idx]:
        visited[start_direction][y][x][direction_idx] = 1  # 방문 처리
    # 현재 좌표에 현재 방향으로 도달한 적이 있다면,
    else:
        print(['U', 'R', 'D', 'L'][start_direction])
        print("Voyager")
        is_voyager = True  # 무한히 순환한다는 뜻이기에, 그에 따른 '출력'과 'flag 변경'
        break

    # 현재 방향을 기반으로 다음 좌표 도출
    dy, dx = direction[direction_idx]
    ny, nx = y + dy, x + dx

    # '/'나 '\'라면, 반사될 방향으로 변경
    if not oob(ny, nx):
        if area[ny][nx] == '/':
            direction_idx = meet_right_up[direction_idx]
        elif area[ny][nx] == '\\':
            direction_idx = meet_left_up[direction_idx]

    # 소멸되지 않은 전파의 다음 좌표와 부가 정보 append
    queue.append((ny, nx, direction_idx, time + 1, start_direction))

# 위의 while문 종료 후, 무한히 순환하지 않는다면, 그에 대한 최대값 출력
if not is_voyager:
    # 같은 max를 가져도 U,R,D,L의 순서로 앞서는 것을 출력해야 합니다.
    print(['U', 'R', 'D', 'L'][max_per_directions.index(max(max_per_directions))])
    print(max(max_per_directions))
