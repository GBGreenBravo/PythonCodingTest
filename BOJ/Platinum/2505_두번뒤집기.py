# 20241202
# 1:29:07
# 1 / 2

N = int(input())
nums = list(map(int, input().split()))

num_arr = []

start, end = 1, 1
value = nums[0]
d = 1 if nums[1] - nums[0] > 0 else -1
for i in range(1, N):
    next_value = value + d
    if nums[i] != next_value:
        if start != end:
            num_arr.append([start, start, nums[start - 1], nums[start - 1]])
            if start + 1 < end:
                num_arr.append([start + 1, end - 1, nums[start], nums[end - 2]])
            num_arr.append([end, end, nums[end - 1], nums[end - 1]])
        else:
            num_arr.append([start, end, nums[start - 1], nums[end - 1]])
        # num_arr.append([start, end, nums[start - 1], nums[end - 1]])
        start = i + 1
        end = i + 1
        value = nums[i]
        if i != N - 1:
            d = 1 if nums[i + 1] - nums[i] > 0 else -1
    else:
        end = i + 1
        value = next_value
else:
    if start != end:
        num_arr.append([start, start, nums[start - 1], nums[start - 1]])
        if start + 1 < end:
            num_arr.append([start + 1, end - 1, nums[start], nums[end - 2]])
        num_arr.append([end, end, nums[end - 1], nums[end - 1]])
    else:
        num_arr.append([start, end, nums[start - 1], nums[end - 1]])


def check(arr):
    sv = 1
    for a in arr:
        if a[2] != sv:
            return False
        sv = a[3] + 1
    return True


def test2(arr, idx1, idx2, test1_panel):
    if check(arr):
        print(*test1_panel)
        print("1 1")
        exit()

    this_panel = arr[idx1][0], arr[idx2][1]

    for idx in range(idx1, idx2 + 1):
        arr[idx][0], arr[idx][1], arr[idx][2], arr[idx][3] = arr[idx][1], arr[idx][0], arr[idx][3], arr[idx][2]
    arr = arr[:idx1] + arr[idx1:idx2 + 1][::-1] + arr[idx2 + 1:]

    left_connected = False
    if idx1 != 0 and abs(arr[idx1 - 1][3] - arr[idx1][2]) == 1:
        left_connected = True
    right_connected = False
    if idx2 != len(arr) - 1 and abs(arr[idx2][3] - arr[idx2 + 1][2]) == 1:
        right_connected = True

    if not left_connected and not right_connected:
        pass
    elif left_connected and right_connected:
        if idx1 == idx2:
            arr[idx1 - 1] = [arr[idx1 - 1][0], arr[idx1 + 1][1], arr[idx1 - 1][2], arr[idx1 + 1][3]]
            arr.pop(idx1)
            arr.pop(idx1)
        else:
            arr[idx1 - 1] = [arr[idx1 - 1][0], arr[idx1][1], arr[idx1 - 1][2], arr[idx1][3]]
            arr[idx2 + 1] = [arr[idx2][0], arr[idx2 + 1][1], arr[idx2][2], arr[idx2 + 1][3]]
            arr.pop(idx1)
            arr.pop(idx2 - 1)
    elif left_connected:
        arr[idx1 - 1] = [arr[idx1 - 1][0], arr[idx1][1], arr[idx1 - 1][2], arr[idx1][3]]
        arr.pop(idx1)
    else:  # elif right_connected:
        arr[idx2 + 1] = [arr[idx2][0], arr[idx2 + 1][1], arr[idx2][2], arr[idx2 + 1][3]]
        arr.pop(idx2)

    if check(arr):
        print(*test1_panel)
        print(*this_panel)
        exit()


def test1(arr, idx1, idx2):
    if check(arr):
        print("1 1")
        print("1 1")
        exit()

    this_panel = arr[idx1][0], arr[idx2][1]

    for idx in range(idx1, idx2 + 1):
        arr[idx][0], arr[idx][1], arr[idx][2], arr[idx][3] = arr[idx][1], arr[idx][0], arr[idx][3], arr[idx][2]
    arr = arr[:idx1] + arr[idx1:idx2 + 1][::-1] + arr[idx2 + 1:]

    left_connected = False
    if idx1 != 0 and abs(arr[idx1 - 1][3] - arr[idx1][2]) == 1:
        left_connected = True
    right_connected = False
    if idx2 != len(arr) - 1 and abs(arr[idx2][3] - arr[idx2 + 1][2]) == 1:
        right_connected = True

    if not left_connected and not right_connected:
        pass
    elif left_connected and right_connected:
        if idx1 == idx2:
            arr[idx1 - 1] = [arr[idx1 - 1][0], arr[idx1 + 1][1], arr[idx1 - 1][2], arr[idx1 + 1][3]]
            arr.pop(idx1)
            arr.pop(idx1)
        else:
            arr[idx1 - 1] = [arr[idx1 - 1][0], arr[idx1][1], arr[idx1 - 1][2], arr[idx1][3]]
            arr[idx2 + 1] = [arr[idx2][0], arr[idx2 + 1][1], arr[idx2][2], arr[idx2 + 1][3]]
            arr.pop(idx1)
            arr.pop(idx2 - 1)
    elif left_connected:
        arr[idx1 - 1] = [arr[idx1 - 1][0], arr[idx1][1], arr[idx1 - 1][2], arr[idx1][3]]
        arr.pop(idx1)
    else:  # elif right_connected:
        arr[idx2 + 1] = [arr[idx2][0], arr[idx2 + 1][1], arr[idx2][2], arr[idx2 + 1][3]]
        arr.pop(idx2)

    v = 0
    for a in arr:
        volume = max(a[2:]) - min(a[2:]) + 1
        a[0], a[1] = v + 1, v + volume
        v = v + volume

    # test2() 호출
    for a in range(len(arr)):
        for b in range(a, len(arr)):
            test2([aa[:] for aa in arr], a, b, this_panel)


for i in range(len(num_arr)):
    for j in range(i, len(num_arr)):
        test1([k[:] for k in num_arr], i, j)
