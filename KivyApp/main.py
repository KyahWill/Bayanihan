from kivy.garden.mapview import MapView, MapMarkerPopup
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label


class MainApp(App):
    def on_start(self):
        output = [
            MapMarkerPopup(lat=13.4210, lon=123.4137, source="marker.png"),
            MapMarkerPopup(lat=14.7289, lon=121.1441, source="marker.png"),
            MapMarkerPopup(lat=14.6959, lon=121.1217, source="marker.png")
        ]
        output[1].lat = 14.5533
        x = []
        for i in output:
            x.append(i)
        for i in x:
            self.root.add_widget(i)
        # iriga = MapMarkerPopup(lat=13.4210, lon=123.4137, source="marker.png")
        # iriga.add_widget(Button(text="Iriga"))
        # self.root.add_widget(iriga)

        # rodriguez = MapMarkerPopup(lat=14.7289, lon=121.1441, source="marker.png")
        # rodriguez.add_widget(Button(text="Rodriguez"))
        # self.root.add_widget(rodriguez)

        # sanmateo = MapMarkerPopup(lat=14.6959, lon=121.1217, source="marker.png")
        # sanmateo.add_widget(Button(text="San Mateo"))
        # self.root.add_widget(sanmateo)

MainApp().run()