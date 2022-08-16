'''
의석이의 세로로 말해요

입력
테케 갯수T
1~15 문자열
1~15 문자열
1~15 문자열
1~15 문자열
1~15 문자열

출력
#1 세로로 읽은거
'''

for testcase in range(1, int(input())+1):
    sl = [['']*15 for _ in range(5)] # 최대 15개라 빈문자열 15개 만들어줌
    for i in range(5):
        s = input() # 문자열 받아서
        for j in range(len(s)): # 그거 순회해서
            sl[i][j] = s[j] # sl에 넣어줌
    yxsl = list(map(list, zip(*sl))) # 뒤집고
    print(f"#{testcase}", end=' ') # 출력
    for i in yxsl:
        for s in i:
            print(s, end='')
    print()