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
        super().__init__(**kwargs)
        self.screen = Builder.load_file("main.kv")
################################sunday#####################################
        options = ["open", "not open", "doesnt matter"]
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

##############################monday#######################################
        options = ["open", "not open", "doesnt matter"]
        menu_items = [
            {"viewclass": "IconListItem",
             "icon": "git",
             "height": dp(50),
             "text": f"{options[i]}",
             "on_release": lambda x=f"{options[i]}": self.set_item1(x)
             } for i in range(3)
        ]
        self.menu1 = MDDropdownMenu(
            caller=self.screen.ids.drop_item1,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        self.menu1.bind()


    def set_item1(self, text_item):
        self.screen.ids.drop_item1.set_item(text_item)
        self.menu1.dismiss()

##############################tuesday###########################################
        options = ["open", "not open", "doesnt matter"]
        menu_items = [
            {"viewclass": "IconListItem",
             "icon": "git",
             "height": dp(50),
             "text": f"{options[i]}",
             "on_release": lambda x=f"{options[i]}": self.set_item2(x)
             } for i in range(3)
        ]
        self.menu2 = MDDropdownMenu(
            caller=self.screen.ids.drop_item1,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        self.menu2.bind()


    def set_item2(self, text_item):
        self.screen.ids.drop_item2.set_item(text_item)
        self.menu2.dismiss()
##################################wednesday##############################
        options = ["open", "not open", "doesnt matter"]
        menu_items = [
            {"viewclass": "IconListItem",
             "icon": "git",
             "height": dp(50),
             "text": f"{options[i]}",
             "on_release": lambda x=f"{options[i]}": self.set_item3(x)
             } for i in range(3)
        ]
        self.menu3 = MDDropdownMenu(
            caller=self.screen.ids.drop_item3,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        self.menu3.bind()


    def set_item3(self, text_item):
        self.screen.ids.drop_item3.set_item(text_item)
        self.menu3.dismiss()
####################################thursday#####################################
        options = ["open", "not open", "doesnt matter"]
        menu_items = [
            {"viewclass": "IconListItem",
             "icon": "git",
             "height": dp(50),
             "text": f"{options[i]}",
             "on_release": lambda x=f"{options[i]}": self.set_item4(x)
             } for i in range(3)
        ]
        self.menu4 = MDDropdownMenu(
            caller=self.screen.ids.drop_item4,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        self.menu4.bind()


    def set_item4(self, text_item):
        self.screen.ids.drop_item4.set_item(text_item)
        self.menu4.dismiss()
###################################friday##########################################
        options = ["open", "not open", "doesnt matter"]
        menu_items = [
            {"viewclass": "IconListItem",
             "icon": "git",
             "height": dp(50),
             "text": f"{options[i]}",
             "on_release": lambda x=f"{options[i]}": self.set_item5(x)
             } for i in range(3)
        ]
        self.menu5 = MDDropdownMenu(
            caller=self.screen.ids.drop_item1,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        self.menu5.bind()


    def set_item5(self, text_item):
        self.screen.ids.drop_item5.set_item(text_item)
        self.menu5.dismiss()
#######################################saturday#################################
        options = ["open", "not open", "doesnt matter"]
        menu_items = [
            {"viewclass": "IconListItem",
             "icon": "git",
             "height": dp(50),
             "text": f"{options[i]}",
             "on_release": lambda x=f"{options[i]}": self.set_item6(x)
             } for i in range(3)
        ]
        self.menu6 = MDDropdownMenu(
            caller=self.screen.ids.drop_item6,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        self.menu6.bind()


    def set_item6(self, text_item):
        self.screen.ids.drop_item6.set_item(text_item)
        self.menu6.dismiss()
#################################################################################################
    def build(self):
        return self.screen
    
    

MainApp().run()