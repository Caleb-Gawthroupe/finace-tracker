# Error Messages
entry_type_error = "Error: Invalid Entry Type"
out_of_range_error = "Error: Out of Range"

class BankAccount:
    def __init__(self, checkings, savings, tithing, savings_to_transfer):
        self.checkings = checkings
        self.savings = savings
        self.tithing = tithing
        self.savings_to_transfer = savings_to_transfer

def create_account():
    checkings = ""
    savings = ""
    tithing = ""
    savings_to_transfer = ""
    while type(checkings) != float:
        try:
            checkings = float(input("Checkings Balance: "))
        except:
            print(entry_type_error)
    while type(savings) != float:
        try:
            savings = float(input("Savings Balance: "))
        except:
            print(entry_type_error)
    while type(tithing) != float:
        try:
            tithing = float(input("Tithing: "))
        except:
            print(entry_type_error)
    while type(savings_to_transfer) != float:
        try:
            savings_to_transfer = float(input("Savings To Transfer: "))
        except:
            print(entry_type_error)
            
    return BankAccount(checkings,savings,tithing, savings_to_transfer)

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

def save_account(account):
    # Checkings -> Savings -> Tithing -> To Transfer
    with open("banking.txt", "w") as f:
        f.write(
            str(account.checkings)+"\n"+str(account.savings)+"\n"+str(account.tithing)+"\n"+str(account.savings_to_transfer)
        )
    
def paycheck(account):
    pay = ""
    while type(pay) != float:
        try:
            pay = float(input("Paycheck: "))
        except:
            print(entry_type_error)
    
    # Tithing
    account.tithing += pay*0.1
    # Savings
    account.savings += pay*0.4
    account.savings_to_transfer += pay*0.4
    # Checkings
    account.checkings += pay*0.5
    input()
    return account
    
def transfer_savings(account):
    account.savings_to_transfer = 0
    input()
    return account
    
def spend_money(account):
    while True:
        try:
            spent = float(input("Spent: "))
            break
        except:
            print(entry_type_error)
    
    account.checkings -= spent
    input()
    return account

def view_balances(account):
    print("Checkings: "+str(account.checkings))
    print("Savings: "+str(account.savings))
    print("Tithing: "+str(account.tithing))
    print("Savings To Transfer: "+str(account.savings_to_transfer))
    input()
            

def main():
    account = import_account()
    while True:
        #Round the account numbers
        account.checkings = round(account.checkings,2)
        account.savings = round(account.savings,2)
        account.tithing = round(account.tithing,2)
        account.savings_to_transfer = round(account.savings_to_transfer,2)
        while True:
            action = 0
            try:
                print("What would you like to do?")
                action = int(input("Reset Account (1) \nAdd Paycheck (2) \nSpend Money (3) \nTransfer Money to Savings (4) \nView Balance (5) \nExit Program(6)\n"))
            except:
                print(entry_type_error)
            if action < 1 or action > 6:
                print(out_of_range_error)
            else:
                break
        if action == 1:
            account = create_account()
        if action == 2:
            account = paycheck(account)
        if action == 3:
            account = spend_money(account)
        if action == 4:
            account = transfer_savings(account)
        if action == 5:
            view_balances(account)
        if action == 6:
            save_account(account)
            break

main()
