stackSize = 10
stack = [0] * stackSize
top = -1

top += 1 # push 1
stack[top] = 1 # 스택에 push

top += 1 # push 2
stack[top] = 2 # 스택에 push

top -= 1 # pop1
temp = stack[top+1]
print(temp)

temp = stack[top] # pop2
top -= 1
print(temp)

stack2 = []

stack2.append(10)
stack2.append(20)
print(stack2.pop())
print(stack2.pop())

직접 구현하는 스택은 여러종류로 가능.

크기가 N인 배열의 모든 원소에 접근하는 재귀함수

def f(i, n):
    if i == n:
        return
    else:
        print(a[i])
        return f(i+1, n)

n = 3
a = [1, 2, 3]
print(f(0, n))


def facto(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*f(n-1)

def fibo(n):
    if n<2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)