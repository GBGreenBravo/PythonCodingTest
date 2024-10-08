# 20240926
# 15:33
# 1 / 2

# 14500_테트로미노

"""
풀이 시간: 16분 (16:49 - 17:05)
풀이 시도: 1 / 2


1. 문제 정독 & 풀이 구상 (16:49 - 16:53)
    (09/27 한정) 정독&메모 하지 않았습니다..
    문제 정독&메모 루틴의 소중함을 깨달은 하루였습니다.

    그래도 이 문제에서는 룩업테이블을 구성했기에, 회전하는 블럭의 모양을 다 그렸습니다.
    (뒤집는 모양은 반영하지 못해, 1번 틀립니다..)


2. 구현 (16:53 - 17:00)
    회고를 쓰는 시점에서 이전 문제(14500_테트로미노)의 코드와 비교해보니,
    거의 같지만, 한 가지 차이가 있었습니다.

    이전 코드에서는 자신의 좌표가 무조건 블럭임을 가정한 룩업테이블이었는데,
    이번 코드에서는 자신의 좌표는 블럭 모양의 좌상단(블럭일 수도 있고 블럭이 아닐 수도 있음)임을 가정한 룩업테이블이었습니다.

    0 1 0  =>  이 모양에서 좌상단을 기준으로 블럭 칸(1)들의 (dy, dx)를 적었습니다.
    1 1 1
    이번의 방식이, 룩업테이블 작성에 있어서 더 쉽고 검증하기도 편한 것으로 생각합니다.
    따라서, 앞으로 간단한 룩업테이블을 구성할 일이 있다면, 오늘의 피드백을 활용할 수 있도록 해야겠습니다.


3. 디버깅 (-)


4. 틀렸습니다 (17:01 - 17:05)
    문제를 제대로 읽지 않았기에 틀렸습니다.
    테트리스 블럭이 뒤집을 수도 있음을 인지하지 못하고, 회전만 반영해줘서 틀렸습니다.

    뒤집힌 모양도 추가해서 수정&제출했습니다.
"""

all_shapes = (((0, 0), (1, 0), (2, 0), (3, 0)),
              ((0, 0), (0, 1), (0, 2), (0, 3)),

              ((0, 0), (0, 1), (1, 0), (1, 1)),

              ((0, 0), (1, 0), (2, 0), (2, 1)),
              ((0, 0), (0, 1), (0, 2), (1, 0)),
              ((0, 0), (0, 1), (1, 1), (2, 1)),
              ((0, 2), (1, 0), (1, 1), (1, 2)),

              ((0, 1), (1, 1), (2, 0), (2, 1)),
              ((0, 0), (1, 0), (1, 1), (1, 2)),
              ((0, 0), (0, 1), (1, 0), (2, 0)),
              ((0, 0), (0, 1), (0, 2), (1, 2)),

              ((0, 0), (1, 0), (1, 1), (2, 1)),
              ((0, 1), (0, 2), (1, 0), (1, 1)),

              ((0, 1), (1, 0), (1, 1), (2, 0)),
              ((0, 0), (0, 1), (1, 1), (1, 2)),

              ((0, 0), (1, 0), (1, 1), (2, 0)),
              ((0, 1), (1, 0), (1, 1), (1, 2)),
              ((0, 1), (1, 0), (1, 1), (2, 1)),
              ((0, 0), (0, 1), (0, 2), (1, 1)))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

answer = 0

for sy in range(n):
    for sx in range(m):

        for shape in all_shapes:

            now_score = 0
            for dy, dx in shape:
                ny, nx = sy + dy, sx + dx
                if oob(ny, nx):
                    break
                now_score += area[ny][nx]
            else:
                answer = max(answer, now_score)

print(answer)
