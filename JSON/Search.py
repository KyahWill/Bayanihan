import json
import sys

if __name__ == "__main__":

# loads the json file containing community pantries
    f = open("JSON\\latestPantriess.json", 'r', encoding='utf8', errors='ignore')
    data = json.load(f)
    for i in data:
        print("{}: {},{}".format(i['name'],i["longtitude"],i["latitude"]))
    f.close()


