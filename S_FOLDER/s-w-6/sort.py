
def quick_sort(li) : 
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(li) <= 1 :
        return li
    p = li[0] # 피벗은 첫번째 원소
    t = li[1:] # 피벗을 제외한 리스트

    left_side = [x for x in t if x <= p] # 분할된 왼쪽 부분을 피벗보다 작으면 왼쪽에 담고
    right_side = [x for x in t if x > p] # 분할된 오른쪽 부분을 피벗보다 큰 값을 채워준다.
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행을 한 뒤, 전체 리스트를 반환한다.
    return quick_sort(left_side) + [p] + quick_sort(right_side)

def sor(l) :
    ln = len(l)
    for i in range(ln) :
        for j in range(i+1, ln) :
            if l[i] > l[j] :
                l[i], l[j] = l[j], l[i]
    return l

'''
버블 소트
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input()))

    cnts = [0]*10
    for n in lst:
        cnts[n] += 1

    idx = 0
    for i in range(1, 10):
        if cnts[idx] <= cnts[i]:
            idx = i
    print(f'#{test_case} {idx} {cnts[idx]}')
'''

'''

'''


for testcase in range(1, int(input())+1) :
    n = int(input())
    nl = list(map(int, input().split()))
    print(f"#{testcase} {' '.join(list(map(str, quick_sort(nl))))}")



