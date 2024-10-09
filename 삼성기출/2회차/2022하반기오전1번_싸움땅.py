# 20241009
# 1:14:03
# 1 / 1

"""
풀이 시간: 1시간 14분 (13:25 - 14:39)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (13:25 - 13:38)
    이전 풀이에서는 player가 최대 30명이었기에,
    players_map을 두지 않고 players_info로만 관리하여 위치 겹침 유무를 파악했습니다.
    그러나, 이 풀이 방식만을 고집하면, 자칫하면 시간복잡도에 걸릴 수도 있기에,
    이러한 유형의 문제에 대해서는, players_map과 players_info로 정보를 중복관리 하는 스타일로 구현하도록 2회차 풀이 계획을 세웠습니다.


2. 구현 (13:38 - 14:04)
    이미 인지하고 있었지만, 더더욱 강조해서 생각하고 있어야 하는 건,
    정보의 중복 관리에서 players_info를 튜플로 선언한다면, 값을 바꿀 때 한꺼번에 바꿔줘야 하고,
    하나의 값만 바꾸고 싶다면, 리스트로 선언해야하는 점입니다.

    이전 풀이에서는 함수화를 더 잘게 했었는데,
    최근에 와서는, 검증 시 변수 하나하나가 어디서 쓰였는지 살펴보는 과정에서 함수가 적은 편이 더 검증이 쉬운 것 같아,
    조금은 함수의 단위가 커진 것으로 구현 스타일에 약간의 변동이 있어 보입니다.

    그리고 늘 생각했듯이, 깔끔한 함수화와 다른 사람이 보기에 가독성 좋은 코드보다,
    중복된 코드가 있더라도 무조건 정확하게 구현된 코드가
    현재 풀이&시험의 목표에 맞기에, 별도의 리팩토링을 진행하지는 않았습니다.


3. 디버깅 (14:04 - 14:10)
    구현 당시를 떠올리면, 늘 급하게 쓴 코드에서 사소한 실수들이 발생하는 것 같습니다.
    이번에도 인덴트를 주지 말아야 할 부분에 인덴트를 줘서,
    기존에 무기가 없었다면 무기를 줍지 못하는 실수가 있었습니다.
    그래도 디버깅 절차가 생겨 그런지, 별다른 어려움 없이 발견할 수 있었습니다.


4. 검증 (14:10 - 14:39)
    O (1) 주어진 테스트케이스로 검증
    O (2) 메모 vs. 코드
    O (3) (머릿속 환기 후) 문제 재정독
    O (4) 커스텀 테스트케이스 검증
    O (5) 철저한 코드 검증
    O (6) 오답노트 활용
    X (7) 다양한 구상에 따른, 다른 구현
"""

direction = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 상우하좌


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def move_player(player_idx):
    sy, sx, p_d_idx, p_power, p_weapon = player_infos[player_idx]

    dsy, dsx = direction[p_d_idx]
    nsy, nsx = sy + dsy, sx + dsx
    if oob(nsy, nsx):
        p_d_idx = (p_d_idx + 2) % 4
        dsy, dsx = direction[p_d_idx]
        nsy, nsx = sy + dsy, sx + dsx

    player_map[sy][sx] = 0

    if not player_map[nsy][nsx]:
        if weapons[nsy][nsx]:
            if p_weapon:
                weapons[nsy][nsx].append(p_weapon)
            p_weapon = max(weapons[nsy][nsx])
            weapons[nsy][nsx].remove(p_weapon)

        player_infos[player_idx] = nsy, nsx, p_d_idx, p_power, p_weapon
        player_map[nsy][nsx] = player_idx
    else:
        another_idx = player_map[nsy][nsx]
        ay, ax, a_d_idx, a_power, a_weapon = player_infos[another_idx]

        if (p_power + p_weapon > a_power + a_weapon) or (p_power + p_weapon == a_power + a_weapon and p_power > a_power):
            player_points[player_idx] += p_power + p_weapon - a_power - a_weapon
            # Lose
            if a_weapon:
                weapons[nsy][nsx].append(a_weapon)
                a_weapon = 0
            for __ in range(4):
                if __:
                    a_d_idx = (a_d_idx + 1) % 4
                dly, dlx = direction[a_d_idx]
                nly, nlx = ay + dly, ax + dlx
                if not oob(nly, nlx) and not player_map[nly][nlx]:
                    if weapons[nly][nlx]:
                        a_weapon = max(weapons[nly][nlx])
                        weapons[nly][nlx].remove(a_weapon)
                    break
            player_infos[another_idx] = nly, nlx, a_d_idx, a_power, a_weapon
            player_map[nly][nlx] = another_idx

            # Win
            if weapons[nsy][nsx]:
                if p_weapon:
                    weapons[nsy][nsx].append(p_weapon)
                p_weapon = max(weapons[nsy][nsx])
                weapons[nsy][nsx].remove(p_weapon)

            player_infos[player_idx] = nsy, nsx, p_d_idx, p_power, p_weapon
            player_map[nsy][nsx] = player_idx
        else:
            player_points[another_idx] += a_power + a_weapon - p_power - p_weapon
            # Lose
            if p_weapon:
                weapons[nsy][nsx].append(p_weapon)
                p_weapon = 0
            for __ in range(4):
                if __:
                    p_d_idx = (p_d_idx + 1) % 4
                dly, dlx = direction[p_d_idx]
                nly, nlx = nsy + dly, nsx + dlx
                if not oob(nly, nlx) and not player_map[nly][nlx]:
                    if weapons[nly][nlx]:
                        p_weapon = max(weapons[nly][nlx])
                        weapons[nly][nlx].remove(p_weapon)
                    break
            player_infos[player_idx] = nly, nlx, p_d_idx, p_power, p_weapon
            player_map[nly][nlx] = player_idx

            # Win
            if weapons[nsy][nsx]:
                if a_weapon:
                    weapons[nsy][nsx].append(a_weapon)
                a_weapon = max(weapons[nsy][nsx])
                weapons[nsy][nsx].remove(a_weapon)

            player_infos[another_idx] = nsy, nsx, a_d_idx, a_power, a_weapon
            player_map[nsy][nsx] = another_idx


n, m, k = map(int, input().split())
weapons_input = [list(map(int, input().split())) for _ in range(n)]
weapons = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if weapons_input[i][j]:
            weapons[i][j].append(weapons_input[i][j])

player_map = [[0] * n for _ in range(n)]
player_infos = [None]
for p_idx in range(1, m + 1):
    aa, bb, dd, ss = map(int, input().split())
    player_map[aa - 1][bb - 1] = p_idx
    player_infos.append((aa - 1, bb - 1, dd, ss, 0))

player_points = [None] + [0] * m
for _ in range(k):
    for p_idx in range(1, m + 1):
        move_player(p_idx)
print(*player_points[1:], sep=" ")
