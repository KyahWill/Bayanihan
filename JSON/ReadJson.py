import json

def getPantries():
    f = open("JSON\\Pantries.json", 'r', encoding='utf8', errors='ignore')
    data = json.load(f)
    f.close()
    return data

if __name__ == "__main__":
    import os
    print(os.listdir())
    f = open("JSON\\Pantries.json", 'r', encoding='utf8', errors='ignore')
    data = json.load(f)

    print(data[1].keys())

    f.close()
    