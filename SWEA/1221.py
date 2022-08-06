'''
GNS

외계인 숫자 아래처럼 씀. 0~9
"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
정렬해라.

테케 갯수 
다음줄에 #1 테케길이 주어짐. lstrip #해라
이후 테케 제공

'''
trans = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}
for t in range(int(input())) :
    n = int(input().lstrip(f'#{t+1}'))
    ul = list(input().split())
    nl = [0] * n
    for i in range(n) :
        nl[i] = trans[ul[i]]
    
    nul = sorted(zip(nl, ul))

    print(f"#{t+1}")
    for i in range(n) :
        print(nul[i][1], end=' ')
    print()