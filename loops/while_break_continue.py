#Use of Continue with While Loop

def run():
    LIMIT = 1000
    counter = 0
    power_2 = 2**counter
    while power_2 < LIMIT:
        counter = counter + 1
        power_2 = 2**counter
        if counter % 2 != 0:
            continue
        print("2 power " + str(counter) + " it's equal " + str(power_2))


if __name__ == "__main__":
    run()

