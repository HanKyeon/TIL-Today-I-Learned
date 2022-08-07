'''
수열

n개의 숫자. 연속해서 커지거나, 연속해서 감소하는 수열의 가장 긴 길이

입력
n은 1이상 10만 이하
띄어쓰기로 수열 제시

출력
길이가 가장 긴 길이 출력
'''
# 입력
n = int(input())
nl = list(map(int, input(). split()))
ml = 0
# dp. 기본적으로 각각은 최소 1개의 연속수열이다.
incl, decl = [1] * n, [1] * n
# 이전것보다 크거나 작으면 이전것의 길이 +1이 최대 길이
for i in range(1, n) :
    if nl[i] >= nl[i-1] :
        incl[i] = incl[i-1] + 1
    if nl[i] <= nl[i-1] :
        decl[i] = decl[i-1] + 1
# 출력
print(max(max(incl), max(decl)))


'''
def increase(sta, end) :
    # 종료 조건 end가 최대 인덱스 도달하면 길이 반환
    if end == len(nl) - 1 :
        return (end - sta + 1)
    # 기본적으로 sta가 end보다 클 때, 한칸 이동해라.
    if end < len(nl) - 1 and nl[sta] > nl[end] :
        return (increase(end, end+1))
    # 몸체
    check = end
    end += 1
    if nl[check] <= nl[end] :
        return increase(sta, end)
    elif nl[check] > nl[end] :
        if end < len(nl) - 1 :
            return max(end - sta + 1, increase(end, end+1))
    else :
        return (check - sta + 1)

def decrease(sta, end) :
    # 종료 조건
    if end == len(nl) - 1 :
        return (end - sta + 1)
    # 확인 후 이동 조건
    if nl[sta] < nl[end] :
        return (decrease(sta+1, end+1))
    # 몸체
    check = end
    end += 1
    if nl[check] >= nl[end] :
        return decrease(sta, end)
    else :
        return max(end - sta + 1, decrease(end, end+1))

ml = increase(0, 1)

#ml = max(increase(0, 1), decrease(0, 1))

print(ml)
'''