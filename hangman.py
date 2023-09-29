import requests
import sys

# This method will fetch and return a random word from an api
def fetch():
    r = requests.get("https://random-word-api.herokuapp.com/word")
    word = r.json()
    return word[0]

# print the automatic word 
if __name__ == "__main__":
    letters_missed = set() # keeps track of letters entered
    attempts = 5 # attempts to guess word
    word = fetch() # stores word from api
    found = [0] * len(word) # initializes empty array the length of the word

    print(word) # print the word for now for testing. once testing is done delete this line. TODO

    while True:
        # create the output string based on letters found 
        output = ""
        for a in found:
            if a == 0:
                output = output + "_ "
            else:
                output = output + str(found[a]) + " "
        print(output)

        print("Letters missed: " + str(letters_missed) + " Attempts left: " + str(attempts))
        letter = input("Enter letter: ")
        # first check letter is a letter
        if letter.isalpha():
            letter = letter.lower()
            # if letter not in word add to letters missed and subtract attempt
            if letter not in word and letter not in letters_missed:
                letters_missed.add(letter)
                attempts -= 1
                #TODO: When does game over happen???
            else:
                #TODO: What to do if letter is in word???? 
                print("???")
        else:
            print("Invalid Input")


