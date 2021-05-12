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
    elif int(number)<0 or int(number)>13:
        return False
    else :
        return True

#カードのスートと数字を確認   
card1_suit=input('Please choose the suit of the card 0:Spade 1:Diamond 2:Club 3:Heart :')

while validate_suit(card1_suit)==False:
    card1_suit=input('Please choose the colect one 0:Spade 1:Diamond 2:Club 3:Heart :')

card1_number=input('Please choose the number of the card(1 to 13) :')

while validate_number(card1_number)==False:
    card1_number=input('Please choose the collect number(1 to 13) :')










