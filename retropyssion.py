from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.window import Window

MAINAPP = ''

Window.fullscreen = 1


class ScreenController(ScreenManager):
    background = ObjectProperty(Image(source="bg.jpg"))


class MainScreen(Screen):
    background = ObjectProperty(Image(source="select_bar.png"))


class OtherScreen(Screen):
    background = ObjectProperty(Image(source="select_bar.png"))


class ViewApp(App):
    def build(self):
        return ScreenController()

if __name__ == "__main__":
    MAINAPP = ViewApp()
    MAINAPP.run()
