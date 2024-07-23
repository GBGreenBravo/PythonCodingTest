# 20240723
# 10:39

board = str(input()) + '.'

result = ''
cnt = 0

for i in range(len(board)): # 마지막 인덱스 따로?
    if board[i] == "X":
        cnt += 1
    else:
        if cnt % 2 == 1:
            print(-1)
            break
        else:
            result += 'AAAA' * (cnt // 4)
            cnt %= 4
            result += 'BB' * (cnt // 2)
            cnt = 0
            result += '.'

else:
    result = result[:-1]
    print(result)


# replace() 이용하면 훨씬 간편함.
"""
board = str(input())
board = board.replace("XXXX", "AAAA").replace("XX", "BB")
print(-1 if "X" in board else board)
"""