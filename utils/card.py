#Card game project at BeCode: 09/11/2020
#File card.py
#Author: Frédéric Fourré


class Symbol:
    def __init__(self,color,icon):
        self.color=color
        self.icon=icon
        
class Card(Symbol):
    def __init__(self,value,colorsymb):
        red="\033[31m"
        black="\033[30m"
        reset="\033[m"
        self.value=value
        if colorsymb=="h":
            self.colorsymb=red+"\u2665"+reset
        elif colorsymb=="d":
            self.colorsymb=red+"\u2666"+reset
        elif colorsymb=="s":
            self.colorsymb=black+"\u2660"+reset   
        else:
            self.colorsymb=black+"\u2663"+reset 
        print(str(self.value)+self.colorsymb)  
        
   


 

        
 
 

        
        
        
        
        
        
        
        

