'''
카드1

n장의 카드. 1~n 번호.
맨 위에 하나 버리고 맨 위를 하나 맨 아래로 옮긴다. 버린 카드 순서대로 출력

입력
정수 n 제시

출력
버리는 카드 순서대로 출력
'''
nl, ans = list(range(1, int(input())+1)), []
while nl:
    try: ans.append(nl.pop(0)); nl.append(nl.pop(0))
    except: break
print(*ans)
