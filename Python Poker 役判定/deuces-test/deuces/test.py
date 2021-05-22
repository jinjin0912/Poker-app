from deuces import Card
from deuces import evaluator
from deuces import Deck
deck=Deck()
board=deck.draw(5)
player1_hand=deck.draw(2)
player2_hand=deck.draw(2)
print(evaluator.evaluate(board,player1_hand))
