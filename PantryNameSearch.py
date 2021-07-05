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


    for pantry in pantry_list:
        pass

    return output


if __name__ == "__main__":
    import json
    import sys

    f = open("JSON\\Pantries.json", 'r', encoding='utf8', errors='ignore')
    data = json.load(f)

    inputPantryName = input("Enter a community pantry name: ")
    PantryCityFilter = input("Enter a city: ")
    PantryRegionFilter = input("Enter a region: ")

    output = Search(input_string=inputPantryName, pantry_list=data)
    for i in output:
        print(i['name'])
        if i["region"].upper() == PantryRegionFilter.upper():
            print("Region match found!")
            print(i["region"])
        else:
            print("No region match found. Were you looking for the community pantry in...")
            print(i["region"])

# Need to find a way to implement the same checking procedure for pantry name to cities
        if i["city"].upper() == PantryCityFilter.upper():
            print("City match found!")
            print(i["city"])
        else:
            print("No city match found. Were you looking for the community pantry in...")
            print(i["city"])
    f.close()


