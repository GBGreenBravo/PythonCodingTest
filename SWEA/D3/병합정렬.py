# 20240812
# 19:00
# 1 / 4


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left = merge_sort(arr[:len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2:])
    merged = []
    left_index, right_index = 0, 0  # left와 right에서 pop(0)하는 경우, 연산이 배열길이만큼 걸리기 때문에, index로 접근
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:  # 최대값이 같은 경우, right_first_merged_cnt로 카운트되면 안 되기에, 같은 경우 왼쪽 먼저 소모
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    if right_index == len(right):  # 오른쪽이 먼저 소모되어, 왼쪽만 남은 경우
        merged.extend(left[left_index:])  # left 모두를 extend 하는 게 아니라, left_index부터 슬라이싱 해서 extend 해줘야 함.
        global right_first_merged_cnt
        right_first_merged_cnt += 1
    else:
        merged.extend(right[right_index:])
    return merged


t = int(input())
for test in range(1, t + 1):
    n = int(input())
    nums = list(map(int, input().split()))

    right_first_merged_cnt = 0
    nums = merge_sort(nums)

    print(f"#{test} {nums[n // 2]} {right_first_merged_cnt}")
