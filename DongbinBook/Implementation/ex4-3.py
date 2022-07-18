'''
8*8 체스판에서 나이트의 위치가 주어졌을 때 이동 가능한 경우의 수를 출력
좌상단 기준으로 좌측으로 abcdefgh 하단으로 12345678
입력은 연속으로 주어짐. a1 c8 d2 이런 식으로.
'''
# 데이터 입력 받고 데이터 정리하기. column은 영어를 아스키 코드로 바꾸고 그 차이로.
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
# 나이트 이동 가능 경우의 수
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
# 결괏값 초기화
result = 0
for step in steps : # 변수가 steps 리스트를 확인하며
    # 예상 위치를 하나하나 확인한다.
    next_row = row + step[0]
    next_column = column + step[1]
    # 만약 안에 위치하면
    if next_row >=1 and next_row <= 8 and next_column >= 1 and next_column <= 8 :
        result += 1 # 더해준다

print(result) # 결과

