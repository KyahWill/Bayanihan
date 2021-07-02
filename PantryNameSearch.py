def Search(input_string,pantry_list):
    output = []
    input_length = len(input_string)
    for pantry in data:
        # #Append "i" into output if:
        # 1. i["name"] is equal to input_string
        # 3. i["region"] is equal to input_string
        # 4. i["city"] is equal to input_string

        # In addition, find a way that even if the letters are of the wrong case,
        # "i" would be appended to the output array if the above conditions are still
        # satisfied even if the letters are of the wrong case
        # Suggestion: turn all community pantry names in upper case and use upper() for user input?

        for i in range(len(pantry["name"])-input_length + 1):
            if input_string.upper() == pantry["name"][i:i + input_length].upper():
                output.append(pantry)
            if input_string.upper() == pantry["city"][i:i + input_length].upper():
                output.append(pantry)
            if input_string.upper() == pantry["region"][i:i + input_length].upper():
                output.append(pantry)
    
     # yet to find out how to append status, region, and city from the .json file onto output var.
     # for now i've made it so they print out with the community pantry name
    return output

def Filter(input_dictionary,pantry_list):
    output = []

    for pantry in pantry_list:
        pass


    return output
if __name__ == "__main__":
    import json
    import sys  

    
    f = open("JSON\\Pantries.json", 'r', encoding='utf8', errors='ignore')
    data = json.load(f)

    inputPantryName = input("Enter a community pantry name: \n")
    output = Search(input_string = inputPantryName, pantry_list = data)
    for i in output:
        print(i['name'])
    f.close()
