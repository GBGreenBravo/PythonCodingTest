# 20240911
# 1:32:00
# 1 / 1

"""
풀이 시간: 1시간 32분 (15:35 ~ 17:07)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:35 - 15:52)
    이제까지의 기출문제에서 문제 구상 시간이 가장 오래 걸렸던 것 같습니다.
    상어의 냄새를 칸별로 관리할지, 상어별로 관리할지, 아니면 둘다 따로 괸리할지에 대해
    고민이 많았고, 오랜 고민 끝에 상어별로 관리하기로 했습니다.


2. 구현 (15:52 - 16:31)


3. 계획된 검증 (16:31 - 16:38)
    이번 코드리뷰에서는 검증 단계를
    '풀이 템플릿으로 인해 검증한 단계 (계획된 검증)'와 '예기치 못한 에러로 인한 디버깅"으로 나눠봤습니다.

    계획된 검증 단계에서는, 메모와 코드를 비교대조하며 검증했습니다.
    이를 통해, 이동한 상어 위치에 냄새를 기록 안 해준 것을 발견했습니다.


4. 예기치 못한 에러로 인한 디버깅 (16:38 - 17:07)
    1) 상어의 다음 위치에 냄새를 기록할 때 k+1로 해야할 것을 k로 한 실수
    2) range(1, m + 1)을 range(m)으로 작성하여, 마지막 번호 상어의 냄새 보존된 실수
    위 2가지 실수를 발견하기 위해, 약 30분을 소모했습니다.

    1번의 실수는 디버깅으로 발견하기 쉬웠지만,
    2번의 실수는 디버깅으로 발견하기는 어려웠던, 코드를 재작성 했다면 더 발견이 쉬웠을 실수였습니다.

    위의 3.단계가 마무리된 시점이 시험 시간이 1시간 10분 가량 남았을 때지만, 코드를 지우고 재작성하지는 않았습니다.
    금세 해결될 디버깅이라고 생각했기 때문입니다.
    그러나 생각보다 30분이라는 긴 시간이 소모됐고,
    앞으로는 예기치 못한 디버깅 시간을 따로 재서 20분이 소모되면, 코드를 재작성 해야겠습니다.

    오늘 저녁에 팀끼리 논의 시간을 바탕으로, 저의 디버깅 체계가 확립이 안 됐음을 확인했습니다.
    발표 때 응급처치 print라고 소개했던, 가시성이 좋지는 않은 print디버깅만을 활용했고,
    시간을 조금이라도 들여서 구분선, 한글로 스텝 설명을 print()로 활용해야겠다고 자체적으로 회고했습니다.


5. 회고
    초반에 문제 이해가 부족했습니다.
    문제를 다 풀 때까지 상어의 냄새가 한 칸에 여러 마리의 냄새로 존재할 수 있다고 착각했습니다.
   '상어의 냄새가 한 칸에 최대 한 마리의 냄새만 존재함'을 제출할 때까지 알지 못했기에,
    초기 구상 단계에서 냄새를 칸별/상어별로 관리할지에 대한 고민을 오래했고,
    칸별로 하면 더 간단할 것을,
    상어별로 dictionary로 관리하여 조금 더 복잡하게 구현했습니다.

    '문제 지문만을 바탕으로 이해&구상 하고, 문제에서 제공하는 그림은 웬만하면 검증단계에서 활용하도록 아껴두자'
    는 나름의 다짐이 있었지만,
    문제의 그림을 보면서 문제를 좀 더 이해하고자 했다면, '상어가 남기는 냄새가 한 칸에 최대 한 마리의 냄새만 존재함'을
    문제 이해 단계에서 알아챌 수 있었을 것 같기도 합니다.

    문제 지문 1회독만에 이해가 바로 되지 않는 문제의 경우에는,
    문제에서 제공하는 그림을 바탕으로 다시 문제를 이해하면 좋을 듯 합니다.
"""

direction = (None, (-1, 0), (1, 0), (0, -1), (0, 1))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def move_shark(y, x, shark_number, shark_d_idx):
    can_move_to_no_smell = []
    can_move_to_my_smell = []
    for dd in range(1, 5):
        dy, dx = direction[dd]
        ny, nx = y + dy, x + dx
        if oob(ny, nx):
            continue
        if not now_smell[ny][nx]:
            can_move_to_no_smell.append(dd)
        if smell_per_shark[shark_number].get(ny * n + nx):
            can_move_to_my_smell.append(dd)

    if can_move_to_no_smell:
        for next_d_idx in preference_per_shark[shark_number][shark_d_idx]:
            if next_d_idx in can_move_to_no_smell:
                ddy, ddx = direction[next_d_idx]
                nny, nnx = y + ddy, x + ddx
                new_area[nny][nnx].append((shark_number, next_d_idx))
                smell_per_shark[shark_number][nny * n + nnx] = k + 1
                return
    elif can_move_to_my_smell:
        for next_d_idx in preference_per_shark[shark_number][shark_d_idx]:
            if next_d_idx in can_move_to_my_smell:
                ddy, ddx = direction[next_d_idx]
                nny, nnx = y + ddy, x + ddx
                new_area[nny][nnx].append((shark_number, next_d_idx))
                smell_per_shark[shark_number][nny * n + nnx] = k + 1
                return


n, m, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
sharks_dir = [False] + list(map(int, input().split()))

preference_per_shark = [None]
for i in range(m):
    tmp_preference = [None]
    for _ in range(4):
        tmp_preference.append(tuple(map(int, input().split())))
    preference_per_shark.append(tmp_preference)

smell_per_shark = [dict() for _ in range(m + 1)]

for i in range(n):
    for j in range(n):
        shark_num = area[i][j]
        if shark_num:
            smell_per_shark[shark_num][i * n + j] = k
            area[i][j] = [(shark_num, sharks_dir[shark_num])]

dead_cnt = 0
time = 1
while time <= 1000:
    now_smell = [[False] * n for _ in range(n)]
    for smell_dict in smell_per_shark:
        for idx in smell_dict.keys():
            a, b = divmod(idx, n)
            now_smell[a][b] = True

    new_area = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if area[i][j]:
                move_shark(i, j, *area[i][j][0])

    for i in range(n):
        for j in range(n):
            if len(new_area[i][j]) > 1:

                dead_cnt += len(new_area[i][j]) - 1

                new_area[i][j].sort(key=lambda info: info[0])
                new_area[i][j] = [new_area[i][j][0]]

    for i in range(1, m + 1):
        now_dict = smell_per_shark[i]
        new_dict = dict()
        for key in now_dict.keys():
            value = now_dict[key]
            if value == 1:
                continue
            new_dict[key] = value - 1
        smell_per_shark[i] = new_dict

    if dead_cnt == m - 1:
        print(time)
        break
    else:
        time += 1
        area = new_area
else:
    print(-1)
