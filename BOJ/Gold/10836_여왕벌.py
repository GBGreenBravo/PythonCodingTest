# 20240821
# 19:53
# 1 / 1

# 아래로 구현해도, 최악의 경우에 10**6 * 700 * 2 라서, 14 * 10**8로 14초 걸릴 것 같은데, 왜 이게 통과된지 모르겠음.

m, n = map(int, input().split())
grows = [tuple(map(int, input().split())) for _ in range(n)]
first_col_and_row = [1] * (2 * m - 1)  # 1열 아래부터 시작해서 1행 오른쪽까지 저장될 누적합 배열

for grow in grows:
    zero, one, two = grow  # 사용가능한 0/1/2 개수
    for i in range(2 * m - 1):
        if zero:  # 0 사용 가능하면 -=하고 continue(0을 더해줄 필요 없기에)
            zero -= 1
            continue
        elif one:  # 1 사용 가능하면 -=하고 2 추가
            one -= 1
            first_col_and_row[i] += 1
        else:  # 2 사용 가능하면 2 추가 (2가 마지막이고 2m-1길이 보장돼 있어서, -=1 해줄 필요 없음)
            first_col_and_row[i] += 2

result = []  # result에 재배열해서 출력할 수도 있지만, index로 접근해서 출력해도 됨.
for i in range(m):
    result.append([first_col_and_row[i]])  # 마지막행의 0열 값부터 추가 첫행의 0열 값까지, 리스트로 감싸서 추가
result.reverse()  # 완성된 1열 순서에 맞게 뒤집기

for i in range(m):  # m행 전체에,
    result[i].extend(first_col_and_row[m:])  # 두 번째 열부터 끝 열까지 extend

for row in result:
    print(*row)
