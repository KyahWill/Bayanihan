import json
import sys

if __name__ == "__main__":

# loads the json file containing community pantries
    f = open("latestPantries.json", 'r', encoding='utf8', errors='ignore')
    data = json.load(f)

    print("To filter a city, input 0. For provinces, input 1. For regions, input 2 \n")
    filterinput = input("Input a number: \n")

    if (filterinput == "0"):

        inputtedCity = input("Enter a city: \n")

        # prints every city
        for i in data:
            if i["city"] == inputtedCity: print(i["city"])

    elif (filterinput == "1"):

        inputtedProvince = input("Enter a Province: \n")

        # prints every Province
        for i in data:
            if i["province"] == inputtedProvince:print(i["province"])


    elif (filterinput == "2"):

        inputtedRegion = input("Enter a Region: \n")

        # prints every Region
        for i in data:
            if i["region"] == inputtedRegion: print(i["region"])
    else:
        print("Invalid input")


