from kivy.garden.mapview import MapView,MapMarkerPopup
from kivy.clock import Clock
from kivy.app import App
import JSON.ReadJson as ReadJson
from PantryNameSearch import Search
from kivy.uix.button import Button
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineListItem
from kivy.uix.popup import Popup

class PantryMapView(MapView):


    timer = None
    listAllPantries = ReadJson.getPantries()
    pantryNames = []
    
    def shift(self,lat,long):
        self.lat = lat
        self.long = long

       

    def searchPantries(self,input_string):
        return Search(input_string = input_string,pantry_list = self.listAllPantries)


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

    #def info(self,obj):
    #    close_button = MDFlatButton(text = 'Close', on_release = self.close_dialog)
    #    self.wala = MDDialog(
    #        buttons = [close_button],
    #        text = self.pan)
    #    self.wala.open()


    def close_dialog(self, obj):
        self.dialog.dismiss()

    def addPantry(self,pantry):
        lat,lon = pantry["latitude"], pantry["longtitude"]
        marker = MapMarkerPopup(lat = lat,lon = lon,source = "marker.png")
        text  ='''Name: {}\nStatus: {}\nFaceBookpost: {} '''.format(pantry['name'],pantry['status'],pantry['fb_post'])
        # ['id', 'status', 'name', 'longtitude', 'latitude', 'houseNo', 'street', 'barangay', 'region', 'province', 'city', 'gmap', 'fb_post', 'date_started'
        x =MDLabel(text = text)
        x.md_bg_color = (1,1,1,200/255)           
        x.size_hint = (2,3)
        marker.add_widget(x)

        #marker.add_widget(Button(text = "info", on_release = self.info))
        # marker.pantries = pantry
        try:
            self.add_widget(marker)
        except Exception as e:
            print(e)
        name = pantry["name"]
        self.pantryNames.append(name)





