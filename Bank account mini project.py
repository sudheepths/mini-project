class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def login(self, entered_pin):
        return entered_pin == self.pin

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds. Withdrawal failed."

def main():
    # Creating a sample account
    account_number = "4971205190"
    pin = "7777"
    initial_balance = 1000

    user_account = BankAccount(account_number, pin, initial_balance)

    # Login
    entered_pin = input("Enter your PIN: ")
    if user_account.login(entered_pin):
        print("Login successful for account no",account_number)
    else:
        print("Incorrect PIN. Exiting...")
        return

    # Perform transactions
    while True:
        print("\nSelect banking option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            deposit_amount = float(input("Enter the deposit amount: "))
            print(user_account.deposit(deposit_amount))
        elif choice == "2":
            withdraw_amount = float(input("Enter the withdrawal amount: "))
            print(user_account.withdraw(withdraw_amount))
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
