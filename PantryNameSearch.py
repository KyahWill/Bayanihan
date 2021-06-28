import json
import sys

if __name__ == "__main__":
#Program searches for community pantry names within Pantries.json

# loads the json file containing community pantries
    f = open("Pantries.json", 'r', encoding='utf8', errors='ignore')
    data = json.load(f)

#NOTE: As of now, community pantry names have to be EXACT when searching.
    inputPantryName = input("Enter a community pantry name: \n")

    #prints the community pantry name if found
    for i in data:
        if i["name"] == inputPantryName: print(i["name"])


# Need to be able to find a way to check json file for community pantry name string
# and accept the user-inputted string as a substring of the entire name string to enable approximate searches 