from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

class ScreenController(ScreenManager):
	background = ObjectProperty(Image(source="bg.jpg"))


class MainScreen(Screen):
    background = ObjectProperty(Image(source="select_bar.png"))


class OtherScreen(Screen):
    pass


class ViewApp(App):
    def build(self):
        return ScreenController()

if __name__ == "__main__":
    ViewApp().run()
