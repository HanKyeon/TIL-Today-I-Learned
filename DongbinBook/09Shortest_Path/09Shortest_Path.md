
 # 최단경로

 - 최단경로 알고리즘은 가장 짧은 경로를 찾는 알고리즘을 의미.

 - 문제 상황이 다양하다.
  1. 한 지점에서 다른 한 지점까지의 최단 경로
  2. 한 지점에서 다른 모든 지점까지의 최단 경로
  3. 모든 지점에서 다른 모든 지점까지의 최단 경로

 - 각 지점은 그래프에서 노드로 표현.
 - 지점 간 연결된 도로는 그래프에서 간선으로 표현.

 - 노드는 국가, 마을, 도시 등 지점에 대한 정의가 다르게 주어질 수 있다. 노드와 간선의 형태. 통로가 있는 것 처럼 표현이 된다. 간선은 도로, 통로 등으로 표현된다.

## 다익스트라 최단 경로 알고리즘

 - 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산.
 - 다익스트라 알고리즘은 음의 간선이 없을 때 정상적으로 동작. 실제로 현실의 도로는 음의 도로로 표현되지 않기에, 현실 상황의 알고리즘을 풀 때 사용 가능하다.
 - 다익스트라 알고리즘은 그리디 알고리즘으로 분류된다. 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복하기 때문. 아직 방문하지 않은 노드 중, 비용이 가장 적은 노드를 반복하여 고른다는 것.

 - 최단 경로의 경우, dp로도 얘기되기도 한다. 길을 가는 것이 곂칠 수 있기 때문에, 가짓수를 dp 테이블로 넣을 수 있기 때문.

 - 실존인물 다익스트라는 여러가지 알고리즘을 제안했지만 그 중 가장 대표적인 것이 다익스트라 최단경로 알고리즘이다.

### 다익스트라 알고리즘 동작 과정

1. 출발 노드 설정
2. 최단 거리 테이블 초기화 (처음에는 모든 노드까지 가기 위한 비용을 무한으로, 자기 자신은 0)
3. 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드를 선택.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신.
5. 3,4번을 반복한다.

 - 3번과 4번에서 가장 짧은, 가장 최선을 선택하기에 그리디 알고리즘으로 분류가 된다. 좋은 선택을 하게 된다면 최단거리 자체는 바뀌지 않기 때문이다. 특정 노드까지의 최단 거리를 그때그때 반복하여 찾는다. 모든 노드에 방문하여 거리처리가 끝나면 모든 노드들의 최단거리를 알아낼 수 있다.
 - 그렇기에 실제로 시작점에서 각 노드까지의 최단 거리만 알 수 있고, 경로를 알기 위해서는 별도의 로직을 추가적으로 사용해야함. 다만, 경로까지 모두 출력하라는 경우는 코테에서는 거의 없다. 그렇기에 본 교재에서는 최단거리 테이블을 구하는 것을 목표로 한다.

 - 알고리즘 동작 과정에서 최단 거리 테이블은 각 노드에 대한 현재까지의 최단 거리 정보를 가지고 있다.
 -  처음에는 단순 노드 간 거리를 통해 최솟값을 구하고, 이후 다른 노드를 거쳐가는 정보를 확인하여 **처리 과정에서 더 짧은 경로를 찾으면 '이제부터 이 경로가 제일 짧은 경로'라고 갱신.**

#### 그림 영상 참조

1. 테이블에서 출발 노드 설정. 출발 노드에서 자기 자신의 거리는 0, 나머지는 무한으로 초기화.
2. 이후 최단거리가 가장 짧은 노드인 1번 노들를 통해 이동 할 수 있는 노드들의 거리를 0+x 형태로 더해준다. (1번에서 1번으로 이동 할 때 비용 + 1번으로부터 x 노드로 이동 할 때 필요한 비용) 두 기존 테이블의 무한값과 비교하여 더 작다면 갱신 여부를 True로 놓고 테이블을 갱신한다.
3. 이후, 1번 노드를 거쳐 갈 때 최소거리를 찾아 같은 방법을 반복한다. 즉, 1번에서 1번까지의 거리 + 1번부터 4번노드 거리 + 4번부터 y번까지 이동하는 거리를 더해 y노드에 들어있는 값보다 작다면 갱신 여부를 True로 하여 처리한다.
4, 만약 비용이 같은 경우, 번호가 낮은 노드부터 처리한다. 

 - 즉, 출발 노드에서 n번 노드를 거쳐 m번 노트로 이동하는 거리 값의 min(기존 보유한 다른 루트 최단거리, n번 노드를 거쳐 m번 노드로 이동하는 거리)을 구해주는 방식으로 한다.
 - 마지막 노드 같은 경우 구해주지 않아도 된다. 앞서 확인 했던 다른 노드까지의 최단거리값은 바뀌지 않기 때문에.
 - 특히 현 예제에서는 간선형인데 6번에서 이동하는 경우가 없어서 더더욱 바뀌지 않는다.

 - 그리디 알고리즘으로 취급되는 이유는 **매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택**해 과정 반복.
 - 단계를 거치며 한 번 처리된 노드의 최단거리는 고정. 즉, 한 단계당 하나의 노드에 대한 최단 거리르 확실히 찾는 것으로 이해 할 수 있다.
 - 다익스트라 알고리즘을 수행한 뒤에 테이블에 각 노드까지의 최단 거리 정보가 저장된다.
 - 완벽한 형태의 최단경로를 구하려면 소스코드에 추가적인 기능이 더 필요하다.

#### 다익스트라 간단한 구현 방법.

 - 단계마다 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드를 선택하기 위해 **매 단계마다 1차원 테이블의 모든 우너소를 확인(순차 탐색)**합니다.

 - 너무 복잡해서 머리 깨질듯.

총 O(V)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야 한다. 따라서 전체 시간 복잡도느 O(V^2)이다. 전체 노드의 갯수가 5000개 이하라면 다익스트라 알고리즘을 해결 할 수 있다. 하지만 노드의 갯수가 10000개가 넘어 갈 경우에는 1억번 이상의 연산이 필요하여 시간초과 판정을 받을 위험이 있다. 그래서 우선순위 큐 자료구조를 이용해준다.


### 우선순위 큐 자료구조. Priority Queue

 - 우선순위가 가장 높은 데이터를 가장 먼ㅇ저 삭제하는 자료구조.
 - 예를 들어 여러개의 물건 데이터를 자료구조에 넣었다가 가치 높은 물건 데이터부터 꺼내서 확인해야 하는 경우 사용.
 - 파이썬, cpp, java 등 대부분에서  표준 라이브러리로 제공한다. 파이썬의 경우 `import heapq`
 - 스택은 가장 후입선출
 - 큐는 선입선출
 - 우선수위큐는 가장 우선순위가 높은 데이터 순서로 추출

 #### Heap 힙

 - 우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하나.
 - 최소 힙과 최대 힙이 존재.
 - 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 사용된다.
 - 리스트로 이용할 경우 삽입 시간이 O(1), 삭제시간이 O(N)이 들고 힙은 O(logN), O(logN)의 수행시간을 가진다.

 - heappush() : 특정 리스트에 어떠한 데이터를 넣을 때. heappop() : 특정 리스트에서 어떠한 데이터를 꺼낼 때.

 - 데이터를 꺼낼 때 우선순위에 따라 꺼낸다는 특징이 있기에 정렬이 가능하다. 기본적으로 mihheap 방식으로 정렬되어 있기에, 우선순위가 낮은 원소부터 꺼내지게 된다. 오름차순으로 데이터를 정렬하고자 한다면 heap에 모든 자료를 넣었다가 다시 모든 자료를 꺼내게 되면 그렇게 꺼내게 된 데이터 순서 자체가 오름차순이 된 상태가 된다. 시간 복잡도 O(NlogN). 정렬 알고리즘과 동일한 시간 복잡도 보유.

 - 파이썬에서는 최소힙만 제공한다. 따라서 힙에 데이터를 넣을 때 부호를 바꾸고, 꺼낼 때 부호를 바꿔주면 최대힙 형태로 데이터가 작동하게 된다. 내림차순 할 때.

 ### 다익스트라 알고리즘 : 개선 구현

 - 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 heap 자료구조를 이용하는 것이다.
 - 이 때 기본적인 원리는 동일하다. 하지만 거리가 가장 짧은 노드를 고르기 위해서 Heap에 원소를 넣을 때 거리 기준으로 데이터를 넣음으로써 거리가 짧은 순서부터 각 노드에 대한 정보다 나ㅏ올 수 있도록 하여 수행시간을 줄일 수 있다.

 - 현재 가장 가까운 노드를 저장해놓기 위해서 힙 자료구조를 추가적으로 이용한다는 점이 다른다.
 - 현재의 최단거리가 가장 짧은 노드를 선택해야 하므로 최소 힙을 사용한다.

 - 튜플 값의 인덱스 0, 거리 순으로 우선순위를 설정하는듯?

 - 힙 자료구조를 이용하는 다익스트라 알고리즘의 시간 복잡도는 O(ElogV)이다. 노드의 갯수 V 이상을 처리하지 않는다. 새 노드가 처리되어 있다면 무시가 된다.

 - 결과적으로 반복문 안에서 연산이 호출되는 횟수는 간선의 갯수와 도잉ㄹ하다. 즉,간선의 갯수만큼 연산이 수행된다.

 - 직관적으로 전체 과정은 E개의 원소를 우선순위 큐에 넣었다가 보두 빼내는 연산과 매우 유사하다. 시간 복잡도는 O(ElogE)로 판단 할 수 있다.

 - 중복 간선을 포함하지 않는 경우에, 이를 O(ElogV)로 정리 할 수 있다. ElogE에서 E는 V^2보다 작을 것. 즉 2ElogV가 되고, 빅오표기법 상 상수 제거되어 ElogV가 최종 시간 복잡도가 된다.

## 플로이드 워셜 알고리즘

 - 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산한다.
 - 플로이드 워셜 알고리즘은 다익스트라 알고리즘과 마찬가지로 단계별로 거쳐가는 노드를 기준으로 알고리즘을 수행한다. 다만, 매 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드들을 찾는 과정이 필요하지 않다.
 - 플로이드 워셜은 2차원 테이블에 최단 거리 정보를 저장한다. 이후 점화식을 통해 테이블을 맞춘다.
 - 플로이드 워셜 알고리즘은 DP 유형에 속한다.
 - 3중 for 문을 통해 계산을 하며, 모든 노드에서 모든 노드로의 최단거리를 구하는 과정이 있기에 시간 복잡도가 O(N^3)이다. 노드의 갯수, 간선의 갯수가 적을 때만 사용한다.

 - 각 단계마다 특정한 노드 k를 거쳐 가는 경우를 화인한다. a에서 b로 가는 최단 거리보다 a에서 k를 거쳐 b로 가는 거리가 더 짧은지 검사한다.
점화식 : Dab = min(Dab, Dak + Dkb) : 기존 a에서 b로 가는 최단 거리과 a에서 k로, k에서 b로 가는 거리 중 작은 값 선택

 - 노드의 갯수가 500개 안쪽으로 들어오는 경우가 많다.

 - 노드의 갯수가 N개일 때 알고리즘 상 N번의 단계를 수행.
 - 각 단계마다 O(N^2)의 연산을 통해 현재 노드를 거쳐가는 모든 경로를 고려한다. 따라서, 총 시간 복잡도는 O(N^3)이다.
 - 노드의 갯수가 작아야 플로이드 워셜 알고리즘이 가능하다. 이마저도 시간제한이 넉넉하지 않다. 다익스트라, 플로이드 워셜 등 어떤 알고리즘을 하는 것이 좋을지 생각해보고 적합한 알고리즘ㅇ르 쓰는 것이 좋다. 