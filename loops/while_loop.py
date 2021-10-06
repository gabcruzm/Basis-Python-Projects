#Print all power of 2 up to 1000
#counter = 0
# print("2 power " + str(counter) + "it's equal: " + str(2**counter))

#counter = 1
# print("2 power " + str(counter) + "it's equal: " + str(2**counter))

#counter = 2
# print("2 power " + str(counter) + "it's equal: " + str(2**counter))

#This is why it's important Python loops. - while loop it's IMPORTANT! Good practices

def run(): 
    LIMIT = 1000000 #the variable DOES NOT CHANGE. Constant variable.

    counter = 0 #it will increase to multiply by 2 for as many times as the counter says it.
    power_2 = 2**counter
    while power_2 < LIMIT: #while the power of 2 is less than the limit, what is above will be executed. As long as the condition is fulfilled, what is above is going to be executed.
        print("2 power " + str(counter) + " it's equal: " + str(power_2))
        counter = counter + 1
        power_2 = 2**counter


if __name__ + "__main__":
    run()