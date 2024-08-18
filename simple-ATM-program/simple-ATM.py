# Small Project: Simple ATM
# This program simulates a simple ATM with basic features like deposit, withdrawal, and balance inquiry.

def user_info():
    """
    Collects and displays user information.
    Asks for the user's name and ID, then welcomes the user. 
    """
    user_name = input("\n\nEnter your username\n")
    user_id = input("Enter your id\n")
    print(f"Welcome {user_name.upper()}\nYour ID is {user_id}\n\n")


def deposit():
    """
    Handles the deposit process.
    Prompts the user to input a deposit amount, validates the input, and returns the deposited amount.
    """
    while True:
        try:
            deposited_amount = float(input("Enter an amount to deposit\n"))
            if deposited_amount < 0:
                print("Amount cannot be negative! Please try again.\n")
                continue
            print(f"Rs {deposited_amount:.2f} deposited successfully\n")
            return deposited_amount
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")


def withdrawal(current_balance):
    """
    Handles the withdrawal process.
    Prompts the user to input a withdrawal amount, checks if the balance is sufficient, and returns the withdrawn amount.
    """
    while True:
        try:
            withdrawal_amount = float(input("Enter an amount to withdraw\n"))
            if withdrawal_amount < 0:
                print("Amount cannot be negative! Please try again.\n")
                continue

            if withdrawal_amount > current_balance:
                print(f"Sorry, current balance Rs {current_balance:.2f} is less than the requested amount Rs {withdrawal_amount:.2f}\nPlease re-enter amount.\n")
                continue

            print(f"Rs {withdrawal_amount:.2f} withdrawn successfully\n")
            return withdrawal_amount

        except ValueError:
            print("Invalid input! Please enter a valid number.\n")


def checking_current_balance(available_balance):
    """
    Displays the current balance.
    Accepts the current balance as a parameter and prints it.
    """
    print(f"Your current balance Rs {available_balance:.2f}\n")


def main_menu():
    """
    Displays the main menu and handles user selection.
    Returns the user's selected action (1 for Deposit, 2 for Withdraw, 3 for Balance Inquiry).
    """
    while True:
        print("Press 1 to Deposit:")
        print("Press 2 to Withdraw:")
        print("Press 3 to Check Current Balance:")

        try:
            request = int(input())
            if request in [1, 2, 3]:
                return request
            else:
                print("Invalid choice! Please select 1, 2, or 3.\n")
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")


def check_process_status(process_status):
    """
    Determines whether the user wants to continue or exit the program.
    Accepts user input and returns True for 'yes' and False for 'no'.
    """
    process_status = process_status.lower()
    if process_status in ['y', 'yes']:
        return True
    elif process_status in ['n', 'no']:
        return False
    else:
        print("\nInvalid input! Please try again.\n")
        return None


def main():
    """
    The main function where the program flow is controlled.
    It initializes the user's balance, handles the main loop, and processes user requests.
    """
    user_info()

    actual_current_balance = 0.00

    while True:
        request = main_menu()

        if request == 1:
            temp_deposit = deposit()
            actual_current_balance += temp_deposit

        elif request == 2:
            temp_withdrawal = withdrawal(actual_current_balance)
            actual_current_balance -= temp_withdrawal

        elif request == 3:
            checking_current_balance(actual_current_balance)

        continue_process = input("Go to Main Menu? (Y for yes or N for no)\n").strip()
        continue_process_stat = check_process_status(continue_process)
        if not continue_process_stat:
            break


if __name__ == "__main__":
    main()
