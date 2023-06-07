'''
하노이 탑 이동 순서

세 개의 장대. n개 원판 반경이 큰 순서대로 쌓여있다.
한 번에 한 개의 원판만 이동 가능.
쌓아놓은 원판은 항상 위가 아래보다 작아야 함
이동이 최소가 되는 이동 순서 출력

입력
n

출력
횟수 k 출력
수행 과정 출력
a, b a번째 탑의 가장 위에 있는 원판을 b번째 탑의 가장 위로 옮긴다는 뜻
'''

def rec(n, s, e) :
    if n == 1 :
        print(s, e)
        return
    rec(n-1, s, 6-s-e)
    print(s, e)
    rec(n-1, 6-s-e, e)
n = int(input())
print(2**n-1)
rec(n, 1, 3)

'''
# 빠른 코드
def hanoi(value,start,finish,support):
        key=(value,start,finish,support)
        if key in memo:
            return memo[key]
        if value==1:
            return f"{start} {finish}"
        if value>=2:
            output= "\n".join([hanoi(value-1,start,support,finish),f"{start} {finish}",hanoi(value-1,support,finish,start)])
            memo[key] = output
            return output
        
num=int(input())
print(f"{2**num-1}")
print(hanoi(num,"1","3","2"))
'''
