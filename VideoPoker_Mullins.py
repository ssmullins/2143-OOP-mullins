import os
import random
import time


class Card(object):
    def __init__(self, suit ='', rank = 0):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "(suit: %s,rank: %s)" % (self.suit, self.rank)
    def __cmp__(self,other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return int(t1[1]) < int(t2[1])
    def __it__(self,other):
        return self.__cmp__(other)
class Deck(object):
    def __init__(self):
        self.cards = []

        for suit in range(1,5):
            for rank in range(2,15):
                self.cards.append(Card(suit,rank))
                
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return " ".join(res)
    
    def pop_card(self):
        return self.cards.pop(0)
    
    def add_card(self,card):
        self.cards.append(card)
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def sort(self):
        self.cards = sorted(self.cards)
class Hand(Deck):
    def __init__(self):
        self.cards = []
        self.suitCount = {}
        self.rankCount = {}

    def addCard(self,card):
        if not card.suit in self.suitCount:
            self.suitCount[card.suit] = 1
        else:
            self.suitCount[card.suit] += 1
            
        if not card.rank in self.rankCount:
            self.rankCount[card.rank] = 1
        else:
            self.rankCount[card.rank] += 1   
        self.cards.append(card)
        
    def suitDict(self):
        return self.suitCount
    def rankDict(self):
        return self.rankCount

    def getCards(self):
        return self.cards
    
    def sortHand(self):
        self.cards.sort()
        
    
 
    def getPosition(self,card):
        return self.cards.index(card)
    
    def trashHand(self):
        self.cards = []
        self.rankCount = {}
        self.suitCount = {}

class VideoPoker(object):
    def __init__(self):
        self.deck = Deck()
        self.hand = Hand()
    def deal(self, num = 5):
        self.deck.shuffle()

        for i in range(0,num):
            self.hand.addCard(self.deck.pop_card())
        print(self.hand)
        ##self.hand.replaceCard()
        return self.hand
    def getcard(self):
        self.deck.shuffle()
        return self.deck.pop_card()
        
    def replaceCard(self,Discard):
        self.cards[x] = Deck.pop_card(self)
            
    def checkHand(self):
##        self.hand.sortHand()
        self.points = 0
        RD = self.hand.rankDict()
        SD = self.hand.rankDict()
        hand = self.hand.getCards()
        
        if len(RD) == 4:
            self.points = 1
            print("1 pair")
        elif len(RD) == 3:
            if 3 in RD.values():
                self.points = 3
                print("3 of a kind")
            else:
                self.points = 2
                print("2 pairs")
        elif len(RD) == 2:
            if 2 in RD.values():
                self.points = 8
                print("Full House")
            elif  7 in RD:
                if RD[7] == 4:
                    self.points = 50
                    print("4 sevens")
            elif  8 in RD:
                if RD[8] == 4:
                    self.points = 80
                    print("4 eights")
                elif 14 in RD:
                    if RD[14] == 4:
                        self.points = 80
                        print("4 aces")
            else:
                self.points = 25
                print("4 of a kind")
        elif len(SD) == 1:
            if len(RD) == 5 and (hand[4].rank - hand[0].rank) == 4:
                self.points = 50 
                print("straight flush")
        elif len(SD) == 1:
            self.points = 5
            print("flush")
        elif len(RD) == 5 and (hand[4].rank - hand[0].rank) == 4:
            self.points = 4
            print("straight")
        elif len(RD) == 5:
            if hand[4].rank == 14:
                if hand[4] - hand[0] == 4:
                    self.points = 800
                    print("Royal Flush")
        else:
            print("Yout got nothing dude")

class Game_driver(VideoPoker):
    def __init__(self):
        super().__init__()
    def menu(self):
        print("1: New Game")
        print("2: Play Again")
        print("3: Quit")

        choice = input()
        choice = int(choice)

        if choice == 1:
            V = VideoPoker()
            V.deal()
            
            print(" ")
            print("Choose cards you wish to discard, type the number of the cards in seperated by commas")
            
            Discard = input()
            Discard = int(Discard)
            VideoPoker.replaceCard(Discard)
            print(self.hand)
            
        elif choice == 2:
            V = VideoPoker()
            V.deal()
            
            
            

        
        
        

       
g = Game_driver()
g.menu()
