from kivy.garden.mapview import MapView,MapMarkerPopup
from kivy.clock import Clock
from kivy.app import App
import JSON.ReadJson as ReadJson
from kivy.uix.button import Button
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

class LocationPopupMenu(MDDialog):
    
    def __init__(self, pantry_data):
        super().__init__()
        
        # Set all of the fields of market data
        self.text = str(pantry_data)

    def show_dialog(self, instance):
        if not self.dialog:
            self.dialog = MDDialog(
                buttons=[
                    MDFlatButton(
                        on_release=lambda _: self.dialog.dismiss()
                    )
                ],
            )
        self.dialog.open()
class PantryMarker(MapMarkerPopup):

    # 
    #     marker.add_widget(Label())
    source = "marker.png"
    pantries = {}


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
        marker.add_widget(MDFlatButton(text = str(pantry)))
        # marker.pantries = pantry
        try:
            self.add_widget(marker)
        except Exception as e:
            print(e)
        name = pantry["name"]
        self.pantryNames.append(name)