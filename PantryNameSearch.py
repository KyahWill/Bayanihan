def Search(input_string,pantry_list):
    output = []
    for i in data:
        # #Append "i" into output if:
        # 1. i["name"] is equal to input_string
        # 2. i["status"] is equal to input_string
        # 3. i["region"] is equal to input_string
        # 4. i["city"] is equal to input_string

        # In addition, find a way that even if the letters are of the wrong case,
        # "i" would be appended to the output array if the above conditions are still
        # satisfied even if the letters are of the wrong case


        if i["name"] == input_string: output.append(i)

    return output


if __name__ == "__main__":
    import json
    import sys  

    
    f = open("Pantries.json", 'r', encoding='utf8', errors='ignore')
    data = json.load(f)
    f.close()
    inputPantryName = input("Enter a community pantry name: \n")
    output = Search(input_string = inputPantryName, pantry_list = data)

    for i in output:
        print(i["name"])
