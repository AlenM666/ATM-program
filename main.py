import time
import os
import sys

balance = 5000

class ATM:
    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd

    def withdraw(self, balance,withdraw_amount):
        wav = balance - withdraw_amount
        return f"You have {wav} left in your accoutn. "

    def deposit(self):
        pass

    def check_balance(self):
        pass


    def login(self):
        pass


print("****************************************************************************")
print("*                                                                          *")
print("   *                        WELCOME TO FIZZ BANK                        *   ")
print("*                                                                          *")
print("****************************************************************************")
print("\n")
print("************************* PLEASE CREATE NEW USER **************************")



#new user
user1 = ATM(input("Enter username: "), int(input("Enter password: ")))

new_user = user1.username
new_passwd = user1.passwd
print("New user crated")
#os.system("clear")

print("\n")
while True:
    print("****************************************************************************")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check balance")
    print("****************************************************************************")
    choice = int(input("Choice (1/2/3): "))
    if choice == 1:
        withdraw_amount = int(input("Enter the amount you would like to withdraw: "))
        print(user1.withdraw(balance, withdraw_amount))
        break
    else:
        print("invalid")
    continue














