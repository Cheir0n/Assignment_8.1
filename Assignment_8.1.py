# Steven Thompson Jr
# 4-30-2020
# Assignment 8.1
# Interactive banking program with 2 preset starting balances

class Banking:
    #parent banking class
    def __init__(self, balance):
        self.balance = balance

    #withdraw money
    def withdraw (self):
        confirmed = False
        while confirmed != True:
            withdrawl = input("How much would you like to withdraw? ")
            try:
                withdrawl = int(withdrawl)
            except:
                print("An invalid entry has been made.  Please try again.\n")
            else:
                if withdrawl > self.balance:
                    print("You cannot withdraw more than you have.")
                else:
                    self.balance -= withdrawl
                    break

    #deposit money
    def deposit (self):
        confirmed = False
        while confirmed != True:
            deposit = input("How much would you like to deposit? ")
            try:
                deposit = int(deposit)
            except:
                print("An invalid entry has been made.  Please try again.\n")
            else:
                self.balance += deposit
                break

    #check account balance
    def getBalance(self):
        printed_balance = "{:,.2f}".format(self.balance)
        print(f"Your current balance is ${printed_balance}.")


class Checking(Banking):
    #child of Banking class for checking account
    def __init__(self, balance):
        super().__init__(balance)
        self.fee = 5

    def deductFee(self):
        self.balance -= self.fee

    def checkMinimumBalance(self):
        self.minimumBalance = 50
        if self.balance < self.minimumBalance:
            print(f"Your balance is less than ${self.minimumBalance}. A ${self.fee} will be subtracted from your account.")
            check1.deductFee()
            printed_balance = "{:,.2f}".format(self.balance)
            print(f"You now have ${printed_balance} left in your account.")


class Savings(Banking):
    #child of Banking class for savings account
    def __init__(self, balance):
        super().__init__(balance)
        self.interest_rate = 0.02

    def addInterest(self):
        print(f"There is an interest rate of {self.interest_rate * 100}% on your savings account.")
        loop_done = False
        while loop_done != True:
            add_interest = input("Would you like to add interest to your account (Y/N)? ")
            if add_interest == 'y' or add_interest == 'Y':
                loop_done = True
                break
            elif add_interest == 'n' or add_interest == 'N':
                loop_done = False
                break
            else:
                "An invalid entry has been made.  Please try again."
        self.balance = self.balance + (self.balance * self.interest_rate)
        printed_balance = "{:,.2f}".format(self.balance)
        print(f"Your new balance after adding interest is ${printed_balance}.")

cycle_number = 1
finish = False
ending = False

#starting loop to allow customer to bank again or finish
while finish != True:
    acct_numb = input("Wecome to The Bank.  Please enter your account number: ")
#determining which starting balance to use
    if cycle_number % 2 != 0:
        balance = 100
    else:
        balance = 25
    cycle_number += 1
    check1 = Checking(balance)
    saving1 = Savings(balance)
#starting actual banking
    account_done = False
    while account_done != True:
        done = False
        while done != True:
            account_type = input("Do you want your (C)hecking account or (S)avings account? ")
            if account_type != 'c' and account_type != 'C' and account_type != 's' and account_type != 'S':
                print ("Invalid entry.  Please try again.")
            else:
                break
#checking account
        if account_type == 'c' or account_type == 'C':
            print("OK, checking it is.\n")
            checkingDone = False
            check1.checkMinimumBalance()
            while checkingDone != True:
                choice_made = False
                print("\nYou have the following options to choose from:")
                print("\t (G)et your account balance.")
                print("\t (D)eposit money.")
                print("\t (W)ithdraw money.")
                while choice_made != True:
                    choice = input("What would you like to do? ")
                    if choice == 'g' or choice == 'G':
                        check1.getBalance()
                        break
                    elif choice == 'd' or choice == 'D':
                        check1.deposit()
                        check1.checkMinimumBalance()
                        break
                    elif choice == 'w' or choice == 'W':
                        check1.withdraw()
                        break
                    else:
                        print ("Invalid Entry.  Please try again.")
                leave_checking = input("Are you done with Checking (Y/N)? ")
                if leave_checking == 'y' or leave_checking == 'Y':
                    checkingDone = True
                elif leave_checking == 'n' or leave_checking == 'N':
                    checkingDone = False
                else:
                    print("An invalid entry has been made.  Please try again.")
#savings account
        elif account_type == 's' or account_type == 'S':
            print("OK, savings it is.\n")
            savingDone = False
            while savingDone != True:
                choice_made = False
                print("\nYou have the following options to choose from:")
                print("\t (G)et your account balance.")
                print("\t (D)eposit money.")
                print("\t (W)ithdraw money.")
                print("\t (C)heck interest rate.")
                while choice_made != True:
                    choice = input("What would you like to do? ")
                    if choice == 'g' or choice == 'G':
                        saving1.getBalance()
                        break
                    elif choice == 'd' or choice == 'D':
                        saving1.deposit()
                        break
                    elif choice == 'w' or choice == 'W':
                        saving1.withdraw()
                        break
                    elif choice == 'c' or choice == 'C':
                        saving1.addInterest()
                        break
                    else:
                        print ("Invalid Entry.  Please try again.")
                leave_saving = input("Are you done with Savings (Y/N)? ")
                if leave_saving == 'y' or leave_saving == 'Y':
                    savingDone = True
                elif leave_saving == 'n' or leave_saving == 'N':
                    savingDone = False
                else:
                    print("An invalid entry has been made.  Please try again.")
 #leaving account
        loop_done = False
        while loop_done != True:
            leave_account = input("Are you done with this account (Y/N)? ")
            if leave_account == 'y' or leave_account == 'Y':
                account_done = True
                break
            elif leave_account == 'n' or leave_account == 'N':
                account_done = False
                break
            else:
                print("An invalid entry has been made.  Please try again.")

#done banking altogether?
    while ending != True:
        end = input("Would you like to access another account? (Y) or (N): ")
        if end == 'Y' or end == 'y':
            finish = False
            break
        elif end == 'N' or end == 'n':
            print("Thank you for using The Bank.")
            finish = True
            break
        else:
            print ("An invalid answer has been made.  Please try again.")
