import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

# Map colors to flavor names for display in inventory
flavor_names = {
    'r': 'Spicy',
    'o': 'Bitter',
    'y': 'Umami',
    'g': 'Sour',
    'b': 'Salty',
    'p': 'Sweet'
}

start = True

class DiceGameUI:
    # This is the tkinter UI for the whole game, it operates whatever the user sees
    def __init__(self, master):
        global start
        self.master = master
        self.master.title("Dice Dish Game")

        # Dish definitions are all possible dishes, the ideas are all by me but avoid repetitive work that would take weeks, AI wrote the implementations
        self.dish_definitions = {
            "Pepper Pair": {
                "description": "Red and Orange dice with the same value.",
                "requirement": lambda dice, grid=None: any(
                    d1[0] == 'r' and d2[0] == 'o' and d1[1] == d2[1]
                    for d1 in dice for d2 in dice if d1 != d2
                )
            },
            "Sundrop Duo": {
                "description": "Red and Yellow dice with the same value.",
                "requirement": lambda dice, grid=None: any(
                    d1[0] == 'r' and d2[0] == 'y' and d1[1] == d2[1]
                    for d1 in dice for d2 in dice if d1 != d2
                )
            },
            "Hot Herb Harmony": {
                "description": "Red and Green dice with the same value.",
                "requirement": lambda dice, grid=None: any(
                    d1[0] == 'r' and d2[0] == 'g' and d1[1] == d2[1]
                    for d1 in dice for d2 in dice if d1 != d2
                )
            },
            "Ocean Heat": {
                "description": "Red and Blue dice with the same value.",
                "requirement": lambda dice, grid=None: any(
                    d1[0] == 'r' and d2[0] == 'b' and d1[1] == d2[1]
                    for d1 in dice for d2 in dice if d1 != d2
                )
            },
            "Berry Blaze": {
                "description": "Red and Purple dice with the same value.",
                "requirement": lambda dice, grid=None: any(
                    d1[0] == 'r' and d2[0] == 'p' and d1[1] == d2[1]
                    for d1 in dice for d2 in dice if d1 != d2
                )
            },
            "Citrus Snap": {
                "description": "Orange and Yellow dice with the same value.",
                "requirement": lambda dice, grid=None: any(
                    d1[0] == 'o' and d2[0] == 'y' and d1[1] == d2[1]
                    for d1 in dice for d2 in dice if d1 != d2
                )
            },
            "Garden Zing": {
                "description": "Orange and Green dice with the same value.",
                "requirement": lambda dice, grid=None: any(
                    d1[0] == 'o' and d2[0] == 'g' and d1[1] == d2[1]
                    for d1 in dice for d2 in dice if d1 != d2
                )
            },
            "Sunset Splash": {
                "description": "Orange and Blue dice with the same value.",
                "requirement": lambda dice, grid=None: any(
                    d1[0] == 'o' and d2[0] == 'b' and d1[1] == d2[1]
                    for d1 in dice for d2 in dice if d1 != d2
                )
            },
            "Twilight Twist": {
                "description": "Orange and Purple dice with the same value.",
                "requirement": lambda dice, grid=None: any(
                    d1[0] == 'o' and d2[0] == 'p' and d1[1] == d2[1]
                    for d1 in dice for d2 in dice if d1 != d2
                )
            },
            "Lemon Leaf": {
                "description": "Yellow and Green dice with the same value.",
                "requirement": lambda dice, grid=None: any(
                    d1[0] == 'y' and d2[0] == 'g' and d1[1] == d2[1]
                    for d1 in dice for d2 in dice if d1 != d2
                )
            },
            "Sunny Sea": {
                "description": "Yellow and Blue dice with the same value.",
                "requirement": lambda dice, grid=None: any(
                    d1[0] == 'y' and d2[0] == 'b' and d1[1] == d2[1]
                    for d1 in dice for d2 in dice if d1 != d2
                )
            },
            "Sunberry Match": {
                "description": "Yellow and Purple dice with the same value.",
                "requirement": lambda dice, grid=None: any(
                    d1[0] == 'y' and d2[0] == 'p' and d1[1] == d2[1]
                    for d1 in dice for d2 in dice if d1 != d2
                )
            },
            "Herbal Ocean": {
                "description": "Green and Blue dice with the same value.",
                "requirement": lambda dice, grid=None: any(
                    d1[0] == 'g' and d2[0] == 'b' and d1[1] == d2[1]
                    for d1 in dice for d2 in dice if d1 != d2
                )
            },
            "Forest Berry": {
                "description": "Green and Purple dice with the same value.",
                "requirement": lambda dice, grid=None: any(
                    d1[0] == 'g' and d2[0] == 'p' and d1[1] == d2[1]
                    for d1 in dice for d2 in dice if d1 != d2
                )
            },
            "Deep Crush": {
                "description": "Blue and Purple dice with the same value.",
                "requirement": lambda dice, grid=None: any(
                    d1[0] == 'b' and d2[0] == 'p' and d1[1] == d2[1]
                    for d1 in dice for d2 in dice if d1 != d2
                )
            },
            "Hearty Haul": {
                "description": "Sum of dice is 20 or more.",
                "requirement": lambda dice, grid=None: sum(d[1] for d in dice) >= 20
            },
            "Light Snack": {
                "description": "Sum of dice is less than 12.",
                "requirement": lambda dice, grid=None: sum(d[1] for d in dice) < 12
            },
            "Perfect Balance": {
                "description": "Average dice value between 3 and 4.",
                "requirement": lambda dice, grid=None: 3 <= (sum(d[1] for d in dice) / len(dice)) <= 4
            },
            "Even Stew": {
                "description": "All dice values are even.",
                "requirement": lambda dice, grid=None: all(d[1] % 2 == 0 for d in dice)
            },
            "Odd Omelette": {
                "description": "All dice values are odd.",
                "requirement": lambda dice, grid=None: all(d[1] % 2 == 1 for d in dice)
            },}
        
        self.dice_colors = ['r', 'o', 'y', 'g', 'b', 'p']
        # Start with 2 of each dice in inventory
        self.dice_inventory = {color: 2 for color in self.dice_colors}
        self.dice_images = {}
        self.load_dice_images()

        self.reserved_dice = []
        self.dishes = random.sample(list(self.dish_definitions.keys()), 4)
        self.current_phase = 0  # 0: Dish Selection, 1: Dice Reservation
        self.health = 3
        self.wins = 0
        self.removal_count = 3
        self.draw_count = 3

        if start:
            self.available = random.sample(self.dishes, 3)
            start = False
        
        self.setup_ui()
        self.populate_dice_grid()
        self.display_dish_cards()
        self.update_phase_title()
        self.update_health_display()

    def load_dice_images(self):
        #Loads in dice images from resources folder for the visual look on the grid
        for color in self.dice_colors:
            for value in range(1, 7):
                path = f"resources/{color}{value}.gif"
                try:
                    img = Image.open(path)
                    self.dice_images[f"{color}{value}"] = ImageTk.PhotoImage(img)
                except:
                    self.dice_images[f"{color}{value}"] = None

    def setup_ui(self):
        #This method sets up everything on the UI from labels to buttons
        # Title & phase label
        self.title_label = tk.Label(self.master, text="", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=5)

        # Left frame for health and inventory button
        self.left_frame = tk.Frame(self.master)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5)

        self.health_label = tk.Label(self.left_frame, text=f"Health: {self.health}", font=("Arial", 14))
        self.health_label.pack(pady=10)

        self.wins_label = tk.Label(self.left_frame, text=f"Wins: {self.wins}", font=("Arial", 14))
        self.wins_label.pack(pady=10)

        self.inv_button = tk.Button(self.left_frame, text="Inventory (Possible Dice)", command=self.show_inventory)
        self.inv_button.pack(pady=20)

        self.remove_label = tk.Label(self.left_frame, text=f"Removals Left: {self.removal_count}", font=("Arial", 12))
        self.remove_label.pack(pady=5)

        self.draw_label = tk.Label(self.left_frame, text=f"Draws Left: {self.draw_count}", font=("Arial", 12))
        self.draw_label.pack(pady=5)

        # Dice grid
        self.grid_frame = tk.Frame(self.master)
        self.grid_frame.pack()

        # Dish cards
        self.card_frame = tk.Frame(self.master)
        self.card_frame.pack(pady=10)

        # Control buttons
        self.control_frame = tk.Frame(self.master)
        self.control_frame.pack(pady=10)

        self.next_button = tk.Button(self.control_frame, text="Next Phase", command=self.advance_phase)
        self.next_button.pack(side=tk.LEFT, padx=5)

        self.draw_button = tk.Button(self.control_frame, text="Draw Dish", command=self.draw_dish)
        self.draw_button.pack(side=tk.LEFT, padx=5)

    def update_health_display(self):
        #Refresh health and wins values
        self.health_label.config(text=f"Health: {self.health}")
        self.wins_label.config(text=f"Wins: {self.wins}")

    def update_phase_title(self):
        #Refresh what phase the user is in
        phases = ["Dish Selection", "Ingredient Shopping (Dice Reservation)"]
        self.title_label.config(text=f"Phase {self.current_phase + 1}: {phases[self.current_phase]}")

    def populate_dice_grid(self):
        # Clear previous grid
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        # Show dice buttons based on inventory (partially filled grid)
        self.dice_grid = []
        total_slots = 16
        # Build list of dice available to draw from inventory
        available_dice = []
        for color, count in self.dice_inventory.items():
            for _ in range(count):
                value = random.randint(1, 6)
                available_dice.append((color, value))
        random.shuffle(available_dice)
        dice_to_show = available_dice[:total_slots]

        # Fill rest with empty slots (None) if inventory < 16
        while len(dice_to_show) < total_slots:
            dice_to_show.append(None)

        for i in range(4):
            row = []
            for j in range(4):
                idx = i*4 + j
                dice = dice_to_show[idx]
                if dice:
                    color, value = dice
                    img_key = f"{color}{value}"
                    img = self.dice_images.get(img_key)
                    btn = tk.Button(self.grid_frame, image=img)
                    btn.grid(row=i, column=j, padx=3, pady=3)
                    btn.config(command=lambda d=dice, b=btn: self.reserve_dice(d, b))
                else:
                    btn = tk.Label(self.grid_frame, text="", width=4, height=2, relief=tk.FLAT)
                    btn.grid(row=i, column=j, padx=3, pady=3)
                row.append((dice, btn))
            self.dice_grid.append(row)

    def reserve_dice(self, dice, btn):
        #This method understands which dice button is clicked and turns it green
        if self.current_phase != 1:
            return
        if dice in self.reserved_dice:
            # Already reserved, unreserve
            self.reserved_dice.remove(dice)
            btn.config(relief=tk.RAISED, bg='SystemButtonFace')
        elif len(self.reserved_dice) < 5:
            self.reserved_dice.append(dice)
            btn.config(relief=tk.SUNKEN, bg='lightgreen')

    def display_dish_cards(self):
        #Lists the dish cards out (the for second for loop is written partly with the assistance of AI)
        for widget in self.card_frame.winfo_children():
            widget.destroy()
        self.dish_cards = []
        for dish in self.available:
            frame = tk.Frame(self.card_frame, bd=2, relief=tk.RIDGE, width=150, height=100)
            frame.pack_propagate(0)
            frame.pack(side=tk.LEFT, padx=5)
            tk.Label(frame, text=dish, font=("Arial", 10, "bold")).pack()
            tk.Label(frame, text=self.dish_definitions[dish]["description"], wraplength=140).pack()
            if self.current_phase == 0 and self.removal_count > 0:
                btn = tk.Button(frame, text="Remove Dish", command=lambda d=dish, f=frame: self.remove_dish(d, f))
                btn.pack(pady=(0,5))
            self.dish_cards.append(frame)

    def remove_dish(self, dish, frame):
        # Removes a dish from the kitchen
        if self.current_phase != 0 or self.removal_count <= 0:
            return
        if dish in self.available:
            self.available.remove(dish)
            self.removal_count -= 1
            self.remove_label.config(text=f"Removals Left: {self.removal_count}")
            self.display_dish_cards()

    def draw_dish(self):
        #Draws a new dish into the kitchen
        if self.current_phase != 0 or self.draw_count <= 0:
            return
        if self.available:
            new_dish = random.choice(self.dishes)
            self.available.append(new_dish)
            self.draw_count -= 1
            self.draw_label.config(text=f"Draws Left: {self.draw_count}")
            self.display_dish_cards()

    def show_inventory(self):
        # Show a simple popup with dice flavors and counts in inventory and dishes
        inv_str = "Dice inventory (possible dice to draw):\n"
        for color in self.dice_colors:
            inv_str += f"{flavor_names[color]} ({color}): {self.dice_inventory.get(color,0)}\n"
        inv_str += "\nDish inventory (possible dish to draw):\n"
        for adish in self.dishes:
            inv_str += f"{adish}: {self.dish_definitions[adish]['description']}\n"
        messagebox.showinfo("Inventory", inv_str)

    def advance_phase(self):
        #As the 'next' button is clicked, the phase has to go to the next one to advance the flow of the game
        if self.current_phase == 0:
            if not self.available or not self.dishes:
                messagebox.showwarning("No Dishes", "You must have at least one dish!")
                return
            self.current_phase = 1
            self.removal_count = 3
            self.draw_count = 3
            self.reserved_dice.clear()
            self.display_dish_cards()
            self.update_phase_title()
        else:
            if len(self.reserved_dice) != 5:
                messagebox.showwarning("Have 5 flavors", "You must have exactly 5 flavor dice!")
                return
            successful_dishes = []
            for dish in self.available:
                requirement = self.dish_definitions[dish]["requirement"]
                if requirement(self.reserved_dice):
                    successful_dishes.append(dish)

            if successful_dishes:
                self.wins += len(successful_dishes)
                messagebox.showinfo("Success!", f"You successfully completed {len(successful_dishes)} dish(es):\n" +
                                    "\n".join(successful_dishes))
            else:
                self.health -= 1
                messagebox.showerror("Failure", "No dishes were completed. You lose 1 health.")
            self.show_reward_screen()
            self.current_phase = 0
            self.reserved_dice.clear()
            self.update_health_display()
            self.update_phase_title()
            self.populate_dice_grid()
            self.display_dish_cards()

            # Check for win or loss
            if self.wins >= 30:
                messagebox.showinfo("Victory!", "Congratulations! You completed 6 dishes and won the game.")
                self.master.destroy()
                exit()
            elif self.health <= 0:
                messagebox.showinfo("Game Over", "You ran out of health. Game over.")
                self.master.destroy()
                exit()
            
    def show_reward_screen(self):
        # Clear main window
        for widget in self.master.winfo_children():
            widget.destroy()

        self.reward_frame = tk.Frame(self.master)
        self.reward_frame.pack(padx=10, pady=10)

        tk.Label(self.reward_frame, text="Reward Phase: Select 2 Dice and 1 Dish", font=("Arial", 14, "bold")).pack(pady=10)

        # Dice selection
        self.reward_dice_choices = []
        self.selected_dice = []
        for i in range(2):
            frame = tk.LabelFrame(self.reward_frame, text=f"Select Dice {i+1}")
            frame.pack(side=tk.LEFT, padx=10)

            choices = random.sample(self.dice_colors, 3)
            self.reward_dice_choices.append(choices)
            var = tk.StringVar()
            var.set(None)
            for color in choices:
                btn = tk.Radiobutton(frame, text=flavor_names[color], variable=var, value=color)
                btn.pack(anchor=tk.W)
            setattr(self, f"dice_choice_var_{i}", var)

        # Dish selection
        frame_dish = tk.LabelFrame(self.reward_frame, text="Select a Dish to add")
        frame_dish.pack(side=tk.LEFT, padx=10)

        self.reward_dish_choices = random.sample(list(self.dish_definitions.keys()), 4)
        self.dish_choice_var = tk.StringVar()
        self.dish_choice_var.set(None)
        for dish in self.reward_dish_choices:
            btn = tk.Radiobutton(frame_dish, text=dish+' = '+self.dish_definitions[dish]['description'], variable=self.dish_choice_var, value=dish)
            btn.pack(anchor=tk.W)

        # Confirm button
        self.confirm_button = tk.Button(self.master, text="Confirm Selections", command=self.apply_rewards)
        self.confirm_button.pack(pady=10)

    def apply_rewards(self):
        #Gives you the rewards you selected during the Rewarding Phase
        # Check dice selections
        dice1 = getattr(self, "dice_choice_var_0").get()
        dice2 = getattr(self, "dice_choice_var_1").get()
        dish = self.dish_choice_var.get()

        if not dice1 or not dice2 or not dish:
            messagebox.showwarning("Incomplete Selection", "Please select 2 dice and 1 dish.")
            return

        # Add dice to inventory
        self.dice_inventory[dice1] = self.dice_inventory.get(dice1, 0) + 1
        self.dice_inventory[dice2] = self.dice_inventory.get(dice2, 0) + 1

        # Add dish to deck if not already present
        self.dishes.append(dish)

        # Remove reward screen widgets
        self.reward_frame.destroy()
        self.confirm_button.destroy()

        # Reset reserved dice
        self.reserved_dice.clear()

        # Reset to phase 0 and refresh UI
        for widget in self.master.winfo_children():
            widget.destroy()

        self.setup_ui()
        self.populate_dice_grid()
        self.display_dish_cards()
        self.update_phase_title()
        self.update_health_display()
        self.available = random.sample(self.dishes, 3)

if __name__ == "__main__":
    root = tk.Tk()
    game = DiceGameUI(root)
    root.mainloop()
