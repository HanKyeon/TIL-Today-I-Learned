'''
gns 추가
'''
trans = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}
snart = dict(zip(trans.values(), trans.keys())) # trans의 키와 밸류를 뒤집은 딕셔너리
for t in range(1, int(input())+1) :
    n = int(input().lstrip(f'#{t}'))
    ul = list(input().split())
    ns = [0] * 10 # 0~9 카운팅
    nl = [] # 추가 할 것
    for i in ul : # 카운팅
        ns[trans[i]] += 1
    for i in range(10): # 0~9를 갯수만큼 곱해서 더해줌
        nl += [i] * ns[i]
    print(f"#{t}") # 테케 출력
    for s in nl : # 외계어 출력
        print(snart[s], end=' ')
    print() # 엔터