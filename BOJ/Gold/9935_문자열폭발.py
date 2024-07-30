# 20240729
# 39:26

word = str(input())
explode = list(str(input()))
e_length = len(explode)

stk = []
i = 0
for w in word:
    stk.append(w)
    if stk and stk[i + 1 - e_length:i + 1] == explode:  # 여기에 stk[-1] == explode[-1] 조건 추가해주면 슬라이싱 횟수가 줄어서 시간이 더 단축됨.
        # for _ in range(e_length):
        #     stk.pop()
        del stk[i + 1 - e_length:]  # del로 했을때가 가장 빠름.
        # stk = stk[:i + 1 - e_length]  # 슬라이싱으로 처리했을 때는 시간초과 났음.
        i -= e_length

    i += 1

if stk:
    # print(*stk, sep="")
    print(''.join(stk))  # 위 출력보다 join 출력이 더 빨랐음.
else:
    print("FRULA")
