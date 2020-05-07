import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def check(word):
    
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif len(get_close_matches(word,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y" or 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N" or 'n':
            return "The word doesn't exist."
        else:
            return "We didn't understand your entry."
    else:
        return "The word does not exists !"


print("Welcome to my dictionary")

word=input("Enter a word: ")
output=check(word)

if type(output)==list:
    for item in output:
        print (" means: " ,item)

else:
    print (" means: " ,output)