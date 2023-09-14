'''
점수 계산

8개 문제. 풀기 시작한 시간부터 경과한 시간의 난이도로 점수 결정. 못풀면 0점 총 점수는 가장 높은 5개의 합

입력
8개줄 점수 제시

출력
어떤 문제가 최종 점수에 포함되는지 공백 구분 출력 출력은 문제 번호 증가하는 순서
'''
nl = sorted([[int(input()), i] for i in range(1,9)], key=lambda x: (-x[0], x[1]))
print(sum([v for v, _ in nl][:5]))
print(*sorted([i for _, i in nl][:5]))
