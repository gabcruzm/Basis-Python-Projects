def palindrome(word):
    word = word.replace(" ", "")
    word = word.lower()
    inverted_word = word[::-1]
    if word == inverted_word:
        return True
    else:
        return False

def run():
    word = input("Write a word: ")
    is_palindrome = palindrome(word)
    if is_palindrome == True:
    # if palindrome(word) == True: --> This can be done to simplify
        print("It's a palindrome word")
    else: 
        print("Isn't a palindrome word")

#EntryPoint
if __name__ == "__main__":
    run()

