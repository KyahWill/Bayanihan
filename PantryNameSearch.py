def Search(input_string, pantry_list):
    output = []
    input_length = len(input_string)
    for pantry in pantry_list:

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
    # Append every community pantry to output if it has equal value to input_dictionary
    for i in pantry_list:
        if i["region"].upper() == input_dictionary["region"].upper():
            output.append(i)
        else:
            print("No region match found. Were you looking for the community pantry in...")
            print(i["region"])
        if i["active_sun"] == input_dictionary["active_sun"]:
            output.append(i)
        else:
            print("None found")

        if i["active_mon"] == input_dictionary["active_mon"]:
            output.append(i)
        else:
            print("None found")

        if i["active_tue"] == input_dictionary["active_tue"]:
            output.append(i)
        else:
            print("None found")

        if i["active_wed"] == input_dictionary["active_wed"]:
            output.append(i)
        else:
            print("None found")

        if i["active_thu"] == input_dictionary["active_thu"]:
            output.append(i)
        else:
            print("None found")

        if i["active_fri"] == input_dictionary["active_fri"]:
            output.append(i)
        else:
            print("None found")

        if i["active_sat"] == input_dictionary["active_sat"]:
            output.append(i)
        else:
            print("None found")


    return output


if __name__ == "__main__":
    import json
    import sys

    f = open("JSON\\Pantries.json", 'r', encoding='utf8', errors='ignore')
    data = json.load(f)

    # inputPantryName = input("Enter a community pantry name: ")
    # output = Search(input_string=inputPantryName, pantry_list=data)
    # for i in output:
    #     print(i['name'])

    input_dictionary = {
        "region": "NCR",
        "active_sun":True,
        "active_mon":True,
        "active_tue":True,
        "active_wed":True,
        "active_thu":True,
        "active_fri":True,
        "active_sat":True,


    }

    output = Filter(input_dictionary=input_dictionary, pantry_list=data)
    for i in output:
        print(i['name'])

    f.close()


