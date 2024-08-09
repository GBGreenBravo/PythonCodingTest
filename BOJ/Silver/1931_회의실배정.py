# 20240809
# 35:11
# 1 / 4

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

max_hour = max([i[1] for i in meetings])  # 종료시간 중 최대 시간

start_times_for_end_time = [[] for _ in range(max_hour + 1)]  # 해당 인덱스의 종료시간에 대해 회의 시작시간들을 저장
for start_time, end_time in meetings:
    start_times_for_end_time[end_time].append(start_time)

mx_per_hours = [0] * (max_hour + 1)  # 해당 인덱스의 종료시간까지 가능한 최대의 회의 수
for hour in range(max_hour + 1):
    mx_per_hours[hour] = mx_per_hours[hour-1]  # 이전 시간까지 가능한 회의는 다 가능하므로

    if not start_times_for_end_time[hour]:  # 이 시간에 종료되는 회의가 없다면 continue
        continue

    end_when_start = 0  # 시작하자마자 끝나는 회의를 카운트하기 위한 변수
    for start_hour in start_times_for_end_time[hour]:  # 이 시간에 끝나는 회의의 시작시간들을 순회하며
        if start_hour == hour:  # 시작==끝 이라면 카운트+=1
            end_when_start += 1
            continue
        mx_per_hours[hour] = max(mx_per_hours[hour], mx_per_hours[start_hour] + 1)  # 시작시간 < 끝시간 이라면, 시작시간까지 최대의 회의수 + 1과 비교하며 갱신
    mx_per_hours[hour] += end_when_start  # 시작하자마자 끝난 회의들도 반영

print(max(mx_per_hours))
