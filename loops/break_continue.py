def run():
    # for counter in range(1000):
    #     if counter % 2 != 0: #If the reminder when the counter is divided by 2 it's different from 0, the loop is skipped and what is below the word 'continue' will not be executed.
    #         continue
    #     print(counter) 
    #Now we will see what happens with 'break'
    # for i in range(10000): 
    #     print(i)
    #     if i == 500: 
    #         break

    text = input("Write a text: ")
    for letter in text:
        if letter == "o":
            break
        print(letter)

        

if __name__ == "__main__":
    run()
