'''
세제곱근을 찾아라

n = x**3이 되는 양의 정수 x를 구해라.

입력
테케T 제시.
각 테케의 첫 번째 줄에 하나의 정수 제시.

출력
#테케T N = x**3이 되는 양의 정수 x 출력. 없다면 -1 출력
'''
from cmath import isclose

for tc in range(1, int(input())+1):
    n = int(input())
    n3 = n**(1/3)
    a = n3%1
    if isclose(a, 0) or isclose(a, 1):
        print(f"#{tc} {int(n3+0.5)}")
    else:
        print(f"#{tc} -1")

for tc in range(1,int(input())+1):
    n,ans=int(input()),-1
    a=int(n**(1/3))
    for i in (a,a+1):
        if i**3==n:ans=i;break
    print(f"#{tc} {ans}")