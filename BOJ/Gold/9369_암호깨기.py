# 20240820
# 40:29
# 1 / 1


def check_possible(encrypt, decrypt):
    converted = [set(list('abcdefghijklmnopqrstuvwxyz')) for _ in range(26)]  # index순의 암호화된 알파벳에 어떤 알파벳이 복호화 가능한지
    for i in range(len(encrypt)):
        e = encrypt[i]
        e_idx = ord(e) - ord('a')
        d = decrypt[i]

        if d not in converted[e_idx]:  # 이미 다른 알파벳에서 d 쓰였다면
            return False
        for c in range(26):  # 다른 알파벳들에서 d 불가능해지므로 d 빼주기
            converted[c] = converted[c].difference(d)
        converted[e_idx] = {d}

    for c in range(26):
        if not converted[c]:  # 아무 알파벳도 대응될 수 없으면, 유효한 매칭 아님.
            return False
        if len(converted[c]) > 1:  # 여러 알파벳이 대응 가능하다면, ?로 변환
            converted[c] = {'?'}

    return dict([(chr(ord('a') + idx), alpha) for idx, alpha in enumerate(converted)])  # 해동 가능한 dictionary로 return


t = int(input())
for _ in range(t):
    n = int(input())
    encrypted = [str(input()) for _ in range(n)]  # 암호화된 문자열들
    decrypted = str(input())  # 복호화된 문자열
    target = str(input())  # 해독해야 할 문자열

    merged_converted = dict()  # target을 해독해줄 문자열
    for s in 'abcdefghijklmnopqrstuvwxyz':
        merged_converted[s] = set()

    for encrypted_string in encrypted:
        if len(decrypted) != len(encrypted_string):  # 복호화문자열과 길이 같지 않으면, 일단 이건 아니므로 continue
            continue
        valid_conversion = check_possible(encrypted_string, decrypted)  # 유효한 매칭인지, 유효하다면 dict()반환됨
        if not valid_conversion:  # 유효하지 않으면 continue
            continue
        for s in 'abcdefghijklmnopqrstuvwxyz':  # 기존에 있던 converted에 더하기
            merged_converted[s] = valid_conversion[s].union(merged_converted[s])

    if not merged_converted['a']:  # 유효한 매칭이 없었다면, merged_converted에 아무 변화 없어서 아무 값 안 담겨 있으므로 IMPOSSIBLE
        print('IMPOSSIBLE')
        continue

    for s in 'abcdefghijklmnopqrstuvwxyz':  # merged_converted 재정비
        if len(merged_converted[s]) > 1:  # 둘 이상의 암호문이 유효해서 한 알파벳에 여러 해석이 가능한 경우 제거
            merged_converted[s] = '?'
        else:
            merged_converted[s] = list(merged_converted[s])[0]  # 하나만 있다면, set에서 값 꺼내기

    answer = ''
    for t in target:
        answer += merged_converted[t]  # 해독
    print(answer)
