import csv
import json
import geocoder
from dataclasses import asdict, dataclass




@dataclass(init = True,repr=True)
class Pantry:
    id: int
    status: str
    name:str
    longtitude:float
    latitude: float
    houseNo: str
    street: str
    barangay: str
    region: str
    province: str
    city: str
    gmap: str
    fb_post:str
    date_started:str
    active_mon:bool
    active_tue:bool
    active_wed:bool
    active_thu:bool
    active_fri:bool
    active_sat:bool
    active_sun:bool    
 
#Opens the CSV document
def initiate():
    pantries = []
    with open('Community_Pantry.csv',encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        uniqueId = 1
            #i[2] = Status
            #i[3] = Name of Pantry
            #i[4] = House No.
            #i[5] = Street
            #i[6] = Barangay
            #i[7] = City
            #i[8] = Province
            #i[9] = Region
            #i[10] = Gmaps Link
            #i[11] = Date Started
            #i[12] = Operational Days
            #i[13] = Operational Hours
            #i[14] = FB Post
            #i[15] = Remarks
        for i in csv_reader:
            long = 0
            lat = 0    
            

            #This segment attempts geo-coding
            address = i[6] + ", " + i[7] + ", " + i[8]
            print(address)
            try:
                g = geocoder.osm(address)
                if type(g.osm['x']) == float and type(g.osm['y']) == float:
                    long = g.osm['x']
                    lat = g.osm['y']
                else:
                    print(str(g.osm['x']) + " , " + str(g.osm['y']))
            except Exception as e:
                print(e)

            pantry =Pantry(
                    id= uniqueId,
                    status=i[2],
                    name=i[3],
                    longtitude=long,
                    latitude=lat,
                    houseNo= i[4],
                    street = i[5],
                    barangay=i[6],
                    city=i[7],
                    province=i[8],
                    region= i[9],
                    gmap= i[10],
                    fb_post=i[14],
                    date_started=i[11],
                    active_mon=True,
                    active_tue=True,
                    active_wed=True,
                    active_thu=True,
                    active_fri=True,
                    active_sat=True,
                    active_sun=True
                )
            print(str(pantry.id) +", "+str(pantry.name), " = ("+ str(pantry.longtitude) + " , " + str(pantry.latitude)+")" )
            pantries.append(asdict(pantry))
            uniqueId+=1
    return pantries
#Scans the operational days

if __name__ == "__main__":
    pantry_list = initiate()
    with open("latestPantries.json", "w") as outfile: 
        json.dump(pantry_list, outfile)
    print("Done!!!!")


#removes all the capitals of the letter