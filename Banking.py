def show_balance(balance):
    print(f'Your balance is ₹{balance:.2f}')


def deposit():
    amt = float(input("Enter the amount to be deposited: "))
    if amt < 0:
        print("That's not a valid amount.")
        return 0
    return amt


def withdraw(balance):
    amt = float(input("Enter amount to be withdrawn: "))
    if amt > balance:
        print("Insufficient balance.")
        return 0
    if amt < 0:
        print("Amount must be greater than 0.")
        return 0
    return amt


def main():
    balance = 0.0
    is_running = True

    while is_running:
        print("\nBanking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw Money")
        print("4. EXIT")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            is_running = False
        else:
            print("Not a valid choice.")

    print("THANK YOU !!!! HAVE A NICE DAY!!!")


if __name__ == "__main__":
    main()

