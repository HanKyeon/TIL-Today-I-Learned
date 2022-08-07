'''
두개의 숫자열

입력
테케 T
수열의 길이 N M 3이상 10 이하
수열A
수열B

출력
#1 #2 #2
곱한뒤 더한 최댓값
'''
# l2가 더 길 때 맥곱합 반환
def maxgophap(l1, l2) :
    len1, len2 = len(l1), len(l2)
    mgh = 0
    gh = 0
    for i in range(len2 - len1 + 1) :
        for j in range(len1) :
            gh += l2[i+j] * l1[j]
        mgh = max(mgh, gh)
        gh = 0
    return mgh

# testcase!!!!!!!!!!!!! testcase!!!!!!!!!!!
for testcase in range(1, int(input())+1) :
    n, m = map(int, input().split())
    nl = list(map(int, input().split()))
    ml = list(map(int, input().split()))
    result = 0
    if n <= m :
        result = maxgophap(nl, ml)
    else :
        result = maxgophap(ml, nl)
    print(f"#{testcase} {result}")





