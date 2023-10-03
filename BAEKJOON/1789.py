'''
수들의 합

n개 자연수 합이 s
자연수 n의 최댓값

입력
s 제시

출력
n의 최댓값
'''
s, cnt = int(input()), 0
while s >= cnt:s-=cnt;cnt+=1
print(cnt-1)


