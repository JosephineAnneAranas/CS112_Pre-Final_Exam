print("CS112: COMPUTER PROGRAMMING 1 - PRE-FINAL EXAM") #Introductory Statement
print("Created by: Josephine Anne B. Aranas\n") #Name of student

#Stating the problem and rules tp consider
print("Problem: Create python program that displays all prime numbers within a range:\n\nRULES TO CONSIDER:")
print("[1] If number [start] is a negative number. The program will prompt a message: \"Enter a non-negative number\"\n[2] If number[end] is less than number [start]. The program will prompt a message: \"Enter a number greater than number [start]\"\n[3] If the user enter the number \"0\", the program will terminate.\n ")

def IsIt_Prime(Number): #To determine prime numbers
    if Number < 2:
        return False
    for i in range(2, int(Number**0.5) + 1):
        if Number % i == 0:
            return False
    return True

while True: #Create an infinite loop to get the right input required for the range of Number [Start]
    PrimeNumber_Start = int(input("Enter a number [Start]: "))

    if PrimeNumber_Start < 0: #To invalidate user's negative inputs
        print("Invalid input. Enter a non-negative number.")
        continue

    if PrimeNumber_Start == 0: #To terminate a zero input taken from user
        print("Program terminated.")
        exit()

    while True: #Create an infinite loop inside an infinite loop to get the right input required for the range of Number [End]
        PrimeNumber_End = int(input("Enter a number [End]: "))

        if PrimeNumber_End < 0 and PrimeNumber_End < PrimeNumber_Start: #To invalidate user's negative input that are lesser than Number [Start]
            print(f"Invalid input. Enter a non-negative number that is greater than {PrimeNumber_Start}")
            continue

        if PrimeNumber_End == 0: #To terminate a zero input taken from user
            print("Program terminated.")
            exit()

        if PrimeNumber_End < PrimeNumber_Start and PrimeNumber_End > 0: #To invalidate user's input that are lesser than Number [Start]
            print(f"Invalid input. Enter a number greater than than {PrimeNumber_Start}")
            continue

        PrimeRange = [Number for Number in range(PrimeNumber_Start, PrimeNumber_End + 1) if IsIt_Prime(Number)] #To get a list of prime numbers within the range
        print(f"Prime numbers within {PrimeNumber_Start} and {PrimeNumber_End} are: {PrimeRange}\n")
        break
