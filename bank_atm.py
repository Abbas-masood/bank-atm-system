class Bank_atm:
    def __init__(self):
        self.bal = 0
        self.pin = ""
        self.menu()

    def menu(self):
        options = input(''' 
        1. Set balance
        2. Set PIN
        3. Check balance
        4. Withdrawal
        5. Exit
        Enter your choice: ''')
        if options == "1":
            self.set_amount()
        elif options == "2":
            self.set_pin()
        elif options == "3":
            self.check_balance()
        elif options == "4":
            self.withdrawal()
        elif options == "5":
            print("Thank you for using Bank ATM.")
        else:
            print("Invalid option. Try again.")
            self.menu()

    def set_amount(self):
        amount = float(input("Enter amount to set as balance: "))
        self.bal = amount
        print("Balance set successfully.")
        self.menu()

    def set_pin(self):
        new_pin = input("Enter new PIN: ")
        self.pin = new_pin
        print("PIN changed successfully.")
        self.menu()

    def check_balance(self):
        pin = input("Enter PIN to check balance: ")
        if pin == self.pin:
            print("Your balance is:", self.bal)
        else:
            print("Incorrect PIN.")
        self.menu()

    def withdrawal(self):
        pin = input("Enter PIN to withdraw: ")
        if pin == self.pin:
            amount = float(input("Enter amount to withdraw: "))
            if self.bal >= amount:
                self.bal -= amount
                print("Transaction successful.")
                print("Amount withdrawn:", amount)
                print("Remaining balance:", self.bal)
            else:
                print("Insufficient balance.")
        else:
            print("Incorrect PIN.")
        self.menu()

# Run the ATM system
Bank_atm()
