from tkinter import *
import random

level = 1
dice = {'blue':4}
sales = 3
bag = {
   'wand' : False,
   'white mouse' : False,
   'gray mouse' : False,
   'black mouse' : False,
   'clover' : False,
   'magic hat' : False,
   'backpack' : False,
   'salesman' : False
}
pool = ['blue']

def prob(pv):
   return random.random() <= pv/100

def item(refer):
   bag[refer] = True
   ## HERE EACH ITEM DOES WHAT IT DOES... THIS IS TO BE ADDED IN A LATER BUILD

def inventory():
   ## THIS WILL BE BUTTON OPERATED, WHEN ITS CALLED, IT SHOULD SHOW BAG
   print(bag) ##TESTER

def market():
   stock = []
   stockref = []

   for i in range(sales):
      if prob(90):
         stock.append(pool[random.randint(0,len(pool))])
         stockref.append(0)
      else:
         tempitem = filter(lambda x: not bag[x], bag.keys())
         stock.append(tempitem[random.randint(0,len(tempitem))])
         stockref.append(1)

   select = input(stock) ##TESTER
   if stockref[select] == 1:
      item(stock[select])
   elif stockref[select] == 0:
      dice[stock[select]] += 1

def play():
   def my_command():
      text.config(text= "You have clicked Me...")

   click_btn= PhotoImage(file='resources\\b1.gif')

   img_label= Label(image=click_btn)

   button= Button(win, image=click_btn,command= my_command,
   borderwidth=0)
   button.pack(pady=30)

   text= Label(win, text= "")
   text.pack(pady=30)

def main():
   win = Tk()
   win.title("Dice Warriors")
   win.geometry("700x300")
   win.mainloop()
   
   Icon1 = PhotoImage(file='resources\\b1.gif')


main()