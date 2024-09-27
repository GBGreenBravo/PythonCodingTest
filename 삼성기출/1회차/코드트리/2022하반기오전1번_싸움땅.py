# 20240923
# 49:00
# 1 / 1

"""
풀이 시간: 49분 (09:03 - 09:52)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (09:03 - 09:14)
    문제에 명시된 절차들을 충실하게 반영하는 문제였습니다.

    다만, 한 가지 고민됐던 것은, 플레이어 유무 파악을 위한 N*N 2차원 배열을 구성할지였습니다.
    해당 배열을 둔다면, 플레이어 위치를 2번 갱신해줘야 하는 불편함이 있지만, 플레이어 유무 파악에서 시간복잡도의 이점이 있습니다.
    플레이어 최대 수가 30으로 크지 않았기에, 해당 배열을 두지 않기로 결정했습니다.


2. 구현 (09:14 - 09:45)
    메모에 나름의 체계로 작성해둔 가이드를 따라,
    함수를 적극적으로 활용하며 구현했습니다.


3. 디버깅 (09:45 - 09:48)
    플레이어들의 위치가 정상적으로 반영이 되지 않는 이슈가 있었습니다.
    플레이어 정보 배열과, 싸움을 하는 플레이어를 출력하여,
    다음 좌표에 있는 플레이어 유무 판단 조건에,
    "player_idx != other_player_idx"가 빠져있었음을 확인했습니다.


4. 검증 (09:48 - 09:52)
    O (1) 주어진 테스트케이스로 검증
        - 테스트케이스 각 과정의 무기 정보, 플레이어 정보가 그림과 일치하는지 비교했습니다.
    O (2) 메모 vs. 코드
        - 절차대로 구현됐는지 체크
        - 처음에 모호하다고 생각했던 부분들에 대한 재검토
    X (3) (머릿속 환기 후) 문제 재정독
    X (4) 커스텀 테스트케이스 검증
    X (5) 철저한 코드 검증
    X (6) 오답노트 활용
    X (7) 다양한 구상에 따른, 다른 구현
"""

direction = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 북동남서


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


# 싸움에서 진 플레이어의 결과를 반영하는 함수
def move_loser(loser):
    py, px, pd = players_info[loser][:3]

    # 가진 총 내려놓기 (player_info[loser]에 반영은 아래에서 따로 해줌)
    if players_info[loser][4]:
        weapons[py][px].append(players_info[loser][4])

    # 현재 방향 1칸 가보기
    npy, npx = py + direction[pd][0], px + direction[pd][1]
    for _ in range(4):  # (싸움의 전제 조건인 플레이어 1칸 이동으로 인해) 인접한 곳에 플레이어 없는 칸 무조건 있음
        # 영역 밖 -> 우회전
        if oob(npy, npx):
            pd = (pd + 1) % 4
            npy, npx = py + direction[pd][0], px + direction[pd][1]
            continue

        for opi in range(1, m + 1):
            opy, opx = players_info[opi][:2]
            # 플레이어 O -> 우회전
            if opi != loser and opy == npy and opx == npx:
                pd = (pd + 1) % 4
                npy, npx = py + direction[pd][0], px + direction[pd][1]
                break

        # 플레이어 X -> 그리로 이동
        else:
            # 좌표/방향/무기 갱신
            players_info[loser] = [npy, npx, pd, players_info[loser][3], 0]

            # 이동한 칸에 총 확인하고, 가장 센 총 획득
            all_weapons = weapons[npy][npx]
            if all_weapons:
                players_info[loser][4] = max(all_weapons)
                all_weapons.remove(max(all_weapons))
            weapons[npy][npx] = all_weapons

            return


# 싸움에서 이긴 플레이어의 결과를 반영하는 함수
def move_winner(winner):
    py, px = players_info[winner][:2]

    # 해당 칸에 총 확인하고, 가장 센 총 획득
    all_weapons = weapons[py][px] + [players_info[winner][4]] if players_info[winner][4] else weapons[py][px]
    if all_weapons:
        players_info[winner][4] = max(all_weapons)
        all_weapons.remove(max(all_weapons))
    weapons[py][px] = all_weapons


# 두 플레이어의 싸움 결과를 반영하는 함수
def fight(fighter1, fighter2):
    # 이긴/진 플레이어 비교
    if sum(players_info[fighter1][3:]) > sum(players_info[fighter2][3:]):
        winner, loser = fighter1, fighter2
    elif sum(players_info[fighter1][3:]) == sum(players_info[fighter2][3:]):
        if players_info[fighter1][3] > players_info[fighter2][3]:
            winner, loser = fighter1, fighter2
        else:
            winner, loser = fighter2, fighter1
    else:
        winner, loser = fighter2, fighter1

    # 이긴 플레이어 점수 추가
    players_score[winner] += sum(players_info[winner][3:]) - sum(players_info[loser][3:])

    # 진/이긴 플레이어 결과 반영
    move_loser(loser)
    move_winner(winner)


# player_idx 번째 플레이어 이동시키는 함수
def move_player(player_idx):
    py, px, pd = players_info[player_idx][:3]

    npy, npx = py + direction[pd][0], px + direction[pd][1]  # 현재 방향대로 1칸 이동
    if oob(npy, npx):  # 영역 밖이라면, 방향 반대로 바꾸고 1칸 이동
        pd = (pd + 2) % 4
        npy, npx = py + direction[pd][0], px + direction[pd][1]

    # 이동한 위치/방향 저장
    players_info[player_idx] = [npy, npx, pd, players_info[player_idx][3], players_info[player_idx][4]]

    for opi in range(1, m + 1):
        opy, opx = players_info[opi][:2]
        # 이동한 곳에 플레이어 O
        if player_idx != opi and opy == npy and opx == npx:
            fight(player_idx, opi)  # Fight!
            break

    # 이동한 곳에 플레이어 X
    else:
        # 해당 칸에 총 확인하고, 가장 센 총 획득
        all_weapons = weapons[npy][npx] + [players_info[player_idx][4]] if players_info[player_idx][4] else weapons[npy][npx]
        if all_weapons:
            players_info[player_idx][4] = max(all_weapons)
            all_weapons.remove(max(all_weapons))
        weapons[npy][npx] = all_weapons


n, m, k = map(int, input().split())

# 무기 정보 저장
weapons = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not weapons[i][j]:  # 빈 칸은 빈 리스트로
            weapons[i][j] = []
        else:                  # 무기 있다면, 리스트로 감싸기
            weapons[i][j] = [weapons[i][j]]

players_info = [None]  # index 1~M 활용
players_score = [0] * (m + 1)
for m_idx in range(1, m + 1):
    a, b, c, d = map(int, input().split())
    players_info.append((a - 1, b - 1, c, d, 0))  # Y / X / 방향 / 능력치 / 무기

# K라운드 동안, 반복 수행
for _ in range(k):
    for pi in range(1, m + 1):
        move_player(pi)

# 정답 출력
print(*players_score[1:])
