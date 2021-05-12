#スーツ、数、役のリストを用意
suits=["スペード","ダイヤ","クラブ","ハート"]
numbers=['A','2','3','4','5','6','7','8','9','T','J','Q','K']
suits_2=['s','d','c','h']
yaku=['ハイカード','ワンペア','ツーペア','スリーオブアカインド','ストレート','フラッシュ','フルハウス','クアッズ','ストレートフラッシュ','ロイヤルフラッシュ']
a_cards=[]
b_cards=[]
# class Cardを定義
class Card:
    def __init__(self,suit=0,number=0):
        self.suit=suit
        self.number=number
    def judge(self):
        print(suits[self.suit]+'の'+numbers[self.number]+'です')
    def identify(self):
        return numbers[self.number]+suits_2[self.suit]

#validate_suit関数を用意
def validate_suit(suit):
    if  suit.isdecimal()==False:
        return False
    elif int(suit)>3 or int(suit)<0:
        return False
    else :
        return True

#validate_number関数を用意
def validate_number(number):
    if  number.isdecimal()==False:
        return False
    elif int(number)<1 or int(number)>13:
        return False
    else :
        return True

#card_input関数を定義
def card_input(person):
    card_suit=input('カードのスートを選んでください (0:スペード 1:ダイヤ 2:クラブ 3:ハート) :')
      
    while validate_suit(card_suit)==False:
        card_suit=input('正しく入力してください (0:スペード 1:ダイヤ 2:クラブ 3:ハート) :')

    card_number=input('カードの数字を選んでください (A:1 2-9:2-9 T:10 J:11 Q:12 K:13) :')

    while validate_number(card_number)==False:
        card_number=input('正しいカードの数字を選んでください (A:1 2-9:2-9 T:10 J:11 Q:12 K:13):')
    
    card=Card(int(card_suit),int(card_number)-1)

    if person==0:
        a_cards.append(card)

    
    elif person==1:
        b_cards.append(card)

#a_judge_hand 関数を定義
def a_judge_hand(hand):
    for i in range(hand):
        if a_cards[hand].suit==a_cards[i].suit and a_cards[hand].number==a_cards[i].number:
            return False

#b_judge_hand 関数を定義
def b_judge_hand(hand):
    for i in range(hand):
        if b_cards[hand].suit==b_cards[i].suit and b_cards[hand].number==b_cards[i].number:
            return False
        elif b_cards[hand].suit==a_cards[0].suit and b_cards[hand].number==a_cards[0].number:
            return False
        elif b_cards[hand].suit==a_cards[1].suit and b_cards[hand].number==a_cards[1].number:
            return False
        elif b_cards[hand].suit==a_cards[2].suit and b_cards[hand].number==a_cards[2].number:
            return False
        elif b_cards[hand].suit==a_cards[3].suit and b_cards[hand].number==a_cards[3].number:
            return False     
        elif b_cards[hand].suit==a_cards[4].suit and b_cards[hand].number==a_cards[4].number:
            return False

#Aさんのハンド入力
print('-------------------------------------')    

print('Aさんの1枚目のカードを入力してください') 

card_input(0)

for i in range(1,5): 
    print('-------------------------------------')

    print('Aさんの' +str(i+1)+ '枚目のカードを入力してください') 

    card_input(0)

    while  a_judge_hand(i)==False:
        print('同じカードは使えません　正しく入力してください')
        a_cards.pop(i)
        card_input(0)   



print('-------------------------------------')   

print('-------------------------------------')  

#Bさんのハンド入力

print('Bさんの1枚目のカードを入力してください') 

card_input(1) 

while (b_cards[0].suit==a_cards[0].suit and b_cards[0].number==a_cards[0].number) or (b_cards[0].suit==a_cards[1].suit and b_cards[0].number==a_cards[1].number) or (b_cards[0].suit==a_cards[2].suit and b_cards[0].number==a_cards[2].number) or (b_cards[0].suit==a_cards[3].suit and b_cards[0].number==a_cards[3].number) or (b_cards[0].suit==a_cards[4].suit and b_cards[0].number==a_cards[4].number):
    print('同じカードは使えません　正しく入力してください')
    b_cards.pop(0)
    card_input(1)
            
for i in range(1,5):
    print('-------------------------------------')

    print('Bさんの'+str(i+1)+'枚目のカードを入力してください') 

    card_input(1) 

    while  b_judge_hand(i)==False:
        print('同じカードは使えません　正しく入力してください')
        b_cards.pop(i)
        card_input(1)   



print('-------------------------------------')   
print('-------------------------------------')   
print('Aさんのハンド:'+ a_cards[0].identify()+','+a_cards[1].identify()+','+a_cards[2].identify()+','+a_cards[3].identify()+','+a_cards[4].identify())
print('Bさんのハンド:'+ b_cards[0].identify()+','+b_cards[1].identify()+','+b_cards[2].identify()+','+b_cards[3].identify()+','+b_cards[4].identify())


#ハンドをリストに入れる
a_suits=[]
a_numbers=[]
b_suits=[]
b_numbers=[]

for i in range(0,5):
    a_suits.append(a_cards[i].suit)
    a_numbers.append(a_cards[i].number)
    b_suits.append(b_cards[i].suit)
    b_numbers.append(b_cards[i].number)

#ハンドリストをソートする
a_suits.sort()
a_numbers.sort()
b_suits.sort()
b_numbers.sort()

#役を判定する関数を作る
# ハイカード=0 ツーペア=1....
def a_poker_hand():
    if a_suits[0]==a_suits[1]==a_suits[2]==a_suits[3]==a_suits[4] :
        if a_numbers==[0,9,10,11,12]:
            return 9
        elif a_numbers[1]==a_numbers[0]+1 and a_numbers[2]==a_numbers[1]+1 and a_numbers[3]==a_numbers[2]+1 and a_numbers[4]==a_numbers[3]+1 : 
            return 8
        else:
            return 5
    dup=[x for x in set(a_numbers) if a_numbers.count(x)==4]

    if len(dup)==1 :
        return 7
    dup=[x for x in set(a_numbers) if a_numbers.count(x)==3]
    dup2=[x for x in set(a_numbers) if a_numbers.count(x)>=2]
    if len(dup)==1 and len(dup2)==2:
        return 6
    
    if a_numbers[1]==a_numbers[0]+1 and a_numbers[2]==a_numbers[1]+1 and a_numbers[3]==a_numbers[2]+1 and a_numbers[4]==a_numbers[3]+1 :
        return 4
    
    if len(dup)==1 :
        return 3
    
    if len(dup2)==2 :
        return 2

    if len(dup2)==1 :
        return 1
    else:
        return 0

def b_poker_hand():
    if b_suits[0]==b_suits[1]==b_suits[2]==b_suits[3]==b_suits[4] :
        if b_numbers==[0,9,10,11,12]:
            return 9
        elif b_numbers[1]==b_numbers[0]+1 and b_numbers[2]==b_numbers[1]+1 and b_numbers[3]==b_numbers[2]+1 and b_numbers[4]==b_numbers[3]+1 : 
            return 8
        else:
            return 5
    dup=[x for x in set(b_numbers) if b_numbers.count(x)==4]

    if len(dup)==1 :
        return 7
    dup=[x for x in set(b_numbers) if b_numbers.count(x)==3]
    dup2=[x for x in set(b_numbers) if b_numbers.count(x)>=2]
    if len(dup)==1 and len(dup2)==2:
        return 6
    
    if b_numbers[1]==b_numbers[0]+1 and b_numbers[2]==a_numbers[1]+1 and b_numbers[3]==b_numbers[2]+1 and b_numbers[4]==b_numbers[3]+1 :
        return 4
    
    if len(dup)==1 :
        return 3
    
    if len(dup2)==2 :
        return 2

    if len(dup2)==1 :
        return 1
    else:
        return 0

     

print('Aさんの役は'+ yaku[a_poker_hand()] + 'です')   
print('Bさんの役は'+ yaku[b_poker_hand()] + 'です')    


def judge_win(a,b):
    if a>b:
        return 'Aさんの勝ちです'
    elif a<b :
        return 'Bさんの勝ちです'
    elif a==b==9:
        return 'チョップです'
    elif a==b==8:
        if max(a_numbers) > max(b_numbers):
            return 'Aさんの勝ちです'
        elif max(a_numbers) < max(b_numbers):
            return 'Bさんの勝ちです'
        else:
            return 'チョップです'
    
    elif a==b==7:
        dup_a_4=[x for x in set(a_numbers) if a_numbers.count(x)==4]
        dup_b_4=[x for x in set(b_numbers) if b_numbers.count(x)==4]
        dup_a_1=[x for x in set(a_numbers) if a_numbers.count(x)==1]
        dup_b_1=[x for x in set(b_numbers) if b_numbers.count(x)==1]
        if dup_a_4[0]>dup_b_4[0]:
            return 'Aさんの勝ちです'
        elif dup_a_4[0]<dup_b_4[0]:
            return 'Bさんの勝ちです'
        elif dup_a_1[0]>dup_b_1[0]:
            return 'Aさんの勝ちです'
        elif dup_a_1[0]>dup_b_1[0]:
            return 'Bさんの勝ちです'
        else:
            return 'チョップです'
    
    elif a==b==6:
        dup_a_3=[x for x in set(a_numbers) if a_numbers.count(x)==3]
        dup_b_3=[x for x in set(b_numbers) if b_numbers.count(x)==3]
        dup_a_2=[x for x in set(a_numbers) if a_numbers.count(x)==2]
        dup_b_2=[x for x in set(b_numbers) if b_numbers.count(x)==2]
        if dup_a_3>dup_b_3:
            return 'Aさんの勝ちです'
        elif dup_a_3[0]<dup_b_3[0]:
            return 'Bさんの勝ちです'
        elif dup_a_2[0]>dup_b_2[0]:
            return 'Aさんの勝ちです'
        elif dup_a_2[0]<dup_b_2[0]:
            return 'Bさんの勝ちです'
        else:
            return 'チョップです'
    
    elif a==b==5:
        if a_numbers[4]>b_numbers[4]:
            return 'Aさんの勝ちです'
        elif a_numbers[4]<b_numbers[4]:
            return 'Bさんの勝ちです'
        elif a_numbers[3]>b_numbers[3]:
            return 'Aさんの勝ちです'
        elif a_numbers[3]<b_numbers[3]:
            return 'Bさんの勝ちです'
        elif a_numbers[2]>b_numbers[2]:
            return 'Aさんの勝ちです'
        elif a_numbers[2]<b_numbers[2]:
            return 'Bさんの勝ちです'
        elif a_numbers[1]>b_numbers[1]:
            return 'Aさんの勝ちです'
        elif a_numbers[1]<b_numbers[1]:
            return 'Bさんの勝ちです'
        elif a_numbers[0]>b_numbers[0]:
            return 'Aさんの勝ちです'
        elif a_numbers[0]<b_numbers[0]:
            return 'Bさんの勝ちです'    
        else:
            return 'チョップです'
        
    elif a==b==4:
        if max(a_numbers) > max(b_numbers):
            return 'Aさんの勝ちです'
        elif max(a_numbers) < max(b_numbers):
            return 'Bさんの勝ちです'
        else:
            return 'チョップです'
    elif a==b==3:
        dup_a_3=[x for x in set(a_numbers) if a_numbers.count(x)==3]
        dup_b_3=[x for x in set(b_numbers) if b_numbers.count(x)==3]
        dup_a_1=[x for x in set(a_numbers) if a_numbers.count(x)==1]
        dup_b_1=[x for x in set(b_numbers) if b_numbers.count(x)==1]
        dup_a_1.sort()
        dup_b_1.sort()
        if dup_a_3[0]>dup_b_3[0]:
            return 'Aさんの勝ちです'
        elif dup_a_3[0]<dup_b_3[0]:
            return 'Bさんの勝ちです'
        elif dup_a_1[1]>dup_b_1[1]:
            return 'Aさんの勝ちです'
        elif dup_a_1[1]<dup_b_1[1]:
            return 'Bさんの勝ちです'
        elif dup_a_1[0]>dup_b_1[0]:
            return 'Aさんの勝ちです'
        elif dup_a_1[0]<dup_b_1[0]:
            return 'Bさんの勝ちです'
        else:
            return 'チョップです'
    elif a==b==2:
        dup_a_2=[x for x in set(a_numbers) if a_numbers.count(x)==2]
        dup_b_2=[x for x in set(b_numbers) if b_numbers.count(x)==2]
        dup_a_1=[x for x in set(a_numbers) if a_numbers.count(x)==1]
        dup_b_1=[x for x in set(b_numbers) if b_numbers.count(x)==1]
        dup_a_2.sort()
        dup_b_2.sort()
        if dup_a_2[1]>dup_b_2[1]:
            return 'Aさんの勝ちです'
        elif dup_a_2[1]<dup_b_2[1]:
            return 'Bさんの勝ちです'
        elif dup_a_2[0]>dup_b_2[0]:
            return 'Aさんの勝ちです'
        elif dup_a_2[0]<dup_b_2[0]:
            return 'Bさんの勝ちです'
        elif dup_a_1[0]>dup_b_1[0]:
            return 'Aさんの勝ちです'
        elif dup_a_1[0]<dup_b_1[0]:
            return 'Bさんの勝ちです'
        else:
            return 'チョップです'
    
    elif a==b==1:
        dup_a_2=[x for x in set(a_numbers) if a_numbers.count(x)==2]
        dup_b_2=[x for x in set(b_numbers) if b_numbers.count(x)==2]
        dup_a_1=[x for x in set(a_numbers) if a_numbers.count(x)==1]
        dup_b_1=[x for x in set(b_numbers) if b_numbers.count(x)==1]
        dup_a_1.sort()
        dup_b_1.sort()
        if dup_a_2[0]>dup_b_2[0]:
            return 'Aさんの勝ちです'
        elif dup_a_2[0]<dup_b_2[0]:
            return 'Bさんの勝ちです'
        elif dup_a_1[2]>dup_b_1[2]:
            return 'Aさんの勝ちです'
        elif dup_a_1[2]<dup_b_1[2]:
            return 'Bさんの勝ちです'
        elif dup_a_1[1]>dup_b_1[1]:
            return 'Aさんの勝ちです'
        elif dup_a_1[1]<dup_b_1[1]:
            return 'Bさんの勝ちです'
        elif dup_a_1[0]>dup_b_1[0]:
            return 'Aさんの勝ちです'
        elif dup_a_1[0]<dup_b_1[0]:
            return 'Bさんの勝ちです'

        else :
            return 'チョップです'
    
    elif a==b==0:
        if a_numbers[4]>b_numbers[4]:
            return 'Aさんの勝ちです'
        elif a_numbers[4]<b_numbers[4]:
            return 'Bさんの勝ちです'
        elif a_numbers[3]>b_numbers[3]:
            return 'Aさんの勝ちです'
        elif a_numbers[3]<b_numbers[3]:
            return 'Bさんの勝ちです'
        elif a_numbers[2]>b_numbers[2]:
            return 'Aさんの勝ちです'
        elif a_numbers[2]<b_numbers[2]:
            return 'Bさんの勝ちです'
        elif a_numbers[1]>b_numbers[1]:
            return 'Aさんの勝ちです'
        elif a_numbers[1]<b_numbers[1]:
            return 'Bさんの勝ちです'
        elif a_numbers[0]>b_numbers[0]:
            return 'Aさんの勝ちです'
        elif a_numbers[0]<b_numbers[0]:
            return 'Bさんの勝ちです'    
        else:
            return 'チョップです'
print(judge_win(a_poker_hand(),b_poker_hand()))

        
        
        
