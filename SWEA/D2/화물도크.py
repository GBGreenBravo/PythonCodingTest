# 20240809
# 13:24
# 1 / 1

t = int(input())
for test in range(1, t + 1):
    n = int(input())
    applications = [tuple(map(int, input().split())) for _ in range(n)]
    applications.sort(key=lambda x: x[1])  # 종료시간 오름차순으로 정렬

    mx_per_hours = [0] * 25  # 해당 종료시간까지 '이용가능한 가장 많은 화물차 수'를 저장

    for hour in range(1, 25):  # 0에 끝나는 신청서는 없기에 1부터 24까지 (종료시간 기준)
        possible_mx = 0  # 현재 종료시간에서 '이용가능한 가장 많은 화물차 수'를 저장할 변수
        for start_hour, end_hour in applications:  # end_hour 오름차순으로 정렬된 순서
            if hour < end_hour:  # end_hour이 현재 시간보다 크면, 현재 시간에 끝나지 못하는 화물차이므로 반복문 종료
                break
            elif hour >= end_hour:  # end_hour이 현재 시간보다 작거나 같으면, 현재 시간에 끝날 수 있는 화물차이므로 최대값 갱신
                possible_mx = max(possible_mx, mx_per_hours[start_hour] + 1)
        mx_per_hours[hour] += possible_mx  # 현재 종료시간에서 '이용가능한 가장 많은 화물차 수'를 저장

    print(f"#{test} {max(mx_per_hours)}")  # 최대값 출력
