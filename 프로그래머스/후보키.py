'''
후보키

indexedDB에서 keyPath를 지정하듯 key를 사용이 가능하다.
즉, 유일해야하며, 최소여야 한다.
유일 : 모든 자료에 대해 유일하다.
최소 : 어떤 값이 빠졌을 때 유일이 유지되지 못해야 한다. 즉, subset이 key면 안된다.
후보키의 최대 갯수 구하기.

입력
relation은 2차원 배열이며 값은 str
[[col1, col2, col3, col4], [],...] 형태
제약사항은 칼럼 길이는 1이상 8이하, row 길이는 1이상 20이하, 문자열은 1이상 8이하, 모든 튜플은 유일하게 식별이 가능하다. 완전히 동일한 값은 없다. === 언제나 정답이 존재한다.

출력
후보키 최대 갯수 리턴
'''
from itertools import combinations
def solution(relation):
    n, m = len(relation), len(relation[0])
    ans, nui = set(), []
    noitaler = [set([item[idx] for item in relation]) for idx in range(m)]
    for i in range(m):
        if len(noitaler[i]) == n: ans.add(tuple([i]))
        else: nui.append(i)
    for combiLen in range(2, len(nui)+1):
        for combi in combinations(nui, combiLen):
            if len(set([tuple([item[idx] for idx in combi]) for item in relation])) != n: continue
            flag = True
            for j in ans:
                if set(j) <= set(combi): flag = False
            if flag: ans.add(tuple(combi))
    answer = len(ans)
    return answer