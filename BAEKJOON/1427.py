'''
소트인사이드

숫자 제시하면 자릿수를 정렬해라.

입력
n 제시

출력
정렬한 수 출력
'''
n=list(input().rstrip())
n.sort(reverse=True)
print("".join(n))
