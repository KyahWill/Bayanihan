from kivy.garden.mapview import MapView,MapMarkerPopup
from kivy.clock import Clock
from kivy.app import App
import JSON.ReadJson as ReadJson
from kivy.uix.button import Button

class PantryMapView(MapView):
    timer = None
    listAllPantries = ReadJson.getPantries()
    pantryNames = []

    def getMarketsTry(self):
        try: 
            self.timer.cancel()
        except:
            pass
        self.timer = Clock.schedule_once(self.getMarkets,1)

    def getMarkets(self, *args):
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()

        pantries = []
        print("{}, {}, {}, {}".format(min_lat,min_lon,max_lat,max_lon))

        for i in self.listAllPantries:
            if min_lon < i["longtitude"] < max_lon and min_lat < i["latitude"] < max_lat:
                pantries.append(i)
        for pantry in pantries:
            if pantry["name"] in self.pantryNames:
                continue
            else:
                self.addPantry(pantry)
    
    def addPantry(self,pantry):
        lat,lon = pantry["latitude"],pantry["longtitude"]
        marker = MapMarkerPopup(lat = lat,lon = lon,source = "marker.png")
        marker.add_widget(Button(text = str(pantry)))
        try:
            self.add_widget(marker)
        except Exception as e:
            print(e)
        name = pantry["name"]
        self.pantryNames.append(name)