import random
import function as Fun
from player_class import Player
Cards=['A','K','Q']
players=[]
player_num=2
for i in range(player_num):
    player=Player()
    players.append(player)   


SB=1
BB=1


while players[0].stack !=0 and player[1].stack !=0 :
    players[0].stack -=SB
    player[1].stack -=BB
    pot=SB+BB
    for i in range(player_num)
    player[i-1].clear_bet()
    player[i-1].clear_status()
    
    x=random.sample(Cards,2)
    players[0].hand,players[1].hand=Fun.split_list(x,1)    
    print("player1のハンド:"+player[0].hand+" palyer2のハンド:"+player[1].hand)
    
    while players[0].status==1 and players.status[1]==1
        players[0].action=input('player1のアクションを選択してください(0:チェック 1:ベットorレイズ 2:コール 3:フォールド ):')
        while Fun.validate_action(action,player_bet,enemy_bet,player_stack)==False:
            players[0].action=input('player1の正しいアクションを選択してください(0:チェック 1:ベットorレイズ 2:コール 3:フォールド ):')
　　　　　
        if players[0].action==3:
            players[1].stack += pot
            Fun.who_win('player2')
            players[0].status=0 
            players[1].status=0
        if action==2:
            pot+=players[1].bet-players[0].bet
            if Fun.judge_player_win(players[0].hand,players[1].hand):
                players[0].stack += pot
                Fun.who_win('player1')
            else:
                players[1].stack=pot
                Fun.who_win("player2")
            players[0].status=0 
            players[1].status=0
        
        if action==1:
            while
            print('player1のスタック:'+str(player[0].stack))
            players[0].bet+=int(input('レイズorベット額を整数で打ち込んでください:'))
            while 2*players[1].bet-players[0]<=0 :
                players[0].bet=int(input('正しいレイズorベット額を整数で打ち込んでください:'))
            if players[0].bet>players[0].stack:
                players[0].bet=players[0].stack
            
            print("player2のスタック:"+str(player[1].stack))
            

        
        
        
                

    
    
        if enemy_hands[0]=="A":
            enemy_bet=random.random(1,enemy_stack)
            print('相手が'+str(enemy_bet)+'しました')
            action_player==
            



    print(judge_player_win(player_hands,enemy_hands))



       