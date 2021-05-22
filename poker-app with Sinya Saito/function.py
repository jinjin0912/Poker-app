#split_list関数を定義
def split_list(l,n):
    for idx in range(0,len(l),n):
        yield l[idx:idx+n]

#プレイヤー勝利判定関数
def judge_player_win(x,y):
    if x[0]=="A":
        return True
    elif y[0]=="A":
        return False
    elif y[0]=="Q":
        return True
    elif x[0]=="Q":
        return False

def action(状態):
    print(相手がraise,check)
    comandChoice(状態)
    何かの処理
    if 状態:
        action(状態)
def blindBet(1,pot):
    
    pot+=1
    return pot
def validate_action(action,player_bet,enemy_bet,player_stack,enemy_stack):
    if action==3:
        return True
    if action==2:
        if enemy_bet>player_bet:
            return True
        if enemy_bet==player_bet:
            return False
    if action==1:
        if player_stack>
    
def who_win(player):
    print(player+"がポットを取りました")
