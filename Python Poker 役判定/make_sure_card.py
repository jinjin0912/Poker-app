# #validate_suit関数を用意
# def validate_suit(suit):
#     if  suit.isdecimal()==False:
#         return False
#     elif int(suit)>3 or int(suit)<0:
#         return False
#     else :
#         return True

# #validate_number関数を用意
# def validate_number(number):
#     if  number.isdecimal()==False:
#         return False
#     elif int(number)<1 or int(number)>13:
#         return False
#     else :
#         return True

# #カードのスートと数字を確認   
# card1_suit=input('Please choose the suit of the card 0:Spade 1:Diamond 2:Club 3:Heart :')

# while validate_suit(card1_suit)==False:
#     card1_suit=input('Please choose the colect one 0:Spade 1:Diamond 2:Club 3:Heart :')

# card1_number=input('Please choose the number of the card(1 to 13) :')

# while validate_number(card1_number)==False:
#     card1_number=input('Please choose the collect number(1 to 13) :'a

a={1,2,3,4}

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
    card_suit=input('カードのスートを選んでください 0:スペード 1:ダイヤ 2:クラブ 3:ハート :')
      
    while validate_suit(card_suit)==False:
        card_suit=input('正しく入力してください 0:スペード 1:ダイヤ 2:クラブ 3:ハート :')

    card_number=input('カードの数字を選んでください(A:1 2-9:2-9 T:10 J:11 Q:12 K:13) :')

    while validate_number(card_number)==False:
        card_number=input('正しいカードの数字を選んでください(A:1 2-9:2-9 T:10 J:11 Q:12 K:13):')
    
    card=Card(int(card_suit),int(card_number)-1)

    if person==0:
        a_cards.append(card)

    
    elif person==1:
        b_cards.append(card)

a=[0,0,2,10,12]
b=[0,0,3,9,12]

dup_a_2=[x for x in set(a) if a_numbers.count(x)==2]
dup_b_2=[x for x in set(b) if a_numbers.count(x)==2]
dup_a_1=[x for x in set(a) if a_numbers.count(x)==1]
dup_b_1=[x for x in set(b) if a_numbers.count(x)==1]
dup_a_1.sort()
dup_b_1.sort()

print(dup_a_1)
print(dup_b_1)