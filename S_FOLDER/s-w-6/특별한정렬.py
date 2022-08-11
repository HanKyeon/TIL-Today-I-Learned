# 셀렉팅 소트 흉내내는 그냥 정렬
def ss(li) :
    # 내림차순 짝수
    for i in range(0,10,2) :
        Mi = i
        for j in range(i+1, len(li)):
            if li[Mi] < li[j] :
                li[Mi], li[j] = li[j], li[Mi]
    # 오름차순 홀수
    for i in range(1, 10, 2) :
        mi = i
        for j in range(i+1, len(li)):
            if li[mi] > li[j] :
                li[mi], li[j] = li[j], li[mi]


for testcase in range(1, int(input())+1):
    # 입력
    n = int(input())
    nl = list(map(int, input().split()))
    # 실행
    ss(nl)
    # 출력
    print(f"#{testcase}", *nl[:10])



