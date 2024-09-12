# 20240912
# 47:00
# 1 / 1

"""
풀이 시간: 47분 (14:10 ~ 14:57)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:10 - 14:21)
    게임판의 명확한 규칙을 단번에 알아볼 수 없는,
    전형적이지는 않은 문제유형이라고 생각했습니다.

    게임판의 노드 수가 그렇게 많지 않았기에,
    각 노드들의 index를 임의로 지정하고, 화살표가 가리키는 방향들을 하드코딩 하기로 생각했습니다.
    각 노드들의 index를 임의 지정하고, 해당 과정에서 실수하지 않도록,
    종이에 최대한 보기 좋게 표시했습니다.

    시간복잡도는 10회 동안 4개의 말을 선택하는 것이었기에,
    4**10(대략 10**6)으로 구상대로 하면 된다고 판단했습니다.

    그리고 '말이 이동을 마치는 칸에 다른 말이 있으면 그 말은 고를 수 없다. 단, 이동을 마치는 칸이 도착 칸이면 고를 수 있다.'
    라는 지문에 대해 몇 번을 읽어봐도 이해가 잘 되지 않았습니다.
    지문의 '그 말'을 '이동하는 칸에 원래 있던 다른 말'로 이해하고 구현을 시작했습니다.
    ('그 말'을 '이동하는 말'로 이해하는 것이 정답)


2. 구현 (14:21 - 14:45)
    임의로 지정한 노드들의 index를 바탕으로 먼저 하드코딩 한 뒤,
    주요 로직이 담긴 dfs() 함수를 구현했습니다.

    문제를 읽으며 모호하다고 생각했던 부분을 제외하고 모든 부분을 구현한 뒤,
    다시 지문을 읽어봤지만, 틀린 이해를 바로잡지 못했습니다.
    그렇게 틀린 이해를 바탕으로, 구현을 끝냈습니다.


3. 검증 (14:45 - 14:57)
    테스트케이스 검증에서 모두 오답이 나왔습니다.
    4분 동안의 디버깅을 통해, 최대값 갱신할 때 tmp_score로 해야할 것을 score로 적은 실수를 발견했습니다.

    그렇게 4개의 테스트케이스 중, 앞의 2개는 정답이었지만,
    문제를 잘못 이해한 부분으로 인해, 테스트케이스 3,4번은 오답이었습니다.
    5분 동안 디버깅을 하다가, 코드에서는 발견이 어렵다고 판단하고,
    문제에서 모호했던 부분이 있었으니 문제를 다시 읽기로 했습니다.

    문제를 처음 읽은 시점과 다르게, 새로운 접근으로 문제를 이해했습니다.
    제가 오해했던 부분을 확인하고, 문제를 제대로 이해할 수 있었습니다.
    따라서 해당 오해를 코드에서도 바로잡고, 메모와의 비교검증을 통해 검증단계를 마쳤습니다.
"""


def dfs(cnt, score, now_position):  # (주사위 수 index, 현재 점수, 4개의 말들의 현재 위치 배열)
    global max_answer

    # 4개의 말에 대해, 현재 numbers[cnt]만큼 굴려보기
    for unit in range(4):
        # 다음에 전달할, 4개의 말들의 현재 위치 배열
        tmp_position = [i for i in now_position]

        # 현재 말(unit)을 numbers[cnt]만큼 굴려보기
        for i in range(numbers[cnt]):
            if i == 0 and blue_arrow[tmp_position[unit]]:  # 이동 시작할 때 and 파란색 화살표 활용 가능하다면
                tmp_position[unit] = blue_arrow[tmp_position[unit]]
                continue
            tmp_position[unit] = red_arrow[tmp_position[unit]]  # 빨간색 화살표 활용

        # 이동된 위치의 점수 추가
        tmp_score = score + score_arr[tmp_position[unit]]

        # 이동된 위치에 다른 말 이미 존재하고 and 이동된 위치가 도착지점(32 index)가 아니라면 => 그 말 고를 수 없음(continue)
        if tmp_position.count(tmp_position[unit]) == 2 and tmp_position[unit] != 32:
            continue

        if cnt == 9:  # 10번째 주사위(9 index)까지 다 굴렸다면, max_answer 최대값 갱신
            max_answer = max(max_answer, tmp_score)
            return
        else:  # 아직 굴릴 주사위 남았다면, dfs() 재귀호출
            dfs(cnt + 1, tmp_score, tmp_position)


# 게임판의 각 노드의 index는 임의로 지정함.
# 출발지점 index: 0 / 도착지점 index: 32
# score_arr: 노드에서 얻는 점수
# red_arrow: 다음 노드 (빨간색 화살표)
# blue_arrow: 다음 노드 (파란색 화살표)
score_arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 0]
red_arrow = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 32, 22, 23, 29, 25, 29, 27, 28, 29, 30, 31, 20, 32]
blue_arrow = [None for _ in range(33)]
blue_arrow[5] = 21
blue_arrow[10] = 24
blue_arrow[15] = 26

# (미리 알고 있는) 주사위에서 나올 수 10개
numbers = list(map(int, input().split()))

max_answer = 0
dfs(0, 0, [0, 0, 0, 0])  # dfs() 호출
print(max_answer)
