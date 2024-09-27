# 20240913
# 47:00
# 1 / 1

"""
풀이 시간: 47분 (15:13 ~ 16:00)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:13 - 15:26)
    앞의 문제('21609_상어중학교')에서, 문제를 정확하게 읽지 않아서 한번 틀렸기에,
    더 천천히 & 정확히 읽기로 했습니다.
    (항상 천천히 & 정확히 읽도록 노력해야 함!)

    처음 구상은 6*4 배열로 초록색 보드를 생각하고, 4*6 배열로 파란색 보드를 생각했습니다.
    초록색 보드는 행을 기준으로 살펴보고, 파란색 보드는 열을 기준으로 살펴보기로 생각하고,
    더 익숙하고 편한 행 기준(초록색 보드)을 먼저 구현하기로 했습니다.


2. 구현 (15:26 - 15:54)
    초록색 보드에 관한 함수를 구현하다 보니,
    파란색 보드도 6*4 배열로 돌려서 생각하면,
    지금 구현하고 있는 초록색 보드 함수를 그대로 쓸 수 있겠다고 생각했습니다.
    따라서, 초기의 행/열만 잘 변경해주고, 파란색에 관한 함수를 구현 완료했습니다.

    초록색 보드를 구현하면서,
    1) 블록이 제대로 쌓이는지
    2) 행이 다 차면 제대로 지우고, 윗행 채우고, 점수 추가하는지
    3) 연한 칸에 대한 수행 잘 되는지
    에 체크포인트를 두어, 체크&수정 했습니다.

    그리고 파란색 보드도 추가로 구현했고,
    파란색 보드를 처음에 선언할 때, 6*4로 해야할 것을
    초/파 둘 다 4*6으로 변경했던 이슈가 있었습니다.
    print() 디버깅을 통해 바로 확인했고, 수정했습니다.


3. 검증 (15:54 - 16:00)
    구현이 끝나고, 테스트케이스에서는 모두 정답을 출력했습니다.
    그리고 루틴의 검증을 수행했습니다.

    루틴의 "확인 가능한 테스트케이스의 각 단계를 출력하며, 생각대로 넘어가는지 체크" 단계에서,
    구현 마지막 부분에 4*6 배열로 수정하는 과정에서
    초록색을 6*6 배열로 수정한 오류를 발견했습니다.

    이 오류가 이 문제에서는 그대로 제출했어도 정답이었겠지만,
    다른 문제에서는 치명적인 결과로 돌아올 수도 있었기에,
    "확인 가능한 테스트케이스의 각 단계를 출력하며, 생각대로 넘어가는지 체크"
    위 루틴의 효용을 확인할 수 있었습니다.
"""


# (초록색 보드에) ix열의 기준으로 i_type의 블록을 쌓고, 꽉 찬 행 제거하고, 연한 칸 작업도 하는 함수
def load_green(ix, i_type):
    global score

    # 위에서 떨어지는 블록 마련
    if i_type == 1:
        falling = [(ix, 1)]               # 1깊이 1개
    elif i_type == 2:
        falling = [(ix, 1), (ix + 1, 1)]  # 1깊이 2개
    elif i_type == 3:
        falling = [(ix, 2)]               # 2깊이 1개

    # 떨어지는 블록이 쌓일 곳 체크
    now_row = 0
    while now_row <= 4:  # 현재 행이 index5(마지막 행)이면 종료
        for col, dist in falling:  # 떨어지는 블록들에 대해
            if now_row + dist >= 6 or green[now_row + dist][col]:  # (현재 행+깊이)가 범위 벗어나거나, 이미 블록 쌓여있다면 => break
                break
        else:  # 더 떨어져도 된다면
            now_row += 1
            continue
        break

    # 떨어진 블록 쌓음 처리
    for col, dist in falling:
        for d in range(dist):
            green[now_row + d][col] = 1

    # 꽉 채워진 행 탐색
    removed_row = []
    for row in range(2, 6):
        if sum(green[row]) == 4:
            removed_row.append(row)

    # 채워진 행 있다면, 점수 추가 & 뒤의 index부터 삭제
    for r in removed_row[::-1]:
        score += 1
        del green[r]

    # 삭제된 행 있다면, 맨 위에 [0, 0, 0, 0]으로 채워주기
    for _ in range(len(removed_row)):
        green.insert(0, [0, 0, 0, 0])

    # 연한 칸에 블록이 있는지 체크
    removed_below = 0
    for row in range(2):
        if sum(green[row]):
            removed_below += 1

    # 연한 칸에 블록 있다면, 맨 아래 행 삭제 & 맨 위에 행 [0, 0, 0, 0]으로 채우기
    for _ in range(removed_below):
        green.insert(0, [0, 0, 0, 0])
        green.pop()


# (초록색 보드에) ix열의 기준으로 i_type의 블록을 쌓고, 꽉 찬 행 제거하고, 연한 칸 작업도 하는 함수
# 위의 load_green 함수와 로직 같음.
def load_blue(ix, i_type):
    global score

    # 파란색 보드는, 문제의 그림에서 시계방향 90도 회전하여 생각하므로,
    # i_type 처리만 달리 함.
    if i_type == 1:
        falling = [(ix, 1)]               # 1깊이 1개
    elif i_type == 2:
        falling = [(ix, 2)]               # 2깊이 1개
    elif i_type == 3:
        falling = [(ix, 1), (ix - 1, 1)]  # 1깊이 2개

    now_row = 0
    while now_row <= 4:
        for col, dist in falling:
            if now_row + dist >= 6 or blue[now_row + dist][col]:
                break
        else:
            now_row += 1
            continue
        break
    for col, dist in falling:
        for d in range(dist):
            blue[now_row + d][col] = 1

    removed_row = []
    for row in range(2, 6):
        if sum(blue[row]) == 4:
            removed_row.append(row)

    for r in removed_row[::-1]:
        score += 1
        del blue[r]

    for _ in range(len(removed_row)):
        blue.insert(0, [0, 0, 0, 0])

    removed_below = 0
    for row in range(2):
        if sum(blue[row]):
            removed_below += 1

    for _ in range(removed_below):
        blue.insert(0, [0, 0, 0, 0])
        blue.pop()


n = int(input())
input_blocks = [map(int, input().split()) for _ in range(n)]

green = [[0] * 4 for _ in range(6)]  # 문제 그림 그대로, 6*4 배열로 선언
blue = [[0] * 4 for _ in range(6)]   # 문제 그림을 시계방향 90도 회전하여 생각해서, 6*4 배열로 선언

score = 0
for input_type, input_y, input_x in input_blocks:

    load_green(input_x, input_type)
    load_blue(abs(input_y - 3), input_type)  # 파란색 보드를 회전시켰으므로, index 조정해서 전달

print(score)
print(sum(map(sum, green)) + sum(map(sum, blue)))
