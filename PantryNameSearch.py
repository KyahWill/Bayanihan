def Search(input_string, pantry_list):
    output = []
    input_length = len(input_string)
    for pantry in pantry_list:

        for i in range(len(pantry["name"]) - input_length + 1):
            if input_string.upper() == pantry["name"][i:i + input_length].upper():
                output.append(pantry)
                break
            elif input_string.upper() == pantry["city"][i:i + input_length].upper():
                output.append(pantry)
                break
            elif input_string.upper() == pantry["region"][i:i + input_length].upper():
                output.append(pantry)
                break

    return output

def Filter(input_dictionary, pantry_list):

    output = []
    for i in pantry_list:
        if i["active_sun"] == input_dictionary["active_sun"] or i["active_sun"] == "Doesn't Matter":
            if i["active_mon"] == input_dictionary["active_mon"] or i["active_mon"] == "Doesn't Matter":
                if i["active_tue"] == input_dictionary["active_tue"] or i["active_tue"] == "Doesn't Matter":
                    if i["active_wed"] == input_dictionary["active_wed"] or i["active_wed"] == "Doesn't Matter":
                        if i["active_thu"] == input_dictionary["active_thu"] or i["active_thu"] == "Doesn't Matter":
                            if i["active_fri"] == input_dictionary["active_fri"] or i["active_fri"] == "Doesn't Matter":
                                if i["active_sat"] == input_dictionary["active_sat"] or i["active_sat"] == "Doesn't Matter":
                                    output.append(i)

    return output


if __name__ == "__main__":
    import json
    import sys

    f = open("JSON\\Pantries.json", 'r', encoding='utf8', errors='ignore')
    data = json.load(f)



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


