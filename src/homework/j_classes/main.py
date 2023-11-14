#
import random 
from class_a import Die

def main():
    die = Die()

    while True:
        input("Press Enter to roll the die...")
        die.roll()
        print(str(die))

        choice = input("Do you want to roll again? (yes/no): ").lower()
        if choice != 'yes':
            print("Exiting the program. Goodbye!")
            break
