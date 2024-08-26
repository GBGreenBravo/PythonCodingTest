# 20240826
# 1:00:02
# 1 / 1

"""
풀이 시간: 1시간 2분 (15:16 ~ 16:18)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:16 - 15:22)
    주사위 숫자가 계속 변할 수 있기에,
    주사위 숫자를 어떻게 저장해줄 것인지가 관건이라고 생각했습니다.

    문제에서 주어진 평면도에서 a-b, c-d, e-f가 반대면이 되는 것으로 설정하고,
    알파벳 a~f에 따른 숫자를 저장해주면 될 것으로 생각했습니다.

    그리고 주사위가 동서북남으로 굴러갈 때의 다음 알파벳 또한 dictionary로 처음에 정확히 구해준 다음,
    해당 dictionary를 갱신 필요 없이 계속 써주면 된다고 생각했습니다.


2. 구현 (15:22 - 15:29)
    위와 같이 구상했을 때는 큰 문제 없이 구현할 수 있었습니다.


3. 검증 및 재구상 (15:29 - 16:18)
    그러나 첫 번째 테스트케이스를 돌려본 결과, 정답과는 다른 출력을 확인할 수 있었고, 문제점을 파악하고자 했습니다.
    머릿속에서 생각하기만으로는 어려운 문제였기에, print()를 찍어보며 테스트케이스에서의 과정을 따라가보고자 했습니다.
    이를 통해, 같은 열에 대해서는, 방향에 따른 다음 알파벳이 유지됐지만,
    같은 행에서도 다음 방향의 알파벳이 다른 경우가 있음을 확인했습니다.

    해당 문제를 해결하기 위해, 다음 방향의 알파벳을 구하는 규칙을 찾고자 했습니다.
    많은 시뮬레이션과 시도들을 하며 시간을 많이 소모하다가, 문득 너무 복잡하게 생각하고 있는 것은 아닌지 하는 생각이 들었습니다.

    위 생각을 통해 어차피 방향은 4군데로 많지 않으므로, 현재 밑면의 알파벳에 따른 다음 방향을 그때그때 갱신해주자는 생각이 들었고,
    이전의 다른 시도들보다도 훨씬 명확하고 편안하게 구현할 수 있었습니다.

    그리고 테스트케이스를 다 돌려본 결과, 생각대로 구현되었음을 확인하고 제출했습니다.
"""

direction = (None, (0, 1), (0, -1), (-1, 0), (1, 0))  # 1234 index => 동서북남


def oob(xx, yy):
    return xx < 0 or n <= xx or yy < 0 or m <= yy


n, m, x, y, k = map(int, input().split())
sy = y
area = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

"""
주사위 평면도를 아래와 같이 설정하고, 시작 시 아래가 a 동쪽이 d를 바라보는 것으로 설정.
  e
c a d
  f
  b
"""
opposite = {'a': 'b', 'b': 'a', 'c': 'd', 'd': 'c', 'e': 'f', 'f': 'e'}  # 아랫면의 반대 면(윗면)을 반환하는 dictionary
dice_numbers = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0}  # 주사위에 적힌 번호들
next_dice = '0dcef'  # 1234 index => 동서북남
dice_bottom = 'a'  # 시작 시, 아래는 a로 설정

for d_idx in commands:
    dx, dy = direction[d_idx]  # 다음 방향
    nx, ny = x + dx, y + dy  # 다음 좌표
    if oob(nx, ny):  # 다음 좌표가 영역 밖이면, 무시
        continue
    x, y = nx, ny  # 다음 좌표 갱신

    """
    아래에서는 '1234->동서북남'으로 굴러가는 각 경우의 다음 동서북남 문자열[현재 방향]  
    """
    next_dice, dice_bottom = (None,
                 '0' + opposite[dice_bottom] + dice_bottom + next_dice[3] + next_dice[4],
                 '0' + dice_bottom + opposite[dice_bottom] + next_dice[3] + next_dice[4],
                 '0' + next_dice[1] + next_dice[2] + opposite[dice_bottom] + dice_bottom,
                 '0' + next_dice[1] + next_dice[2] + dice_bottom + opposite[dice_bottom])[d_idx]\
        , next_dice[d_idx]  # 다음 좌표 밑면은, 현재 밑면에서 현재 방향으로 이동한 것

    if area[x][y]:  # 지도에 숫자 0 아니라면
        dice_numbers[dice_bottom] = area[x][y]
        area[x][y] = 0
    else:  # 지도에 숫자 0이라면
        area[x][y] = dice_numbers[dice_bottom]

    print(dice_numbers[opposite[dice_bottom]])  # 윗면의 숫자를 출력
