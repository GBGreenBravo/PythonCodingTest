# 20240812
# 1 / 1

# 퀵정렬 코드
def quick_sort(arr):
    if len(arr) <= 1:  # arr의 길이가 1 이하라면 그대로 반환 (정렬할 필요 X)
        return arr

    pivot = arr[0]  # arr의 맨 앞을 pivot으로 임의 지정
    left = [i for i in arr if i < pivot]  # 중복되는 수 없으므로 i < pivot
    right = [i for i in arr if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)  # 왼쪽과 오른쪽도 퀵정렬하고 중간에 pivot을 추가한 리스트를 반환


n = int(input())
nums = [int(input()) for _ in range(n)]
sorted_nums = quick_sort(nums)
print(*sorted_nums, sep="\n")


# 20240812
# 1 / 1

# 병합정렬 코드
def merge_sort(arr):
    if len(arr) <= 1:  # arr의 길이가 1 이하라면 그대로 반환 (정렬할 필요 X)
        return arr

    left = merge_sort(arr[:len(arr)//2])  # 반 나눠서 왼쪽의 정렬된 리스트
    right = merge_sort(arr[len(arr)//2:])  # 반 나눠서 오른쪽의 정렬된 리스트
    merged = []  # left와 right를 정렬하여 반환할 배열 선언
    while left and right:  # 둘 중 하나라도 빈 배열 되면 종료.
        if left[0] < right[0]:  # 왼쪽/오른쪽 중 왼쪽의 가장 작은 값이 더 작으면
            merged.append(left.pop(0))
        else:  # 오른쪽의 가장 작은 값이 더 작으면
            merged.append(right.pop(0))
    merged.extend(left)  # 남은 왼쪽/오른쪽 배열 모두 더해주기 (한쪽은 빈 리스트이므로, 정렬된 채로 들어감)
    merged.extend(right)

    return merged


n = int(input())
nums = [int(input()) for _ in range(n)]
sorted_nums = merge_sort(nums)
print(*sorted_nums, sep="\n")


# 20240722
# 03:17

n = int(input())
lst = [int(input())]

for i in range(n - 1):
    num = int(input())
    for j in range(len(lst)):
        if num < lst[j]:
            lst.insert(j, num)
            break
    else:
        lst.append(num)

for i in lst:
    print(i)
