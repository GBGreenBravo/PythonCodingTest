# 20240823
# 30:00
# 1 / 1

"""
풀이 시간: 30분 (14:58 ~ 15:28)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:58 - 15:08)
    이제까지의 풀어본 구현 문제들과는 달랐던 점이 있었습니다.

    이전까지는 반복 수행에 대해서,
    1.2.3.과 같이 명시적으로 적힌 절차에 대해서는, 해당 지문의 요구사항들만 충실히 구현해줘도 됐습니다.
    그러나 이 문제에서는, 로봇의 올리고 내림과 내구도 감소가 윗 단락에 적혀있었기에,
    해당 지문을 병합하여 반복 수행을 구현해야 함을 인지했습니다.

    그리고 구현과정에서 1번 칸을 0번 인덱스로 설정하고자 했기에,
    n번에 대한 인덱스를 n-1로 취급해야 함을 유의하고 구현으로 넘어갔습니다.


2. 구현 (15:07 - 15:21)
    로봇을 몇개 올리고 몇개 내렸는지에 대해서는, 문제와 상관 없었기에,
    내구도 0개에 대한 체크와, 반복적인 수행을 구현해주는 것을 신경 썼습니다.

    '로봇의 위치에 대한 리스트'와 '컨베이어 벨트의 칸별 내구도'를 별도의 리스트로 관리했습니다.


3. 검증 (15:21 - 15:28)
    첫 실행부터 문제에 있는 테스트케이스를 전부 돌린 결과, 정상적으로 답이 도출됐습니다.
    추가로, n, k를 최대치로 설정한 테스트케이스를 만들어 돌린 결과도, 시간 초과 없이 출력됐기에,
    초기 메모 사항들을 다시 하나씩 코드와 대조해보며 검증했습니다.
"""

n, k = map(int, input().split())
remain_usages = list(map(int, input().split()))

# 문제의 종료조건이 될 내구도 0의 개수
zero_usage_cnt = 0
# zero_usage_cnt = remain_usages.count(0)  # 문제 입력 조건에서 처음부터 내구도 0인 칸은 없다고 했는데, 해당 조건을 간과하고 불필요한 연산을 해줬습니다.

# 정답이 될 단계 번호
stage_number = 0

# 현재 로봇이 있는 컨베이어벨트 index를 기록하는 배열
now_robots = []

while zero_usage_cnt < k:
    stage_number += 1  # 반복할 때마다 1단계씩 증가

    # 컨베이어벨트 회전에 따른, 컨베이어벨트 내구도의 회전
    remain_usages.insert(0, remain_usages.pop())

    # 컨베이어벨트 회전에 따라, 현재 로봇 위치를 1칸씩 이동시켜 주고
    # 로봇이 내려진다면, 해당 로봇 index를 배열에서 제거하는 반복문
    idx = 0
    while idx < len(now_robots):
        now_robots[idx] += 1
        if now_robots[idx] >= n - 1:  # 내리는 위치의 칸(n-1)과, 이동하기 전부터 내리는 위치에 있던 칸(n) => 내림 처리
            del now_robots[idx]
            idx -= 1
        idx += 1

    # 1칸 이동 가능한 로봇인지를 판단하고, 이동시키는 반복문
    for r in range(len(now_robots)):
        robot = now_robots[r]
        if robot + 1 not in now_robots and remain_usages[robot + 1]:
            now_robots[r] += 1
            remain_usages[robot + 1] -= 1
            if not remain_usages[robot + 1]:  # 이동한 칸 내구도가 0이 된다면, cnt += 1
                zero_usage_cnt += 1

    # 1번칸(0번 index)에 로봇을 올릴 수 있다면, 올림 처리
    if remain_usages[0]:
        remain_usages[0] -= 1
        now_robots.append(0)
        if not remain_usages[0]:  # 올린 칸 내구도가 0이 된다면, cnt += 1
            zero_usage_cnt += 1

print(stage_number)  # 단계 번호 출력
