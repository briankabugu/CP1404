"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
 - A ValueError will occur if the user enters a non-integer value when asked for the numerator or denominator.
2. When will a ZeroDivisionError occur?
 - A ZeroDivisionError will occur if the user enters 0 as the denominator which will in division by zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Yes, this is done by checking that the denominatior is not zero before the operation.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


