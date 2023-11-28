from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("boxlayout_with_action_bar.kv")


class BoxLayoutWithActionBar(BoxLayout):
    title = StringProperty()


class BoxLayoutWithMainMenu(BoxLayout):
    title = StringProperty() #oder muss hier Hauptmenü stehen?
