import tkinter as tk
from tkinter import messagebox

# Prices dictionary: Holds the prices of pasta, sauce, meat, and side options.
prices = {
    "Spaghetti": 4,
    "Fettuccine": 3,
    "Angel Pasta": 5,
    "Tomato Sauce": 4,
    "Alfredo": 4,
    "Shrimp": 5,
    "Steak": 7,
    "No Meat": 0,
    "Breadsticks": 5,
    "Cookie": 3,
    "No Side": 0
}

# Global variable to track order number
order_number = 1

# Function to handle the submission of the order
def submit_order():
    """
    Verifies if pasta, sauce, and meat selections are made. If incomplete,
    prompts the user to make selections. Otherwise, proceeds to select a side dish.
    """
    pasta = pasta_var.get()  # Selected pasta
    sauce = sauce_var.get()  # Selected sauce
    meat = meat_var.get()    # Selected meat

    if not pasta or not sauce or not meat:
        messagebox.showerror("Incomplete Selection", "Please select pasta, sauce, and meat.")
        return

    open_side_window()  # Opens the window to select a side dish

# Final submission function
def final_submit():
    """
    Finalizes the order by displaying the selection details and price breakdown.
    Also increments the order number for the next order.
    """
    global order_number

    pasta = pasta_var.get()  # Selected pasta
    sauce = sauce_var.get()  # Selected sauce
    meat = meat_var.get()    # Selected meat
    side = side_var.get()    # Selected side dish

    # Set order text and show price breakdown
    order_text.set(f"{pasta} with {sauce}, {meat}, Side: {side}")
    show_price_breakdown(pasta, sauce, meat, side)

    # Increment order number for the next order
    order_number += 1

# Function to reset selections and start a new order
def new_order():
    """
    Resets all the user selections (pasta, sauce, meat, side) to empty.
    Clears the order summary.
    """
    pasta_var.set("")  # Reset pasta selection
    sauce_var.set("")  # Reset sauce selection
    meat_var.set("")   # Reset meat selection
    side_var.set("")   # Reset side selection
    order_text.set("") # Clear the order summary text

# Display the price breakdown of the order
def show_price_breakdown(pasta, sauce, meat, side):
    """
    Opens a new window to display the detailed price breakdown for the selected items.
    Displays the pasta, sauce, meat, and side selections along with the total price.
    """
    global order_number
    top = tk.Toplevel(root)
    top.title("Order Pricing")
    top.geometry("300x300")
    top.configure(bg="#f0f0f0")

    # Calculate the total price of the order
    total = prices[pasta] + prices[sauce] + prices[meat] + prices[side]

    # Display price breakdown
    tk.Label(top, text="Price Breakdown", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#333").pack(pady=10, anchor="center")
    tk.Label(top, text=f"{pasta}: ${prices[pasta]}", bg="#f0f0f0", fg="#333").pack(anchor="center")
    tk.Label(top, text=f"{sauce}: ${prices[sauce]}", bg="#f0f0f0", fg="#333").pack(anchor="center")
    tk.Label(top, text=f"{meat}: ${prices[meat]}", bg="#f0f0f0", fg="#333").pack(anchor="center")
    tk.Label(top, text=f"{side}: ${prices[side]}", bg="#f0f0f0", fg="#333").pack(anchor="center")
    tk.Label(top, text=f"\nTotal: ${total}", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#e74c3c").pack(pady=5, anchor="center")

    # Display order number at the bottom
    tk.Label(top, text=f"Order Number: {order_number}", font=("Arial", 10, "italic"), bg="#f0f0f0", fg="#333").pack(pady=10, anchor="center")

    # Buttons for navigating
    tk.Button(top, text="Go Back", command=lambda: [top.destroy(), new_order()], bg="#3498db", fg="white").pack(pady=5)
    tk.Button(top, text="Close", command=top.destroy, bg="#e74c3c", fg="white").pack(pady=5)

# Function to open the side selection window
def open_side_window():
    """
    Opens a new window for the user to choose a side dish (Breadsticks, Cookie, No Side).
    """
    side_window = tk.Toplevel(root)
    side_window.title("Choose a Side")
    side_window.geometry("300x200")
    side_window.configure(bg="#f0f0f0")

    tk.Label(side_window, text="Select a Side ($):", font=("Arial", 12), bg="#f0f0f0", fg="#333").pack(pady=5, anchor="center")

    # Displaying available side options (Breadsticks, Cookie, No Side)
    for side in ["Breadsticks", "Cookie", "No Side"]:
        tk.Radiobutton(side_window, text=f"{side} - ${prices[side]}", variable=side_var, value=side, bg="#f0f0f0", fg="#333").pack(anchor="w")

    tk.Button(side_window, text="Confirm", command=lambda: [side_window.destroy(), final_submit()], bg="#3498db", fg="white").pack(pady=10)

# Button click handlers
def on_submit_click():
    submit_order()

def on_new_order_click():
    new_order()

def on_exit_click():
    exit_cleanup()

def exit_cleanup():
    """
    Confirms with the user if they want to exit the application.
    """
    confirm_exit()

def confirm_exit():
    """
    Displays a confirmation dialog to exit the application.
    """
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

# Setting up the GUI window
root = tk.Tk()
root.title("Pasta Order")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

# Declaring variables to hold user selections
pasta_var = tk.StringVar()  # Holds selected pasta
sauce_var = tk.StringVar()  # Holds selected sauce
meat_var = tk.StringVar()   # Holds selected meat
side_var = tk.StringVar()   # Holds selected side dish
order_text = tk.StringVar() # Holds the order summary text

# Setting up scrollable canvas and frame for the main window
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Updating scrollable region when new content is added
def update_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", update_scroll_region)

# Adding header
header_frame = tk.Frame(scrollable_frame, bg="#f0f0f0")
header_frame.pack(pady=5, anchor="center")
tk.Label(header_frame, text="Build Your Pasta", font=("Arial", 16), bg="#f0f0f0", fg="#333").pack()

# Adding pasta, sauce, and meat options
def add_radiobuttons(frame, options, var):
    """
    Helper function to add radio buttons dynamically for pasta, sauce, and meat.
    """
    for option in options:
        tk.Radiobutton(frame, text=f"{option} - ${prices[option]}", variable=var, value=option, bg="#f0f0f0", fg="#333").pack(anchor="w")

# Pasta options
pasta_frame = tk.LabelFrame(scrollable_frame, text="Choose Pasta ($)", padx=10, pady=5, bg="#f0f0f0", fg="#333")
pasta_frame.pack(pady=5, fill="x", padx=10, anchor="center")
add_radiobuttons(pasta_frame, ["Spaghetti", "Fettuccine", "Angel Pasta"], pasta_var)

# Sauce options
sauce_frame = tk.LabelFrame(scrollable_frame, text="Choose Sauce ($)", padx=10, pady=5, bg="#f0f0f0", fg="#333")
sauce_frame.pack(pady=5, fill="x", padx=10, anchor="center")
add_radiobuttons(sauce_frame, ["Tomato Sauce", "Alfredo"], sauce_var)

# Meat options
meat_frame = tk.LabelFrame(scrollable_frame, text="Choose Meat ($)", padx=10, pady=5, bg="#f0f0f0", fg="#333")
meat_frame.pack(pady=5, fill="x", padx=10, anchor="center")
add_radiobuttons(meat_frame, ["Shrimp", "Steak", "No Meat"], meat_var)

# Order summary label
order_summary_frame = tk.Frame(scrollable_frame, bg="#f0f0f0")
order_summary_frame.pack(pady=10, anchor="center")
tk.Label(order_summary_frame, textvariable=order_text, fg="blue", font=("Arial", 12), bg="#f0f0f0").pack()

# Button frame for submit, new order, and exit
btn_frame = tk.Frame(scrollable_frame, bg="#f0f0f0")
btn_frame.pack(pady=10, anchor="center")

# Buttons for different actions
tk.Button(btn_frame, text="Submit Order", command=on_submit_click, bg="#3498db", fg="white").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="New Order", command=on_new_order_click, bg="#2ecc71", fg="white").grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Exit", command=on_exit_click, bg="#e74c3c", fg="white").grid(row=0, column=2, padx=5)

# Main event loop to run the GUI
root.mainloop()
