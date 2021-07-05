from kivy.lang import builder
from kivymd.app import MDApp
from pantryMapView import PantryMapView
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.garden.mapview import MapMarkerPopup
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp
from kivymd.uix.list import OneLineIconListItem


class IconListItem(OneLineIconListItem):
    icon = StringProperty()


class MainApp(MDApp):

    def on_start(self):
        #Iloload na yung gps location.
        #magload ng gps location.
        pass

    def __init__(self, **kwargs):
        options = ["open", "not open", "doesnt matter"]
        super().__init__(**kwargs)
        self.screen = Builder.load_file("main.kv")
        menu_items = [
            {    "viewclass": "IconListItem",
                "icon": "git",
                "height": dp(50),
                "text": f"{options[i]}",
                "on_release": lambda x = f"{options[i]}": self.set_item(x)
            } for i in range (3)
        ]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.drop_item,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        self.menu.bind()

    def set_item(self, text_item):
        self.screen.ids.drop_item.set_item(text_item)
        self.menu.dismiss()


    def build(self):
        return self.screen
    
    

MainApp().run()