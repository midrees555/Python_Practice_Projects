# Prime Numbers Printer

This project contains a Python program that prints all prime numbers between 1 and 50.

## Description

The program defines a function `isPrime(num)` that checks if a number is prime. It then uses this function in the `main()` function to print all prime numbers between 1 and 50.

## Usage

To run the program, simply execute the `main()` function. The program will print all prime numbers between 1 and 50.

## Code

```python
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main():
    for i in range(2, 50):
        if isPrime(i):
            print(i)

if __name__ == "__main__":
    main()
