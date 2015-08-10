from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.properties import ObjectProperty

MAINAPP = ''

class MainScreen(Screen):

    def close_app(self):
        MAINAPP.stop()



class OtherScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    background_image = ObjectProperty(
        Image(source='nes.jpg')
        )


class MyButton(Widget):
    def print_to(self):
        print "Inside My Button"

present = Builder.load_file("main.kv")


class MainApp(App):
    def build(self):
        return present


if __name__ == "__main__":
    MAINAPP = MainApp()
    MAINAPP.run()
