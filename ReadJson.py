import json


if __name__ == "__main__":
    f = open("latestPantries.json", 'r', encoding='utf8', errors='ignore')
    data = json.load(f)

    for i in data:
        print(i["city"])

    f.close()
    