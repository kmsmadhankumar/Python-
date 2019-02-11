import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def findword(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        yn = input("Did you mean %s instead?.Enter Y if yes or N if no: " % get_close_matches(word,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N":
            return "Word doesn't exist.Please check"
        else:
            return "Please enter only Y/N."
    else:
        return "Word doesn't exist; Please check!"

# input
word = input("Enter word: ")

#output
output = findword(word)

x=1
if type(output) == list:
    for item in output:
        print(str(x)+". "+item)
        x += 1
else:
    print(output)
# print(findword(word))
