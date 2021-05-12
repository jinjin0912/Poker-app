import random
import function as Fun
Cards=['A','K','Q']
player_stack=100
enemy_stack=100
SB=1
BB=1


while player_stack !=0 and enemy_stack !=0 :
    player_stack -=SB
    enemy_stack -=BB
    pot=SB+BB
    player_bet=0
    enemy_bet=0
    player_status=1 #アクションに残っている状態が1、fold済みは0
    enemy_status=1　#アクションに残っている状態が1、fold済みは0

    x=random.sample(Cards,2)
    player_hands,enemy_hands=Fun.split_list(x,1)
    print(player_hands)
    print(enemy_hands)
    while player_status==enemy_status:
    # action=input('アクションを選択してください(0:チェック 1:ベットorレイズ 2:コール 3:フォールド ):')
    while player_status==1:
        action=input('アクションを選択してください(0:チェック 1:ベットorレイズ 2:コール 3:フォールド ):')
        while Fun.validate_action(action,player_bet,enemy_bet,player_stack)==False:
            action=input('正しいアクションを選択してください(0:チェック 1:ベットorレイズ 2:コール 3:フォールド ):')
　　　　　
        if action==3:
            enemy_stack += pot
            who_win('相手')
        if action==2:
            if Fun.judge_player_win(player_hands,enemy_hands):
                player_stack += pot
                who_win('プレイヤー')
            else:
                enemy_stack += pot
                who_win("相手")
        
        if action==1:
            player_bet+=int(input(レイズorベット額を打ち込んでください:))
                

        player_bet+=0
    
        if enemy_hands[0]=="A":
            enemy_bet=random.random(1,enemy_stack)
            print('相手が'+str(enemy_bet)+'しました')
            action_player==
            



    print(judge_player_win(player_hands,enemy_hands))



       