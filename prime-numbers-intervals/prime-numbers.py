# Prime Numbers Printer

# This project contains a Python program that prints all prime numbers between 1 and 50.


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
