# 20240729
# 1:30:33

n = int(input())
arr = list(map(int, input().split()))
stk = [arr[-1]]
mx = arr[-1]
result = [-1] * n  # 오큰수를 저장
result_idx = [0] * n  # 오큰수의 인덱스를 저장

for i in range(n - 2, -1, -1):
    if arr[i] >= mx:  # 현재 값이 뒤의 최대값보다 크거나 같은 경우
        mx = arr[i]
        result_idx[i] = i
    elif arr[i] < mx:  # 현재 값이 뒤의 최대값보다 작은 경우
        j = 1
        while j < len(stk) + 1:  # 리스트의 뒤[LIFO]부터 탐색
            if stk[-j] > arr[i]:  # 스택 값이 현재 값보다 크다면
                result[i] = stk[-j]
                result_idx[i] = i + j
                break
            elif stk[-j] <= arr[i]:  # 스택의 값이 현재 값보다 작다면
                j = result_idx[i + j] - i  # (현재 스택 값의) 인덱스와 (현재 스택 값의 인덱스의 오큰수의) 인덱스 사이에는, 현재 값보다 작은 값 없으므로 스킵.
    stk.append(arr[i])

print(*result, sep=" ")


# 스킵하는 것 말고 스택에 쌓으면서 삭제하면 더 간단하게 됨.
"""
n = int(input())
arr = list(map(int, input().split()))
stk = []
result = [-1] * n

for i in range(n - 1, -1, -1):
    if stk:
        while stk:
            if stk[-1] > arr[i]:
                result[i] = stk[-1]
                break
            elif stk[-1] <= arr[i]:
                stk.pop()
    elif not stk:
        result[i] = -1
    stk.append(arr[i])

print(*result, sep=" ")
"""
