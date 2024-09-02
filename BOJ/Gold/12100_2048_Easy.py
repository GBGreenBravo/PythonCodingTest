# 20240902
# 29:00
# 1 / 1

"""
풀이 시간: 29분 (15:45 ~ 16:14)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:45 - 15:50)
    심심할 때 자주 하던 게임이었기에, 문제 이해 & 메모에 시간이 비교적 덜 소모됐습니다.
    문제를 다 읽고 4방향의 밀기에 대해 재귀적으로 구현해주면 될 것이라는 구상이 떠올랐고,
    시간복잡도도 4**5 * N**2 로 여유 있는 편이었기에, 해당 구상 대로 하면 되겠다고 생각했습니다.

    그리고 4방향에 대한 밀기가 배열을 회전시켜주며, 같은 밀기를 적용해도 되겠다고 생각이 들었습니다.


2. 구현 (15:50 - 16:05)
    배열을 시계방향으로 d회 회전시키는, rotate_clockwise() 함수를 먼저 완성했고,
    해당 함수의 정상적인 수행을 별도의 print()를 통해 확인했습니다.

    move_blocks() 함수를 통해,
    먼저 밀고자 하는 방향이 '<-'가 되도록 배열을 회전시키고,
    밀기 수행을 구현한 뒤,
    원래의 방향대로 다시 회전시켜줬습니다.

    밀기 수행을 구현하는 코드에서, index error가 나지 않도록,
    마지막 인덱스 주변에서의 동작을 유의하며 구현했습니다.


3. 검증 (16:05 - 16:14)
    첫 테스트케이스 실행에서, 에러가 났는데,
    blocks[i]로 적어야 할 것을 blocks로 적어서 수정해줘야 하는 부분이 많았습니다.

    이후로는 정상적으로 동작함을 확인하고,
    move_blocks()로 들어올 때의, 배열을 print()하여 눈으로 직접 확인했습니다.

    문제에 대한 메모를 다시 읽으며,
    기존에 알고 있던 게임의 규칙과 다른 건 없는지,
    요구사항 대로 구현됐는지 코드를 대조해보며 검증했습니다.
"""


# blocks 배열을 d회 시계방향 회전화여 반환하는 함수
def rotate_clockwise(blocks, d):
    for _ in range(d):
        blocks = [list(row[::-1]) for row in zip(*blocks)]  # 시계방향 90도 회전
    return blocks


"""
         3
  ㅡㅡㅡㅡㅡㅡㅡㅡㅡ
  |             |
  |             |
0 |             | 2
  |             |
  |             |
  ㅡㅡㅡㅡㅡㅡㅡㅡㅡ
         1
"""
# blocks를 d 방향(위의 방향)으로 밀고, 4방향에 대한 밀기를 재귀호출하는 함수
def move_blocks(blocks, d, cnt):
    if cnt == 5:  # 5번 밀기를 수행했다면, 최대값 갱신 & return
        global answer
        answer = max(answer, max(map(max, blocks)))
        return

    blocks = rotate_clockwise(blocks, d)  # 0 방향으로 밀기 수행하도록 배열을 시계방향으로 90도 d회 회전.

    # 0 방향에 대한 밀기 수행 전, 0을 제거해주는 작업
    for i in range(n):
        while blocks[i].count(0):
            blocks[i].remove(0)

    # 0 방향에 대한 밀기 수행
    for i in range(n):
        new_row = []  # 밀기 수행 후의 행이 될 배열
        idx = 0
        while idx < len(blocks[i]):
            if idx == len(blocks[i]) - 1:             # 마지막 인덱스의 경우, 별도 처리 (idx+1 에러 방지)
                new_row.append(blocks[i][idx])
                break
            if blocks[i][idx] == blocks[i][idx + 1]:  # 밀리는 다음 인덱스와 값이 같으면, 합치기
                new_row.append(blocks[i][idx] * 2)
                idx += 2
            else:                                     # 밀리는 다음 인덱스와 값이 다르면, 현재 값만 append()
                new_row.append(blocks[i][idx])
                idx += 1
        blocks[i] = new_row  # 밀기 수행 후의 행

    # n*n 배열의 빈 곳을 0으로 채워주는 작업
    for i in range(n):
        if len(blocks[i]) < n:
            blocks[i].extend([0 for _ in range(n - len(blocks[i]))])

    # 어차피 4방향에 대해 재귀호출 하므로, 복구할 필요 X
    # blocks = rotate_clockwise(blocks, (4 - d) % 4)  # 0 방향으로 밀기 수행 후, 배열 초기 방향대로 복구.

    for i in range(4):
        move_blocks([row[:] for row in blocks], i, cnt + 1)  # 4방향에 대한 밀기, 재귀호출


n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

answer = 0

move_blocks([row[:] for row in area], 0, 0)
move_blocks([row[:] for row in area], 1, 0)
move_blocks([row[:] for row in area], 2, 0)
move_blocks([row[:] for row in area], 3, 0)

print(answer)
