#Loop through a string with For

def run():
    # name = input("Write your name: ")
    # for letter in name: #For letters in the name it will print each letter in each loop.
    #     #letter is the variable that will represent each character in each repetition in the for loop. The characters are taken from the name wich is a str.
    #     print(letter)

    frase = input("Write a phrase: ")
    for caracter in frase:
        print(caracter.upper())

if __name__ == "__main__":
    run()