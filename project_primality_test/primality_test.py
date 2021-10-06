def is_prime(number):
    counter = 0

    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            counter += 1 #I's the same to write counter = counter + 1
    if counter == 0:
        return True
    else:
        return False

def run():
    number = int(input("Write a number: ")) #As the number enter through the console comes as str format, we must put 'int' to transformate the number into integer.
    # if is_prime(number) == True: # Inside a conditional and the function result or variable is equal to True, this can be ignored and removed ' == True ' It's optional.
    if is_prime(number): #This is enough. Python understands what is asking for if the function result is equal to True the following is executed. 
        print("It is a prime number!")
    else:
        print("It is NOT a prime number!")


if __name__ == "__main__":
    run()