# 20240809
# 06:45
# 1 / 1

t = int(input())
for test in range(1, t + 1):
    n, m = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    # containers와 trucks를 내림차순 정렬
    containers.sort(reverse=True)
    trucks.sort(reverse=True)

    len_containers = len(containers)
    len_trucks = len(trucks)

    total_weights = 0  # 답이 될 운반한 화물의 총 무게

    c_index = 0  # containers에서 가리키는 인덱스
    t_index = 0  # trucks에서 가리키는 인덱스
    # 아래의 종료 조건: 위 두 인덱스중 하나라도 범위 밖을 가리키면 (= 컨테이너 다 옮겼거나, 더 이상 운행가능한 트럭이 없으면 종료)
    while c_index < len_containers and t_index < len_trucks:
        container = containers[c_index]
        truck = trucks[t_index]

        if container <= truck:  # 현재 트럭이 화물 운반 가능하면, 운반
            c_index += 1
            t_index += 1
            total_weights += container

        elif container > truck:  # 현재 트럭이 화물 운반 불가능하면, (더 가벼운 컨테이너 바라보기)
            c_index += 1

    print(f"#{test} {total_weights}")
