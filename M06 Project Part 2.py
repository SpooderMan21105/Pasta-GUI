'''
M06 Project Part 2
'''
'''
Name: M06 Project Part 2
Author : Evan
Date: 04/26/2025
Version : 6
'''

import tkinter as tk
from tkinter import messagebox

# Prices
prices = {
    'Spaghetti': 4,
    'Fettuccine': 3,
    'Angel Pasta': 5,
    'Tomato Sauce': 4,
    'Alfredo': 4,
    'Shrimp': 5,
    'Steak': 7,
    'No Meat': 0
}

#main code
class PastaOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pasta Order")
        self.root.geometry("400x400")

        # Variables
        self.pasta_var = tk.StringVar()
        self.sauce_var = tk.StringVar()
        self.meat_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Frames for sections
        pasta_frame = tk.LabelFrame(self.root, text="Choose your Pasta", padx=10, pady=10)
        pasta_frame.pack(fill="both", expand="yes", padx=10, pady=5)

        sauce_frame = tk.LabelFrame(self.root, text="Choose your Sauce", padx=10, pady=10)
        sauce_frame.pack(fill="both", expand="yes", padx=10, pady=5)

        meat_frame = tk.LabelFrame(self.root, text="Choose your Meat", padx=10, pady=10)
        meat_frame.pack(fill="both", expand="yes", padx=10, pady=5)

        # Pasta options
        for pasta in ['Spaghetti', 'Fettuccine', 'Angel Pasta']:
            tk.Radiobutton(pasta_frame, text=f"{pasta} (${prices[pasta]})", variable=self.pasta_var, value=pasta).pack(anchor='w')

        # Sauce options
        for sauce in ['Tomato Sauce', 'Alfredo']:
            tk.Radiobutton(sauce_frame, text=f"{sauce} (${prices[sauce]})", variable=self.sauce_var, value=sauce).pack(anchor='w')

        # Meat options
        for meat in ['Shrimp', 'Steak', 'No Meat']:
            tk.Radiobutton(meat_frame, text=f"{meat} (${prices[meat]})", variable=self.meat_var, value=meat).pack(anchor='w')

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Submit Order", command=self.submit_order).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="New Order", command=self.new_order).grid(row=0, column=1, padx=5)

        # Order label
        self.order_label = tk.Label(self.root, text="")
        self.order_label.pack(pady=10)

    def submit_order(self):
        pasta = self.pasta_var.get()
        sauce = self.sauce_var.get()
        meat = self.meat_var.get()

        if not (pasta and sauce and meat):
            messagebox.showerror("Error", "Please make all selections!")
            return

        order_text = f"Order: {pasta} with {sauce} and {meat}"
        self.order_label.config(text=order_text)

        self.show_price_window(pasta, sauce, meat)

    def new_order(self):
        self.pasta_var.set("")
        self.sauce_var.set("")
        self.meat_var.set("")
        self.order_label.config(text="")

    def show_price_window(self, pasta, sauce, meat):
        price_window = tk.Toplevel(self.root)
        price_window.title("Order Pricing")
        price_window.geometry("300x300")

        pasta_price = prices[pasta]
        sauce_price = prices[sauce]
        meat_price = prices[meat]
        total = pasta_price + sauce_price + meat_price

        tk.Label(price_window, text=f"{pasta}: ${pasta_price}").pack(pady=5)
        tk.Label(price_window, text=f"{sauce}: ${sauce_price}").pack(pady=5)
        tk.Label(price_window, text=f"{meat}: ${meat_price}").pack(pady=5)

        tk.Label(price_window, text=f"Total: ${total}", font=('Arial', 14, 'bold')).pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = PastaOrderApp(root)
    root.mainloop()
