from tkinter import *
import random

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
   pool = sum(list(dice.values()))

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


   play()

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
      img_label= Label(image=self.appear)
      self.button.place(x=ww//2,y=wh//2)
      self.button.pack(pady=30)
   
   def use(self):
      #Use the dice's ability
      self.text.config(text= "You have clicked Me...")
      self.button['state'] = "disabled"
   
def play():
   #Play the next level
   board = []
   for i in range(width):
      innerlist = [Dice(j,i) for j in range(height)]
      board.append(innerlist)

   for i in board:
      for j in i:
         j.show()

def guide():
   guidew = Toplevel(win)
   guidew.title('Guide')
   guidew.geometry(f'{ww//2}x{wh//2}')
   text1 = Label(guidew, text='USER GUIDE', font='Helvetica 24 bold').pack()

def main():
   global level
   global activation
   global maxactivation
   global dice
   global sales
   global width
   global height
   global bag
   global gold
   level = 1 #What level is the user on?
   activation = 0 #The user can activate this many dice
   maxactivation = 3 #What is the max activation a user gets each turn
   dice = {'w': 4, 'r':0, 'b':0, 'g':0, 'y':0, 'p':0, 'o':0} #All dice
   sales = 3 #This is the number of items the user gets to choose from during the market
   width = 3 #This is the size of the standard playing area
   height = 3 #This is the size of the standard playing area
   gold = 0 #This is the starting gold
   bag = {
      'wand' : {'Owned': False, 'Desc': '', 'Rarity': 0, 'Dice': []},
      'white mouse' : {'Owned': False, 'Desc': '', 'Rarity': 0, 'Dice': []},
      'gray mouse' : {'Owned': False, 'Desc': '', 'Rarity': 0, 'Dice': []},
      'black mouse' : {'Owned': False, 'Desc': '', 'Rarity': 0, 'Dice': []},
      'clover' : {'Owned': False, 'Desc': '', 'Rarity': 0, 'Dice': []},
      'magic hat' : {'Owned': False, 'Desc': '', 'Rarity': 0, 'Dice': []},
   } #The bag contains all possible items, their descriptions, whether the person has them and how rare they are to pop up.

   dplaybutton.destroy()
   
   ###STUFF FOR GUIDE BUTTON THAT OPENS USER GUIDE
   #guidebutton = PhotoImage(file='resources\\guide.gif')
   dguidebutton = Button(win, text='Guide', command=lambda:guide(), borderwidth=0)
   #img_label= Label(image=guidebutton)
   dguidebutton.pack(pady=30, side = TOP, anchor = NE)
   
   play()

      
def setup():
   global win
   global ww
   global wh
   global dplaybutton
   win = Tk()
   ww = win.winfo_screenwidth()
   wh = win.winfo_screenheight()
   win.title("DiceVille")
   win.geometry(f'{ww}x{wh}')
   playbutton = PhotoImage(file='resources\\DiceVillePlay.gif')
   dplaybutton = Button(win, image=playbutton, command=lambda:main(), borderwidth=0)
   img_label= Label(image=playbutton)
   dplaybutton.pack(pady=30)
   win.mainloop()

setup()
