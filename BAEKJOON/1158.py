'''
/*
요세푸스 문제

1번부터 n명의 사람이 원을 이루며 앉아있고, 양의 정수 k가 주어진다.
순서대로 k번째 사람을 제거하는 것을 반복한다. 모두 제거 될 때까지.
제거되는 순서를 N-K 요세푸스 순열이라고 한다.
7, 3의 경우 3 6 2 7 5 1 4 이다.

입력
n, k 제시.

출력
<요세푸스 순열>
*/
'''
n, k = map(int, input().split())
nl = list(range(1, n+1))
p = k-1
ans = "<"
fla = False
while nl:
    p %= len(nl)
    if fla:
        ans += f", {nl.pop(p)}"
    else:
        ans += f"{nl.pop(p)}"
        fla = True
    p+=k-1
ans += ">"
print(ans)