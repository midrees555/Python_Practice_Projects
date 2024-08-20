def factorial(num):
    """
    Calculate the factorial of a given number recursively.
    
    Args:
    num (int): The number to find the factorial of.
    
    Returns:
    int: Factorial of the number.
    """
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif num == 0 or num == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    return num * factorial(num - 1)  # Recursive case

def process_status(process_stat):
    """
    Determine whether to continue the process based on user input.
    
    Args:
    process_stat (str): User input indicating whether to continue (e.g., 'y', 'yes', 'n', 'no').
    
    Returns:
    bool: False if user wants to continue, True if they want to stop.
    """
    process_stat = process_stat.lower()
    if process_stat in ['y', 'yes']:
        return False
    elif process_stat in ['n', 'no']:
        return True
    else:
        print("Invalid input! Please enter 'y'/'yes' or 'n'/'no'.")
        return None

def main():
    """
    Main function to continuously calculate factorials based on user input until the user decides to stop.
    """
    while True:    
        try:
            user_input = int(input("Enter a non-negative integer to find its factorial: "))
            if user_input < 0:
                print("Please enter a non-negative integer.\n")
                continue
            print(f"Factorial of {user_input} = {factorial(user_input)}")
        except ValueError:
            print("Invalid input! Please enter a valid integer.\n")
            continue

        continue_process = input("Continue the process? (Press y or n): ").strip()
        process_result = process_status(continue_process)
        if process_result is None:
            continue  # If invalid input is given, ask again
        elif process_result:
            break

if __name__ == "__main__":
    main()
