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
    op_days:str
    op_time:str
 
#Opens the CSV document
def initiate():
    pantries = []
    with open('CSV\\new_data.csv',encoding="utf8") as csv_file:
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
            lon = 0
            lat = 0    
            address = ""
            if i[1] == "CPPH ORG":
                for j in range(3):
                    if i[j+5] != ' ' and i[j+5] != None:
                        address+="{},".format(i[j+5])
                #This segment attempts geo-coding
                print('>>>>>'+address)
                try:
                    g = geocoder.osm(address)
                    lon = g.osm['x']
                    lat = g.osm['y']
                    print(str(g.osm["addr:country"]))
                    if(g.osm["addr:country"]=='Mindanao'):
                        pantry =Pantry(
                        id= uniqueId,
                        status=i[1],
                        name=i[2],
                        longtitude=lon,
                        latitude=lat,
                        houseNo= i[3],
                        street = i[4],
                        barangay=i[5],
                        city=i[6],
                        province=i[7],
                        region= i[8],
                        gmap= i[9],
                        fb_post=i[13],
                        date_started=i[10],
                        active_mon=True,
                        active_tue=True,
                        active_wed=True,
                        active_thu=True,
                        active_fri=True,
                        active_sat=True,
                        active_sun=True,
                        op_days=i[11],
                        op_time=i[12]
                        )
                        print(str(pantry.id) +", "+str(pantry.name), " = ("+ str(pantry.longtitude) + " , " + str(pantry.latitude)+")" )
                        pantries.append(asdict(pantry))
                        uniqueId+=1
                except Exception as e:
                    print(e)
    return pantries
#Scans the operational days

if __name__ == "__main__":
    pantry_list = initiate()
    print(pantry_list)
    with open("latestPantries.json", "w") as outfile: 
        json.dump(pantry_list, outfile)
    print("Done!!!!")


#removes all the capitals of the letter