'''
방 번호

6, 9는 공통. 0~9 숫자세트 몇개 필요?

입력
방 번호 제시

출력
필요한 세트 갯수
'''
n = input().rstrip()
cs = [0]*10
for i in n:
    cs[int(i)]+=1
exc = cs.pop(9)+cs.pop(6)
nor = max(cs)
print(max(exc//2+1 if exc%2 else exc//2, nor))