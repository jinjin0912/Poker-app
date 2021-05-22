class Player:
    def __init__(self,stack=100,status=1,bet=0,hand='A',action=4):
        self.stack=stack
        self.status=status
        self.bet=bet
        self.hand=hand
        self.action=action
    def clear_bet(self):
        self.bet=0
    def clear_status(self):
        self.status=0
    

