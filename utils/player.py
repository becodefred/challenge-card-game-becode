#Card game project at BeCode: 09/11/2020
#File player.py
#Author: Frédéric Fourré


class Player:
    def __init__(self,name,cards):
        self.name=name  
        from card import Card #optional
        self.cards=cards #a list of Card objects  
        self.turn_count=0
        self.number_of_cards=len(self.cards) 
        self.history=[] #all the cards played by the player 
    
    def play(self):
        import random
        self.i=random.randint(1,self.number_of_cards)-1
        self.history.append(self.cards[self.i])
        self.number_of_cards-=1
        print(self.name + " played : " + str(self.cards[self.i].value) + self.cards[self.i].colorsymb)
        self.cards.pop(self.i)
        self.turn_count+=1
        for j in range(len(self.cards)):  
            print(str(self.cards[j].value)+self.cards[j].colorsymb) #will display the cards of the player after he/she played
        
class Deck:
    def __init__(self):
        from card import Card 
        self.cards=[]
        for val in ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]:
            for symb in ["h","s","c","d"]:
                self.cards.append(Card(val,symb)) #all the cards in list self.cards, call class Card               
                
    def shuffle(self): #can be called any number of times to shuffle
        import random    
        self.number_of_cards=len(self.cards) 
        random.shuffle(self.cards)      
        for i in range(self.number_of_cards):  
            print(str(self.cards[i].value)+self.cards[i].colorsymb)

    def distribute(self,playerlist):
        self.playerlist=playerlist
        nb=52//len(self.playerlist)
        i=0
        for item in self.playerlist:
            print(item)
            from player import Player
            cards=self.cards[0+nb*i:nb*(i+1)]          
            self.playerlist[i]=Player(item,cards) 
            for j in range(nb*i,nb*(i+1),1):
                print(str(self.cards[j].value)+self.cards[j].colorsymb) #will display the initial set of cards for each player   
            i+=1
            
            

#def fill_deck(self): #not mandatory for now


#For class Deck 
#from player import Deck
#deck=Deck()
#deck.shuffle() #to shuffle (any number of times)
#deck.distribute(["me","you","he","she","another"]) #to name the players
#print(deck.number_of_cards)

#print(deck.playerlist) #to display the players as objects
#print(deck.playerlist[0].name) #to display the first player in the list
#print(str(deck.playerlist[4].cards[0].value)+deck.playerlist[4].cards[0].colorsymb) #to display the first card of 
#player number 4+1
#deck.playerlist[3].play() #to make player 3+1 play

#For class Player
#me=Player("me",cards) #to name a new player "me"
#me.play() #to make player "me" play a card
#print(me.cards[0].value, me.cards[0].colorsymb) #to see a card of player "me" in list self.cards





       
        
