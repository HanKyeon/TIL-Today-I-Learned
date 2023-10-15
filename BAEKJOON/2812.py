'''
크게 만들기

n자리 숫자 제시. 숫자 k개 지워서 얻을 수 있는 가장 큰 수

입력
n, k 제시
n자리 숫자 제시

출력
k개 지웠을 때 얻ㅇ르 수 있는 가장 큰 수 출력
'''
n, k = map(int, input().split())
num, stk = list(input()), []
for i in num:
    while k and stk and stk[-1] < i: stk.pop(); k-=1
    stk.append(i)
while k: stk.pop(); k-=1
print(''.join(stk))