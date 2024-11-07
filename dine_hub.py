import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("Restaurant Management System")
root.geometry('1920x3520')
# Initializing variables
order = []
total_price = 0

# Menu
menu = {
    'STARTERS': [
        {'name': 'SANDWICH', 'price': 100},
        {'name': 'SAMOSA', 'price': 50},
        {'name': 'KACHORI', 'price': 50},
        {'name': 'SOUP', 'price': 80},
        
    ],
    'MAINS': [
        {'name': 'PANEER BUTTER MASALA', 'price': 210},
        {'name': 'DAL FRY', 'price': 170},
        {'name': 'MALAI KOFTA', 'price': 200},
        {'name': 'MIX VEG', 'price': 150}
       
        
    ],
    'DESSERT': [
        {'name': 'GULAB JAMUN', 'price': 100},
        {'name': 'RASMALAI', 'price': 150},
        {'name': 'ICECREAM', 'price': 80},
        
    
    ],
    'BREADS': [
        {'name': 'TAWA ROTI', 'price': 20},
        {'name': 'TANDOORI ROTI ', 'price': 25},
        {'name': 'NAAN', 'price': 50},
        
      
    ]
   
}

# Menu items
def show_menu(category_listbox):
    category = category_listbox.get(tk.ACTIVE)
    menu_listbox.delete(0, tk.END)
    for item in menu[category]:
        menu_listbox.insert(tk.END, f"{item['name']} - Rs {item['price']:.2f}")

# Adding items 
def add_to_order(menu_listbox, quantity_entry):
    item_index = menu_listbox.curselection()
    if not item_index:
        messagebox.showwarning("Warning", "Please select an item.")
        return

    try:
        quantity = int(quantity_entry.get())
        if quantity <= 0:
            raise ValueError("Invalid quantity")

        item = menu[category_listbox.get(tk.ACTIVE)][item_index[0]]
        item_total_price = item['price'] * quantity
        order_listbox.insert(tk.END, f"{item['name']} ({quantity}) - Rs {item_total_price:.2f}")
        order.append({'name': item['name'], 'quantity': quantity, 'price': item_total_price})

        global total_price
        total_price += item_total_price
        total_label.config(text=f"Total Price: Rs {total_price:.2f}")

        quantity_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showwarning("Warning", "Invalid quantity. Please enter a positive integer.")

# Bill
def generate_bill():
    if not order:
        messagebox.showinfo("Information", "No items in the order.")
        return

    bill_window = tk.Toplevel(root)
    bill_window.title("Bill")

    bill_text = tk.Text(bill_window, height=20, width=40)
    bill_text.pack()

    bill_text.insert(tk.END, "-------------------\n")
    bill_text.insert(tk.END, "     Restaurant\n")
    bill_text.insert(tk.END, "-------------------\n\n")

    for item in order:
        bill_text.insert(tk.END, f"{item['name']} ({item['quantity']}) - Rs {item['price']:.2f}\n")

    bill_text.insert(tk.END, f"\nTotal Price: Rs {total_price:.2f} \n")
    bill_text.insert(tk.END, "-------------------\n")
    bill_text.config(state=tk.DISABLED)

# Category listbox
category_listbox = tk.Listbox(root,width=50, selectmode=tk.SINGLE)
category_listbox.pack()
for category in menu.keys():
    category_listbox.insert(tk.END, category)

# Menu listbox
menu_listbox = tk.Listbox(root,width=50, selectmode=tk.SINGLE)
menu_listbox.pack()

# Order listbox
order_listbox = tk.Listbox(root,width=50, selectmode=tk.SINGLE)
order_listbox.pack()

# Total price labels
total_label = tk.Label(root, text="Total Price: Rs 0.00",)
total_label.pack()

# Quantity Entries
quantity_label = tk.Label(root, text="Enter Quantity:")
quantity_label.pack()
quantity_entry = tk.Entry(root,width=50,)
quantity_entry.pack()

# Buttons
show_menu_button = tk.Button(root, text="Show Menu", 
                command=lambda: show_menu(category_listbox))
add_to_order_button = tk.Button(root, text="Add to Order", 
                command=lambda: add_to_order(menu_listbox, quantity_entry))
generate_bill_button = tk.Button(root, text="Generate Bill", 
                command=generate_bill)

show_menu_button.pack()
add_to_order_button.pack()
generate_bill_button.pack()
 

root.mainloop()