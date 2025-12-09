import tkinter as tk
from tkinter import messagebox

class BankATM_GUI:
    def __init__(self, root):
        self.bal = 0
        self.pin = ""
        self.root = root
        self.root.title("Bank ATM")
        self.root.geometry("300x300")
        self.menu_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def menu_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Select an option:").pack(pady=10)
        tk.Button(self.root, text="1. Set Balance", command=self.set_amount).pack(pady=5)
        tk.Button(self.root, text="2. Set PIN", command=self.set_pin).pack(pady=5)
        tk.Button(self.root, text="3. Check Balance", command=self.check_balance).pack(pady=5)
        tk.Button(self.root, text="4. Withdrawal", command=self.withdrawal).pack(pady=5)
        tk.Button(self.root, text="5. Exit", command=self.root.quit).pack(pady=5)

    def set_amount(self):
        self.clear_screen()
        tk.Label(self.root, text="Enter amount to set as balance:").pack(pady=10)
        amount_entry = tk.Entry(self.root)
        amount_entry.pack()
        def save_amount():
            try:
                self.bal = float(amount_entry.get())
                messagebox.showinfo("Success", "Balance set successfully.")
                self.menu_screen()
            except ValueError:
                messagebox.showerror("Error", "Enter a valid number.")
        tk.Button(self.root, text="Submit", command=save_amount).pack(pady=10)

    def set_pin(self):
        self.clear_screen()
        tk.Label(self.root, text="Enter new PIN:").pack(pady=10)
        pin_entry = tk.Entry(self.root, show="*")
        pin_entry.pack()
        def save_pin():
            self.pin = pin_entry.get()
            messagebox.showinfo("Success", "PIN changed successfully.")
            self.menu_screen()
        tk.Button(self.root, text="Submit", command=save_pin).pack(pady=10)

    def check_balance(self):
        self.clear_screen()
        tk.Label(self.root, text="Enter PIN to check balance:").pack(pady=10)
        pin_entry = tk.Entry(self.root, show="*")
        pin_entry.pack()
        def verify_pin():
            if pin_entry.get() == self.pin:
                messagebox.showinfo("Balance", f"Your balance is ₹{self.bal}")
            else:
                messagebox.showerror("Error", "Incorrect PIN.")
            self.menu_screen()
        tk.Button(self.root, text="Submit", command=verify_pin).pack(pady=10)

    def withdrawal(self):
        self.clear_screen()
        tk.Label(self.root, text="Enter PIN to withdraw:").pack(pady=10)
        pin_entry = tk.Entry(self.root, show="*")
        pin_entry.pack()
        tk.Label(self.root, text="Enter amount to withdraw:").pack(pady=10)
        amount_entry = tk.Entry(self.root)
        amount_entry.pack()
        def process_withdrawal():
            if pin_entry.get() == self.pin:
                try:
                    amount = float(amount_entry.get())
                    if self.bal >= amount:
                        self.bal -= amount
                        messagebox.showinfo("Success", f"₹{amount} withdrawn.\nRemaining balance: ₹{self.bal}")
                    else:
                        messagebox.showerror("Error", "Insufficient balance.")
                except ValueError:
                    messagebox.showerror("Error", "Enter a valid amount.")
            else:
                messagebox.showerror("Error", "Incorrect PIN.")
            self.menu_screen()
        tk.Button(self.root, text="Submit", command=process_withdrawal).pack(pady=10)

# Run the GUI ATM
root = tk.Tk()
app = BankATM_GUI(root)
root.mainloop()
