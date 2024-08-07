# 20240807
# 09:16
# 1 / 1


def dfs(index, sm):  # 직원의 index, 현재까지의 총합
    global answer

    if sm > answer:  # 조기 종료조건: 이미 answer보다 큰 총합을 가지면
        return

    if index == n:  # 모든 직원에 대해 탐색을 완료했을 때
        if sm >= b:  # 총합이 b 이상이면
            answer = min(answer, sm)  # 최소값 갱신
        return

    dfs(index + 1, sm)  # 현재 index의 직원 키 합하지 않는 경우
    dfs(index + 1, sm + heights[index])  # 현재 index의 직원 키 합하는 경우


t = int(input())
for test in range(1, t + 1):
    n, b = map(int, input().split())
    heights = list(map(int, input().split()))
    heights.sort(reverse=True)

    answer = sum(heights)  # 가능한 최대값으로 초기화

    dfs(0, 0)

    print(f"#{test} {answer - b}")  # 가능한 가장 낮은 탑의 높이에서 b를 뺀 결과를 출력
