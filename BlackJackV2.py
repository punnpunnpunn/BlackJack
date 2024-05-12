import random
class Deck:
    def __init__(self):
        valueList=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
        faceList=["♠","♥","♦","♣"]
        self.deckList=[]
        for x in faceList:
            for y in valueList:
                self.deckList.append(f"{x} {y}")
    def shuffle(self):
        random.shuffle(self.deckList)
    def giveCard(self):
        return(self.deckList.pop(0))

class Player:
    def __init__(self):
        self.cardsList=[]
    def dealCard(self,card):
        self.cardsList.append(card)
    def checkValue(self,cardsList):
        faceCards="JQK1"
        cardValue=0
        A=False
        for card in cardsList:
            if card[2] in faceCards:
                cardValue+=10
            elif card[2] == "A":
                cardValue+=1
                A=True
            else:
                cardValue+=int(card[2])
        if cardValue<=11:
            if A:
                cardValue+=10
        return cardValue
    def checkBust(self):
        if self.checkValue(self.cardsList)>21:
            return True
        return False
    def checkBlackJack(self):
        if self.checkValue(self.cardsList)==21:
            return True
        return False
        
class Game:
    def __init__(self,deck,player,dealer):
        self.deck=deck
        self.player=player
        self.dealer=dealer
        self.deck.shuffle()
        for i in range(2):
            self.player.dealCard(self.deck.giveCard())
            self.dealer.dealCard(self.deck.giveCard())
        print("Your cards:",self.player.cardsList)
        print("Dealer cards:",[self.dealer.cardsList[0],"?"])
    def hitOrStandPhase(self):
        response="hit"
        while response.lower()!="stand" and not self.player.checkBust():
            response=input("Hit or Stand: ")
            if response.lower()=="hit":
                self.player.dealCard(self.deck.giveCard())
            print(self.player.cardsList)
        while self.dealer.checkValue(self.dealer.cardsList)<17:
            self.dealer.dealCard(self.deck.giveCard())
        print(self.dealer.cardsList)
    def checkWinner(self):
        if self.player.checkBust():
            print("You're Busted")
        elif self.player.checkBlackJack():
            print("BlackJack!")
        elif self.dealer.checkBust():
            print("Dealer Busted. You won")
        else:
            if self.player.checkValue(self.player.cardsList)>self.dealer.checkValue(self.dealer.cardsList):
                print("You won!")
            elif self.player.checkValue(self.player.cardsList)==self.dealer.checkValue(self.dealer.cardsList):
                print("You tied with the dealer")
            else:
                print("You lost")
print("BlackJack Game \n")
print("Get closer to 21 than the dealer")
print("But don't go over 21\n")
print("Aces can be 1 or 11")
print("Face cards are worth 10\n")
game=Game(Deck(),Player(),Player())
game.hitOrStandPhase()
game.checkWinner()