import json
from difflib import get_close_matches
import pyttsx3

engine = pyttsx3.init()
data = json.load(open("data.json"))
choice = ''
no_exit = True


def translate(dictionary, key):
    key = key.lower()
    if key in dictionary:
        return dictionary[key]
    elif len(get_close_matches(key, data.keys())) > 0:
        choice = input(
            f"Did you mean {get_close_matches(key,data.keys())[0]} ?[Y/n]\n")
        if choice.lower() == 'y':
            return dictionary[get_close_matches(key, data.keys())[0]]
        elif choice.lower() == 'n':
            return "The word doesn't exist. Please double check it."
        else:
            return "Sorry, We didn't understand..."
    else:
        return "The word doesn't exist. Please double check it."


def main():
    print("========================================================")
    print("\t\tENGLISH DICTIONARY")
    print("========================================================")

    word = input("\nType your word:\n")
    print("\n")
    output = translate(data, word)
    if type(output) == list:
        for i in output:
            newVoiceRate = 145
            engine.setProperty('rate', newVoiceRate)
            engine.say(i)
            engine.runAndWait()
            print(i)

    else:
        newVoiceRate = 145
        engine.setProperty('rate', newVoiceRate)
        engine.say(output)
        engine.runAndWait()
        print(output)


while no_exit:
    main()
    choice = input("\nWould you like to search for another word? [Y/n]\n")
    if choice.lower() == 'n':

        print("\tGood Bye 🥲")
        engine.setProperty('rate', 145)
        engine.say('Good Bye')
        engine.runAndWait()
        no_exit = False
