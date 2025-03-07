from tkinter import *
import random

level = 1 #What level is the user on?
activation = 0 #The user can activate this many dice
maxactivation = 3 #What is the max activation a user gets each turn
dice = {'blue':4}
sales = 3 #This is the number of items the user gets to choose from during the market
width = 3 #This is the size of the standard playing area
height = 3 #This is the size of the standard playing area
bag = {
   'wand' : {'Owned': False, 'Desc': '', 'Rarity': 0},
   'white mouse' : {'Owned': False, 'Desc': '', 'Rarity': 0},
   'gray mouse' : {'Owned': False, 'Desc': '', 'Rarity': 0},
   'black mouse' : {'Owned': False, 'Desc': '', 'Rarity': 0},
   'clover' : {'Owned': False, 'Desc': '', 'Rarity': 0},
   'magic hat' : {'Owned': False, 'Desc': '', 'Rarity': 0},
   'backpack' : {'Owned': False, 'Desc': '', 'Rarity': 0},
   'salesman' : {'Owned': False, 'Desc': '', 'Rarity': 0}
} #The bag contains all possible items, their descriptions, whether the person has them and how rare they are to pop up.
pool = ['blue'] #Pool is all the dice the user has.

def prob(pv):
   #Uses a percentage probability from 0-100 to simulate whether it happens using random.random
   return random.random() <= pv/100

def item(refer):
   #This function runs the function of the item when they are bought
   bag[refer] = True
   ## HERE EACH ITEM DOES WHAT IT DOES... THIS IS TO BE ADDED IN A LATER BUILD

def inventory():
   #This displays a list of the items the user possesses
   ## THIS WILL BE BUTTON OPERATED, WHEN ITS CALLED, IT SHOULD SHOW BAG
   print(bag) ##TESTER

def market():
   #When market phase happens at the end of every level, this is called
   stock = []
   stockref = []

   for i in range(sales):
      if prob(90):
         stock.append(pool[random.randint(0,len(pool)-1)])
         stockref.append(0)
      else:
         tempitem = list(filter(lambda x: not bag[x], bag.keys()))
         stock.append(tempitem[random.randint(0,len(tempitem)-1)])
         stockref.append(1)

   select = int(input(stock)) ##TESTER
   if stockref[select] == 1:
      item(stock[select])
   elif stockref[select] == 0:
      dice[stock[select]] += 1

class Dice():
   #Class that creates each dice
   def __init__(self,bx,by):
      self.bx = bx
      self.by = by
      self.text= Label(win, text= "")
      self.text.pack(pady=30)
      self.appear = PhotoImage(file='resources\\b1.gif')
   
   def show(self):
      #Show the dice on the screen in the grid
      self.button = Button(win, image=self.appear, command=lambda:self.use(), borderwidth=0)
      self.button.pack()
      img_label= Label(image=self.appear)
      self.button.pack(pady=30)
   
   def use(self):
      #Use the dice's ability
      self.text.config(text= "You have clicked Me...")
      self.button['state'] = "disabled"
   
def play():
   #Play the next level
   outerlist = []
   for i in range(width):
      innerlist = [Dice(j,i) for j in range(height)]
      outerlist.append(innerlist)
   print(outerlist)
   button = myDice.show()

def main():
   global win
   win = Tk()
   win.title("DiceVille")
   win.geometry("700x300")
   play()
   win.mainloop()


main()
