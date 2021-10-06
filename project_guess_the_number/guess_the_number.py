# Python module: code package written by Python. Available to run. They are functions already written.
import random #Package of code that has functions to work with randomness in the language

def run():
    random_number = random.randint(1, 100) #randint is to generate an integer and the range.
    chosen_number = int(input("Choose a number from 1 to 100: "))
    while chosen_number != random_number:
        if chosen_number < random_number:
            print("Look for a higher number...")
        else:
            print("Look for a lower number...")
        chosen_number = int(input("Choose another number: "))
    print("YOU WIN!!")


if __name__ == "__main__":
    run()
