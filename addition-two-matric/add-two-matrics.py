# Greetings
print("\nWelcome To Addition of Two Matrics Program\n\n")

# Initilizing two empty lists
matric_A = []
matric_B = []
result_matric = []



    
def sum_two_matric(matric_A, matric_B, result_matric):
    for rows in matric_A:
        for col in rows:
            result_matric[col] = matric_A[col] + matric_B[col]

    return result_matric


def show_result(result_matric):
    for rows in matric_A:
        for col in rows:
            print(result_matric[col], end = ", ")
        
        print("\n")


# Function to checks continuesly Process status
def process_status(process_stat):
    """function, who ask the user whether user wants to continue the process or exit"""
    process_stat = process_stat.lower()

    if process_stat in ['y', 'yes']:
        return False
    elif process_stat in ['n', 'no']:
        return True
    else:
        print("\nInvalid choice! Try again\n")
        return None


while True:
    num_of_rows = int(input("\nEnter number of Rows...\n"))
    num_of_col = int(input("Enter number of Columns...\n"))
    # Asking user to specify orders of a matrics if user wants to continue the process
    processStatus = input("Continue process? (Y/YES or N/NO)\n").split()
    continueProcess = process_status(processStatus)


    if num_of_rows <= 0 or num_of_col <= 0:
        print("\nNumber of Rows/Columns can't be zero\n")

    elif num_of_rows == num_of_col:
        pass
        # Inputing Matric - A values from users

        # Inputing Matric - B values from users

        # Adding Matric - A & Matric - B

        # Showing result
    else:
        pass


