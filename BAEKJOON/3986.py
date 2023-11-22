'''
좋은 단어

좋은 단어 세야함.
A는 A끼리 B는 B끼리 쌍을 짓는다. 선끼리 교차하지 않으면서 각 글자르 ㄹ정확히 한개의 다른 위치에 있는 글자와 짝지을 수 있다면 좋은 단어이다. 좋은 단어 갯수 세라.

입력
단어 수 n 제시
n개 줄 단어 제시

출력
좋은 단어 수 출력
'''
def check(s: list):
    global ans
    stk = []
    for i in s:
        if not stk: stk.append(i); continue
        stk.append(i) if stk[-1] != i else stk.pop()
    ans += 1 if not stk else 0

ans = 0
for _ in range(int(input())): check(list(input()))
print(ans)