# 20240927
# 55:00 & 13:00
# 0 / 4 & 1 / 1

# 13460_구슬탈출2

"""
풀이 시간: 55분 (13:01 - 13:56)  &  13분 (16:00 - 16:13)
풀이 시도: 0 / 4                &  1 / 1


1. 문제 정독 & 풀이 구상 (13:01 - 13:04)
    정독&메모 하지 않았습니다.

    회고를 하는 지금 시점에 생각해보면,
    정독&메모는 기본적으로 가져가는 게 맞는데, 너무 빨리 구현하는 것에만 매몰돼 있었던 것 같습니다.
    그래서 오늘 이후의 문제들도 빨리 푸는 것에 과몰입했고, 실수들이 많이 나왔습니다.
    그래도 제가 습관적으로 치는 코드에서 어떤 실수들이 나오는지, 확인할 수 있다는 장점이 있기도 했습니다.


2. 구현 (13:04 - 13:13)
    이전에 풀었던 방식(구슬 좌표를 따로 변수로 관리한 풀이)을
    까먹지 않았기에, 다른 분들이 주로 채택했던, 배열에 사탕을 넣어놓고 관리해보는 것으로 시도했습니다.

    그리고 사탕을 항상 오른쪽으로 굴리도록, 배열회전을 활용했습니다.


3. 디버깅 (13:13 - 13:32)
    오른쪽으로 굴리려면 이중for문의 첫번째에 행이 아닌 열을 반복시켜야 했는데, 습관적으로 행을 먼저 반복시켰습니다.
    코드를 급하게 짜면 이런 실수도 나올 수 있음을 확인할 수 있었습니다.


4. 시간초과 (13:32 - 13:40)
    코드트리의 시간초과에서도 테케를 제공해주는지 몰라, 아래에서 1번 더 시간초과가 났습니다.

    초기 구현에서, 반시계방향 회전도 시계방향3번으로 처리해줬기에,
    이 부분에서 시간초과 이슈가 발생했겠구나하고 생각했습니다.
    그래서 해당 코드를 90/180/270 도 회전을 코드를 따로 구현했습니다.

    실제 시험에서, 반시계방향을 시계방향3회로 처리하지 않게 주의해야겠습니다.
    (!!코드가 간결한 것보다, 정확하고 시간초과 안 나는 코드가 훨씬 중요!!)


5. 틀렸습니다 (13:40 - 13:45)
    빨간 사탕과 파란 사탕이 동시에 탈출해도 안된다는 문제 지문을 간과했기에,
    디버깅할 게 아니라, 문제를 다시 봐야한다는 걸 깨닫기까지 시간이 소요됐습니다.


6. 시간초과 (13:45 - 13:55)
    아래 2개의 수정사항이 있었습니다.
    - 이전에 굴렸던 방향에 대해서 다시 굴려도, 아무 변화가 없는데, 굴려주고 있었습니다.
    - 사탕을 2개 다 굴렸다면, 반복문을 break하도록 구현했습니다.


7. 틀렸습니다 (13:55 / 16:00 - 16:13)
    주어진 55분이 끝나고, 모의시험을 보러갔다가 16시에 다시 돌아왔습니다.
    디버깅을 해보니, 굴러야 할 2번째 구슬이 구르지 않음을 확인했습니다.

    제가 오해&실수했던 부분을 간략하게 코드로 보면 아래와 같습니다.
    for i in range(1, 10):
        for j in range(1, 10):
            i += 1
    파이썬의 for문에 쓰인 변수는 값을 변경해줘도 다음 반복에서는, 그 반복문 내 변경이 영향을 미치지 않음을 알고 있었습니다.
    그러나, 위 코드와 같이 j의 for문은 i의 for문 내에 위치하기 때문에,
    j의 반복에서는 갱신되는 것이 아닙니다.
    이 부분을 명확하게 인지하지 않고 구현했기 때문에, 실수가 나왔습니다.

    이번 기회에 제대로 알게 된 실수였습니다.
"""


def dfs(cnt, arr, rotate_flag):
    global possible_cnt

    if possible_cnt <= cnt + 1:
        return

    # if cnt == 10:
    #     return

    if rotate_flag == 0:
        copied_arr = [row[:] for row in arr]
    if rotate_flag == 1:
        copied_arr = [list(row)[::-1] for row in zip(*arr)]
    elif rotate_flag == 2:
        copied_arr = [row[::-1] for row in arr[::-1]]
    elif rotate_flag == 3:
        copied_arr = [list(row) for row in list(zip(*arr))[::-1]]

    possible = False

    found = 0
    for sx in range(len(copied_arr[0]) - 2, 0, -1):
        for sy in range(1, len(copied_arr) - 1):
            if found == 2:
                break

            if copied_arr[sy][sx] in ['B', 'R']:
                found += 1
                rolling = copied_arr[sy][sx]

                y, x = sy, sx
                while True:
                    if copied_arr[y][x + 1] == '.':
                        copied_arr[y][x], copied_arr[y][x + 1] = '.', rolling
                        x += 1
                    elif copied_arr[y][x + 1] in ['#', 'B', 'R']:
                        break
                    elif copied_arr[y][x + 1] == 'O':
                        if rolling == 'R':
                            possible = True
                            copied_arr[y][x] = '.'
                            break
                        else:
                            return
        else:
            continue
        break

    if possible:
        possible_cnt = min(possible_cnt, cnt + 1)
        return
    else:
        # dfs(cnt + 1, copied_arr, 0)
        dfs(cnt + 1, copied_arr, 1)
        dfs(cnt + 1, copied_arr, 2)
        dfs(cnt + 1, copied_arr, 3)


n, m = map(int, input().split())
area = [list(str(input())) for _ in range(n)]

possible_cnt = 11
dfs(0, area, 0)
dfs(0, area, 1)
dfs(0, area, 2)
dfs(0, area, 3)

print(possible_cnt if possible_cnt != 11 else - 1)
