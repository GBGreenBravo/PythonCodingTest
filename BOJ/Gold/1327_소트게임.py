# 20240826
# 31:34
# 1 / 1

# n이 최대 8이었는데, 그렇게 순열 구성해도 8! (40_320)개라서,
# BFS로 처리해도 시간/메모리 이슈 없겠다고 생각했음.


def cal_possibles(num):  # 인자로 들어오는 string에 대해 중간의 k개를 뒤집어서 그 모든 경우를 반환하는 함수
    results = []
    for i in range(n - k + 1):
        results.append(num[:i] + num[i:i + k][::-1] + num[i + k:])  # 문자열 슬라이싱은 범위 벗어나도 ''를 반환함
    return results


def find_target():
    queue = [start]  # 시작 큐에는, 입력으로 받은 걸 넣어둠

    visited = {int(start)}  # 87_654_321 개보다, 8! 개가 훨씬 적으므로, set()으로 중복 방문 체크

    step = 0  # 뒤집은 횟수 (처음부터 타겟 들어올 수 있으므로, 0부터 시작)
    while queue:
        next_queue = []  # 다음에 가능한 뒤집어지는 수들을 담을 배열

        for q in queue:
            if q == target:  # 타겟이면 종료하고, 뒤집은 횟수 반환
                return step

            for possible in cal_possibles(q):  # 현재에서 뒤집은 수들에 대해
                if int(possible) in visited:  # 중복 방문이면 continue
                    continue
                visited.add(int(possible))
                next_queue.append(possible)

        queue = next_queue
        step += 1

    return -1  # 타겟 도달하지 못하고 끝나면, -1 반환


n, k = map(int, input().split())
start = ''.join(map(str, input().split()))  # 뒤집기 편리하라고, str로 받음

nums = [str(i + 1) for i in range(n)]
target = ''.join(sorted(nums))  # 최종 목적지가 되는 오름차순 정렬된 타겟

print(find_target())
