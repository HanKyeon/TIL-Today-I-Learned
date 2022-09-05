'''
상어 초등학교

n*n 교실 n**2 학생 수
r,c는 r행 c열. 1,1로 시작, n,n끝 학생순서, 학생이 좋아하는 학생 4명 조사.
칸 당 하나 |r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸이 (r1, c1)과 (r2, c2)를 인접하다고 한다. -> 사방인접

1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. 1을 만족하는 칸이 여러개면 인접한 칸 중 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3. 2를 만족하는 칸도 여러개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러개이면 열의 번호가 가장 작은 칸으로.

선호 학생 인접 수 우선, 인접 빈칸 수 우선, 좌상단 우선.

자리배치 이후 만족도. 주변에 앉은 좋아하는 애 수 0 0, 1or2 10, 3 100, 4 1000
학생 만족도의 총합.

입력
n 3이상 20이하
학생번호 선호4학생 n**2만큼 제시.

출력
만족도 총 합
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
# 사방이동
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

n = int(input())
g = [[0]*n for _ in range(n)] # 그래프
dic = {} # 번호가 선호하는 숫자 넣을 딕트
sit = set() # 자리 앉았는지 여부 확인용
for i in range(n**2):
    idx, l1, l2, l3, l4 = map(int, input().rstrip().split())
    dic[idx] = set([l1, l2, l3, l4])
    nsits = [] # 힙
    for i in range(n):
        for j in range(n):
            if (i, j) in sit: # 이미 앉았으면 다음 자리
                continue
            # [fz, zs, h, w]
            fz, zs = 0, 0 # 근처 친구 숫자, 빈자리 숫자
            for k in range(4):
                ni, nj = i + dh[k], j + dw[k]
                if 0<=ni<n and 0<=nj<n:
                    if g[ni][nj] == 0:
                        zs+=1
                    elif g[ni][nj] in dic[idx]:
                        fz+=1
            if nsits and nsits[0][0] < -fz: # 들어가있고, 친구 수가 이미 들어간 자리보다 적으면 넣을 필요 없음.
                continue
            heappush(nsits, [-fz, -zs, i, j]) # 힙에 추가
    frnz, zerz, h, w = heappop(nsits) # 앉힐거임
    sit.add((h, w)) # 앉히고
    g[h][w] = idx # 기록


score = [0]*5 # 점수
for i in range(n):
    for j in range(n):
        bgr = dic[g[i][j]] # 좋아하는 친구 딕트 부를 것임.
        c = 0 # 좋아하는 친구 숫자 셀 것.
        for k in range(4):
            ni, nj = i + dh[k], j + dw[k]
            if 0<=ni<n and 0<=nj<n and g[ni][nj] in bgr:
                c+=1
        # print(g[i][j], c)
        # print(bgr)
        score[c] += 1 # 친구 숫자에 맞게 넣고
# print(dic)
# for i in g:
#     print(*i)
# print(score)
ans = score[1] + score[2]*10 + score[3]*100 + score[4]*1000 # 정답 정리
print(ans) # 출력




'''
2 2 1 2 3 2 1 1 0
'''
'''
빠른 코드

def get_is_in_bound(size, row, col):
    return row >= 0 and row < size and col >= 0 and col < size

class Seat:
    def __init__(self, board_size, row, col):
        self.student = 0
        self.near_student_list = []
        self.near_blank_count = 4
        if row == 0 or row == board_size - 1:
            self.near_blank_count -= 1
        if col == 0 or col == board_size - 1:
            self.near_blank_count -= 1
        
    def set_student(self, board, size, row, col, student):
        # print(f'set_student {row} {col} {student}')
        self.student = student
        
        near_coord_list = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        for near_row, near_col in near_coord_list:
            if get_is_in_bound(size, near_row, near_col):
                # 제대로 구현한다면 덮어쓰기도 고려해야됨
                seat = board[near_row][near_col]
                seat.near_blank_count -= 1
                seat.near_student_list.append(student)
                # 방어적으로 한다면 0이하도 고려해야됨
        # 다른 좌표의 near_student_list, near_blank_count 설정해주기
        

def print_board(board, size):
    for row in range(size):
        for col in range(size):
            print(f'{board[row][col].student} {board[row][col].near_blank_count}', end = '/ ')
        print('')
    
def get_like_count(near_student_list, favorite_students):
    count = 0
    for student in near_student_list:
        if student in favorite_students:
            count += 1
    
    return count
    
def arrange_by_like_count(board, size, student, candidate_seats, favorite_students):
    max_like_count = -1
    max_like_list = []
    
    for row in range(size):
        for col in range(size):
            seat = board[row][col]
            if seat.student > 0:
                continue
            
            like_count = get_like_count(seat.near_student_list, favorite_students)
        
            if max_like_count < like_count:
                max_like_count = like_count
                max_like_list = [(row, col)]
            elif max_like_count == like_count:
                max_like_list.append((row, col))
          
    candidate_seats.clear()
    candidate_seats.extend(max_like_list)
    
    if len(candidate_seats) == 1:
        row, col = candidate_seats[0]
        board[row][col].set_student(board, size, row, col, student)
        # near_student_list, near_blank_count 재조정
        return True
    
    return False
    
def arrange_by_blank_count(board, size, student, candidate_seats):
    big_blank_list = [candidate_seats[0]]
    
    for row, col in candidate_seats:
        big_seat = board[big_blank_list[0][0]][big_blank_list[0][1]]
        seat = board[row][col]
        
        if big_seat.near_blank_count < seat.near_blank_count:
            big_blank_list = [(row, col)]
        elif big_seat.near_blank_count == seat.near_blank_count:
            big_blank_list.append((row, col))
            
    candidate_seats.clear()
    candidate_seats.extend(big_blank_list)
    
    if len(candidate_seats) == 1:
        row, col = candidate_seats[0]
        board[row][col].set_student(board, size, row, col, student)
        return True
    
    return False
    
def arrange_by_small_row(board, size, student, candidate_seats):
    small_row_list = [candidate_seats[0]]
    
    for row, col in candidate_seats[1:]:
        if small_row_list[0][0] == row:
            small_row_list.append((row, col))
        elif small_row_list[0][0] > row:
            small_row_list = [(row, col)]
    
    candidate_seats.clear()
    candidate_seats.extend(small_row_list)
    
    if len(candidate_seats) == 1:
        row, col = candidate_seats[0]
        board[row][col].set_student(board, size, row, col, student)
        return True
    
    return False
    
def arrange_by_small_col(board, size, student, candidate_seats):
    seat = candidate_seats[0]
    for candidate in candidate_seats[1:]:
        if seat[1] > candidate[1]:
            seat = candidate
    
    row, col = seat
    board[row][col].set_student(board, size, row, col, student)
    
def arrange_seat(board, size, arrange_sequence, student_like_map):
    for student in arrange_sequence:
        candidate_seats = []
        # 1. 좋아하는 학생이 가장 많은 곳으로 배치
        if arrange_by_like_count(board, size, student, candidate_seats, student_like_map[student]):
            continue
            
        # 2. 인접한 빈칸이 가장 많은 곳 구하기
        if arrange_by_blank_count(board, size, student, candidate_seats):
            continue
        
        # 3. 행번 가장 작은 곳 구하기
        if arrange_by_small_row(board, size, student, candidate_seats):
            continue
        
        # 4. 열번 가장 작은 곳 구하기
        arrange_by_small_col(board, size, student, candidate_seats)
        
    
def get_satisfaction(student_like_count):
    if student_like_count == 0:
        return 0
    else:
        return 10 ** (student_like_count - 1)
            
def get_satisfaction_sum(board, size, student_like_map):
    satisfaction = 0
    near_coord_list = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    for row in range(size):
        for col in range(size):
            student_like_count = 0
            student = board[row][col].student
            for row_variation, col_variation in near_coord_list:
                near_row = row + row_variation
                near_col = col + col_variation
                
                if get_is_in_bound(size, near_row, near_col):
                   near_student = board[near_row][near_col].student
                   if near_student in student_like_map[student]:
                       student_like_count += 1
            
            satisfaction += get_satisfaction(student_like_count)
    
    return satisfaction

size = int(input())
student_count = size ** 2
arrange_sequence = []
student_like_map = {}
board = [[Seat(size, row, col) for col in range(size)] for row in range(size)]

for i in range(student_count):
    line = [int(num) for num in input().split()]
    arrange_sequence.append(line[0])
    student_like_map[line[0]] = line[1:]
    
arrange_seat(board, size, arrange_sequence, student_like_map)

# print_board(board, size)
       
# 출력: 만족도 총합
print(get_satisfaction_sum(board, size, student_like_map))

'''