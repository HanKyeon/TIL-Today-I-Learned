'''
1. 카드가 N * M 형태로 놓여있다. n은 행 m은 열
2. 뽑고자 하는 카드의 행 선택
3. 선택 된 행에 있는 카드 중 가장 낮은 숫자 뽑기
4. 그러므로 처음 골라낼 행을 선택 할 때, 
이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 
최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

최솟값이 가장 큰 행은?

'''

n, m = map(int, input().split) # 행렬 입력

result = 0 # 결괏값 초기화

for i in range(n): # n행 만큼 반복
    data = list(map(int, input().split())) # 일단 행 먼저 입력 받으셈
    min_value = min(data) # 최소치도 받아두셈
    result = max(result, min_value) # 첫 실행시 첫 값이 들어갈테니 둘 비교해서 큰거 넣으셈ㅋ

print(result) # 결과 출력



'''
--- 아래는 이중 for 문 ---
'''

n, m = map(int, input().split) # 행렬 입력

result = 0 # 결괏값 초기화

for i in range(n): # n행 만큼 반복 '행 갯수만큼 순회'
    data = list(map(int, input().split())) # 행 입력 받아
    min_value = 10001 # 이건 잘 모르겠는걸! -> 입력 조건이 10000 이하의 숫자이므로 최솟값을 구하려고 10001 로 설정
    for a in data: # 행 리스트의 값을 순회 '행을 순회'
        min_value = min(min_value, a) # 최소값은 순회중인 a와 비교해서 작은 값이다.
    result = max(result, min_value) # 결과는 최솟값 중 큰 값이란다

print(result) # 결과 출력
