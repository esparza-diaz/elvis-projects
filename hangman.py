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
    attempts = 6 # attempts to guess word
    word = fetch() # stores word from api
    found = [0] * len(word) # initializes empty array the length of the word

    while True:
        # create the output string based on letters found 
        output = ""
        for a in range(0,len(found)):
            if found[a] == 0:
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
                if attempts == 0:
                    print("GAMEOVER! WORD WAS: " + word)
                    break
            else:
                #TODO: What to do if letter is in word???? 
                if letter in word:
                    for i in range(0,len(word)):
                        if word[i] == letter:
                            found[i] = letter

                if 0 not in found:
                    print("CONGRATULATIONS")
                    break
        else:
            print("Invalid Input")


