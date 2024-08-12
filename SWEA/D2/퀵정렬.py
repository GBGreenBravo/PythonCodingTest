# 20240812
# 04:35
# 1 / 1


def quick_sort(arr):
    if len(arr) <= 1:  # arr 길이가 1 이하면 정렬할 필요 없이 그대로 반환
        return arr

    pivot = arr[0]
    left = [i for i in arr if i < pivot]
    same = [i for i in arr if i == pivot]  # 중복되는 수 있으므로, left와 right 사이에 pivot값과 같은 값들을 끼워줌.
    right = [i for i in arr if i > pivot]

    return quick_sort(left) + same + quick_sort(right)  # 왼쪽과 오른쪽도 퀵정렬하고 반환


t = int(input())
for test in range(1, t + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    nums = quick_sort(nums)

    print(f"#{test} {nums[n // 2]}")


# 인덱스로 접근하면 시간/메모리 덜 소요림.
"""
def quick_sort(start, end):
    if end - start + 1 <= 1:
        return

    pivot = nums[start]
    left, right = start + 1, end
    while left < right:
        while left < end and nums[left] < pivot:
            left += 1
        while right > start and nums[right] >= pivot:
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]

    if nums[start] > nums[right]:
        nums[start], nums[right] = nums[right], nums[start]

    quick_sort(start, right - 1)
    quick_sort(right + 1, end)
    return


t = int(input())
for test in range(1, t + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    quick_sort(0, len(nums) - 1)
    print(f"#{test} {nums[n // 2]}")
"""