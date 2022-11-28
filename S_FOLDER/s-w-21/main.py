import random

DEER = 0
RABBIT = 1
SNAKE = 2

# ※ 전역변수 및 함수 사용 가능합니다
# ※ 단, 팀명을 앞에 prefix로 붙여주세요
#     ex) seoul12_2_sum = 0
#     ex) def seoul12_2() { } 
# ※ 현재 상태에서 빌드 시 사용할 수 있는 API는 사용 가능합니다
# ※ 제출방법 : Me 함수와 사용한 전역변수 또는 전역함수를 포함하여 txt 파일로 만들어서 제출
seoul1_6_myli = []
def Me(opp, turn, opp_prev, opp_last_pattern) :
    global seoul1_6_myli
    if turn == 0:
        seoul1_6_myli.append(2)
        return 2
    if len(set(map(tuple, opp_last_pattern))) == 1:
        if opp_prev == opp_last_pattern[0][turn-1]:
            if sum(opp_last_pattern[0]) == 20:
                if turn % 3:
                    seoul1_6_myli.append(2)
                    return 2
                else:
                    seoul1_6_myli.append(0)
                    return 0
            else:
                if opp_last_pattern[0][turn] == 0:
                    seoul1_6_myli.append(1)
                    return 1
                if opp_last_pattern[0][turn] == 1:
                    seoul1_6_myli.append(2)
                    return 2
                if opp_last_pattern[0][turn] == 2:
                    seoul1_6_myli.append(2)
                    return 2
    else:
        if seoul1_6_myli.count(0) <= 2 and (seoul1_6_myli and seoul1_6_myli[-1] != 0):
            return [2,2,2,0][random.randrange(0, 4)]
        else:
            return 2

# 아래 Opponent1~3은 테스트용 상대 사냥꾼입니다
# 기본 제공 코드는 임의 수정해도 관계 없습니다
# 상대방 추가 시, Register 함수를 통해 상대방을 등록합니다. ex) Register("Opp1", "Opponent1") 
def Opponent1(opp, turn, opp_prev, opp_last_pattern) :
    return random.randrange(0, 3)
    
def Opponent2(opp, turn, opp_prev, opp_last_pattern) :
    return random.randrange(0, 3)
    
def Opponent3(opp, turn, opp_prev, opp_last_pattern) :
    return 0
    
def Register(name, func) :
    global f_inx
    names[f_inx] = name
    f[f_inx] = func
    f_inx += 1
    
########################## MAIN ##########################
f = [0] * 150
names = [""] * 100
f_inx = 0
total_score = [0] * 150
last_pattern = [[[0] * 10 for _ in range(150)] for _ in range(150)] 
pattern_count = [0] * 150

Register("Me", "Me")
Register("Opp1", "Opponent1")
Register("Opp2", "Opponent2")
Register("Opp3", "Opponent3")

for i in range(140):
    for j in range(140):
        for k in range(10):
            last_pattern[i][j][k] = -1

for i in range(1, f_inx):
    for j in range(f_inx):
        team_a = j % f_inx
        team_b = (j+i) % f_inx
        
        print(f"[{names[team_a]}] vs [{names[team_b]}]")
        
        a_game_score = 0
        b_game_score = 0
        
        prev_a = -1
        prev_b = -1
        
        team_a_count = 0
        team_b_count = 0
        
        a_pattern = [0] * 10
        b_pattern = [0] * 10
        
        for k in range(10):
            a = eval("{} (team_b, k, prev_b, last_pattern[team_b])".format(f[team_a]))
            b = eval("{} (team_a, k, prev_a, last_pattern[team_a])".format(f[team_b]))
            a_pattern[k] = a
            b_pattern[k] = b
            
            if a == prev_a: team_a_count += a+1
            else: team_a_count = 0
            if b == prev_b: team_b_count += b+1
            else: team_b_count = 0
            
            if a != 0 and a != 1 and a != 2: team_a_count = 100
            if b != 0 and b != 1 and b != 2: team_b_count = 100
            
            prev_a = a
            prev_b = b
            
            a_score = 0
            b_score = 0
            
            if a == DEER and b == DEER: a_score = 50; b_score = 50;
            elif a == DEER and b == RABBIT: a_score = 0; b_score = 20;
            elif a == DEER and b == SNAKE: a_score = 0; b_score = 10;
            elif a == RABBIT and b == DEER: a_score = 20; b_score = 0;
            elif a == RABBIT and b == RABBIT: a_score = 20; b_score = 20;
            elif a == RABBIT and b == SNAKE: a_score = 0; b_score = 30;
            elif a == SNAKE and b == DEER: a_score = 10; b_score = 0;
            elif a == SNAKE and b == RABBIT: a_score = 30; b_score = 0;
            elif a == SNAKE and b == SNAKE: a_score = 10; b_score = 10;
            print(a, b)
            a_score -= team_a_count
            b_score -= team_b_count
            
            a_bonus = random.randrange(3)
            b_bonus = random.randrange(3)
            a_score += a_bonus
            b_score += b_bonus
            
            a_game_score += a_score
            b_game_score += b_score
            
            a_str = "SNAKE" if a == 2 else "RABBIT" if a == 1 else "DEER"
            b_str = "SNAKE" if b == 2 else "RABBIT" if b == 1 else "DEER"
            
            print(f"Turn [{k+1}] [{names[team_a]}:({a_str})] vs [{names[team_b]}:({b_str})] ---> score [{a_game_score}] / [{b_game_score}] ")
            
        for z in range(10):
            last_pattern[team_a][pattern_count[team_a]][z] = a_pattern[z]
            last_pattern[team_b][pattern_count[team_b]][z] = b_pattern[z]
            
        pattern_count[team_a] += 1
        pattern_count[team_b] += 1
            
        print("<Game Result>")
        if a_game_score == b_game_score: print("Draw")
        else:
            print("Win : [{}]".format(names[team_a] if a_game_score > b_game_score else names[team_b]))
        print()
        total_score[team_a] += a_game_score
        total_score[team_b] += b_game_score
            
print("<Final score>")
max_inx = 0
max_score = 0
for i in range(f_inx):
    print(f"[{names[i]}] Total Score : {total_score[i]}")
    if max_score < total_score[i]:
        max_inx = i
        max_score = total_score[i]

print(f"<Winner : [{names[max_inx]}] !!!>")

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        










