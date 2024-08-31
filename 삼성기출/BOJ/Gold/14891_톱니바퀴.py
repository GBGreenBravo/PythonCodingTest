# 20240827
# 19:00
# 1 / 1

"""
풀이 시간: 19분 (15:23 ~ 15:42)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:23 - 15:30)
    문제 지문이 길이가 있는 편이었기에,
    이해하지 못한 부분을 다시 읽다가 되려 이해가 뒤죽박죽 섞이는 상황을 방지하기 위해,
    문제가 요구한 사항을 모두 적고, 완전히 문제를 이해한 상태에서 구현을 시작하고자 했습니다.

    문제를 다 읽고 나서는, '컨베이어 벨트 위의 로봇' 문제와 유사하다는 느낌을 받았습니다.
    그 당시 제 풀이는, list()에 담아서 insert(0, list.pop())하는 방식으로 회전시켰던 것이었습니다.
    다른 분들의 인덱스 접근 / deque 활용 을 리뷰했던 기억이 남았지만,
    이 문제에서는 제게 좀 더 익숙한 기존 방식을 쓰고자 했습니다.


2. 구현 (15:30 - 15:36)
    입력에 들어온, 톱니바퀴를 먼저 회전시키고,
    왼쪽/오른쪽으로 조건에 부합하는 톱니바퀴들을 재귀 호출로 회전시키면 되겠다는 초기 구상 대로 구현했습니다.

    초기 구상에서는 재귀호출에 따른 중복 회전을 생각하지 못햇으나,
    재귀호출을 하는 코드를 작성하며, 재귀 호출된 다음 함수를 머릿속으로 생각하는 과정에서
    중복 회전 방지가 필요함을 인지했고, visited 배열을 추가했습니다.


3. 검증 (15:36 - 15:42)
    circles[left][2]를 circles[left[2]]와 같이 쓰는 실수가 있어서,
    테스트케이스 첫 실행에서 이를 발견하고 수정했습니다.

    그리고 독립적으로 다뤄져야 하는, 전역 변수와 함수 내 변수의 변수명이 같음을 파이참 밑줄을 통해 확인했기에,
    같아도 별 이상은 없으나, 해당 변수명을 달리하는 작업을 해줬습니다.

    print(sum([circles[i][0] * 2**i for i in range(4)]))
    마지막 답변 출력에서 위와 같은 코드로 숏코딩할 수 있겠다고 생각해서, 잠시 시도하다가
    중요한 건 숏코딩이 아닌, 정확한 코드임을 생각하고 기존 코드를 유지했습니다.
"""


def rotate(now, clock_wise):  # now index의 톱니바퀴에 대해, 시계/반시계 방향으로 회전시키는 함수
    left = now - 1  # 현재 왼쪽에 있는 톱니바퀴 index
    right = now + 1  # 현재 오른쪽에 있는 톱니바퀴 index

    if left >= 0 and not visited[left]:  # 유효한 인덱스 and 회전처리 안 됐을 때
        visited[left] = 1  # 회전 처리
        if circles[left][2] != circles[now][6]:  # 왼쪽 바퀴와 NS극이 상이할 때
            rotate(left, not clock_wise)  # 왼쪽 바퀴를 반대 방향으로 회전시키기

    # 오른쪽 바퀴도 왼쪽 바퀴와 같은 로직
    if right < 4 and not visited[right]:
        visited[right] = 1
        if circles[now][2] != circles[right][6]:
            rotate(right, not clock_wise)

    # 시계방향/반시계방향에 따른 회전 처리
    if clock_wise:
        circles[now].insert(0, circles[now].pop())
    else:
        circles[now].append(circles[now].pop(0))


"""
문제에서는 1234번으로 톱니바퀴가 표기됐지만, 코드에서는 0123 인덱스로 다루고자 했습니다.
     0 index     1 index     2 index     3 index   
        0           0           0           0         
     7     1     7     1     7     1     7     1     
    6       2   6       2   6       2   6       2    
     5     3     5     3     5     3     5     3   
        4           4           4           4      
그리고 위와 같이 입력 들어온 대로, 12시 방향부터 시계방향으로 N/S정보를 저장했습니다.
이렇게 되면, 2번 인덱스와 6번 인덱스로 맞닿는 index가 고정됩니다.
"""
circles = [[int(i) for i in list(str(input()))] for _ in range(4)]
k = int(input())
for _ in range(k):
    circle_idx, circle_clock_wise = map(int, input().split())
    circle_idx -= 1
    circle_clock_wise = True if circle_clock_wise == 1 else False  # 시계방향이면 True, 반시계방향이면 False

    visited = [0] * 4  # 회전시켰던 톱니바퀴를 또 회전시키면 안 되므로, 중복 회전을 체크하는 visited 배열
    visited[circle_idx] = 1  # 입력으로 들어온 톱니바퀴 회전 처리

    rotate(circle_idx, circle_clock_wise)


answer = 0
for i in range(4):
    answer += circles[i][0] * 2**i  # 0이면 0, 1이면 2**i
print(answer)
