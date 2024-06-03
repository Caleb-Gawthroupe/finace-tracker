from account import *


# Error Messages
entry_type_error = "Error: Invalid Entry Type"
out_of_range_error = "Error: Out of Range"


def main():
    #Error Messages
    entry_type_error = "Error: Invalid Entry Type"
    out_of_range_error = "Error: Out of Range"
    account = BankAccount.import_account()
    
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
            account = BankAccount.reset_account(account)
        if action == 2:
            account = BankAccount.paycheck(account)
        if action == 3:
            account = BankAccount.spend_money(account)
        if action == 4:
            account = BankAccount.transfer_savings(account)
        if action == 5:
            BankAccount.view_balances(account)
        if action == 6:
            BankAccount.save_account(account)
            break
 


main()
