balance = 5000
class ATM:
    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd

    def withdraw(self, balance,withdraw_amount):
        wav = balance - withdraw_amount
        return f"You have {wav}€ left in your accoutn. "

    def deposit(self, balance, deposit_amount):
        dav = balance + deposit_amount
        return f"You have deposited {deposit_amount}€ and now you have {dav}€."

    def check_balance(self, balance):
        return f"You have {balance}€ in you account."


print("****************************************************************************")
print("*                                                                          *")
print("   *                        WELCOME TO FIZZ BANK                        *   ")
print("*                                                                          *")
print("****************************************************************************")
print("\n")
print("************************* PLEASE CREATE NEW USER **************************")

#new user
user1 = ATM(input("Enter username: "), int(input("Enter password: ")))

print("New user crated")

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
    elif choice == 2:
        deposit_amount = int(input("Enter the amout you wish to deposit in your account: "))
        print(user1.deposit(balance, deposit_amount))
        break
    elif choice == 3:
        print(user1.check_balance(balance))
        break
    else:
        print("\n")
        continue















