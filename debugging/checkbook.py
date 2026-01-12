#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            while True:
                try:
                    amount_input = input("Enter the amount to deposit: $")
                    amount = float(amount_input)
                    if amount < 0:
                        print("Amount cannot be negative. Please enter a valid amount.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            cb.deposit(amount)
        elif action == 'withdraw':
            while True:
                try:
                    amount_input = input("Enter the amount to withdraw: $")
                    amount = float(amount_input)
                    if amount < 0:
                        print("Amount cannot be negative. Please enter a valid amount.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
