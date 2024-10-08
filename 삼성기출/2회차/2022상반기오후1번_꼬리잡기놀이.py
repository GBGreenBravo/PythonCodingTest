# 20241008
# 1:40:11
# 1 / 1

"""
풀이 시간: 1시간 40분 (09:47 - 11:27)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (09:47 - 09:55)
    이전 풀이방식(팀 정보 따로 저장하지 않고, area 배열에서 바로 변경)이 대중적이지 않은 접근이었기 때문에,
    다른 풀이로 풀어보고자 했습니다.

    이번에는 팀 정보를 따로 관리하여, area가 아닌 팀 정보를 변경하는 방식을 채택했습니다.
    팀별 이동선 좌표를 모두 저장해놓고, 해당 팀의 멤버들이 현재 어떤 죄표에 있는지 관리하고자 했습니다.


2. 구현 (09:55 - 10:23)
    같은 값을 가져오기 위해 반복적으로 인덱싱하는, 긴 코드가 작성되어도 틀린 코드가 아니기에,
    바로 리팩토링하지 않고 추후 검증 단계에서 리팩토링하기로 했습니다.


3. 디버깅 (10:23 - 10:32)
    의도와 다르게 작성된 코드가 있었습니다.
    find_team() 함수에서 12...34... 이렇게 오름차순으로 탐색해야 하는 구상인데,
    위의 우선순위가 아닌, direction의 우선순위에 따라 탐색되고 있었습니다.
    수정은 어렵지 않았습니다.


4. 검증 (10:32 - 11:27)
    원래 파일을 temp.py 하나만 두고,
    구현&검증&리팩토링 모두 한 파일에서 하는 스타일이었습니다.

    Pycharm의 Local History기능으로 이전 코드를 쉽게 불러올 수는 있지만,
    시험장에서 다양한 구상/검증을 하는 과정에서 자칫하면 헷갈릴 수도 있을 것 같아,
    이번에는 test(최종 제출할 코드), temp(초기 구현), temp2(다른 구현), print_(print검증용)으로
    파일을 목적에 맞게 여러 개 생성해놓고, 다앙하게 검증&구현 했습니다.

    이전 풀이와 다르게, area 출력만으로는 팀의 이동이 한눈에 보기 어려웠기 때문에,
    검증만을 위한 코드를 print_.py 파일에서 작성하고, 손쉽게 한눈에 살펴볼 수 있었습니다.
    (확실히 print용 코드를 따로 빼두니, 더 적극적이고 다양한 커스텀 테케를 돌려볼 수 있었습니다.)

    그리고 리팩토링을 통해 중복되는 코드를 (성능 저하 없이) 더 가독성 좋게 변환했습니다.

    팀의 이동방향은 1이나 -1로 정해지는데,
    원래는 team_directions 배열에 1/-1을 저장하지 않고,
    이동할 때마다 계산해주고 있었습니다.
    따라서, 이를 계속 계산하는 것보다, team_directions 배열을 두는 것이 더 가독성 좋고 실수도 없을 코드라고 생각하여,
    새로운 구상에 따른, 다른 구현을 했습니다.
    temp2.py 파일에서 진행했고, Pycharm의 View - Compare With 기능을 이용하여
    변경 과정에서 빠진 로직은 없는지 검토했습니다.

    추가로, 이 풀이에 index() 함수가 자주 쓰였기에, IndexError를 반환할 부분을 집중하며 검증했습니다.

    O (1) 주어진 테스트케이스로 검증
    O (2) 메모 vs. 코드
    O (3) (머릿속 환기 후) 문제 재정독
    O (4) 커스텀 테스트케이스 검증
    O (5) 철저한 코드 검증
    O (6) 오답노트 활용
    O (7) 다양한 구상에 따른, 다른 구현
"""

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 우 하 좌 상


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def find_team(sy, sx):
    global team_flag

    team_flag += 1
    team_visited[sy][sx] = team_flag
    team_indexes = [(sy, sx)]
    team_line_indexes = [(sy, sx)]

    y, x = sy, sx
    while True:
        two, three, four = None, None, None
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or not area[ny][nx]:
                continue
            if area[ny][nx] == 1 and len(team_indexes) > 2:
                team_indexes = [team_line_indexes.index(ti) for ti in team_indexes]
                return team_indexes, team_line_indexes
            if team_visited[ny][nx]:
                continue

            if area[ny][nx] == 2:
                two = ny, nx
            elif area[ny][nx] == 3:
                three = ny, nx
            elif area[ny][nx] == 4:
                four = ny, nx

        if two:
            ny, nx = two
            team_visited[ny][nx] = team_flag
            team_indexes.append((ny, nx))
            team_line_indexes.append((ny, nx))
            y, x = ny, nx
        elif three:
            ny, nx = three
            team_visited[ny][nx] = team_flag
            team_indexes.append((ny, nx))
            team_line_indexes.append((ny, nx))
            y, x = ny, nx
        elif four:
            ny, nx = four
            team_visited[ny][nx] = team_flag
            team_line_indexes.append((ny, nx))
            y, x = ny, nx


n, m, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

team_infos = [None]
team_all_lines = [None]
team_directions = [None]
team_flag = 0
team_visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if area[i][j] == 1:
            now_lines, all_lines = find_team(i, j)
            team_infos.append(now_lines)
            team_all_lines.append(all_lines)
            team_directions.append(-1)

throwing_balls = []
for i in range(n):
    throwing_balls.append((i, 0, 0))
for i in range(n):
    throwing_balls.append((n - 1, i, 3))
for i in range(n):
    throwing_balls.append((n - 1 - i, n - 1, 2))
for i in range(n):
    throwing_balls.append((0, n - 1 - i, 1))

total_score = 0
for turn in range(k):
    for team_idx in range(1, m + 1):
        team_infos[team_idx] = [(ti + team_directions[team_idx]) % len(team_all_lines[team_idx]) for ti in team_infos[team_idx]]

    ball_y, ball_x, ball_d = throwing_balls[turn % len(throwing_balls)]
    dby, dbx = direction[ball_d]
    while not oob(ball_y, ball_x):
        team_num = team_visited[ball_y][ball_x]
        if team_num:
            now_point = team_all_lines[team_num].index((ball_y, ball_x))
            if now_point in team_infos[team_num]:
                total_score += (team_infos[team_num].index(now_point) + 1) ** 2
                team_infos[team_num].reverse()
                team_directions[team_num] *= -1
                break
        ball_y, ball_x = ball_y + dby, ball_x + dbx
print(total_score)
