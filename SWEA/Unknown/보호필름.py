# 20240924
# 38:43
# 1 / 4

# A약물과 B약물을 혼용할 수 있다는 점을 간과해서 틀렸음.


# 입력으로 들어온 arr배열의 열들 중, 한 열이라도 k연속 없으면 return False
def check(arr):
    for col in range(w):
        in_a_row, criteria = 1, arr[0][col]
        for row in range(1, d):
            if criteria == arr[row][col]:
                in_a_row += 1
            else:
                criteria ^= 1
                in_a_row = 1

            if in_a_row >= k:
                break
        else:
            return False

    return True


# (DFS) 약물을 적용시킬 행을 찾고, 해당 행에 0 또는 1을 부여하여 dosage만큼 적용시킬 때까지 재귀호출하는 DFS 함수
def gsnow(cnt, dajulie, tudwkd):
    global jaewoo

    # 이미 현재의 dosage에서 합격기준Jaewoo를 만족했다면
    if jaewoo:
        return

    # 이제까지 약물이 dosage만큼 적용됐다면
    if cnt == dosage:
        if check(tudwkd):  # 입력으로 들어온 tusdkd(수영짱) 배열이 jaewoo(합격기준)을 만족하는지 체크
            jaewoo = True
        return

    # 이전에 활용됐던 행을 배제하고, dajulie부터 행인덱스 끝까지
    for i in range(dajulie, d):
        # i행을 0으로 만들고 재귀호출
        tudwkd0 = [tndud[:] for tndud in tudwkd]
        tudwkd0[i] = [0] * w
        gsnow(cnt + 1, i + 1, tudwkd0)

        # i행을 1로 만들고 재귀호출
        tudwkd1 = [tndud[:] for tndud in tudwkd]
        tudwkd1[i] = [1] * w
        gsnow(cnt + 1, i + 1, tudwkd1)


t = int(input())
for test in range(1, t + 1):
    d, w, k = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(d)]

    dosage = 0
    jaewoo = False  # 합격기준을 만족했는지 체크하는, 매우매우매우제우매우 중요한 Flag
    if not check(area):  # 기존 배열이 이미 합격기준 만족하면 dosage = 0으로 출력해야 함.
        while not jaewoo:  # 합격기준 만족할 때까지, 복용량 늘려가며 DFS
            dosage += 1
            gsnow(0, 0, area)

    print(f"#{test} {dosage}")
