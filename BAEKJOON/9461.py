'''
파도반 수열

P(1)부터 P(10)까지 첫 10개 숫자는 1, 1, 1, 2, 2, 3, 4, 5, 7, 9
i-5 + i-1
'''

nl = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0]*90
for i in range(11, 101):
    nl[i] = nl[i-5] + nl[i-1]

for _ in range(int(input())):
    n = int(input())
    print(nl[n])
