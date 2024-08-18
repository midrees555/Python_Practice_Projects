# Simple ATM Program

## Overview

This project simulates a simple ATM system that allows users to perform basic banking operations such as depositing money, withdrawing money, and checking their balance. The program is designed to run in a loop until the user decides to exit, providing a straightforward and interactive experience.

## Features

- **User Authentication:** The program collects and displays the user's name and ID for a personalized experience.
- **Deposit Money:** Users can deposit a specified amount of money into their account.
- **Withdraw Money:** Users can withdraw a specified amount, provided they have sufficient funds in their account.
- **Check Balance:** Users can check their current account balance at any time.
- **Continuous Operation:** The program runs in a loop, allowing multiple transactions until the user opts to exit.

## How to Use

1. **Run the Program:**
   - Execute the `main()` function to start the program.
   - You will be prompted to enter your username and ID.

2. **Main Menu:**
   - After the welcome message, the main menu will be displayed with three options:
     1. Deposit money.
     2. Withdraw money.
     3. Check your current balance.

3. **Deposit Money:**
   - Select the deposit option by entering `1`.
   - Enter the amount you wish to deposit.
   - The program will validate the input and confirm the deposit.

4. **Withdraw Money:**
   - Select the withdrawal option by entering `2`.
   - Enter the amount you wish to withdraw.
   - The program will check if you have sufficient funds and process the withdrawal accordingly.

5. **Check Balance:**
   - Select the balance inquiry option by entering `3`.
   - The program will display your current account balance.

6. **Exit:**
   - After each transaction, you will be asked if you want to return to the main menu.
   - Enter `Y` for yes to continue, or `N` for no to exit the program.

## Example Interaction

```plaintext
Enter your username:
JohnDoe
Enter your ID:
12345
Welcome JOHNDOE
Your ID is 12345

Press 1 to Deposit:
Press 2 to Withdraw:
Press 3 to Check Current Balance:
1
Enter an amount to deposit:
500
Rs 500.00 deposited successfully

Go to Main Menu? (Y for yes or N for no)
Y

Press 1 to Deposit:
Press 2 to Withdraw:
Press 3 to Check Current Balance:
2
Enter an amount to withdraw:
200
Rs 200.00 withdrawn successfully

Go to Main Menu? (Y for yes or N for no)
Y

Press 1 to Deposit:
Press 2 to Withdraw:
Press 3 to Check Current Balance:
3
Your current balance Rs 300.00

Go to Main Menu? (Y for yes or N for no)
N


## Requirements
 - **Python 3.x** is required to run this program.
 - No additional libraries are needed.

## How to Run
1. **Clone the repository:**
    - git clone https://github.com/midrees555/python-small-projects.git
2. **Navigate to the Project Directory:**
    - cd python-small-projects/simple-ATM-program
3. **Run The Program**
    - simple-ATM.py

## License
- This project is licensed under the MIT License. Feel free to use, modify, and distribute this program as you wish.

Happy coding! If you have any questions or suggestions, feel free to reach out.


