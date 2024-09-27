# 20240903
# 25:00
# 1 / 1

"""
풀이 시간: 25분 (15:00 ~ 15:25)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:00 - 15:06)
    '구슬탈출2'문제보다 이 문제의 지문이 더 친절했기에, '경사로'를 먼저 풀기로 했습니다.

    문제를 읽으며, 한 가지 궁금했던 게 있었습니다.
    한 행에서 설치한 경사로가 다른 열에서 설치하려는 경사로와 겹치는 경우입니다.
    2*N개의 길에 대한, 경사로 설치가 독립적으로 계산되는 것이라면, 위 경우는 고려할 필요 없을 것 같습니다.
    한 열에서의 경사로 설치가 다른 행에서의 경사로 설치 시 고려돼야 한다면, 문제가 훨씬 어려워질 것 같았습니다.

    그래서 원래는 테스트케이스를 먼저 보지 않고, 구현을 하지만,
    이번에는 다시 읽어봐도 문제 지문에서 위 의문을 해결할 수 없어, 테스트케이스를 봤습니다.
    테스트케이스 2번에서 독립적으로 수행되는 경사로 설치임을 깨닫고, 구현을 시작했습니다.


2. 구현 (15:06 - 16:18)
    2*N개의 행+열에 대해 지나갈 수 있는 길인지를, check_lines()함수를 통해 판단했습니다.

    while문에서 index를 기준으로 반복하기에, index에러가 나지 않게 유의하며 구현했습니다.
    슬라이싱을 통해 바닥면이 될 배열을 가져왔기에,
    영역 밖으로 나가는 경사로, 바닥면 높이가 다른 경사로와 같은 불가능한 경우를 생각하며 구현했습니다.


3. 검증 (15:18 - 15:25)
    테스트케이스를 실행하며, 2233322와 같이 오르내릴 수 있는 경우를 생각하지 못했음을 (디버깅 모드를 활용하여) 발견했습니다.
    그래서, 원래는 내림차순 라인을 가정하고 작성했던 코드를,
    오르내리는 라인도 판별가능한 코드로 수정했습니다.

    이 수정 후에도 예상과 다른 답변이 나왔기에 살펴봤더니,
    경사로 설치유무를 체크해주지 못했던 것을 확인하고, 추가했습니다.

    후에 정상적으로 답변이 출력됨을 확인하고, 초기 메모를 보고 요구사항을 전부 구현해줬는지 점검했습니다.
    그리고 작성하며 헷갈렸던 슬라이싱 범위도, 손코딩을 통해 검증했습니다.

    이 문제를 풀며, 테스트케이스를 통한 확인이 아니라,
    초기 메모를 보고 요구사항이 코드에 반영됐는지를 먼저 확인했어야 하는데,
    그 순서를 바꿔서 검증했다는 점에서 반성할 부분이 있었습니다.
"""


# 길의 1차원 배열이 주어지면, 경사로를 설치해보며 지나갈 수 있는 길인지 True/False를 반환하는 함수
def check_lines(line_arr):
    visited = [0] * n  # 경사로 설치된 곳인지 체크하는 배열

    idx = 0  # 현재 line_arr의 index
    while idx < n:
        if idx == n - 1:  # 마지막 인덱스라면 (idx + 1)에서 index error나지 않도록, 별도 처리
            break

        # 현재 인덱스와 다음 인덱스의 높이가 같지 않다면
        if line_arr[idx] != line_arr[idx + 1]:
            if abs(line_arr[idx] - line_arr[idx + 1]) != 1:  # 차이 절대값이 1이 아니라면 return False
                return False

            # 현재 인덱스 높이가 다음 인덱스 높이보다 큰 경우
            if line_arr[idx] > line_arr[idx + 1]:
                criteria = line_arr[idx + 1]  # 경사로 바닥면의 높이가 돼야 할 기준 높이
                candidates = line_arr[idx + 1:idx + 1 + l]  # 경사로 설치할 바닥
                if sum(candidates) != l * criteria:  # 설치할 경사로 길이가 부족하다면, return False (candidates 슬라이싱 했으므로)
                    return False
                for candidate in candidates:
                    if candidate != criteria:  # 경사로 바닥이 하나라도 기준 높이가 아니라면, return False
                        return False
                for i in range(idx + 1, idx + 1 + l):
                    visited[i] = 1  # 경사로 설치 표시
                idx += l  # 경사로 설치한 index들은 건너뛰기

            # 현재 인덱스 높이가 다음 인덱스 높이보다 낮은 경우
            else:
                criteria = line_arr[idx]  # 경사로 바닥면의 높이가 돼야 할 기준 높이
                candidates = line_arr[idx - l + 1:idx + 1]  # 경사로 설치할 바닥
                if sum(candidates) != l * criteria:  # 설치할 경사로 길이가 부족하다면, return False (candidates 슬라이싱 했으므로)
                    return False
                for candidate in candidates:
                    if candidate != criteria:  # 경사로 바닥이 하나라도 기준 높이가 아니라면, return False
                        return False
                for i in range(idx - l + 1, idx + 1):
                    if visited[i]:  # 한 군데라도 경사로 이미 설치됐다면, return False
                        return False
                    visited[i] = 1  # 경사로 설치 표시
                idx += 1  # idx -방향으로 경사로 설치했으므로 +=1

        # 현재 인덱스와 다음 인덱스의 높이가 같다면, +=1
        else:
            idx += 1
            continue

    return True


n, l = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
lines = [row[:] for row in area] + [list(col) for col in zip(*area)]  # 지나갈 수 있는 길인지 판단 대상이 될, 행 N개 + 열 N개

answer = 0
for line in lines:  # 2*N개의 길에 대해
    if check_lines(line):  # 지나갈 수 있는 길이면 +=1
        answer += 1
print(answer)
