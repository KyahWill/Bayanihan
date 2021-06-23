from kivymd.app import MDApp
from pantryMapView import PantryMapView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.garden.mapview import MapMarkerPopup

from kivy.core.window import Window
from kivy.lang.builder import Builder
map_toolbar = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Toolbar"
                        left_action_items: [["menu",lambda x: nav_drawer.set_state()]]
                        elevation: 10
                    MapView:
                        double_tap_zoom: False
                        lat: 14.5995
                        lon: 120.9842
                        zoom: 5

                    Widget:

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                Image:
                    source: "bean.jpg"
                MDLabel:
                    text: "Community Pantry PH"
                    font_style: 'Subtitle1'
                    size_hint_y: None
                MDLabel:
                    text: "TITE HEHE"
                    font_style: 'Caption'     
"""
class MainApp(MDApp):
    def on_start(self):
        #Iloload na yung gps location.
        screen = Builder.load_string(map_toolbar)
        #magload ng gps location.
        return screen

MainApp().run()