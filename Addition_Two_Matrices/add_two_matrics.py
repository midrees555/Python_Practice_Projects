# Initialize empty lists to store the matrices
listOne = []
listTwo = []

# Function to get a positive integer input from the user
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please input a positive integer\n")
                continue
            return value
        except ValueError:
            print("Invalid input! Please try again\n")

# Get the number of rows and columns from the user
numberOfRows = get_positive_integer("\nEnter number of Rows:\n")
numberOfCols = get_positive_integer("Enter number of Columns:\n")

# Function to input values into two matrices A and B
def inputValue(A, B, rows, cols):
    # Input values for Matrix A
    print("\n\nMatrix A:")
    for row in range(rows):
        current_row = []
        for col in range(cols):
            value = int(input(f"\nEnter value for A[{row}][{col}]:\n"))
            current_row.append(value)
        A.append(current_row)

    # Input values for Matrix B
    print("\n\nMatrix B:")
    for row in range(rows):
        current_row = []
        for col in range(cols):
            value = int(input(f"\nEnter value for B[{row}][{col}]:\n"))
            current_row.append(value)
        B.append(current_row)

# Function to add two matrices P and Q
def add_matrices(P, Q):
    # Check if matrices have the same dimensions
    if len(P) != len(Q) or len(P[0]) != len(Q[0]):
        print("\nError: Matrices must have the same dimensions to be added.\n")
        return None
    
    # Initialize the result matrix
    result = []

    # Add corresponding elements of matrices P and Q
    for i in range(len(P)):
        new_row = []
        for j in range(len(P[0])):
            new_row.append(P[i][j] + Q[i][j])
        result.append(new_row)

    return result

# Function to display matrices and their addition result
def showResult(X, Y):
    # Display Matrix A
    print("\nMatrix A:")
    for row in X:
        print("  ".join(str(element) for element in row))

    # Display Matrix B
    print("\nMatrix B:")
    for row in Y:
        print("  ".join(str(element) for element in row))

    # Calculate and display the result of adding Matrix A and Matrix B
    print("\n\nResultant Matrix (A + B):\n")
    result = add_matrices(X, Y)

    if result:  # Check if the addition was successful
        for row in result:
            print("  ".join(str(element) for element in row))
        print("\n")

# Main execution
inputValue(listOne, listTwo, numberOfRows, numberOfCols)  # Get matrix inputs
showResult(listOne, listTwo)  # Display matrices and their sum
