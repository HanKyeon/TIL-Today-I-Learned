'''
비밀번호
'''

for testcase in range(1, 11):
    _, s = input().split()
    li = []
    for i in s:
        if li == [] or i != li[-1]: # 비어있거나 가장 최근 입력 받은거랑 다르면 append
            li.append(i)
        elif i == li[-1]: # 가장 최근 입력받은거랑 같으면 pop
            li.pop()
    print(f"#{testcase} {''.join(li)}")

# 숏코딩
'''
for t in range(1,11):
    l=[]
    for i in input().split()[1]:
        if not l or i!=l[-1]:l.append(i)
        elif i==l[-1]:l.pop()
    print(f"#{t} {''.join(l)}")
'''