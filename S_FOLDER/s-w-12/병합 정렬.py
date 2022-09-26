'''
병합 정렬

N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할 한다.
병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.

입력
테케T
정수 갯수n
정수 리스트 제시.

출력
#테케T N//2 원소, 오른쪽 원소가 먼저 복사되는 경우의 수
'''
def ms(li): # 머지 소트
    global cnt
    if len(li) < 2: # 길이가 0이나 1이면 그대로 리턴
        return li
    
    mid = len(li)//2 # 중앙값
    left = ms(li[:mid]) # 왼쪽
    right = ms(li[mid:]) # 오른쪽
    if left[-1] > right[-1]: # 정답을 위한 내용.
        cnt+=1
    ret = [] # 리턴값
    l, h = 0, 0 # 왼쪽 인덱스, 우측 인덱스
    while l < len(left) and h < len(right): # 어느 한 쪽이 리스트 벗어나기 전까지
        if left[l] < right[h]: # 더 작은 쪽을 넣고, 넣어준 쪽 인덱스 증가.
            ret.append(left[l])
            l += 1
        else:
            ret.append(right[h])
            h += 1
    ret += left[l:] # 남은 잔여 리스트
    ret += right[h:] # 리턴 값에 넣어주기
    return ret

for tc in range(1, int(input())+1):
    n = int(input())
    nl = list(map(int, input().rstrip().split()))
    cnt = 0
    nl = ms(nl)
    print(f"#{tc} {nl[n//2]} {cnt}")






def ms(li):
    global cnt
    if len(li) < 2: # 길이 1 이하면 리스트 그대로 반환
        return li

    mid = len(li)//2 # 중앙 분리 할 값
    left = ms(li[:mid]) # 왼쪽
    right = ms(li[mid:]) # 오른쪽
    if left[-1] > right[-1]: # 정답 출력을 위한 내용
        cnt+=1
    ret = [] # 리턴 값
    while left and right:
        if left[0] < right[0]: # 오른쪽이 더 크면 왼쪽을 넣어주고 인덱스 이동시켜주고
            ret.append(left.pop(0))
        else: # 왼쪽이 더 크면 오른쪽 넣어주고 인덱스 늘려준다.
            ret.append(right.pop(0))
    if left:
        ret += left # 남은 것들
    if right:
        ret += right # 넣어주기
    return ret # 리턴

for tc in range(1, int(input())+1):
    n = int(input())
    nl = list(map(int, input().rstrip().split()))
    cnt = 0
    nl = ms(nl)
    print(f"#{tc} {nl[n//2]} {cnt}")


















