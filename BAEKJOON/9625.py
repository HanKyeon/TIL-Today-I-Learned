'''
BABBA

a => b => ba => bab => babba

입력
k 제시.

출력
k번 눌렀을 때 화면에 A와 B의 갯수는 몇 개?
'''
a, b = 1, 0
for _ in range(int(input())):
    a, b = b, a+b
print(a, b)





