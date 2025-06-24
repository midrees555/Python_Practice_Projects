# ------------------------------------------------------------/
# ------------------------------------------------------------/
# Combining it into one CLI Program
print('|-----------------------------------------|')

# Function to take 'user_choice' as a input
def user_choices():
    print('|-----------------------------------------|')
    print("📚 MY NOTES APP\n")
    print("Press 1: Adding New Notes!")
    print("Press 2: Viewing Notes!")
    print("Press 3: Clear Notes!")
    
    # input 'user_choice' with error handling block
    try:
        user_choice = int(input())
    except TypeError as e:
        print("Something went wrong!\nError: {}".format(e))
    
    return user_choice

# Function to ask user to (Continue/Exit)
def process_termination():
    terminate_process = input("Continue Adding New Notes? (y/n)").lower()
    if terminate_process in ['n', 'no']:
        print("Exiting The app...\n\n")
        return True
    else:
        return False
    

# Function to adding new notes
def add_notes():
    # Creating loop untill user want to exit
    while True:
        # Taking input notes from user
        notes_contents = input("Start typing to add new notes...\nREMEMBER: Add single line at a time!\n")
        
        # Appending notes to a file
        with open('my_simple_notes_app_file.txt', 'a') as file:
            file.write(notes_contents + '\n')
            print("Your notes saved successfully!\n\n")
            
        if process_termination:
            break

# Function to view & read notes
def read_notes():
    # Reading from file
    with open('my_simple_notes_app_file.txt', 'r') as file:
        reading_notes = file.read()
        if len(reading_notes.strip()) != 0:
            print('|-----------------------------------------|')
            print('|📚📚📚📚📚📚📚📚📚📚📚📚📚📚|')
            print("Your Notes:\n", reading_notes)
        else:
            print("Error! Notes empty already...\n")

# Function to clear notes
def clear_notes():
    
    clear_status = None
    while True:
        clear_status = input("Are you sure to clear the notes? (y/n): ").lower()
        if clear_status not in ['y', 'yes', 'n', 'no']:
            print("Error: Incorrect input! Please try again...\n")
        else:
            break
        
    if clear_status == 'y' or clear_status == 'yes':
        # check whether notes not empty already
        with open('my_simple_notes_app_file.txt', 'r') as file:
            saved_notes = file.read()
            if len(saved_notes.strip()) != 0:
                # If not empty, write mode will auto clear the contents
                with open('my_simple_notes_app_file.txt', 'w') as file:
                    print("Your notes has been cleared successfully!\n")
            else:
                print("Error! Notes empty already...\n")
    else:
        print("Your notes are still safe")
        print('|-----------------------------------------|')

# Function to ask to user to (Continue/Exit)
def main_menu():
    user_menu_choice = input("Got to Main Menu? (y/n)").lower()
    if user_menu_choice in ['n', 'no', 'nope']:
        print("Exiting the app...")
        print('|-----------------------------------------|')
        return True
        
def main():
    while True:
        user_choice = user_choices()
        if user_choice == 1:
            add_notes()
        elif user_choice == 2:
            read_notes()
        elif user_choice == 3:
            clear_notes()
        else:
            print("Incorrect input! Please try again...")
        
        if main_menu():
            break
    


if __name__ == "__main__":  # Checks if this script is being run directly (not imported as a module)
    main()                  # Calls the main() function to start the Notes App