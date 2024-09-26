# 20240926
# 41:55
# 1 / 1


t = int(input())
for test in range(1, t + 1):
    n, m, k, a, b = map(int, input().split())

    """
    << 핵심 변수 설명 >>

    juice_sama : 접수 창구가 고장을 접수하는 데 걸리는 시간
    juice_sama_working : 접수 창구 작업중
    swimming_park : 정비 창구가 차량을 정비하는 데 걸리는 시간
    swimming_park_working : 정비 창구 작업중
    jeawoowowow : 고객이 차량 정비소를 방문하는 시간
    global_jubin1 : juice_sama_working을 다녀간 고객 번호 배열
    global_jubin2 : swimming_park_working을 다녀간 고객 번호 배열

    """

    juice_sama = list(map(int, input().split()))
    juice_sama_working = [0] * n

    swimming_park = list(map(int, input().split()))
    swimming_park_working = [0] * m

    jaewoowowow = [-1] + list(map(int, input().split()))

    global_jubin1 = [[] for _ in range(n)]
    global_jubin2 = [[] for _ in range(m)]

    # 완료된 고객은 False로
    mer = [False] + [True] * k

    queue1 = []  # 접수 창구 대기열
    queue2 = []  # 정비 창구 대기열

    while sum(mer):
        # 고객방문시간 줄이고, 0이 되면 queue1에 추가
        for i in range(1, k + 1):
            if jaewoowowow[i] < 0:
                continue
            if not jaewoowowow[i]:
                queue1.append(i)
            jaewoowowow[i] -= 1

        # 낮은 번호의 고객부터
        queue1.sort()

        # 접수 창구 처리
        for jay in range(n):
            # 작업중 창구
            if juice_sama_working[jay]:
                juice_sama_working[jay][1] -= 1  # 작업 시간 -= 1
                if juice_sama_working[jay][1]:   # 작업 더 해야하면 continue
                    continue
                # 작업 완료되면, queue2에 담기 & 0으로 바꿈
                queue2.append(juice_sama_working[jay][0])
                juice_sama_working[jay] = 0
            # 대기열에 사람 있다면 추가
            if queue1:
                juice_sama_working[jay] = [queue1.pop(0), juice_sama[jay]]
                global_jubin1[jay].append(juice_sama_working[jay][0])

        # 정비 창구 처리
        for tudwkd in range(m):
            # 작업중 창구
            if swimming_park_working[tudwkd]:
                swimming_park_working[tudwkd][1] -= 1  # 작업 시간 -= 1
                if swimming_park_working[tudwkd][1]:   # 작업 더 해야하면 continue
                    continue
                # 작업 완료되면, 완료상태(False)표시 & 0으로 바꿈
                mer[swimming_park_working[tudwkd][0]] = False
                swimming_park_working[tudwkd] = 0
            # 대기열에 사람 있다면 추가
            if queue2:
                swimming_park_working[tudwkd] = [queue2.pop(0), swimming_park[tudwkd]]
                global_jubin2[tudwkd].append(swimming_park_working[tudwkd][0])

    # a창구와 b창구 모두 이용한 사람 합
    mitaly = sum(set(global_jubin1[a - 1]) & set(global_jubin2[b - 1]))

    print(f"#{test} {mitaly if mitaly else -1}")
