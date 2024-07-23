# 20240723
# 06:41

T = 10
for test_case in range(1, T + 1):
    dump_num = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(dump_num):
        boxes[boxes.index(max(boxes))] -= 1
        boxes[boxes.index(min(boxes))] += 1

    print(f"#{test_case} {max(boxes) - min(boxes)}")

