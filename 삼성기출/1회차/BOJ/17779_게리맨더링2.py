# 20240909
# 38:00
# 1 / 1

"""
풀이 시간: 38분 (09:21 ~ 09:59)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (09:21 - 09:30)
    문제에서 d1, d2, x, y의 범위 제한과 해당 변수들 위주로 설명이 되었기에,
    쉽게 읽히고 바로 구상이 떠오른 문제는 아니었습니다.
    그래도 문제 예시의 그림을 함께 보며 다시 지문을 읽으니 점차 이해가 됐고,
    모든 좌표에 대해 가능한 경계를 다 설정해보고 최소값을 갱신하는 완전탐색 풀이를 구상했습니다.

    완전탐색을 하더라도 N이 20이하였기에, 시간복잡도는 넉넉했습니다.


2. 구현 (09:30 - 09:57)
    각 좌표가 경계선 최상단이 되어, "가능한 경계선 설정 & 최소값 갱신"을 하는 동작은
    모두 독립적인 작업이라고 판단했기에, check()함수를 별도로 적어주고 메인 코드를 먼저 작성했습니다.

    check()함수를 작성하며, print()를 활용한 체크포인트들은 아래와 같습니다.
    1) sy, sx에서의 d1, d2의 최대값이 생각대로 구현됐는지
    2) 가능한 d1, d2에 대해, divisions(5구역 구분열 배열)에 값이 정확하게 저장되는지
    3) divisions의 구분열 대로 area에 정확한 선거구가 저장되는지


3. 검증 (09:57 - 09:59)
    구현부 마지막에 작성한 인구수 차이 최소값 갱신 코드를 작성하고,
    문제만 다시 읽어보며, 1,2,3,4 지역구의 index 확인만 다시 하고 제출했습니다.
    (이전의 구현 중 중간검증(체크포인트들)에서, 바로바로 실수를 확인하고 수정할 수 있었기에,
    최종 검증에서 큰 시간을 소모하지 않았습니다.)

    이전의 구현 과정에서, 각 체크포인트의 print()를 통해
    중간 검증을 충분히 활용하였기에, 이전에 작성해온 코드들은 이상 없음을 확신할 수 있었습니다.
"""


# 입력으로 들어온 좌표가 경계선 최상단의 좌표로 가정하고, "가능한 경계선 설정 & 최소값 갱신"하는 함수
def check(sy, sx):
    d1_limit = min(sx, n - 1 - sy)          # 현재 좌표에서의 d1 최대 길이
    d2_limit = min(n - 1 - sx, n - 1 - sy)  # 현재 좌표에서의 d2 최대 길이

    # 유효한 d1, d2에 대해, 경계선 긋고 인구 차이 최소값 갱신하는 코드
    for d1 in range(1, d1_limit + 1):  # d1,d2 1부터 시작
        for d2 in range(1, d2_limit + 1):
            # row에 대해 5구역의 구분선을 저장하는 코드
            divisions = []  # # 각 row의 5구역의 구분선(시작열/종료열) 저장될 배열
            dd1, dd2 = 0, 0
            for row in range(n):
                if row < sy:  # 경계선 시작행에 아직 도달 안 했다면
                    divisions.append((sx + 0.5, sx + 0.5))
                    continue
                elif row > sy + d1 + d2:  # 경계선 종료행 넘었다면
                    divisions.append((sx + d2 - d1 - 0.5, sx + d2 - d1 - 0.5))
                    continue

                # 경계선 시작행/종료행 사이라면
                divisions.append((sx - dd1, sx + dd2))  # 현재 행의, 5구역 시작열/종료열 저장
                # 다음 5구역 시작열/종료열 조정
                dd1 += 1 if row - sy < d1 else -1
                dd2 += 1 if row - sy < d2 else -1
            """
            <(sy, sx)가 (1, 2)이고, d1과 d2가 각각 1, 3인 경우>
            아래의 |로 5번 선거구의 구분선을 표시할 수 있음.

            0 0 0|0 0 0 0
            0 0 | 0 0 0 0
            0 | 0 | 0 0 0
            0 0 | 0 | 0 0
            0 0 0 | 0 | 0
            0 0 0 0 | 0 0
            0 0 0 0|0 0 0
            0 0 0 0|0 0 0
            """

            # 위에서 구한 5구역 구분선을 기준으로 area에 선거구 기록하는 코드
            area = [[0] * n for _ in range(n)]

            left = 1    # 5구역 시작열 왼쪽에 저장될 선거구 (추후 3으로 바뀜)
            right = 2   # 5구역 종료열 오른쪽에 저장될 선거구 (추후 4으로 바뀜)
            middle = 5  # 3구역 시작열/종료열 사이에 저장될 선거구 (5로 고정)
            for row in range(n):
                div1, div2 = divisions[row]  # 현재 행의 구분선

                # 특정 행 넘어서면, left/right 각각 갱신
                if row - sy == d1:
                    left = 3
                if row - sy == d2 + 1:
                    right = 4

                # 현재 행에 대해 left/middle/right 선거구 번호를 저장
                for col in range(n):
                    if col < div1:    # 5구역 시작열보다 작다면 left
                        area[row][col] = left
                    elif div2 < col:  # 5구역 종료열보다 크다면 right
                        area[row][col] = right
                    else:             # 5구역 시작열/종료열 사이면 middle
                        area[row][col] = middle

            # area의 각 좌표에 적힌 선거구를 기준으로, 선거구 인구 차이 최소값 갱신하는 코드
            population_cnts = [0] * 6  # index로 접근하기 위해 0인덱스 추가
            for r in range(n):
                for c in range(n):
                    population_cnts[area[r][c]] += populations[r][c]

            now_answer = max(population_cnts[1:]) - min(population_cnts[1:])  # 0인덱스 배제

            global min_answer
            min_answer = min(min_answer, now_answer)  # 인구 차이 최소값 갱신


n = int(input())
populations = [list(map(int, input().split())) for _ in range(n)]

min_answer = 100 * n**2  # 도달 불가능 최대값으로 초기화
for i in range(n):      # range(n - 2)로 해도 됨.
    for j in range(n):  # range(1, n - 1)로 해도 됨.
        check(i, j)  # 모든 좌표에 대해, 가능한 경계선 설정 & 최소값 갱신
print(min_answer)
