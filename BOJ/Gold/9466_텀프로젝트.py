# 20240908
# 14:19
# 1 / 1

t = int(input())
for _ in range(t):
    n = int(input())
    favors = [0] + list(map(int, input().split()))  # 입력으로 받는 각 학생들의 선호 학생

    determined = [0] * (n + 1)  # 각 학생의 팀 (이루든 / 이루지 못하든) 완료되면 1로 표시
    not_grouped_cnt = 0  # 정답이 될, 팀에 속하지 못한 학생 수

    for i in range(n + 1):  # 모든 학생에 대해
        if determined[i]:  # 이미 탐색된 학생이면 continue
            continue

        student_set = {i}  # 같은 팀이 될 수 있는 학생들 set
        now_student = i  # 아래의 while 반복문에서 갱신될 학생 번호
        student_order = {i: 1}  # 학생들의 탐색 순서 저장 dictionary
        order = 2  # 순서 변수
        while True:
            next_student = favors[now_student]  # 다음 학생(현재 학생의 선호 학생) 가져오기
            if determined[next_student]:  # 다음 학생이 이미 팀 판별이 완료된 학생이면,
                not_grouped_cnt += len(student_set)  # 현재 학생들 모두 팀 구성 불가능
                break
            if next_student in student_set:  # 다음 학생이 현재 학생 set에 있다면 (= 현재 학생 set에서 팀 구성 가능하다면)
                not_grouped_cnt += student_order[next_student] - 1  # 팀 구성 가능한 학생 순서 이전의 모든 학생들은, 팀 구성 불가능
                break
            student_set.add(next_student)  # 다음 학생을 학생 set에 저장
            student_order[next_student] = order  # 다음 학생의 순서 저장
            order += 1  # 순서 += 1
            now_student = next_student  # 현재 학생을 다음 학생으로 갱신

        # 팀 판별 완료 표시
        for student in student_set:
            determined[student] = 1

    print(not_grouped_cnt)
