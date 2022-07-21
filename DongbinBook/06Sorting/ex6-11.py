'''
N명의 학생의 정보.
정보는 이름/성적 구분.
이름과 성적이 주어질 때
성적이 낮은 순서대로 이름을 출력

N은 1부터 10만 사이 자연수
이후 이름과 성적이 공백을 기준으로 입력.

'''


# N 입력
n = int(input())

array = []
# N명의 학생의 정보를 입력 받는다.
for i in range(n) :
    input_data = input().split()
    # 이름은 문자열 그대로, 정수는 정수형으로 튜플 형태로 저장.
    array.append((input_data[0], int(input_data[1])))
# 키 값을 이용하여 점수를 기준으로 정렬.
# sorted의 key 파라미터는 어떤 것을 기준으로 정렬 할 것인가?
# 라는 물음에 답을 주는 것. key값을 어떤걸로 할 것이냐는 물음에
# 스튜던트를 정렬 할 것인데 1번 인덱스의 스튜던트로.
array = sorted(array, key = lambda student: student[1])

# 정렬된 순서대로 출력하는데 0번 인덱스 이름 출력
for student in array :
    print(student[0], end = ' ')



