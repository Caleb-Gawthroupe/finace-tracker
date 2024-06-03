


class BankAccount:
    def __init__(self, checkings, savings, tithing, savings_to_transfer):
        # Main Account Values
        self.checkings = checkings
        self.savings = savings
        self.tithing = tithing
        self.savings_to_transfer = savings_to_transfer
        
        #Error Messages
        self.entry_type_error = "Error: Invalid Entry Type"
        self.out_of_range_error = "Error: Out of Range"

    def reset_account(self):
        self.checkings = ""
        self.savings = ""
        self.tithing = ""
        self.savings_to_transfer = ""
        while type(self.checkings) != float:
            try:
                self.checkings = float(input("Checkings Balance: "))
            except:
                print(self.entry_type_error)
        while type(self.savings) != float:
            try:
                self.savings = float(input("Savings Balance: "))
            except:
                print(self.entry_type_error)
        while type(self.tithing) != float:
            try:
                self.tithing = float(input("Tithing: "))
            except:
                print(self.entry_type_error)
        while type(self.savings_to_transfer) != float:
            try:
                self.savings_to_transfer = float(input("Savings To Transfer: "))
            except:
                print(self.entry_type_error)
        return self
                
    def import_account():
        # Checkings -> Savings -> Tithing -> To Transfer
        with open("banking.txt","r") as f:
            checkings = f.readline()
            checkings = float(checkings[:-1])

            savings = f.readline()
            savings = float(savings[:-1])
            
            tithing = f.readline()
            tithing = float(tithing[:-1]) 
            
            savings_to_transfer = f.readline()
            savings_to_transfer = float(savings_to_transfer[:-1])
            
            return BankAccount(checkings,savings,tithing,savings_to_transfer)

    def save_account(self):
        # Checkings -> Savings -> Tithing -> To Transfer
        with open("banking.txt", "w") as f:
            f.write(
                str(self.checkings)+"\n"+str(self.savings)+"\n"+str(self.tithing)+"\n"+str(self.savings_to_transfer)
            )
        
    def paycheck(self):
        pay = ""
        while type(pay) != float:
            try:
                pay = float(input("Paycheck: "))
            except:
                print(self.entry_type_error)
        
        # Tithing
        self.tithing += pay*0.1
        # Savings
        self.savings += pay*0.4
        self.savings_to_transfer += pay*0.4
        # Checkings
        self.checkings += pay*0.5
        input()
        return self
        
    def transfer_savings(self):
        self.savings_to_transfer = 0.0
        input()
        return self
        
    def spend_money(self):
        while True:
            try:
                spent = float(input("Spent: "))
                break
            except:
                print(self.entry_type_error)
        
        self.checkings -= spent
        input()
        return self

    def view_balances(self):
        print("Checkings: "+str(self.checkings))
        print("Savings: "+str(self.savings))
        print("Tithing: "+str(self.tithing))
        print("Savings To Transfer: "+str(self.savings_to_transfer))
        input()
                

 
