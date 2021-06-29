from kivymd.app import MDApp
from pantryMapView import PantryMapView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.garden.mapview import MapMarkerPopup

from kivy.core.window import Window
from kivy.lang.builder import Builder

class MainApp(MDApp):
    def on_start(self):
        #Iloload na yung gps location.
        #magload ng gps location.
        pass

MainApp().run()