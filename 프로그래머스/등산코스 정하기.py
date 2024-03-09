'''
출입구, 쉼터, 산봉우리
쉼터 혹은 산봉우리 중에서 휴식 가능. 휴식 없이 이동하는 시간 중 가장 긴 시간을 해당 등산 코스의 intensity이다.
XX산 출입구 중 한 곳에서 출발하여 산봉우리 중 한 곳만 방문한 뒤 다시 원래의 출입구로 돌아오는 등산코스를 정할 것.
즉, 등산코스에서 출입구는 처음과 끝에 한 번 씩, 산봉우리는 한 번만 포함되어야 함.

이 규칙을 지키면서 intensity가 최소가 되도록 등산 코스를 정하려 한다.
노드는 1~n

입력
노드수 n 최대 5만, 최소 2
등산로의 정보 2차원 정수 배열 paths 최대 20만, a, b, c 제시. a와 b를 잇는 c비용의 간선. 최댓값 10,000,000 최대 1개
출입구들 번호 정수 배열 gates 최대 n
산봉우리들의 번호가 담긴 정수 배열 summits 최대 n

출력
intensity가 최소가 되는 등산 코스에 포함된 산봉우리 번호와 intensity의 최솟값을 차례대로 정수 배열에 담아 return
즉, [산봉우리, intensity 최솟값]
'''
from heapq import heappop, heappush

def solution(n, paths, gates, summits):
    # 다익스트라
    def dij(startPoint):
        nonlocal n, gates, startPoints, endPoints, g, ans
        dst = [11111111]*(n+1)
        heap = []
        for co, no in g[sta]:
            if no in startPoints: continue
            heappush(heap, (co, no))
            dst[no] = co
        while heap:
            cost, nod = heappop(heap)
            if dst[nod] < cost: continue
            if nod in endPoints: return [nod, cost]
            for co, nnod in g[nod]:
                if nnod in startPoints: continue
                costco = cost if cost > co else co
                if dst[nnod] > costco:
                    dst[nnod] = costco
                    heappush(heap, (costco, nnod))
        return [11111111, 11111111]
    ans = [0, 11111111]
    startPoints, endPoints = set(gates), set(summits)
    g = [[] for _ in range(n+1)]
    for a, b, c in paths:
        g[a].append((c, b))
        g[b].append((c, a))
    for sta in gates:
        endPoint, intensity = dij(sta)
        if ans[1] > intensity:
            ans = [endPoint, intensity]
        if ans[1] == intensity:
            ans = [min(endPoint, ans[0]), intensity]
    return ans

'''
- 이슈 목록
    - 봉우리에서 dijkstra를 실행하니 답이 틀린 이슈가 있었음. 봉우리 sort를 하지 않아서 그런듯;;; 저런
    - 시작지점들에서 가능한 노드들을 전부 넣고 돌리게 될 경우에 최솟값을 돌아서 최소 봉우리를 방문이 가능하다는 점을 고려해야 한다.
    - dijkstra를 했을 때, 분리되어 봉우리와 만나지 못하는 등산로도 있는 것 같음. 그래서 return값이 None이 되고 None으로 비교 연산자를 수행하면서 런타임 에러가 뜨는 경우가 있었음.
    - 시작 지점 어디서 시작하든 같은 힙에서 다익스트라를 돌릴 수 있다는 것을 까먹고 있었음. 잊지 말자 !
'''