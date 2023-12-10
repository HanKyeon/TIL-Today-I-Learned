'''
k번째 수
앞에서 k번째 수 구해라

입력
n, k 제시
nl 제시

출력
정렬했을 때 앞에서 k번째 수 구해라
'''
n, k = map(int, input().split())
print(sorted(map(int, input().split()))[k-1])