from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy_garden import MapMarkerPopup, MapView


class MainApp(App):
    def on_start(self):
        Manila = MapMarkerPopup(lat=14.6959, lon=121.1217, source="marker.png")
        San_Mateo = MapMarkerPopup(lat=14.7289, lon=121.1441, source="marker.png")
        Montalban = MapMarkerPopup(lat=14.7289, lon=121.1441, source="marker.png")
        Bicol = MapMarkerPopup(lat=13.4210, lon=123.4137, source="marker.png")
        Cebu = MapMarkerPopup(lat=10.3157, lon=123.8854, source="marker.png")
        Pangasinan = MapMarkerPopup(lat=15.8949, lon=120.2863, source="marker.png")
        Pampanga = MapMarkerPopup(lat=15.0794, lon=120.6200, source="marker.png")
        Aklan = MapMarkerPopup(lat=11.8166, lon=122.0942, source="marker.png")
        Romblon = MapMarkerPopup(lat=12.5778, lon=122.2691, source="marker.png")
        Cavite = MapMarkerPopup(lat=14.4791, lon=120.8970, source="marker.png")


        self.root.add_widget(Manila)
        self.root.add_widget(San_Mateo)
        self.root.add_widget(Montalban)
        self.root.add_widget(Bicol)
        self.root.add_widget(Cebu)
        self.root.add_widget(Pangasinan)
        self.root.add_widget(Pampanga)
        self.root.add_widget(Aklan)
        self.root.add_widget(Romblon)
        self.root.add_widget(Cavite)
    pass


MainApp().run()
