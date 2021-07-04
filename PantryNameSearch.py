def Search(input_string, pantry_list):
    output = []
    input_length = len(input_string)
    for pantry in data:

        for i in range(len(pantry["name"]) - input_length + 1):
            if input_string.upper() == pantry["name"][i:i + input_length].upper():
                output.append(pantry)
            if input_string.upper() == pantry["city"][i:i + input_length].upper():
                output.append(pantry)
            if input_string.upper() == pantry["region"][i:i + input_length].upper():
                output.append(pantry)

    return output


def Filter(input_dictionary, pantry_list):
    output = []

# incomplete, still need to find out how to read the city province and region of user-inputted community pantry name
    for pantry in pantry_list:

            inputtedCity = input("Enter a city: \n")

            for i in data:
                if i["city"] == inputtedCity: print(i["city"])

            inputtedProvince = input("Enter a Province: \n")

            for i in data:
                if i["province"] == inputtedProvince: print(i["province"])

            inputtedRegion = input("Enter a Region: \n")

            for i in data:
                if i["region"] == inputtedRegion: print(i["region"])

    return output


if __name__ == "__main__":
    import json
    import sys

    f = open("JSON\\Pantries.json", 'r', encoding='utf8', errors='ignore')
    data = json.load(f)

    inputPantryName = input("Enter a community pantry name: \n")
    output = Search(input_string=inputPantryName, pantry_list=data)
    for i in output:
        print(i['name'])
# added these back in
        print(i["region"])
        print(i["city"])
    f.close()
