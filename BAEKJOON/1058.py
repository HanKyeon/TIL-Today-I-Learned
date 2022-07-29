'''
친구친구
인원 N
'''

'''
친구친구 구하기
1. 순회하면서 친구들 리스트 확인해서 Y 카운트
2. 그 친구들 친구 숫자합 - 자기 친구 수
'''
# 입력 및 그래프로 만들기
n = int(input())
d = []
for i in range(n) :
    x = input()
    d.append(list(x))
# 각 사람의 친구 세기
in_fn = [] # 인덱스 별 친구 수가 나온다.
for q in d :
    in_fn.append(q.count('Y'))

# 인덱스 별 친구 목록
fl = [] # 인덱스 별 친구 목록이 2차원으로 생성
fn = 0
for a in d :
    fl.append(list(filter(lambda x: a[x] == "Y", range(len(a)))))

max_f = 0

print(fl,"\n", in_fn)
for k in fl :
    new_hap = 0
    for j in k :
        new_hap += in_fn[j]
    new_hap = new_hap 
    print("=================",new_hap,"===============")
    max_f = max(max_f, new_hap)

print(max_f)
