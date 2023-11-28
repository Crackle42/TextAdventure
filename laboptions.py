import json  # used for settings
import pickle  # used for ingame points
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.event import EventDispatcher


Builder.load_file("laboptions.kv")


class OptionenWindow(BoxLayout):
    pass


class RoadmapWindow(BoxLayout):
    pass


class FontGlobal(EventDispatcher):
    # this changes the font size to the value chosen by slider (default 18)
    # for all labels necessary - font_size: app.font_global.font_size

    def __init__(self):
        super().__init__()  # Call parent constructor
        self.font_size = NumericProperty(18)  # initialize font size to default value
        self.get_font_size()  # load font size from file on initialization

    def set_font_size(self, size):
        self.font_size = int(size)
        print("Font size set to:", self.font_size)

        # Update the JSON file with the new font_size value
        with open("labsettings.json", "r") as f:
            data = json.load(f)
        data["font_size"] = self.font_size
        with open("labsettings.json", "w") as f:
            json.dump(data, f)

    def get_font_size(self):
        try:
            # load font size from JSON file
            with open("labsettings.json", "r") as f:
                data = json.load(f)
                self.font_size = data.get("font_size", 18)
                print("Font size loaded:", self.font_size)  # add this line
        except FileNotFoundError:
            self.font_size = 18  # set default value
            pass
        return self.font_size


class PointsCount:
    _instance = None

# instance class variable is used to keep track of the singleton instance. The __new__() method creates a new
# instance only if there is no existing instance, otherwise it returns the existing instance.
# In main.py, import the PointsCount class and create an instance of it in the App class. Then you can
# use this instance to increase the example_points variable from any screen.
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init()
        return cls._instance

# 1. create list of variables. try to open file, if not existing, create a new one
    def _init(self):
        self.variables = {
            "raya_points": 0,
            "haunting_points": 0,
            "leader_points": 0
        }
        try:
            with open("ingame_points", "rb") as f:
                self.variables = pickle.load(f)
        except FileNotFoundError:
            pass

# 2. Each added variable needs "def increase_XXXX" AND a "def get_example" in this file"
# 3. ADD all of them for reset at "def reset_variables"
    def increase_raya_points(self):
        self.variables["raya_points"] += 1
        self.save_variables()

    def increase_haunting_points(self):
        self.variables["haunting_points"] += 1
        self.save_variables()

    def increase_leader_points(self):
        self.variables["leader_points"] += 1
        self.save_variables()

    def get_raya_points(self):
        return self.variables["raya_points"]

    def get_haunting_points(self):
        return self.variables["haunting_points"]

    def get_leader_points(self):
        return self.variables["leader_points"]

    def save_variables(self):
        with open("ingame_points", "wb") as f:
            pickle.dump(self.variables, f)

    def reset_variables(self):
        self.variables = {
            "raya_points": 0,
            "haunting_points": 0,
            "leader_points": 0
        }
        self.save_variables()
