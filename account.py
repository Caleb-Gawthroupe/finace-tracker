import pandas as pd
import os


class BankAccount:
    def __init__(self, checkings, savings, tithing, savings_to_transfer):
        # Main Account Values
        self.checkings = checkings
        self.savings = savings
        self.tithing = tithing
        self.savings_to_transfer = savings_to_transfer
        
        # Saving Goals
        self.goals = [] # 2D array with values stored in lists as Name, Goal, Value Per Check, Ammount Saved
        
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
        filename = 'banking.csv'
        if os.path.getsize(filename) != 0:
            df = pd.read_csv(filename, header=None)
            bank = df.values.tolist()
            
            checkings = bank[0][0]
            savings = bank[0][1]
            tithing = bank[0][2]
            savings_to_transfer = bank[0][3]
        else:
            checkings = 0.0
            savings = 0.0
            tithing = 0.0
            savings_to_transfer = 0.0
                
            
        return BankAccount(checkings,savings,tithing,savings_to_transfer)
        
        
        

    def save_account(self):
        # Checkings -> Savings -> Tithing -> To Transfer
        
        filename = 'banking.csv'  
        df = pd.DataFrame([self.checkings,self.savings,self.tithing,self.savings_to_transfer])
        df.to_csv(filename,index=False,header=False)
        
        # Save Saving Goals
        df = pd.DataFrame(self.goals)
        filename = 'goals.csv'
        df.to_csv(filename,index=False,header=False)
        
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
        
    def create_saving_goal(self):
        goal_name = ""
        goal_total = ""
        goal_ammount_per = ""
        while len(goal_name) < 1:
            goal_name = input("Goal Name: ")
        while type(goal_total) != float:
            try:
                goal_total = float(input("Saving Goal Total: "))
            except:
                print(self.entry_type_error)   
        while type(goal_ammount_per) != float:
            try:
                goal_ammount_per = float(input("How much allocated per paycheck (Ammount or Percentage as decimal): "))
            except:
                print(self.entry_type_error)   
        self.goals.append([goal_name,goal_total,goal_ammount_per,0.0]) # 0 is the nothing currently saved
        input()
        
    def view_saving_goals(self):
        for goal in self.goals:
            print(str(goal[0])+": "+str(goal[-1])+"/"+str(goal[1]))
        input()
        
    def load_saving_goals(self):
        filename = 'goals.csv'
        if os.path.getsize(filename) != 0:
            df = pd.read_csv(filename, header=None)

            self.goals = df.values.tolist()
        else:
            self.goals = []
        
