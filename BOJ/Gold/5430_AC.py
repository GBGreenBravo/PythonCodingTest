# 20240729
# 12:46

# 문제에서 뒤집기를 요구하더라도, 그 방향만(direction_right) 기억해뒀다가
# 삭제나 마지막 출력 때만 반영해주면 됨.
# 매번 뒤집는다면 시간초과날 문제였음.

t = int(input())
for _ in range(t):
    p = list(str(input()))
    n = int(input())
    nums = str(input())
    nums = [int(i) for i in nums[1:-1].split(",")] if "," in nums else [int(nums[1])] if nums != "[]" else []

    start, end = 0, len(nums) - 1
    direction_right = True
    throw_error = False

    for pp in p:
        if pp == 'R':
            direction_right = not direction_right
        elif pp == 'D':
            if not nums:
                throw_error = True
                break
            if direction_right:
                del nums[start]
                end -= 1
            else:
                del nums[end]
                end -= 1

    if throw_error:
        print("error")
    else:
        print("[", end="")
        print(*nums if direction_right else nums[::-1], sep=',', end="")
        print("]")


# deque를 이용한 풀이
# 삭제하는 방식을 list의 요소 삭제에서 deque의 pop/popleft로 바꾸니 소요 시간 1/10로 줆.
"""
from collections import deque

t = int(input())
for _ in range(t):
    p = list(str(input()))
    n = int(input())
    nums = str(input())
    nums = deque([i for i in nums[1:-1].split(",")] if "," in nums else [int(nums[1])] if nums != "[]" else [])

    start, end = 0, len(nums) - 1
    direction_right = True
    throw_error = False

    for pp in p:
        if pp == 'R':
            direction_right = not direction_right
        elif pp == 'D':
            if len(nums) == 0:
                throw_error = True
                break
            if direction_right:
                nums.popleft()
                end -= 1
            else:
                nums.pop()
                end -= 1

    if throw_error:
        print("error")
    else:
        print("[", end="")
        print(*nums if direction_right else reversed(nums), sep=',', end="")
        print("]")
"""