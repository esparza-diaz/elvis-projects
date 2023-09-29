import requests

# This method will fetch and return a random word from an api
def fetch():
    r = requests.get("https://random-word-api.herokuapp.com/word")
    word = r.json()
    return word[0]

# print the automatic word 
print(fetch())
