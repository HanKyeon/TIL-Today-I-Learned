'''
주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다.
입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.

입력
테케 T
한 줄

출력
#T 정상이면1
#T 불완전하면0
'''
li = ['(', '{', ')', '}']

for testcase in range(1, int(input())+1):
    st, f = [], 1
    s = input()
    for i in s:
        if i not in li:
            continue
        for j in range(4):
            if i == li[j] and j < 2:
                st.append(i)
            elif i == li[j] and j >= 2:
                if st == []:
                    f = 0
                    break
                b = st.pop()
                if b != li[j-2]:
                    f = 0
                    break
        if f == 0:
            break
    if st != []:
        f = 0
    print(f"#{testcase} {f}")

# ㅅㅂ;; 에러처리 한 프린트 잘 지우자
