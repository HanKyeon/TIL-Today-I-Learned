'''
스택

정수를 저장하는 스택을 구현한 뒤 명령을 처리. 명령 5개.
push X : 스택에 ㄴ허기
pop 가장 위 정수 빼고 출력. 없으면 -1 출력
size 정수 갯수 출력
empty 스택이 비어있으면 1 아니면 0 출력
top 스택 가장 위의 정수 출력. 없으면 -1

입력
명령 수 n
n개 줄 명령 제시.

출력
출력 명령 따라라.
'''
import sys
input = sys.stdin.readline

def printing(option):
    if option == "pop":
        if stk:
            return stk.pop()
    elif option == "size":
        return len(stk)
    elif option == "empty":
        if stk:
            return 0
        return 1
    else:
        if stk:
            return stk[-1]
    return -1

n = int(input())
stk = []
for _ in range(n):
    s = input().rstrip()
    try:
        int(s[-1])
        _, num = s.split()
        stk.append(num)
    except:
        print(printing(s))















