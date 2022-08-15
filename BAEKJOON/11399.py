'''
ATM

atm에 n명의 사람들이 줄을 서 있다. 1~N번 번호
i번째 사람이 인출하는데 걸리는 시간 p분
돈을 인출하는데 걸리는 각각의 시간의 합을 최소로 하기 위한 줄 서기 방법은?

입력
1~1000 사람수 N
p1 p2 p3 p4 p5... 인출하는데 걸리는 시간

출력
p1 p1+p2 p1+p2+p3.. 합
'''
n = int(input())
nl = sorted(list(map(int, input().split())))
nnl = [0] * n
for i in range(n):
    nnl[i] = sum(nl[:i+1])
print(sum(nnl))

