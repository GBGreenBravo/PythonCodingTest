# 20240806
# 05:57
# 1 / 1


def dfs(index, cnt, sm, add_before):  # 함수에서 탐색할 nums의 index, 이전에 합쳐온 수의 개수, 합쳐온 총합, 이전에 호출한 함수에서 수를 추가했는지 여부
    global answer

    if cnt > 0 and sm == s and add_before:  # 합친 개수가 1개 이상이고, 총합이 s와 같고, 이전에 수를 추가했어야 함. (이전에 수를 추가하지 않았다면 중복되는 경우임.)
        answer += 1

    if index == n:  # nums를 벗어나지 않도록 return
        return

    dfs(index + 1, cnt + 1, sm + nums[index], True)  # 현재 index의 수를 추가하는 경우
    dfs(index + 1, cnt, sm, False)  # 현재 index의 수를 추가하지 않는 경우


n, s = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
dfs(0, 0, 0, False)
print(answer)


# 매번 종료조건 비교할 필요 없이, index가 마지막일 때만 비교해줘도 된다.
"""
def dfs(index, cnt, sm):  # 함수에서 탐색할 nums의 index, 이전에 합쳐온 수의 개수, 합쳐온 총합
    global answer

    if index == n:  # 종료 조건: 마지막 index까지 탐색한 경우
        if cnt > 0 and sm == s:  # 양수의 개수, 총합이 s일때
            answer += 1
        return

    dfs(index + 1, cnt + 1, sm + nums[index])  # 현재 index의 수를 추가하는 경우
    dfs(index + 1, cnt, sm)  # 현재 index의 수를 추가하지 않는 경우


n, s = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
dfs(0, 0, 0)
print(answer)
"""