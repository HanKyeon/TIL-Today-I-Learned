'''
스택 수열

스택은 기본 자료 구조고, 1부터 n까지 숫자를 차례로 넣을 것.
주어진 수열이 스택 자료로 만들 수 있다면 push와 pop을 어떤 순서로 해야하는지 출력하고
만들 수 없다면 NO 출력

입력
1이상 10만이하 n
1부터 n까지의 수열

출력
수열을 만들기 위한 연산을 한 줄에 하나씩 ++
'''
n = int(input())
nl = [int(input()) for _ in range(n)]
st, ans = [], []
for i in range(1, n+1):
    while st and st[-1] == nl[0]:
        ans += '-'
        st.pop()
        nl.pop(0)
    st.append(i)
    ans += '+'
while st and st[-1] == nl[0]:
    ans += '-'
    st.pop()
    nl.pop(0)
if st == []:
    for i in ans:
        print(i)
else:
    print('NO')


