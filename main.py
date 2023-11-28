#import self as self
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from laboptions import PointsCount
from navigation_screen_manager import NavigationScreenManager


class MyScreenManager(NavigationScreenManager):
    pass


class LabyrinthApp(MDApp):
    manager = ObjectProperty(None)
    pointscount = ObjectProperty(None)  # necessary to create an instance in order to call the class

    def build(self):
        self.manager = MyScreenManager()
        self.pointscount = PointsCount()  # will increment the value
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        return self.manager

##############################################
    # Loading the entire text of a .txt file
    def load_long_text(self, filepath):
        try:
            with open(filepath, "r") as f:
                text = f.read().strip()
        except Exception as e:
            print(f"Error loading long text: {e}")
            return "Error loading long text2"

        return text
LabyrinthApp().run()
