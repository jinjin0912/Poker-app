# class Cardを定義
class Card:
    def __init__(self,suit="Spade",number="Ace"):
        self.suit=suit
        self.number=number
    def judge(self):
        print('The card is '+self.number+' of ' + self.suit)

#スーツ、数のリストを用意
suits=["Spade","Diamond","Club","Heart"]
numbers=['A','2','3','4','5','6','7','8','9','T','J','Q','K']


numbers[0]="A"
numbers[9]="T"
numbers[10]="J"
numbers[11]='Q'
numbers[12]='K'