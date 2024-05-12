import random
class Deck:
    def __init__(self):
        self.cards=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]*4
class Player:
    def __init__(self,number):
        self.card=[]
        self.numb=number
    def deal(self,deck):
        self.draw=deck.cards[random.randint(0,len(deck.cards)-1)]
        deck.cards.remove(self.draw)
        self.card.append(self.draw)
class GameMaster:
    def deal(self,player,deck):
        deal="Yes"
        while deal=="Yes":
            deal=input("Player "+str(player.numb)+" would you like to deal? ")
            if deal=="Yes":
                player.deal(deck)
                print(player.card)
            if self.checkValue(player)==21:
                print("BlackJack")
                return
            if self.checkValue(player)>21:
                print("You're busted")
                return
    def checkValue(self,player):
        value=0
        for i in range (len(player.card)):
            if player.card[i]=="A":
                value+=1
            elif player.card[i]=="J" or player.card[i]=="Q" or player.card[i]=="K":
                value+=10
            else:
                value+=player.card[i]
        if "A" in player.card and value<=11:
            value+=10
        return value
deck=Deck()
player1=Player(1)
player2=Player(2)
for i in range(2):
    player1.deal(deck)
    player2.deal(deck)
print(player1.card)
print(player2.card)
gm=GameMaster()
gm.deal(player1,deck)
gm.deal(player2,deck)
print("Player 1:",gm.checkValue(player1))
print("Player 2:",gm.checkValue(player2))